# Inara's voice models: master list

**Rules (Eric):**
- One Inara, voiced in each language by the voice that speaks it best. The voices were hand-picked by Eric on 10-19 (`docs/inara-recording-script.md`).
- A voice records only languages ElevenLabs lists as **verified** for it (Eric 10-26).
- No language is recorded until Eric has chosen its voice.

`tools/inara-record.py` follows this list:
- It takes each language's voice from `VOICE_BY_LANG`, which matches the table below.
- It stops before charging anything if the voice isn't verified in that language, or if no voice has been chosen yet.

Keep this file, `VOICE_BY_LANG` and the recording script in step.

| Voice (ElevenLabs) | Voice ID | Inara's languages | Verified languages (ElevenLabs) |
|---|---|---|---|
| Lily - Velvety Actress (British) | (by name) | en, zh (Simplified and Traditional), de, pl | English, Italian, German, Chinese, Czech, Dutch, Polish (checked by Eric 10-26) |
| Kate 1 - Warm, Close and Natural | (by name) | es (Latin American), fr, ko, tr, pt-BR | not yet written down: check in ElevenLabs |
| Julia (Russian) | `MOgsVr0EwwxqQs5cNDhu` | ru | not yet written down: check in ElevenLabs |
| Sumiko Ito - Crisp | `0yh9saSHWVy78QG1HfNs` | ja | not yet written down: check in ElevenLabs |
| *(Arabic female voice: Eric choosing, 10-26)* | | ar | must list Arabic |

**Arabic (10-26):**
- The 179 Arabic lines now on the server were recorded in Lily by mistake, and Lily is not verified in Arabic.
- Once Eric picks an Arabic voice, add it above and to `VOICE_BY_LANG`, then re-record into a fresh folder:
  `python3 tools/inara-record.py --lang ar --out ~/Desktop/inara-ar-new`
- Replace `~/Desktop/inara-ar` with that folder, then upload with `python3 tools/upload-voice.py --only ar --redo INARA-` to replace the server's copies.
