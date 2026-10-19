"""Where everything a player owns is kept, and how credits move (schema v2, Eric 2026-10-11).

Why this module exists: every change to what a player owns goes through these few functions, inside one database
transaction, so goods and credits can never be created, lost or spent twice. audit() proves it: across every account,
credits always add up to zero (the mint's negative balance is exactly what it has issued), and every account's balance
matches its paper trail.

Rules kept here:
  · Nothing is unlimited: storage has a size in cubic metres, the hangar has slots.
  · Unloading at the Starship turns each piece in the ship's hold into grams of its material in the player's space in
    the Starship's cargo hold, until that space is full; whatever doesn't fit stays aboard. Resources wait there until
    they sell (Eric 10-11).
  · Every player has Private Quarters: a small furnished room for personal possessions, with a lockbox.
  · Credits only move between accounts inside the game: never from real money, never out to it.
  · Every transfer of goods gives the player a receipt with a code anyone can check against this server (Eric 10-11)."""
import json, secrets

G_PER_KG = 1000
FURNISHINGS = ["furn-bed", "furn-mirror", "furn-closet", "furn-desk", "furn-lamp", "furn-chair", "furn-filing-drawer", "furn-lockbox"]


# Where each kind of thing is put away (Eric 10-11): raw materials in the Starship's cargo hold, every blueprint in the
# filing cabinet, small personal effects and valuables in the lockbox inside it, library books on the bookshelf.
HOME_OF = {"resource": "starship_cargo", "blueprint": "filing_cabinet", "valuable": "lockbox", "book": "bookshelf"}  # books and valuables arrive with the library and later items

CODE_CHARS = "23456789ABCDEFGHJKMNPQRSTVWXYZ"     # no 0/O, 1/I/L or U: easy to read out and type


def receipt_code():
    """WSC-XXXX-XXXX: 30^8 (about 650 billion) possibilities, drawn from a secure random source, so a code can't be guessed."""
    c = "".join(secrets.choice(CODE_CHARS) for _ in range(8))
    return f"WSC-{c[:4]}-{c[4:]}"


async def issue_receipt(conn, pid, kind, ledger_id, detail):
    """Write a receipt and return it. Call inside the same transaction as the transfer it records."""
    for _ in range(5):                                 # a repeat is astronomically unlikely; retry rather than fail
        code = receipt_code()
        row = await conn.fetchrow("""INSERT INTO receipts(code, player_id, kind, ledger_id, detail) VALUES($1,$2,$3,$4,$5)
                                     ON CONFLICT (code) DO NOTHING RETURNING code, at""",
                                  code, pid, kind, ledger_id, json.dumps(detail))
        if row:
            return {"code": row["code"], "issued_at": row["at"].isoformat(), "kind": kind, **detail}
    raise RuntimeError("could not issue a unique receipt code")


def _receipt_out(r):
    return {"code": r["code"], "issued_at": r["at"].isoformat(), "kind": r["kind"], **json.loads(r["detail"])}


async def receipts(conn, pid, limit=50):
    """The player's receipts, newest first."""
    rows = await conn.fetch("SELECT code, kind, detail, at FROM receipts WHERE player_id=$1 ORDER BY id DESC LIMIT $2", pid, limit)
    return [_receipt_out(r) for r in rows]


async def verify_receipt(conn, code):
    """Check a receipt code. Returns the receipt as the server recorded it (without who owns it), or None if it isn't real."""
    r = await conn.fetchrow("SELECT code, kind, detail, at FROM receipts WHERE code=$1", (code or "").strip().upper())
    return _receipt_out(r) if r else None


class Refused(Exception):
    """Something the rules don't allow. The message is shown to the player."""


async def settings(conn):
    return {r["key"]: float(r["value"]) for r in await conn.fetch("SELECT key, value FROM settings")}


async def system_account(conn, kind):
    return await conn.fetchval("SELECT id FROM accounts WHERE kind=$1", kind)


WSC_KEY = "system:wsc"     # the WSC's own account (Eric 10-11): the governing body; it collects the 2.5% auction fee (its tax, 10-19),
                           # and it can buy and sell what the ship needs on the market, like any account


async def wsc_account(conn):
    """The WSC's account id (created on first use, set up like any account aboard)."""
    return await account_of(conn, await ensure_player(conn, WSC_KEY, "WSC Alexander von Humboldt"))


BANK_KEY = "system:bank"           # the Starship Bank's own account (Eric 10-19): run by the WSC, it collects the blueprint
                                   # printing fees and builds its ledger toward loans later. Separate from its two market desks.
AUCTION_KEY = "system:auction-house"   # the Auction House (Eric 10-19), under the Bank's authority: its own account, no fees yet


async def bank_account(conn):
    return await account_of(conn, await ensure_player(conn, BANK_KEY, "Starship Bank"))


async def auction_house_account(conn):
    return await account_of(conn, await ensure_player(conn, AUCTION_KEY, "Starship Auction House"))


async def account_of(conn, pid):
    return await conn.fetchval("SELECT id FROM accounts WHERE player_id=$1", pid)


async def transfer(conn, frm, to, amount, reason, ref=None):
    """Move credits between two accounts and write the paper-trail row. Call inside a transaction."""
    if not isinstance(amount, int) or amount <= 0:
        raise Refused("Credits must be a whole number above zero.")
    rows = await conn.fetch("SELECT id, kind, credits FROM accounts WHERE id = ANY($1::bigint[]) ORDER BY id FOR UPDATE",
                            [frm, to])                   # lock both, always in the same order, so two transfers can't deadlock
    acct = {r["id"]: r for r in rows}
    if frm not in acct or to not in acct:
        raise Refused("No such account.")
    if acct[frm]["kind"] != "mint" and acct[frm]["credits"] < amount:
        raise Refused("Not enough credits.")
    await conn.execute("UPDATE accounts SET credits = credits - $2 WHERE id=$1", frm, amount)
    await conn.execute("UPDATE accounts SET credits = credits + $2 WHERE id=$1", to, amount)
    await conn.execute("INSERT INTO credit_ledger(from_account, to_account, amount, reason, ref) VALUES($1,$2,$3,$4,$5)",
                       frm, to, amount, reason, json.dumps(ref or {}))


async def ensure_player(conn, key, name=None):
    """The player's id. A new player gets their account, storage aboard the Starship, a hangar, the starter ship with
    its hold, and starting credits from the mint, all at once."""
    async with conn.transaction():
        pid = await conn.fetchval(
            "INSERT INTO players(player_key, display_name) VALUES($1,$2) ON CONFLICT (player_key) DO NOTHING RETURNING id", key, name)
        if pid is None:
            pid = await conn.fetchval("SELECT id FROM players WHERE player_key=$1", key)
            if name:
                await conn.execute("UPDATE players SET display_name=$2 WHERE id=$1 AND display_name IS DISTINCT FROM $2",
                                   pid, name)
            return pid
        s = await settings(conn)
        acct = await conn.fetchval("INSERT INTO accounts(kind, player_id) VALUES('player',$1) RETURNING id", pid)
        await conn.execute("""INSERT INTO locations(player_id, kind, name, capacity_m3)
                              VALUES($1,'starship_cargo','Your space in the Starship''s cargo hold',$2)""", pid, s["cargo_m3_start"])
        quarters = await conn.fetchval("""INSERT INTO locations(player_id, kind, name, capacity_m3)
                                          VALUES($1,'private_quarters','Private Quarters',$2) RETURNING id""", pid, s["quarters_m3"])
        cabinet = await conn.fetchval("""INSERT INTO locations(player_id, kind, name, capacity_m3, parent_id)
                                         VALUES($1,'filing_cabinet','Filing cabinet',$2,$3) RETURNING id""",
                                      pid, s["filing_cabinet_m3"], quarters)
        await conn.execute("""INSERT INTO locations(player_id, kind, name, capacity_m3, parent_id)
                              VALUES($1,'lockbox','Lockbox',$2,$3)""", pid, s["lockbox_m3"], cabinet)
        await conn.execute("""INSERT INTO locations(player_id, kind, name, capacity_m3, parent_id)
                              VALUES($1,'bookshelf','Bookshelf',$2,$3)""", pid, s["bookshelf_m3"], quarters)
        for f in FURNISHINGS:
            await conn.execute("INSERT INTO items(item_code, owner_id, location_id, attrs) VALUES($1,$2,$3,'{\"fixed\": true}')",
                               f, pid, quarters)
        hangar = await conn.fetchval("""INSERT INTO locations(player_id, kind, name, capacity_slots)
                                        VALUES($1,'hangar','Hangar aboard the Starship',$2) RETURNING id""",
                                     pid, int(s["hangar_slots_start"]))
        await new_ship(conn, pid, hangar, "ship-starter", "starter", (1.6, 1.2, 1.0))
        start = int(s["start_credits"])
        if start > 0:
            await transfer(conn, await system_account(conn, "mint"), acct, start, "start", {"note": "starting credits"})
        return pid


async def new_ship(conn, pid, hangar_id, item_code, hull, hold, active=True):
    """A ship is a ships row (how it flies), an item (so it is owned and kept like anything else) and a hold."""
    used = await conn.fetchval("SELECT count(*) FROM items WHERE location_id=$1", hangar_id)
    slots = await conn.fetchval("SELECT capacity_slots FROM locations WHERE id=$1", hangar_id)
    if used >= slots:
        raise Refused("Your hangar is full.")
    sid = await conn.fetchval("INSERT INTO ships(player_id, hull, hold_l, hold_w, hold_h, active) VALUES($1,$2,$3,$4,$5,$6) RETURNING id",
                              pid, hull, *hold, active)
    await conn.execute("INSERT INTO items(item_code, owner_id, location_id, ship_id) VALUES($1,$2,$3,$4)",
                       item_code, pid, hangar_id, sid)
    await conn.execute("""INSERT INTO locations(player_id, kind, ship_id, name, capacity_m3)
                          VALUES($1,'ship_hold',$2,'Ship''s hold',$3)""", pid, sid, hold[0] * hold[1] * hold[2])
    return sid


async def active_ship(conn, pid, lock=False):
    return await conn.fetchrow("SELECT id, hull, hold_l, hold_w, hold_h FROM ships WHERE player_id=$1 AND active"
                               + (" FOR UPDATE" if lock else ""), pid)


async def used_m3(conn, location_id):
    """Space taken in a place: resources by real density, counted and unique things by their size each."""
    stacked = await conn.fetchval(
        """SELECT coalesce(sum(CASE WHEN t.base_unit='g' THEN (s.qty + s.held) / 1000.0 / t.density_kg_m3
                                    ELSE (s.qty + s.held) * coalesce(t.volume_m3_each, 0) END), 0)
           FROM stacks s JOIN item_types t ON t.code = s.item_code WHERE s.location_id=$1""", location_id)
    unique = await conn.fetchval(
        """SELECT coalesce(sum(coalesce((i.attrs->>'volume_m3')::numeric, t.volume_m3_each, 0)), 0) FROM items i JOIN item_types t ON t.code=i.item_code
           WHERE i.location_id=$1 AND i.ship_id IS NULL AND NOT coalesce((i.attrs->>'fixed')::boolean, false)""", location_id)
    # a ship's hold also carries loose pieces straight from the fields, each taking the box it needs
    loose = await conn.fetchval("""SELECT coalesce(sum(c.box_m3), 0) FROM cargo c JOIN locations l ON l.ship_id=c.ship_id
                                   WHERE l.id=$1 AND l.kind='ship_hold' AND c.unloaded_at IS NULL""", location_id)
    return float(stacked) + float(unique) + float(loose)


async def unload(conn, pid):
    """Unload the active ship's hold into the player's space in the Starship's cargo hold. Each piece becomes grams
    of its material. Pieces go in oldest first until that space is full; the rest stay aboard."""
    async with conn.transaction():
        ship = await active_ship(conn, pid, lock=True)
        store = await conn.fetchrow("SELECT id, capacity_m3 FROM locations WHERE player_id=$1 AND kind='starship_cargo' FOR UPDATE", pid)
        cap, used = float(store["capacity_m3"]), await used_m3(conn, store["id"])
        pieces = await conn.fetch("""SELECT c.id, c.material, c.mass_kg, c.volume_m3, c.dim_a, c.dim_b, c.dim_c, c.flawless,
                                            t.density_kg_m3 FROM cargo c
                                     JOIN item_types t ON t.code=c.material
                                     WHERE c.ship_id=$1 AND c.unloaded_at IS NULL ORDER BY c.id""", ship["id"])
        moved, grams_by, gems = [], {}, []
        lockbox = await conn.fetchrow("SELECT id, capacity_m3 FROM locations WHERE player_id=$1 AND kind='lockbox' FOR UPDATE", pid)
        for p in pieces:
            if p["flawless"]:
                # a near-flawless diamond (rule 26) is its own item, never mixed in with industrial diamond:
                # kept as a valuable in the lockbox if it fits, otherwise in the Starship cargo hold
                vol = float(p["volume_m3"])
                into = lockbox if await used_m3(conn, lockbox["id"]) + vol <= float(lockbox["capacity_m3"]) + 1e-9 else None
                if not into:
                    if used + vol > cap + 1e-9:
                        break
                    used += vol
                iid = await conn.fetchval("""INSERT INTO items(item_code, owner_id, location_id, attrs)
                                             VALUES('diamond-flawless',$1,$2,$3) RETURNING id""",
                                          pid, (into or store)["id"], json.dumps({
                                              "kg": round(float(p["mass_kg"]), 3), "volume_m3": vol,
                                              "dims_m": [float(p["dim_a"]), float(p["dim_b"]), float(p["dim_c"])]}))
                await conn.execute("UPDATE cargo SET unloaded_at=now() WHERE id=$1", p["id"])
                moved.append(p["id"]); gems.append({"item_id": iid, "kg": round(float(p["mass_kg"]), 3),
                                                    "kept_in": "lockbox" if into else "starship_cargo"})
                continue
            g = int(round(float(p["mass_kg"]) * G_PER_KG))
            need = g / G_PER_KG / float(p["density_kg_m3"])
            if used + need > cap + 1e-9:
                break
            used += need
            await conn.execute("""INSERT INTO stacks(location_id, item_code, qty) VALUES($1,$2,$3)
                                  ON CONFLICT (location_id, item_code) DO UPDATE SET qty = stacks.qty + EXCLUDED.qty""",
                               store["id"], p["material"], g)
            await conn.execute("UPDATE cargo SET unloaded_at=now() WHERE id=$1", p["id"])
            moved.append(p["id"]); grams_by[p["material"]] = grams_by.get(p["material"], 0) + g
        receipt = None
        if moved:
            lid = await conn.fetchval("INSERT INTO ledger(player_id, kind, detail) VALUES($1,'unload',$2) RETURNING id", pid,
                                      json.dumps({"pieces": moved, "grams": grams_by, "ship": ship["id"]}))
            receipt = await issue_receipt(conn, pid, "unload", lid, {
                "issued_by": "WSC Alexander von Humboldt, cargo office",
                "from": f"your ship's hold (ship {ship['id']}, {ship['hull']} hull)",
                "to": "your space in the Starship's cargo hold",
                "pieces": len(moved), "left_aboard": len(pieces) - len(moved),
                "kg": {k: v / G_PER_KG for k, v in sorted(grams_by.items())},
                **({"near_flawless_diamonds": gems} if gems else {}),
                "space_used_m3": round(used, 4), "space_total_m3": round(cap, 4)})
        return {"unloaded_pieces": len(moved), "left_aboard": len(pieces) - len(moved),
                "unloaded_kg": {k: v / G_PER_KG for k, v in grams_by.items()},
                "storage_full": len(moved) < len(pieces), "near_flawless_diamonds": gems, "receipt": receipt}


async def inventory(conn, pid):
    """Everything the player owns and where it is, plus their credits."""
    acct = await conn.fetchrow("SELECT credits, held_credits FROM accounts WHERE player_id=$1", pid)
    places = []
    locs = await conn.fetch("SELECT id, kind, name, capacity_m3, capacity_slots, ship_id, parent_id FROM locations WHERE player_id=$1 ORDER BY id", pid)
    kind_of = {r["id"]: r["kind"] for r in locs}
    for loc in locs:
        stacks = await conn.fetch("""SELECT s.item_code, t.name, t.kind, t.base_unit, s.qty, s.held FROM stacks s
                                     JOIN item_types t ON t.code=s.item_code WHERE s.location_id=$1 AND (s.qty>0 OR s.held>0)
                                     ORDER BY t.kind, t.name""", loc["id"])
        uniq = await conn.fetch("""SELECT i.id, i.item_code, t.name, t.kind, i.attrs, i.held, i.ship_id FROM items i
                                   JOIN item_types t ON t.code=i.item_code WHERE i.location_id=$1
                                   AND NOT coalesce((i.attrs->>'fixed')::boolean, false) ORDER BY i.id""", loc["id"])
        place = {"kind": loc["kind"], "name": loc["name"], "inside": kind_of.get(loc["parent_id"]),
                 "goods": [{"item": r["item_code"], "name": r["name"], "kind": r["kind"],
                            **({"kg": r["qty"] / G_PER_KG, "kg_set_aside": r["held"] / G_PER_KG} if r["base_unit"] == "g"
                               else {"count": r["qty"], "set_aside": r["held"]})} for r in stacks],
                 "items": [{"id": r["id"], "item": r["item_code"], "name": r["name"], "kind": r["kind"],
                            "details": json.loads(r["attrs"]), "set_aside": r["held"]} for r in uniq]}
        if loc["capacity_m3"] is not None:
            place.update(capacity_m3=float(loc["capacity_m3"]), used_m3=round(await used_m3(conn, loc["id"]), 4))
        if loc["capacity_slots"] is not None:
            place.update(capacity_slots=loc["capacity_slots"], used_slots=len(uniq))
        if loc["kind"] == "ship_hold":
            place["pieces_aboard"] = await conn.fetchval("SELECT count(*) FROM cargo WHERE ship_id=$1 AND unloaded_at IS NULL", loc["ship_id"])
            # the pieces still in the hold, by material, so the desk can list them like everything else
            place["goods"] = [{"item": r["material"], "name": r["name"], "kind": "resource", "kg": float(r["kg"]), "pieces": r["n"]}
                              for r in await conn.fetch("""SELECT c.material, t.name, sum(c.mass_kg) AS kg, count(*) AS n FROM cargo c
                                                           JOIN item_types t ON t.code=c.material
                                                           WHERE c.ship_id=$1 AND c.unloaded_at IS NULL
                                                           GROUP BY c.material, t.name ORDER BY t.name""", loc["ship_id"])]
        if loc["kind"] == "filing_cabinet":
            # the player's own blueprint designs live here too, whatever stage their review is at
            place["designs"] = [{"title": r["title"], "status": r["status"], "version": r["version"]} for r in await conn.fetch(
                "SELECT title, status, version FROM blueprint_submissions WHERE designer_id=$1 AND status <> 'withdrawn' ORDER BY updated_at DESC", pid)]
        places.append(place)
    return {"credits": acct["credits"], "credits_set_aside": acct["held_credits"], "places": places}


async def history(conn, pid, limit=50):
    """The player's credit history, newest first, each row with the balance after it."""
    acct = await account_of(conn, pid)
    rows = await conn.fetch(
        """WITH mine AS (
             SELECT l.id, l.at, l.reason, l.ref,
                    CASE WHEN l.to_account=$1 THEN l.amount ELSE -l.amount END AS change,
                    CASE WHEN l.to_account=$1 THEN l.from_account ELSE l.to_account END AS other
             FROM credit_ledger l WHERE l.from_account=$1 OR l.to_account=$1)
           SELECT m.*, a.kind AS other_kind, (sum(m.change) OVER (ORDER BY m.id))::bigint AS balance_after
           FROM mine m JOIN accounts a ON a.id=m.other ORDER BY m.id DESC LIMIT $2""", acct, limit)
    names = {"mint": "Starship bank (new credits)", "bank": "Starship bank", "sink": "Spent", "player": "Another player"}
    return [{"at": r["at"].isoformat(), "change": r["change"], "balance_after": r["balance_after"], "reason": r["reason"],
             "with": names[r["other_kind"]], "ref": json.loads(r["ref"])} for r in rows]


async def audit(conn):
    """Every credit accounted for. Returns a list of problems (empty = all good)."""
    problems = []
    total = await conn.fetchval("SELECT coalesce(sum(credits + held_credits), 0) FROM accounts")
    if total != 0:
        problems.append(f"credits across all accounts add up to {total}, not 0")
    bad = await conn.fetch(
        """SELECT a.id, a.credits + a.held_credits AS have,
                  coalesce((SELECT sum(amount) FROM credit_ledger WHERE to_account=a.id),0)
                - coalesce((SELECT sum(amount) FROM credit_ledger WHERE from_account=a.id),0) AS trail
           FROM accounts a""")
    for r in bad:
        if r["have"] != r["trail"]:
            problems.append(f"account {r['id']} holds {r['have']} but its paper trail says {r['trail']}")
    held = await conn.fetch(
        """SELECT a.id, a.held_credits, coalesce(sum(o.price * o.remaining) FILTER (WHERE o.side='buy' AND o.status='open'), 0)
                  + coalesce((SELECT sum(l.top_bid + l.top_fee)::bigint FROM auction_lots l
                              WHERE l.status='open' AND l.top_bidder=a.player_id), 0) AS bids
           FROM accounts a LEFT JOIN orders o ON o.account_id=a.id GROUP BY a.id""")
    for r in held:
        if r["held_credits"] != r["bids"]:
            problems.append(f"account {r['id']} has {r['held_credits']} set aside but its open bids need {r['bids']}")
    goods = await conn.fetch(
        """SELECT s.location_id, s.item_code, s.held,
                  coalesce((SELECT sum(o.remaining * t.trade_unit) FROM orders o JOIN accounts a ON a.id=o.account_id
                            WHERE a.player_id=l.player_id AND o.item_code=s.item_code AND o.side='sell' AND o.status='open'), 0) AS asks
           FROM stacks s JOIN locations l ON l.id=s.location_id JOIN item_types t ON t.code=s.item_code
           WHERE l.kind='starship_cargo'""")
    for r in goods:
        if r["held"] != r["asks"]:
            problems.append(f"place {r['location_id']} has {r['held']} of {r['item_code']} set aside but its open asks need {r['asks']}")
    return problems

