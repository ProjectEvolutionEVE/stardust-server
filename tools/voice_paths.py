"""Where Inara's Stardust - Terra Deleta recordings live on this iMac (Eric 11-03).

One folder per language inside ~/Desktop/Stardust - Terra Deleta/Inara-Voice/, named for the game, the language and the
voice: Stardust-TerraDeleta_Inara_<lang>_<Voice> (e.g. Stardust-TerraDeleta_Inara_ar_Sara), with raw/, radio/ and
lines.json inside; the files keep their line codes (INARA-CALL-001.mp3), which the game uses to find them.
Signal in the Noise keeps its own recordings apart (Quavara's games-holdback/voice). A line used by both games gets a
copy for each, named for its game, language and voice (Eric 11-03); the two games' files are never mixed.
"""
import glob
import os
import re

ROOT = os.path.expanduser("~/Desktop/Stardust - Terra Deleta/Inara-Voice")
PREFIX = "Stardust-TerraDeleta_Inara_"
# the voice in each language's folder name (docs/voice-models.md is the master list)
VOICE_NAME = {"en": "Lily", "zh": "Lily", "de": "Lily", "pl": "Lily",
              "fr": "Kate1", "ko": "Kate1", "tr": "Kate1", "pt-BR": "Kate1",
              "es": "Johanna", "ru": "Julia", "ja": "SumikoIto", "ar": "Sara"}


def voice_dir(lang):
    """The language's main folder: the set that gets uploaded to the game server."""
    return os.path.join(ROOT, f"{PREFIX}{lang}_{VOICE_NAME.get(lang, 'NoVoiceYet')}")


def language_dirs():
    """{language: main folder} for every language recorded (spare takes and check folders left out)."""
    out = {}
    for d in sorted(glob.glob(os.path.join(ROOT, PREFIX + "*"))):
        m = re.fullmatch(re.escape(PREFIX) + r"([A-Za-z-]+)_([A-Za-z0-9]+)", os.path.basename(d))
        if m and os.path.isdir(d) and VOICE_NAME.get(m.group(1)) == m.group(2):
            out[m.group(1)] = d
    return out
