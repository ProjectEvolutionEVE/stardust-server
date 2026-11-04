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


## When the paid Apple Developer Program is active (prepared 2026-11-02, not done yet)

What changes, in order. Joining costs $99 a year and is Eric's decision.

1. **Enrol** at developer.apple.com/programs. As **Rise Solutions LLC** (organisation) the store shows the company as the seller,
   which needs a **D-U-N-S number** for the LLC (free from Dun & Bradstreet, can take days); as an individual it shows Eric's name.
2. **Team ID:** the new team gets its own ID. Put it in `export_presets.cfg` (`application/app_store_team_id`, now the free
   `PJ3448UWW3`) and sign in to Xcode with the same Apple Account; the team appears under Teams.
3. **App record:** in App Store Connect create the app with bundle ID `com.risesolutions.stardust` (unchanged) and the name
   "Stardust - Terra Deleta" (a working title until the attorney clears it: see CLAUDE.md, still-open item 1).
4. **Upload key:** in App Store Connect > Users and Access > Integrations, create an **App Store Connect API key** (the .p8 file,
   its Key ID and Issuer ID) so builds upload from the command line. Keep it out of git; record where it lives in
   `~/Quavara/CURRENT.md`.
5. **Release build:** set `application/export_method_release=0` (App Store) in the preset, then archive and upload:
   `xcodebuild ... -configuration Release archive`, `xcodebuild -exportArchive` with method `app-store-connect`, and
   `xcrun altool --upload-app` with the API key. A `tools/upload-testflight.sh` beside `build-iphone.sh` should do this.
6. **TestFlight:** internal testers (up to 100 on the team) right away; external testers (up to 10,000, by link) after Apple's
   beta review. Builds last 90 days.

**Apple asks for these before external testing or the App Store** (to settle then, not now):
- A **privacy policy URL** (rule 4: only the phone or email is kept), e.g. on risesolutions-llc.com/stardust/.
- The **App Privacy** answers in App Store Connect (contact info: email or phone, used for sign-in only).
- **Account deletion inside the app** (Apple guideline 5.1.1(v): apps that create accounts must let players delete them). Not built
  yet: it needs a server route and a button, likely on the Bed.
- **Export compliance:** the game uses only standard HTTPS, so `ITSAppUsesNonExemptEncryption = NO` in the Info.plist.
- A **real app icon** and screenshots (the current icon is temporary).
- The store's **age rating questionnaire** (it's about content; players are still never asked their age, rule 5).
