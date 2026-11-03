#!/usr/bin/env python3
"""The crew's tool for two accounts one person made by mistake (Eric 11-03): see what each holds, then move one SDID's
sign-ins to the other. The absorbed account keeps its data untouched (nothing is deleted) but can no longer be signed
into. Uses the upload key (~/.stardust-upload-key), never a player's sign-in.

  python3 tools/merge-accounts.py show --email you@example.com
  python3 tools/merge-accounts.py show --phone "+1 574 555 0123"       (or --sdid SD-XXXX-XXXX-XXXX)
  python3 tools/merge-accounts.py merge --keep SD-AAAA-… --absorb SD-BBBB-…           (a dry run: shows both)
  python3 tools/merge-accounts.py merge --keep SD-AAAA-… --absorb SD-BBBB-… --really  (moves the sign-ins)
"""
import argparse, json, os, sys, urllib.parse, urllib.request, urllib.error

SERVER = "https://game-server-production-9863.up.railway.app"


def call(method, path, key, body=None):
    req = urllib.request.Request(SERVER + path, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"X-Upload-Key": key, "Content-Type": "application/json"})
    try:
        return json.loads(urllib.request.urlopen(req, timeout=60).read())
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode()[:300]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("what", choices=["show", "merge"])
    ap.add_argument("--email"); ap.add_argument("--phone"); ap.add_argument("--sdid")
    ap.add_argument("--keep"); ap.add_argument("--absorb"); ap.add_argument("--really", action="store_true")
    ap.add_argument("--server", default=SERVER); ap.add_argument("--key-file", default="~/.stardust-upload-key")
    a = ap.parse_args()
    global SERVER; SERVER = a.server.rstrip("/")
    key = open(os.path.expanduser(a.key_file)).read().strip()
    if a.what == "show":
        q = {"sdid": a.sdid} if a.sdid else {"channel": "email", "address": a.email} if a.email else {"channel": "sms", "address": a.phone}
        print(json.dumps(call("GET", "/api/dfg/admin/account?" + urllib.parse.urlencode(q), key), indent=1, ensure_ascii=False))
        return
    r = call("POST", "/api/dfg/admin/merge", key, {"keep": a.keep, "absorb": a.absorb, "dry_run": not a.really})
    print(json.dumps(r, indent=1, ensure_ascii=False))
    if not a.really:
        print("\nDry run only. Add --really to move the sign-ins.")


if __name__ == "__main__":
    main()
