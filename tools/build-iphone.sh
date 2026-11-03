#!/bin/zsh
# Build the Godot app and install it on Eric's iPhone over the cable (set up 2026-11-02).
# Needs: Xcode with the iOS platform, Eric's Apple Account signed in to Xcode (Personal Team PJ3448UWW3),
# Godot's iOS export templates, and the iPhone plugged in, unlocked, with Developer Mode on.
# The free Personal Team's app stops opening after 7 days: run this again to reinstall.
set -e
cd "$(dirname "$0")/.."
export DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer
DEVICE="${1:-3C61D07B-952C-55B0-8311-6903F1A4F49C}"   # Eric's iPhone 13 Pro Max (xcrun devicectl list devices)
mkdir -p build/ios
# 1. Godot writes the Xcode project (the preset exports the project only; Godot's own archive step can't register a free-team device).
godot --headless --path godot --export-debug "iOS" ../build/ios/Stardust.ipa > build/ios/export.log 2>&1
# 2. Xcode builds it for this iPhone, registering the device and signing with the Personal Team.
UDID=$(xcrun devicectl device info details --device "$DEVICE" 2>/dev/null | awk '/udid:/{print $NF; exit}')
xcodebuild -project build/ios/Stardust.xcodeproj -scheme Stardust -configuration Debug -destination "id=$UDID" \
  -derivedDataPath build/ios/dd -allowProvisioningUpdates -allowProvisioningDeviceRegistration build > build/ios/xcodebuild.log 2>&1 \
  || { grep -E "error:" build/ios/xcodebuild.log; exit 1; }
# 3. Install over the cable.
xcrun devicectl device install app --device "$DEVICE" build/ios/dd/Build/Products/Debug-iphoneos/Stardust.app > /dev/null
echo "Installed on the iPhone. First launch: Settings > General > VPN & Device Management > trust the Apple Account."
