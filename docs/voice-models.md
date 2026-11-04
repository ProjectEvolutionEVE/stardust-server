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
| Kate 1 - Warm, Close and Natural | by name (library ID `EYBbN7OENxAX5QX56IiW`; in My Voices on the 6e7e account, 10-28) | fr, ko, tr, pt-BR | Spanish (Latin American) +19, incl. French, Korean, Turkish, Portuguese, Arabic, German, English (Eric's screenshot 10-28) |
| Johanna - Podcast Host, bright, warm (chosen by Eric 10-28; the old Spanish set was a male voice) | by name (library ID `c338PHkXJ2cW8fdMPhzP`) | es (Latin American) | Spanish, Latin American (verified badge) |
| Julia (Russian) | `MOgsVr0EwwxqQs5cNDhu` | ru | not yet written down: check in ElevenLabs |
| Sumiko Ito - Crisp | `0yh9saSHWVy78QG1HfNs` | ja | not yet written down: check in ElevenLabs |
| Sara - Soft, Expressive, and Warm (chosen by Eric 10-27) | by name (library ID `XTa3iQyMA6f1qrI4F6kZ`; a My Voices copy has its own ID) | ar | Arabic, Modern Standard (verified badge in the Voice Library) |

**Hindi and the other Indian languages: Sarvam, not ElevenLabs.** Eric picked Sarvam **Bulbul v3, speaker `priya`** on
2026-09-30, from the six samples in `Inara-Voice/Stardust-TerraDeleta_Inara_hi_Sarvam-samples/` (Priya, Neha, Kavya,
Shreya, Ritu, Simran): *"authoritative, clean and clear."* The others were too slow, too sensual or too young, and one
had overlapping, doubled vocals. Use Priya for the other Indian languages too (bn, mr, te, ta planned). Check every
render for doubled or overlapping audio. Sarvam's translation (Mayura) was too literal on game terms ("Recovery",
"sweep the field"), so a game-term glossary comes first. Cost then: Bulbul about ₹3 per 1,000 characters. (Record found
11-03 in the Signal in the Noise notes, the same Inara; no ElevenLabs Hindi voice was ever chosen.)

**Arabic (10-26):**
- The 179 Arabic lines now on the server were recorded in Lily by mistake, and Lily is not verified in Arabic.
- Once Eric picks an Arabic voice, add it above and to `VOICE_BY_LANG`, then re-record into a fresh folder:
  `python3 tools/inara-record.py --lang ar --out "~/Desktop/Stardust - Terra Deleta/Inara-Voice/Stardust-TerraDeleta_Inara_ar_Sara-new"`
- Replace `~/Desktop/Stardust - Terra Deleta/Inara-Voice/Stardust-TerraDeleta_Inara_ar_Sara` with that folder, then upload with `python3 tools/upload-voice.py --only ar --redo INARA-` to replace the server's copies.

**Arabic Gauntlet result (Eric ran `tools/inara-certify.py --lang ar`, 10-26):** Lily's Arabic passed on all 14 of the
hardest lines (round-trip 96.8%-100%, clean tails).
- Two lines need an ear-check:
  - INARA-FAQ-013, where "900" was heard as a non-word;
  - INARA-FAQ-035, where the last word lifts like a question (+64 Hz).
- Minor: Inara's name was heard as إنارة, and على متن ran together on STORY-001.
- The round trip tests that the speech is understood. It does not test a native accent, and Lily is still not
  ElevenLabs-verified in Arabic. Eric decides: keep it, or replace it with a verified Arabic voice.

**Full Arabic round trip (Whisper large-v3, float32, local; 10-26):**
- Of 179 lines, 139 match 95% or better, 34 match 85-95%, and 6 come back under 85%.
- 7 words came back as different words, all on Arabic's hard sounds: ق→غ, س→ص, a lost shadda, م→ن.
- Most other differences are the ear, not the voice: English words, numbers, and words run together.
- Verdict: understandable, but not native-clean. The same pattern as Lily's Tamil in July.
- Details: `~/Desktop/Stardust - Terra Deleta/Inara-Voice/Stardust-TerraDeleta_Inara_ar_Sara_checks/verdict.md` and `report.txt`.

**Sara test (10-27, the same 14 hardest lines, Whisper large-v3 local):** Lily scored better than Sara.
- **Sara:** more mishearings. Numbers came out garbled (the 1.6 / 1.2 / 1.92 line). ارفع was heard as the feminine
  ارفعي, and المس as الماس. The English UI words were spelled out.
- **Lily:** only the name and ship-name variants, plus one vowel.
- **Note:** the round trip measures how clearly the words come across, not how native the accent is.
- **Decision for Eric:** keep Lily's Arabic, try another verified Arabic voice, or have a native speaker judge 2-3
  lines of each (`~/Desktop/Stardust - Terra Deleta/Inara-Voice/Stardust-TerraDeleta_Inara_ar_Sara/raw/` and `~/Desktop/Stardust - Terra Deleta/Inara-Voice/Stardust-TerraDeleta_Inara_ar_Sara_SPARE-second-take/raw/`).

**DECIDED (Eric 10-27): Sara is Inara's Arabic voice.** ElevenLabs verifies her in Arabic, so we trust that and spend no more credits on tests. Next: record all 179 lines in Sara and upload them, replacing Lily's.

**DONE (10-27 evening): all 179 Arabic lines are recorded in Sara and live on the server** (`~/Desktop/Stardust - Terra Deleta/Inara-Voice/Stardust-TerraDeleta_Inara_ar_Sara`, uploaded with `upload-voice.py --only ar --redo INARA-`; spot-checked byte-for-byte against `/voice/ar/`). A second full Sara take was recorded by mistake into `~/Desktop/Stardust - Terra Deleta/Inara-Voice/Stardust-TerraDeleta_Inara_ar_Sara_SPARE-second-take` (16,218 characters spent again); it is a spare and is not uploaded. Sara's key is saved in `~/.stardust-elevenlabs-sara-key` (chmod 600).

**Spoken-words rule (Eric 10-27):** voice scripts spell out every number and carry no quotes, brackets or other symbols. A Whisper check of the two hardest Arabic lines found Sara misreading the numbers: 1800 was heard as 1200, and 1.6, 1.2, 1.0 and 1.92 came out garbled. All 22 Arabic lines with digits or symbols were rewritten in `docs/inara-lines/ar.json` (4,751 characters to re-record). FAQ-026 no longer reads out the sample receipt code. The other languages' scripts still have digits (20-29 lines each); they need the same rewrite before any re-recording.

**Which account (Eric 10-28):** Inara's voices are recorded on the ElevenLabs account whose API key ends **6e7e**, saved in `~/.stardust-elevenlabs-sara-key` (the recorder's default). It has Lily, Sara and Johanna. The key in `~/.stardust-elevenlabs-key` (...dec6) is a different account with neither Johanna nor Kate 1: don't use it for Inara.


**Intro narration (11-04):** the 4 intro parts recorded in Arabic (Sara, eleven_multilingual_v2, 1,267 characters) and Hindi (Sarvam priya, 1,574 characters) by `Inara-Novel/make_intro_lang.py`; files in `Inara-Novel/Audiobook/intro/<lang>/`.
