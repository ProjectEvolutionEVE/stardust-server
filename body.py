"""The character's body (Eric 10-11). Three bars, 0-100: stamina, energy and mental focus.
  · Awake (online, or working offline), each drains 2.2 points an hour: a 16-hour day takes 100% to 65%.
  · Asleep in the cockpit, out in space (Eric 10-24), half that: 35 points per 12 hours. The bed is the best rest.
  · Asleep in bed, each refills 35 points per 6 hours (about 5.83 an hour): 6 hours takes 65% back to 100%; from 50% it
    takes about 8.5 hours. The game runs in real time: rest never speeds anything else up.
  · Abilities decline slightly near the top, severely below 65% (the lowest recommended level) and extremely below 50%.
The database keeps each bar's value at `body_at` and whether the character is asleep; the value now is worked out here."""
from datetime import datetime, timezone

DRAIN_PER_HOUR = 2.2
REST_PER_HOUR = 35 / 6
COCKPIT_REST = 0.5            # sleeping in the cockpit refills at half the bed's rate
PLACES = ("bed", "cockpit")
BARS = ("stamina", "energy", "focus")
RECOMMENDED = 65
IMPAIRED = 50


def _now():
    return datetime.now(timezone.utc)


def current(row, now=None):
    """Each bar's value right now, from the stored value, the time it was stored and whether the character slept since."""
    hours = max(0.0, ((now or _now()) - row["body_at"]).total_seconds() / 3600)
    out = {}
    for b in BARS:
        v = float(row[b])
        rest = REST_PER_HOUR * (COCKPIT_REST if row["rest_place"] == "cockpit" else 1.0)
        v = v + rest * hours if row["asleep"] else v - DRAIN_PER_HOUR * hours
        out[b] = round(min(100.0, max(0.0, v)), 2)
    return out


def ability(v):
    """How well the character performs at bar level v, from 1.0 (fully rested) down: slight above 65, severe 65-50,
    extreme below 50 (Eric 10-11). The exact curve is a first setting to tune in playtesting."""
    if v >= RECOMMENDED:
        return round(1.0 - 0.10 * (100 - v) / (100 - RECOMMENDED), 3)          # 1.00 -> 0.90
    if v >= IMPAIRED:
        return round(0.90 - 0.30 * (RECOMMENDED - v) / (RECOMMENDED - IMPAIRED), 3)  # 0.90 -> 0.60
    return round(max(0.2, 0.60 - 0.40 * (IMPAIRED - v) / IMPAIRED), 3)           # 0.60 -> 0.20


def warning(bars):
    low = min(bars.values())
    if low < IMPAIRED:
        return "You're running on empty. Below 50% you can't do your duties properly. Get to your bed and rest."
    if low < RECOMMENDED:
        return "You're pushing past healthy limits. Rest soon: 65% is the lowest recommended level."
    return None


async def set_state(conn, pid, asleep, place="bed"):
    """Bring the bars up to now (at the rate of wherever they were resting), then switch between awake and asleep,
    in bed or in the cockpit."""
    if place not in PLACES:
        raise ValueError("place")
    row = await conn.fetchrow("SELECT stamina, energy, focus, body_at, asleep, rest_place FROM players WHERE id=$1 FOR UPDATE", pid)
    cur = current(row)
    await conn.execute("UPDATE players SET stamina=$2, energy=$3, focus=$4, body_at=now(), asleep=$5, rest_place=$6 WHERE id=$1",
                       pid, cur["stamina"], cur["energy"], cur["focus"], asleep, place)
    return cur
