extends Control
## The Starship Bank (Eric 10-25, rule 36), reached from the Desk: savings goals, a savings account, term deposits and
## loans. Credits stay in-game (rule 2). The lessons are in the choices: interest earned by saving, the total cost of
## borrowing shown before signing, and paying a loan off early to save interest.

var body: VBoxContainer
var msg: Label
var data: Dictionary = {}
var busy := false


func _ready() -> void:
	var box := Ui.screen(self)
	var top := HBoxContainer.new()
	box.add_child(top)
	var back := Ui.button("◀ Desk", false)
	back.custom_minimum_size = Vector2(180, 64)
	back.pressed.connect(func(): get_tree().change_scene_to_file("res://scenes/quarters.tscn"))
	top.add_child(back)
	var t := Ui.label("  STARSHIP BANK", 32, Ui.GOLD)
	t.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	top.add_child(t)
	msg = Ui.label("", 22, Ui.GOLD)
	box.add_child(msg)
	var scroll := ScrollContainer.new()
	scroll.size_flags_vertical = Control.SIZE_EXPAND_FILL
	scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	box.add_child(scroll)
	body = VBoxContainer.new()
	body.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	body.add_theme_constant_override("separation", 14)
	scroll.add_child(body)
	_load()


func _load() -> void:
	var r: Dictionary = await Api.call_api("GET", "/api/dfg/bank")
	if not r.ok:
		msg.text = r.error
		return
	data = r.data
	_render()


## One counter action; the Bank answers with the whole picture again.
func _act(path: String, payload: Dictionary, done := "") -> void:
	if busy:
		return
	busy = true
	var r: Dictionary = await Api.call_api("POST", "/api/dfg/bank/" + path, payload)
	busy = false
	if not r.ok:
		msg.text = r.error
		return
	msg.text = done
	data = r.data
	_render()


func _heading(text: String) -> Label:
	var l := Ui.label(text, 26, Ui.GOLD)
	l.add_theme_constant_override("line_spacing", 0)
	return l


func _row(parent: Control) -> HBoxContainer:
	var h := HBoxContainer.new()
	h.add_theme_constant_override("separation", 12)
	parent.add_child(h)
	return h


func _small_button(text: String, primary := false) -> Button:
	var b := Ui.button(text, primary)
	b.custom_minimum_size = Vector2(0, 64)
	b.add_theme_font_size_override("font_size", 22)
	b.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	return b


func _amount_field(placeholder := "Credits") -> LineEdit:
	var f := Ui.field(placeholder)
	f.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	return f


func _int(f: LineEdit) -> int:
	return int(f.text.replace(",", "").strip_edges())


func _bar(parent: Control, frac: float, c: Color) -> void:
	var bg := ColorRect.new()
	bg.color = Color(c, 0.18)
	bg.custom_minimum_size = Vector2(0, 14)
	parent.add_child(bg)
	var fill := ColorRect.new()
	fill.color = c
	fill.size = Vector2(0, 14)
	bg.add_child(fill)
	bg.resized.connect(func(): fill.size.x = bg.size.x * clampf(frac, 0.0, 1.0))


func _render() -> void:
	for c in body.get_children():
		c.queue_free()
	var d := data
	body.add_child(Ui.label(tr("Wallet: %s credits   ·   At the Bank: %s credits") % [Ui.num(d.credits), Ui.num(d.at_bank)], 24))
	_craft()
	_goals(d)
	_savings(d)
	_terms(d)
	_loans(d)


# ── your craft, leased from the WSC (rule 38): 50 credits an hour, or 500 a week on a 28-day contract ──
func _craft() -> void:
	body.add_child(_heading("YOUR CRAFT (LEASED FROM THE WSC)"))
	var box := VBoxContainer.new()
	box.add_theme_constant_override("separation", 10)
	body.add_child(box)
	var r: Dictionary = await Api.call_api("GET", "/api/dfg/craft")
	if not r.ok or not is_instance_valid(box):
		return
	var c: Dictionary = r.data
	if c.lease == null:
		box.add_child(Ui.label(tr("You pay %s credits an hour of flight, fuel included. A lease is %s a week on a %d-day contract, each week paid up front, and renews by itself: cheaper if you fly more than %d hours a week.") % [
			Ui.num(c.hourly), Ui.num(c.weekly), int(c.lease_weeks) * 7, int(c.weekly) / int(c.hourly)], 22))
		var take := _small_button(tr("Lease my craft: %s a week") % Ui.num(c.weekly), true)
		take.pressed.connect(func(): _act_craft("craft/lease", {}, tr("Leased. Flight time is included until the lease ends.")))
		box.add_child(take)
		return
	var l: Dictionary = c.lease
	box.add_child(Ui.label(tr("Leased: flight time included. Next payment %s on %s. Contract to %s, %s.") % [Ui.num(c.weekly),
		str(l.next_charge).substr(0, 10), str(l.term_ends).substr(0, 10), tr("renewing automatically") if l.auto_renew else tr("not renewing")], 22, Ui.GREEN))
	var t := _small_button("Stop auto-renew" if l.auto_renew else "Turn auto-renew back on")
	var on: bool = not l.auto_renew
	t.pressed.connect(func(): _act_craft("craft/renew", {"auto_renew": on}, tr("Updated.")))
	box.add_child(t)


func _act_craft(path: String, payload: Dictionary, done: String) -> void:
	var r: Dictionary = await Api.call_api("POST", "/api/dfg/" + path, payload)
	msg.text = done if r.ok else r.error
	_load()


# ── savings goals: what you're saving for, and how far you've got ──
func _goals(d: Dictionary) -> void:
	body.add_child(_heading("SAVINGS GOALS"))
	body.add_child(Ui.label("Name what you're saving for. Everything you keep at the Bank counts toward it.", 20, Ui.MUTED))
	for g in d.goals:
		body.add_child(Ui.label(tr("%s: %s of %s credits%s") % [g.name, Ui.num(g.progress), Ui.num(g.target), ("  " + tr("✓ reached!")) if g.reached else ""], 22,
			Ui.GREEN if g.reached else Ui.TEXT))
		_bar(body, float(g.progress) / float(g.target), Ui.GREEN if g.reached else Ui.GOLD)
		var drop := _small_button("Drop this goal")
		var gid: int = g.id
		drop.pressed.connect(func(): _act("goal/drop", {"goal_id": gid}))
		body.add_child(drop)
	if d.goals.size() < 3:
		var row := _row(body)
		var pick := Ui.picker()
		pick.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		var keys: Array = d.goal_choices.keys()
		for k in keys:
			pick.add_item(d.goal_choices[k])
		row.add_child(pick)
		var tgt := _amount_field("Target")
		row.add_child(tgt)
		var add := _small_button("Set goal", true)
		add.pressed.connect(func(): _act("goal", {"goal": keys[pick.selected], "target": _int(tgt)}, tr("Goal set.")))
		body.add_child(add)


# ── the savings account ──
func _savings(d: Dictionary) -> void:
	body.add_child(_heading("SAVINGS ACCOUNT"))
	body.add_child(Ui.label(tr("Balance %s credits · earns %s%% APR · take it out any time") % [Ui.num(d.savings.balance), str(d.rates.savings_apr)], 22))
	var row := _row(body)
	var amt := _amount_field()
	row.add_child(amt)
	var dep := _small_button("Deposit", true)
	dep.pressed.connect(func(): _act("deposit", {"kind": "savings", "amount": _int(amt)}, tr("Deposited.")))
	row.add_child(dep)
	var wd := _small_button("Withdraw")
	wd.pressed.connect(func(): _act("withdraw", {"amount": _int(amt)}, tr("Withdrawn.")))
	row.add_child(wd)


# ── term deposits: locked for a better rate ──
func _terms(d: Dictionary) -> void:
	body.add_child(_heading("TERM DEPOSITS"))
	body.add_child(Ui.label("Lock credits away for a better rate. Take them out before the end and you give up the interest.", 20, Ui.MUTED))
	for t in d.terms:
		var when := str(t.matures_at).substr(0, 10)
		body.add_child(Ui.label(tr("%s credits for %d weeks at %s%% APR → %s at the end (%s)%s") % [Ui.num(t.principal), t.weeks,
			str(t.apr_pct), Ui.num(t.at_maturity), when, ("  " + tr("✓ ready")) if t.matured else ""], 22, Ui.GREEN if t.matured else Ui.TEXT))
		var close := _small_button("Collect it" if t.matured else "Close early (no interest)")
		var tid: int = t.id
		close.pressed.connect(func(): _act("withdraw", {"deposit_id": tid}, tr("Deposit closed.")))
		body.add_child(close)
	var row := _row(body)
	var pick := Ui.picker()
	pick.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	var weeks := [2, 4, 8]
	for w in weeks:
		pick.add_item(tr("%d weeks · %s%% APR") % [w, str(d.rates.term_apr[str(w)])])
	row.add_child(pick)
	var amt := _amount_field()
	row.add_child(amt)
	var lock := _small_button("Lock it in", true)
	lock.pressed.connect(func(): _act("deposit", {"kind": "term", "amount": _int(amt), "weeks": weeks[pick.selected]}, tr("Locked in.")))
	body.add_child(lock)


# ── loans: the Bank weighs the application, shows the full cost first; paying early saves interest ──
func _loans(d: Dictionary) -> void:
	body.add_child(_heading("LOANS"))
	var st: Dictionary = d.standing
	body.add_child(Ui.label(tr("Your credit standing: %d / 100 (%d payments on time, %d late)") % [st.score, st.on_time, st.late], 22,
		Ui.GREEN if st.score >= 50 else Ui.GOLD))
	for l in d.loans:
		body.add_child(Ui.label(tr("%s: %s credits left · %s a week at %s%% APR · %d of %d paid · next %s") % [l.purpose, Ui.num(l.balance),
			Ui.num(l.payment), str(l.apr_pct), l.payments_made, l.weeks, str(l.next_due).substr(0, 10)], 22))
		var row := _row(body)
		var off := _small_button(tr("Pay off now: %s") % Ui.num(l.payoff), true)
		var lid: int = l.id
		off.pressed.connect(func(): _act("loan/pay", {"loan_id": lid}, tr("Loan paid off. You saved the interest you would have paid.")))
		row.add_child(off)
		var extra := _amount_field("Extra")
		row.add_child(extra)
		var pe := _small_button("Pay extra")
		pe.pressed.connect(func(): _act("loan/pay", {"loan_id": lid, "amount": _int(extra)}, tr("Paid. Less to owe, less interest.")))
		row.add_child(pe)
	body.add_child(Ui.label("Ask the Bank for a loan. It shows the whole cost before you sign. Ask yourself first: will what you buy earn more than the loan costs?", 20, Ui.MUTED))
	var row2 := _row(body)
	var amt := _amount_field("Amount")
	row2.add_child(amt)
	var wk := Ui.picker()
	wk.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	var lw: Array = d.loan_weeks
	for w in range(int(lw[0]), int(lw[1]) + 1):
		wk.add_item(tr("%d weeks") % w)
	row2.add_child(wk)
	var why := Ui.picker()
	var keys: Array = d.purposes.keys()
	for k in keys:
		why.add_item(d.purposes[k])
	body.add_child(why)
	var ask := _small_button("Ask the Bank", true)
	var answer := VBoxContainer.new()
	answer.add_theme_constant_override("separation", 10)
	ask.pressed.connect(func():
		var req := {"amount": _int(amt), "weeks": int(lw[0]) + wk.selected, "purpose": keys[why.selected]}
		var r: Dictionary = await Api.call_api("POST", "/api/dfg/bank/loan/quote", req)
		for c in answer.get_children():
			c.queue_free()
		if not r.ok:
			answer.add_child(Ui.label(r.error, 22, Ui.GOLD))
			return
		var q: Dictionary = r.data
		if not q.approved:
			answer.add_child(Ui.label(tr("Not approved. %s") % str(q.why), 22, Ui.GOLD))
			return
		answer.add_child(Ui.label(tr("Approved at %s%% APR (%d Business bars): %s credits a week for %d weeks.%s") % [str(q.apr_pct), q.bars, Ui.num(q.payment), q.weeks,
			(" " + (tr("Your top bar is gold: the Bank lends the full amount.") if q.gold else tr("The Bank lends %s; your down payment is %s of your own credits. A gold bar waives it.") % [Ui.num(q.amount), Ui.num(q.down_payment)]))], 22, Ui.GREEN))
		answer.add_child(Ui.label(tr("You'd repay %s in all: the loan costs you %s credits. Pay it off early and you pay less.") % [
			Ui.num(q.total), Ui.num(q.cost)], 22))
		var take := _small_button("Take the loan", true)
		take.pressed.connect(func(): _act("loan/take", req, tr("Loan taken. Your first payment is due in a week.")))
		answer.add_child(take))
	body.add_child(ask)
	body.add_child(answer)
