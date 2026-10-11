"""Debris-field game rules the SERVER enforces (mirrors games-holdback/games/debris-flight.js; keep the two in step).

Why the server re-checks: the browser can be edited, so the client's word is never trusted for anything that has value.
The server recomputes mass from real density, re-checks that the piece's shape fits the hold and that its bulk fits
the room left, and refuses collects faster than collecting physically takes."""

DENSITY = {  # kg per cubic metre, real values
    "iron": 5150,      # hematite iron ore
    "copper": 8960,
    "silver": 10490,
    "gold": 19300,
    "diamond": 3510,
}
ICO_VOL = 2.536          # volume of the icosahedron rocks are drawn from, per unit scale³
MIN_COLLECT_S = 2.0      # the quickest a piece can come aboard (client: 2 s + more for bigger pieces)
MAX_PIECE_DIM = 9.0      # metres; nothing in the universe is bigger than a large chunk


class Refused(Exception):
    """A collect the rules don't allow. The message is shown to the player."""


def piece(material, dims, volume_m3):
    """Validate one claimed piece and return its server-side facts (dims sorted, box, mass)."""
    if material not in DENSITY:
        raise Refused("Unknown material.")
    try:
        d = sorted((float(x) for x in dims), reverse=True)
        vol = float(volume_m3)
    except (TypeError, ValueError):
        raise Refused("Bad piece size.")
    if len(d) != 3 or any(not (0.01 <= x <= MAX_PIECE_DIM) for x in d):
        raise Refused("Bad piece size.")
    box = d[0] * d[1] * d[2]
    # an icosahedron fills ~0.52 of its box; allow some slack, never more than the box itself
    if not (0.2 * box <= vol <= box):
        raise Refused("Bad piece volume.")
    return {"dims": d, "box": box, "volume": vol, "mass": vol * DENSITY[material]}


def shape_fits(dims_sorted, hold_dims):
    h = sorted(hold_dims, reverse=True)
    return all(a <= b + 1e-9 for a, b in zip(dims_sorted, h))


def room_for(box, used_box, hold_dims):
    cap = hold_dims[0] * hold_dims[1] * hold_dims[2]
    return used_box + box <= cap + 1e-9


def _selftest():
    ok = True
    def check(name, cond):
        nonlocal ok
        print(("PASS " if cond else "FAIL ") + name); ok &= bool(cond)
    hold = (1.6, 1.2, 1.0)
    p = piece("gold", [0.10, 0.18, 0.15], 0.0014)
    check("dims sorted largest first", p["dims"] == [0.18, 0.15, 0.10])
    check("mass from real density", abs(p["mass"] - 0.0014 * 19300) < 1e-9)
    check("small piece fits shape", shape_fits(p["dims"], hold))
    check("1.7 m piece does not fit a 1.6 m hold", not shape_fits([1.7, 0.5, 0.5], hold))
    check("turning a piece is allowed (1.1 x 1.5 x 0.9 fits)", shape_fits(sorted([1.1, 1.5, 0.9], reverse=True), hold))
    check("bulk counts, not volume: 1.9 m³ used + 0.1 box > 1.92", not room_for(0.1, 1.9, hold))
    try: piece("unobtainium", [1, 1, 1], 0.5); check("unknown material refused", False)
    except Refused: check("unknown material refused", True)
    try: piece("iron", [1, 1, 1], 2.0); check("volume bigger than its box refused", False)
    except Refused: check("volume bigger than its box refused", True)
    print("ALL PASS" if ok else "SOME FAILED"); return ok


if __name__ == "__main__":
    raise SystemExit(0 if _selftest() else 1)
