# Stardust – Terra Deleta: Godot 4 client

First pass: title, sign-in (email or phone + 6-digit code), name and language setup, Private Quarters (Bed tab live; other tabs placeholders). Talks to the live game server.

Not yet tested in Godot. To try it: open Godot 4.3+, Import, pick `godot/project.godot`, then press Run (the ▶ at top right).

## On Eric's iPhone (set up 2026-11-02)

`tools/build-iphone.sh` builds the app and installs it over the cable, in about 30 seconds. Run it from the repository root
with the iPhone plugged in and unlocked. It uses:

- **Xcode 26.5** with the iOS 26.5 platform (Xcode > Settings > Components), and `xcode-select` pointing at Xcode.
- **Eric's Apple Account** signed in to Xcode (Settings > Apple Accounts), **free Personal Team `PJ3448UWW3`**. If a build says
  the login was rejected, or Teams is empty, sign out and back in there.
- **Godot 4.7.2** with the **iOS export templates** (Editor > Manage Export Templates).
- The **iOS export preset** in `export_presets.cfg`: app ID `com.risesolutions.stardust`; it exports the Xcode project only, and the
  script builds it with `xcodebuild` (Godot's own archive step can't register a free-team device).
- The iPhone: **Developer Mode** on (Settings > Privacy & Security), paired with this Mac; on first launch, trust the Apple Account
  (Settings > General > VPN & Device Management).

Limits of the free team: the app stops opening after **7 days** (run the script again), and it installs only on phones plugged in
to this Mac. Sharing without a cable needs the paid Apple Developer Program (TestFlight); Android can share an APK file instead.
The app icon `assets/icon.png` is a **temporary** crop of `static/og-card.jpg` (the old finned Starship): replace it before release.

