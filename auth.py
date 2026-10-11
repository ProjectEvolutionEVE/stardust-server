"""Sign-up and sign-in: the game's OWN accounts (Eric 10-11; replaces the old Quavara game-pass link, auth_link.py).

How it works:
  · The player gives a phone number OR an email address and gets a 6-digit code (no passwords).
      - Phone: Twilio Verify sends and checks the code (subaccount "Stardust game", env TWILIO_*). Twilio holds the code.
      - Email: the server makes the code itself and keeps only a hash of it. Sending it needs the game's own Resend
        address, which doesn't exist yet, so email sign-in is closed on the hosted server until then.
      - DFG_SHOW_CODES=1 (local tests only) makes the server keep phone codes itself too and hand every code back in the
        reply instead of sending it. NEVER set it on Railway: anyone could then sign in as anyone.
  · The only personal information kept is the phone number or email address (`logins`). No age, no real name.
  · A correct code gives the player a sign-in token. The server keeps only a hash of it, so a leaked database can't be
    used to sign in.
  · Limits, so nobody can drain the Twilio balance or guess codes: 5 codes per address and 20 per network address per
    hour, codes last 10 minutes, and 5 wrong tries end a code.

DFG_DEV_AUTH=1 (local tests only) also accepts an 'X-Dev-Player: <id>' header. Never set it on a hosted service."""
import os, re, json, hashlib, secrets
import aiohttp

DEV = os.environ.get("DFG_DEV_AUTH") == "1"
SHOW_CODES = os.environ.get("DFG_SHOW_CODES") == "1"
TW_SID = os.environ.get("TWILIO_ACCOUNT_SID", "")
TW_KEY = os.environ.get("TWILIO_API_KEY_SID", "")
TW_SECRET = os.environ.get("TWILIO_API_KEY_SECRET", "")
TW_VERIFY = os.environ.get("TWILIO_VERIFY_SID", "")
CODE_MINUTES = 10
MAX_TRIES = 5
PER_ADDRESS_HOUR = 5
PER_IP_HOUR = 20
TOKEN_IDLE_DAYS = 30


class NotSignedIn(Exception):
    pass


class Refused(Exception):
    """The message is shown to the player."""


def _h(s):
    return hashlib.sha256(s.encode()).hexdigest()


def normalize(channel, address):
    """A phone number as +<digits> (international form), or an email in lower case. Refuses anything else."""
    a = (address or "").strip()
    if channel == "sms":
        digits = re.sub(r"[\s\-().]", "", a)
        if not re.fullmatch(r"\+[1-9]\d{7,14}", digits):
            raise Refused("Enter your mobile number with its country code, for example +1 574 555 0123.")
        return digits
    if channel == "email":
        a = a.lower()
        if len(a) > 254 or not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", a):
            raise Refused("That doesn't look like an email address.")
        return a
    raise Refused("Choose phone or email.")


def _twilio_ready():
    return bool(TW_SID and TW_KEY and TW_SECRET and TW_VERIFY)


async def _twilio(path, form):
    """POST to Twilio Verify. Returns (status, body); a network failure comes back as (599, {})."""
    url = f"https://verify.twilio.com/v2/Services/{TW_VERIFY}/{path}"
    try:
        async with aiohttp.ClientSession(auth=aiohttp.BasicAuth(TW_KEY, TW_SECRET)) as s:
            async with s.post(url, data=form, timeout=aiohttp.ClientTimeout(total=15)) as r:
                return r.status, (await r.json(content_type=None)) or {}
    except Exception as e:                        # never show the player (or the logs) anything but the kind of failure
        print(f"twilio {path} failed: {type(e).__name__}", flush=True)
        return 599, {}


async def start(conn, channel, address, ip, language=None):
    """Send a sign-in code. Returns {'sent': True} (plus 'dev_code' when DFG_SHOW_CODES=1)."""
    addr = normalize(channel, address)
    n_addr = await conn.fetchval("SELECT count(*) FROM login_attempts WHERE address=$1 AND at > now() - interval '1 hour'", addr)
    n_ip = await conn.fetchval("SELECT count(*) FROM login_attempts WHERE ip=$1 AND at > now() - interval '1 hour'", ip or "")
    if n_addr >= PER_ADDRESS_HOUR or n_ip >= PER_IP_HOUR:
        raise Refused("Too many codes requested. Please wait an hour and try again.")
    await conn.execute("INSERT INTO login_attempts(channel, address, ip) VALUES($1,$2,$3)", channel, addr, ip or "")
    if channel == "sms" and not SHOW_CODES:
        if not _twilio_ready():
            raise Refused("Text-message sign-in isn't switched on yet.")
        # The text is in English for now; Twilio's own languages (its "Locale" list) differ from ours, so matching
        # the player's language is a later step.
        status, body = await _twilio("Verifications", {"To": addr, "Channel": "sms"})
        if status >= 300:
            print(f"twilio send refused: status {status} code {body.get('code')}", flush=True)
            raise Refused("We couldn't text that number. Check it and try again.")
        return {"sent": True}
    if channel == "email" and not SHOW_CODES:
        raise Refused("Email sign-in opens soon. Please use your phone for now.")
    code = f"{secrets.randbelow(10**6):06d}"
    await conn.execute("UPDATE login_codes SET used_at=now() WHERE address=$1 AND used_at IS NULL", addr)  # one live code
    await conn.execute("""INSERT INTO login_codes(channel, address, code_hash, expires_at)
                          VALUES($1,$2,$3, now() + make_interval(mins => $4))""", channel, addr, _h(addr + ":" + code), CODE_MINUTES)
    return {"sent": True, "dev_code": code}


async def check(conn, channel, address, code):
    """True if the code is right. Wrong or expired codes return False; too many wrong tries end the code."""
    addr = normalize(channel, address)
    code = re.sub(r"\D", "", code or "")
    if len(code) != 6:
        return False
    if channel == "sms" and not SHOW_CODES:
        if not _twilio_ready():
            return False
        status, body = await _twilio("VerificationCheck", {"To": addr, "Code": code})
        return status < 300 and body.get("status") == "approved"
    row = await conn.fetchrow("""SELECT id, code_hash, tries FROM login_codes WHERE address=$1 AND used_at IS NULL
                                 AND expires_at > now() ORDER BY id DESC LIMIT 1""", addr)
    if not row:
        return False
    if secrets.compare_digest(row["code_hash"], _h(addr + ":" + code)):
        await conn.execute("UPDATE login_codes SET used_at=now() WHERE id=$1", row["id"])
        return True
    await conn.execute("UPDATE login_codes SET tries = tries + 1, used_at = CASE WHEN tries + 1 >= $2 THEN now() END WHERE id=$1",
                       row["id"], MAX_TRIES)
    return False


async def issue_token(conn, pid):
    token = secrets.token_urlsafe(32)
    await conn.execute("INSERT INTO auth_tokens(token_hash, player_id) VALUES($1,$2)", _h(token), pid)
    return token


async def revoke(conn, token):
    await conn.execute("UPDATE auth_tokens SET revoked_at=now() WHERE token_hash=$1 AND revoked_at IS NULL", _h(token))


def bearer(headers):
    auth = headers.get("Authorization", "")
    return auth[7:].strip() if auth.startswith("Bearer ") else ""


async def player_from(conn, headers):
    """The signed-in player's id, or raise NotSignedIn. (Dev header first, local tests only.)"""
    if DEV and headers.get("X-Dev-Player"):
        return ("dev", headers["X-Dev-Player"].strip()[:64])
    token = bearer(headers)
    if not token:
        raise NotSignedIn("Please sign in.")
    pid = await conn.fetchval(
        f"""UPDATE auth_tokens SET last_seen_at=now() WHERE token_hash=$1 AND revoked_at IS NULL
            AND last_seen_at > now() - interval '{TOKEN_IDLE_DAYS} days' RETURNING player_id""", _h(token))
    if pid is None:
        raise NotSignedIn("Your sign-in has expired. Please sign in again.")
    return ("id", pid)
