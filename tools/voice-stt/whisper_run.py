import sys, glob, os, time, subprocess
import numpy as np

def load(f):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", f, "-f", "f32le", "-ac", "1", "-ar", "16000", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32)
from faster_whisper import WhisperModel
lang, folder, out = sys.argv[1], sys.argv[2], sys.argv[3]
m = WhisperModel("large-v3", device="cpu", compute_type="float32", cpu_threads=int(os.environ.get("WHISPER_THREADS", os.cpu_count())))   # WHISPER_THREADS=2 keeps the iMac usable
done = set()
if os.path.exists(out):
    done = {l.split("\t")[0] for l in open(out, encoding="utf-8") if "\t" in l}
with open(out, "a", encoding="utf-8") as fh:
    for f in sorted(glob.glob(os.path.join(folder, "*.mp3"))):
        name = os.path.basename(f)
        if name in done: continue
        t = time.time()
        segs, _ = m.transcribe(load(f), language=lang, beam_size=5, condition_on_previous_text=False, vad_filter=os.environ.get("WHISPER_VAD") == "1")   # WHISPER_VAD=1 splits long lines: Devanagari hits the 30-second window's token limit
        text = " ".join(s.text.strip() for s in segs)
        fh.write(f"{name}\t{text}\n"); fh.flush()
        print(f"{name} {time.time()-t:.0f}s", flush=True)
print("DONE")
