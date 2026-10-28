"""The Starship Bank's deposits, loans and savings goals (Eric 10-25, rule 36; the Zoud GameLab financial-literacy jam).
Credits stay in-game only (rule 2).

  · Deposits earn interest. A savings account (any time, a small rate) and term deposits (locked for 2, 4 or 8 weeks for
    a better rate; taking one out early gives up its interest). Deposited credits move into the Bank treasury
    (system:bank), and each deposit is the player's claim on it. Interest is simple, worked out on read from the time.
  · Deposits fund the loans. The Bank lends from its treasury but always keeps a reserve (bank_reserve_pct of what it owes
    depositors), so lending is never unlimited (rule 10). It pays depositors' interest out of what its loans earn.
  · Every rate is an APR, a year's rate as in the real world (Eric 10-27): each week charges or pays APR / 52.
  · Only the Bank lends (rule 8), and only to a player wearing the Business uniform (Eric 10-27). The APR falls with that
    uniform's bars (bank_loan_apr_bar1..5: 16, 14, 12, 10, 8); no bar, no loan. If the top bar is silver, the Bank lends
    only part of what's asked: the borrower makes a down payment (bank_loan_down_pct) from their own credits, as banks
    expect. A gold top bar, an exceptional record, waives it: the Bank lends the full amount. The Bank weighs each application (repayment history,
    recent income, what's still owed) for how much it will lend, and sets the term, the weekly payment and the dates.
  · Paying off early saves interest: the payoff amount is what's left plus interest only up to today. A payment the
    player can't cover brings a late fee (added to what's owed) and lowers their standing; the Bank tries again next day.
  · Savings goals: a goal names what the player is saving for and a target; progress is everything they hold at the Bank.
Every number is a live setting (`settings`). Weeks are real weeks."""
import asyncio, os
from datetime import datetime, timedelta, timezone
import store as ST

WEEK_S = 7 * 24 * 3600
PURPOSES = {"equipment": "Equipment for my craft (e.g. a bigger hold)", "ship": "A new ship", "plant": "A production plant",
            "printing": "Printing blueprint copies", "supplies": "Food and supplies", "other": "Something else"}
GOALS = {"ship": "A new ship", "plant": "A production plant", "printing": "Printing my blueprints",
         "emergency": "An emergency fund", "retirement": "Retirement on the New Earth"}
TERMS = (2, 4, 8)


def _now():
    return datetime.now(timezone.utc)


def _weeks(since, now=None):
    return max(0.0, ((now or _now()) - since).total_seconds() / WEEK_S)


async def _s(conn):
    return await ST.settings(conn)


LOAN_CAREERS = ("business",)      # Eric 10-27: only a Business uniform (finance is part of Business) qualifies


def _term_apr(s, weeks):
    return s[f"bank_term{weeks}_apr"]


def weekly(apr):
    """The rate charged or paid each week, %: the APR spread over the 52 weeks of a year."""
    return round(float(apr) / 52, 6)


def _apr(row):
    return float(row["apr_pct"]) if row["apr_pct"] is not None else round(float(row["rate_pct"]) * 52, 2)


def deposit_value(d, s, now=None):
    """What a deposit is worth now: principal plus simple interest. A term deposit earns only to its end, and only at the end."""
    rate = float(d["rate_pct"]) / 100
    if d["kind"] == "savings":
        return d["principal"] + int(d["principal"] * rate * _weeks(d["since"], now))
    matured = (now or _now()) >= d["opened_at"] + timedelta(weeks=d["term_weeks"])
    return d["principal"] + (int(d["principal"] * rate * d["term_weeks"]) if matured else 0)


async def _deposits(conn, pid, lock=False):
    return await conn.fetch("SELECT * FROM bank_deposits WHERE player_id=$1 AND closed_at IS NULL ORDER BY id"
                            + (" FOR UPDATE" if lock else ""), pid)


async def owed_to_depositors(conn, s):
    return sum(deposit_value(d, s) for d in await conn.fetch("SELECT * FROM bank_deposits WHERE closed_at IS NULL"))


async def lendable(conn, s):
    """What the Bank can lend right now: its treasury less the reserve it keeps against what it owes depositors."""
    tre = await conn.fetchval("SELECT credits FROM accounts WHERE id=$1", await ST.bank_account(conn))
    return max(0, int(tre - s["bank_reserve_pct"] / 100 * await owed_to_depositors(conn, s)))


async def deposit(conn, pid, kind, amount, weeks=None):
    s = await _s(conn)
    if kind not in ("savings", "term"):
        raise ST.Refused("Choose a savings account or a term deposit.")
    if kind == "term" and weeks not in TERMS:
        raise ST.Refused("A term deposit is for 2, 4 or 8 weeks.")
    async with conn.transaction():
        acct, tre = await ST.account_of(conn, pid), await ST.bank_account(conn)
        await ST.transfer(conn, acct, tre, amount, "bank_deposit", {"kind": kind, "weeks": weeks})
        if kind == "savings":
            sv = await conn.fetchrow("SELECT * FROM bank_deposits WHERE player_id=$1 AND kind='savings' AND closed_at IS NULL FOR UPDATE", pid)
            if sv:      # earned interest joins the balance, then the new credits
                await conn.execute("UPDATE bank_deposits SET principal=$2, since=now() WHERE id=$1", sv["id"],
                                   deposit_value(sv, s) + amount)
                return
            await conn.execute("INSERT INTO bank_deposits(player_id, kind, principal, rate_pct, apr_pct) VALUES($1,'savings',$2,$3,$4)",
                               pid, amount, weekly(s["bank_savings_apr"]), s["bank_savings_apr"])
            return
        await conn.execute("""INSERT INTO bank_deposits(player_id, kind, principal, rate_pct, apr_pct, term_weeks)
                              VALUES($1,'term',$2,$3,$4,$5)""", pid, amount, weekly(_term_apr(s, weeks)), _term_apr(s, weeks), weeks)


async def withdraw(conn, pid, amount=None, deposit_id=None):
    """Take credits out of savings (any amount up to its value), or close a term deposit (early: principal only)."""
    s = await _s(conn)
    async with conn.transaction():
        if deposit_id is not None:
            d = await conn.fetchrow("SELECT * FROM bank_deposits WHERE id=$1 AND player_id=$2 AND kind='term' AND closed_at IS NULL FOR UPDATE",
                                    deposit_id, pid)
            if not d:
                raise ST.Refused("No such term deposit.")
            pay = deposit_value(d, s)
            await conn.execute("UPDATE bank_deposits SET closed_at=now(), paid_out=$2 WHERE id=$1", d["id"], pay)
        else:
            d = await conn.fetchrow("SELECT * FROM bank_deposits WHERE player_id=$1 AND kind='savings' AND closed_at IS NULL FOR UPDATE", pid)
            if not d:
                raise ST.Refused("You have no savings account yet.")
            have = deposit_value(d, s)
            if not isinstance(amount, int) or amount <= 0 or amount > have:
                raise ST.Refused(f"You can take out up to {have:,} credits.")
            pay = amount
            if amount == have:
                await conn.execute("UPDATE bank_deposits SET closed_at=now(), paid_out=$2, principal=0 WHERE id=$1", d["id"], pay)
            else:
                await conn.execute("UPDATE bank_deposits SET principal=$2, since=now() WHERE id=$1", d["id"], have - amount)
        tre = await ST.bank_account(conn)
        if await conn.fetchval("SELECT credits FROM accounts WHERE id=$1", tre) < pay:
            raise ST.Refused("The Bank can't pay that out right now: too much of its money is out on loan. Try again soon.")
        await ST.transfer(conn, tre, await ST.account_of(conn, pid), pay, "bank_withdraw", {"deposit": d["id"]})
        return pay


# ── loans ──
async def standing(conn, pid):
    """The player's credit standing, 0-100: starts at 50; on-time payments raise it, late ones and big debts lower it."""
    r = await conn.fetchrow("""SELECT coalesce(sum(payments_made),0) n_ok, coalesce(sum(late_count),0) n_late,
                                      coalesce(sum(CASE WHEN closed_at IS NULL THEN balance ELSE 0 END),0) owed
                               FROM bank_loans WHERE player_id=$1""", pid)
    score = 50 + 4 * min(int(r["n_ok"]), 10) - 15 * int(r["n_late"])
    return {"score": max(0, min(100, score)), "on_time": int(r["n_ok"]), "late": int(r["n_late"]), "owed": int(r["owed"])}


async def income(conn, pid, days=28):
    """Credits the player earned in the last few weeks: what came into their account from trades, auctions and the Bank's desks."""
    acct = await ST.account_of(conn, pid)
    return int(await conn.fetchval("""SELECT coalesce(sum(amount),0) FROM credit_ledger WHERE to_account=$1
                                      AND reason NOT IN ('bank_withdraw','bank_loan','start') AND at > now() - make_interval(days => $2)""",
                                   acct, days))


def payment_for(amount, rate_pct, weeks):
    """The weekly payment that clears the loan in `weeks` (interest on what's left each week), rounded up."""
    r = rate_pct / 100
    import math
    return math.ceil(amount * r / (1 - (1 + r) ** -weeks))


async def quote(conn, pid, amount, weeks, purpose):
    """The Bank weighs the application: approve or not, and on what terms. Nothing is signed."""
    s = await _s(conn)
    if purpose not in PURPOSES:
        raise ST.Refused("Tell the Bank what the loan is for.")
    if weeks not in range(int(s["bank_loan_min_weeks"]), int(s["bank_loan_max_weeks"]) + 1):
        raise ST.Refused(f"Loans run from {int(s['bank_loan_min_weeks'])} to {int(s['bank_loan_max_weeks'])} weeks.")
    if not isinstance(amount, int) or amount <= 0:
        raise ST.Refused("Ask for a whole number of credits.")
    import careers as CR
    w = await CR.worn(conn, pid)
    if w["code"] not in LOAN_CAREERS:
        raise ST.Refused("The Bank lends only to an officer in Business uniform. Put it on in your quarters' Closet first.")
    bars = min(5, int(w["step"]))
    if bars < 1:
        raise ST.Refused("Earn your first Business bar in the library; then the Bank will consider a loan.")
    apr = float(s[f"bank_loan_apr_bar{bars}"])
    gold = w["bars"][bars - 1]["medal"] == "gold"
    import math
    down = 0 if gold else math.ceil(amount * float(s["bank_loan_down_pct"]) / 100)    # the borrower's own share
    asked, amount = amount, amount - down
    st, inc = await standing(conn, pid), await income(conn, pid)
    limit = max(0, int(s["bank_loan_base"] + s["bank_loan_income_x"] * inc * st["score"] / 50) - st["owed"])
    room = await lendable(conn, s)
    rate = weekly(apr)
    out = {"amount": amount, "weeks": weeks, "purpose": purpose, "rate_pct": rate, "apr_pct": apr, "bars": bars, "gold": gold, "asked": asked, "down_payment": down,
           "standing": st, "income_4w": inc,
           "limit": min(limit, room)}
    if st["score"] < s["bank_loan_min_score"]:
        return {**out, "approved": False, "why": "Your repayment record is too weak right now. Pay what you owe on time to rebuild it."}
    if amount > out["limit"]:
        return {**out, "approved": False, "why": f"The Bank can lend you up to {out['limit']:,} credits today."
                + (" Its own funds are low: more deposits make more loans possible." if room < limit else
                   " Earn more, and repay on time, to borrow more.")}
    pay = payment_for(amount, rate, weeks)
    return {**out, "approved": True, "payment": pay, "total": pay * weeks, "cost": pay * weeks - amount,
            "first_due": (_now() + timedelta(weeks=1)).isoformat()}


async def take(conn, pid, amount, weeks, purpose):
    async with conn.transaction():
        q = await quote(conn, pid, amount, weeks, purpose)
        if not q["approved"]:
            raise ST.Refused(q["why"])
        acct, tre = await ST.account_of(conn, pid), await ST.bank_account(conn)
        lid = await conn.fetchval("""INSERT INTO bank_loans(player_id, principal, balance, rate_pct, apr_pct, term_weeks, payment, purpose, next_due)
                                     VALUES($1,$2,$2,$3,$4,$5,$6,$7, now() + interval '7 days') RETURNING id""",
                                  pid, q["amount"], q["rate_pct"], q["apr_pct"], weeks, q["payment"], purpose)
        await ST.transfer(conn, tre, acct, q["amount"], "bank_loan", {"loan": lid})
        return {**q, "loan_id": lid}


def payoff_amount(ln, now=None):
    """What clears the loan today: what's left plus interest only for the days since the last payment date."""
    r = float(ln["rate_pct"]) / 100
    since = ln["next_due"] - timedelta(weeks=1)
    return int(round(float(ln["balance"]) * (1 + r * min(1.0, _weeks(since, now)))))


async def pay(conn, pid, loan_id, amount=None):
    """Pay extra toward a loan, or (amount None) pay it off. Paying early saves the interest that wasn't charged yet."""
    async with conn.transaction():
        ln = await conn.fetchrow("SELECT * FROM bank_loans WHERE id=$1 AND player_id=$2 AND closed_at IS NULL FOR UPDATE", loan_id, pid)
        if not ln:
            raise ST.Refused("No such loan.")
        due = payoff_amount(ln)
        amt = due if amount is None else amount
        if not isinstance(amt, int) or amt <= 0:
            raise ST.Refused("Pay a whole number of credits.")
        amt = min(amt, due)
        await ST.transfer(conn, await ST.account_of(conn, pid), await ST.bank_account(conn), amt, "bank_repay", {"loan": loan_id})
        # the interest earned so far is charged first, then the rest comes off what's owed
        interest = due - int(round(float(ln["balance"])))
        left = max(0, int(round(float(ln["balance"]))) - max(0, amt - interest))
        if amt >= due or left == 0:
            await conn.execute("UPDATE bank_loans SET balance=0, closed_at=now() WHERE id=$1", loan_id)
        else:
            await conn.execute("UPDATE bank_loans SET balance=$2 WHERE id=$1", loan_id, left)
        return {"paid": amt, "closed": amt >= due or left == 0, "left": 0 if amt >= due else left}


async def _collect(conn, ln, s):
    """One weekly payment, taken automatically on its date. Short of credits: a late fee, and another try tomorrow."""
    r = float(ln["rate_pct"]) / 100
    owed = int(round(float(ln["balance"]) * (1 + r)))
    payment = min(int(ln["payment"]), owed)
    acct = await ST.account_of(conn, ln["player_id"])
    have = await conn.fetchval("SELECT credits FROM accounts WHERE id=$1", acct)
    if have < payment:
        fee = max(1, int(payment * s["bank_late_fee_pct"] / 100))
        await conn.execute("""UPDATE bank_loans SET balance=balance+$2, late_count=late_count+1, next_due=now() + interval '1 day'
                              WHERE id=$1""", ln["id"], fee)
        return "late"
    await ST.transfer(conn, acct, await ST.bank_account(conn), payment, "bank_repay", {"loan": ln["id"], "scheduled": True})
    left = owed - payment
    await conn.execute("""UPDATE bank_loans SET balance=$2, payments_made=payments_made+1, next_due=next_due + interval '7 days',
                          closed_at=CASE WHEN $3 THEN now() END WHERE id=$1""", ln["id"], max(0, left), left <= 0)
    return "paid"


async def tick(conn):
    s = await _s(conn)
    for ln in await conn.fetch("SELECT * FROM bank_loans WHERE closed_at IS NULL AND next_due <= now() ORDER BY next_due LIMIT 200"):
        async with conn.transaction():
            row = await conn.fetchrow("SELECT * FROM bank_loans WHERE id=$1 AND closed_at IS NULL AND next_due <= now() FOR UPDATE", ln["id"])
            if row:
                await _collect(conn, row, s)


async def run(app):
    """Background loop: takes each loan payment on its date. DFG_LENDING=0 turns it off (tests tick)."""
    if os.environ.get("DFG_LENDING", "1") == "0":
        return
    while True:
        try:
            async with app["pool"].acquire() as conn:
                await tick(conn)
            await asyncio.sleep(60)
        except asyncio.CancelledError:
            raise
        except Exception as e:
            print(f"lending loop error: {type(e).__name__}: {e}", flush=True)
            await asyncio.sleep(120)


# ── savings goals ──
async def set_goal(conn, pid, goal, target):
    if goal not in GOALS:
        raise ST.Refused("Choose what you're saving for.")
    if not isinstance(target, int) or target <= 0:
        raise ST.Refused("Set a target in whole credits.")
    if await conn.fetchval("SELECT count(*) FROM bank_goals WHERE player_id=$1 AND done_at IS NULL", pid) >= 3:
        raise ST.Refused("Three goals at a time. Reach or drop one first.")
    await conn.execute("INSERT INTO bank_goals(player_id, goal, target) VALUES($1,$2,$3)", pid, goal, target)


async def drop_goal(conn, pid, goal_id):
    await conn.execute("UPDATE bank_goals SET done_at=now(), dropped=true WHERE id=$1 AND player_id=$2 AND done_at IS NULL", goal_id, pid)


async def summary(conn, pid):
    """Everything the player has at the Bank, for the Bank screen."""
    s = await _s(conn)
    deps = await _deposits(conn, pid)
    now = _now()
    savings = next(({"balance": deposit_value(d, s, now), "apr_pct": _apr(d)} for d in deps if d["kind"] == "savings"),
                   {"balance": 0, "apr_pct": float(s["bank_savings_apr"])})
    terms = [{"id": d["id"], "principal": d["principal"], "apr_pct": _apr(d), "weeks": d["term_weeks"],
              "matures_at": (d["opened_at"] + timedelta(weeks=d["term_weeks"])).isoformat(),
              "at_maturity": d["principal"] + int(d["principal"] * float(d["rate_pct"]) / 100 * d["term_weeks"]),
              "matured": now >= d["opened_at"] + timedelta(weeks=d["term_weeks"])} for d in deps if d["kind"] == "term"]
    at_bank = savings["balance"] + sum(deposit_value(d, s, now) for d in deps if d["kind"] == "term")
    loans = [{"id": l["id"], "principal": l["principal"], "balance": int(round(float(l["balance"]))), "apr_pct": _apr(l),
              "weeks": l["term_weeks"], "payment": l["payment"], "payments_made": l["payments_made"], "late": l["late_count"],
              "next_due": l["next_due"].isoformat(), "payoff": payoff_amount(l, now), "purpose": PURPOSES[l["purpose"]]}
             for l in await conn.fetch("SELECT * FROM bank_loans WHERE player_id=$1 AND closed_at IS NULL ORDER BY id", pid)]
    goals = [{"id": g["id"], "goal": g["goal"], "name": GOALS[g["goal"]], "target": g["target"],
              "progress": min(at_bank, g["target"]), "reached": at_bank >= g["target"]}
             for g in await conn.fetch("SELECT * FROM bank_goals WHERE player_id=$1 AND done_at IS NULL ORDER BY id", pid)]
    return {"credits": await conn.fetchval("SELECT credits FROM accounts WHERE player_id=$1", pid), "savings": savings,
            "terms": terms, "at_bank": at_bank, "loans": loans, "goals": goals, "standing": await standing(conn, pid),
            "rates": {"savings_apr": float(s["bank_savings_apr"]), "term_apr": {w: float(_term_apr(s, w)) for w in TERMS},
                      "loan_apr_by_bars": {b: float(s[f"bank_loan_apr_bar{b}"]) for b in range(1, 6)}, "loan_uniform": "Business",
                      "loan_down_payment_pct": float(s["bank_loan_down_pct"])},
            "purposes": PURPOSES, "goal_choices": GOALS,
            "loan_weeks": [int(s["bank_loan_min_weeks"]), int(s["bank_loan_max_weeks"])]}
