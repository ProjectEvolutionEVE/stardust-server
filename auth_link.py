"""The game's ONE link to Quavara: who is this player?

Quavara (core) will hand the signed-in member a short-lived GAME PASS: a JWT signed with DFG_PASS_KEY carrying
{sub: qcid, name, exp}. The game only checks the signature, so it never reads Quavara's database. A buyer or licensee
replaces this file with their own login and nothing else changes.

DFG_DEV_AUTH=1 (local tests only) accepts an 'X-Dev-Player: <id>' header instead. Never set it on a hosted service."""
import os
import jwt

PASS_KEY = os.environ.get("DFG_PASS_KEY", "")
DEV = os.environ.get("DFG_DEV_AUTH") == "1"


class NotSignedIn(Exception):
    pass


def player_from(headers):
    """Return (qcid, display_name) for the request, or raise NotSignedIn."""
    if DEV and headers.get("X-Dev-Player"):
        q = headers["X-Dev-Player"].strip()[:64]
        return "dev:" + q, q
    auth = headers.get("Authorization", "")
    if not auth.startswith("Bearer ") or not PASS_KEY:
        raise NotSignedIn("Sign in with your Quavara account to play.")
    try:
        claims = jwt.decode(auth[7:], PASS_KEY, algorithms=["HS256"], options={"require": ["sub", "exp"]})
    except jwt.PyJWTError:
        raise NotSignedIn("Your game pass has expired. Sign in again.")
    return str(claims["sub"]), (claims.get("name") or "")[:64]
