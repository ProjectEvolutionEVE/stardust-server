"""The review team's tool for blueprints (rule 23; blueprints.py). Players design; the team reviews.

    python3 review.py list                      blueprints waiting for the team (submitted), oldest first
    python3 review.py show ID                   the whole form, its weight and size, and the notes so far
    python3 review.py ask ID "question"         ask the designer something (it stays with the team)
    python3 review.py changes ID "what"         send it back with the changes needed
    python3 review.py approve ID ["note"]       approve it: it becomes a design that can be built and sold
    python3 review.py reject ID "why"           turn it down
    python3 review.py furnace ID KG MINUTES     mark an approved design as a furnace: KG of ore a batch, MINUTES a batch
                                                (the team sets these from the design, Eric 11-03; workshop.py)

Needs DATABASE_URL (the game's database). The designer sees every note as from "The review team"; the name given in
REVIEWER (default "Review team") is kept on the record only."""
import asyncio, json, os, sys
import asyncpg
import blueprints as BP
import store as ST
import workshop as WS


async def main(args):
    if not args or args[0] not in ("list", "show", "ask", "changes", "approve", "reject", "furnace"):
        raise SystemExit(__doc__)
    who = os.environ.get("REVIEWER", "Review team")
    conn = await asyncpg.connect(os.environ["DATABASE_URL"])
    try:
        cmd = args[0]
        if cmd == "list":
            rows = await conn.fetch("""SELECT s.id, s.title, s.version, s.updated_at, p.first_name, p.last_name FROM blueprint_submissions s
                                       JOIN players p ON p.id=s.designer_id WHERE s.status='submitted' ORDER BY s.updated_at""")
            for r in rows:
                print(f"#{r['id']}  {r['title']}  (version {r['version']}, by {r['first_name']} {r['last_name']}, {r['updated_at']:%Y-%m-%d %H:%M} UTC)")
            print(f"{len(rows)} waiting.")
            return
        sid = int(args[1])
        text = " ".join(args[2:]).strip()
        if cmd == "furnace":
            if len(args) != 4:
                raise SystemExit("review.py furnace ID KG MINUTES")
            product = await WS.mark_furnace(conn, sid, args[2], args[3])
            print(f"#{sid} ({product}) is a furnace: {float(args[2]):g} kg of ore a batch, {int(args[3])} minutes a batch.")
            return
        if cmd == "show":
            s = await conn.fetchrow("SELECT * FROM blueprint_submissions WHERE id=$1", sid)
            if not s:
                raise SystemExit("No such blueprint.")
            form = json.loads(s["form"])
            t = BP.totals(form)
            print(f"#{sid}  {s['title']}  [{s['status']}, version {s['version']}]")
            for k, q in BP.QUESTIONS:
                if k == "parts":
                    print(f"\n{q.upper()}:")
                    for p in form.get("parts") or []:
                        print(f"  {p['name']}: " + ", ".join(f"{BP.MATERIALS[m['item']]['name']} {(m['grams'] or 0) / 1000:g} kg" for m in p["materials"]))
                elif k == "books":
                    print(f"\n{q.upper()}: " + ", ".join(BP.BOOK_NAMES[b] for b in form.get("books") or []))
                elif k == "origin":
                    print(f"\n{q.upper()}: {BP.ORIGINS.get(form.get('origin'), form.get('origin'))}")
                    if form.get("based_on"):
                        name = await conn.fetchval("SELECT name FROM item_types WHERE code=$1", form["based_on"])
                        print(f"  BUILDS ON: {name} ({form['based_on']})\n  WHAT'S DIFFERENT: {form.get('changes')}")
                elif k == "build_minutes":
                    print(f"\n{q.upper()}: {form.get('build_minutes')} minutes")
                else:
                    print(f"\n{q.upper()}: {form.get(k)}")
            print(f"\nWEIGHT {t['mass_kg']:g} kg · MATERIAL VOLUME {t['volume_m3']:g} m³")
            for m in await BP.thread(conn, sid):
                print(f"  [{m['kind']}, v{m['version']}] {m['from_reviewer'] or 'designer'}: {m['body']}")
            return
        if cmd in ("ask", "changes", "reject") and not text:
            raise SystemExit("Write the message too.")
        if cmd == "ask":
            await BP.ask(conn, sid, who, text)
        elif cmd == "changes":
            await BP.request_changes(conn, sid, who, text)
        elif cmd == "approve":
            code = await BP.approve(conn, sid, who, text or "Approved.")
            model = await conn.fetchval("SELECT model_code FROM item_types WHERE code=$1", code)
            print(f"Design: {code} · model {model} · the designer's original: {model}-ORIGINAL")
        elif cmd == "reject":
            await BP.reject(conn, sid, who, text)
        print("Done.")
    except ST.Refused as e:
        raise SystemExit(str(e))
    finally:
        await conn.close()


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))
