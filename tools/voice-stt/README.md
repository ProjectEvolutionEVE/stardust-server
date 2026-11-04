# Voice round-trip check: did Inara say the words right? (Eric 10-26)

Each recording is transcribed back to text by a speech-to-text ear and compared word by word with the script. If a hard
sound is mispronounced, the ear hears a different word: Inara's July method, which caught மொழி becoming முடி in Tamil.
Registry rows: `~/Quavara/CURRENT.md`, under "Speech-to-text ear" and "Voice certification".

**The ear (accuracy first):** Whisper large-v3, full precision (float32), run locally with faster-whisper.
- The environment is `~/.local/share/inara-stt/wenv` (Python 3.12; faster-whisper's audio package won't build on 3.14).
- The model is in `~/.cache/huggingface/hub/models--Systran--faster-whisper-large-v3`.
- No key is needed, and nothing leaves the iMac.

```
~/.local/share/inara-stt/wenv/bin/python tools/voice-stt/whisper_run.py ar "~/Desktop/Stardust - Terra Deleta/Inara-Voice/Stardust-TerraDeleta_Inara_ar_Sara/raw" "~/Desktop/Stardust - Terra Deleta/Inara-Voice/Stardust-TerraDeleta_Inara_ar_Sara_checks/"whisper-large-v3.txt
python3 tools/voice-stt/compare.py docs/inara-lines/ar.json "~/Desktop/Stardust - Terra Deleta/Inara-Voice/Stardust-TerraDeleta_Inara_ar_Sara_checks/"whisper-large-v3.txt
```

The runner resumes where it stopped. The comparer handles Arabic text: it strips vowel marks, unifies the alef and ya
forms and ignores punctuation. It prints each line's match and the exact words that differ.

**Second ears:**
- `~/.openclaw/models/whisper/ggml-large-v3-turbo-q5_0.bin` (July 7, for whisper.cpp). It's faster and less accurate.
  A word that both ears mishear was really mispronounced.
- `apple-speech/`: macOS's own recognizer, wrapped as a small app because macOS allows speech recognition only from
  an app. It's too weak for Arabic: on 10-26 it scored 55% on a line Whisper heard perfectly. Kept only as a quick
  check.
