#!/usr/bin/env python3
"""One short Lily sample per language (Eric, 2026-10-19), so Eric can hear which languages Lily speaks well before the
full recording in each. Steam's most-used languages (Valve's full-year 2024 figures, plus Polish from the 2025 survey).
The same three approved lines as the English sample (INARA-TWR-004, STORY-001, STORY-002), translated by Claude.
Recorded files only. The key comes from ELEVENLABS_API_KEY or a hidden prompt; it is never printed or saved.
Saves ~/Desktop/inara-language-samples/<code>.mp3

    python3 tools/inara-language-samples.py
"""
import argparse, getpass, json, os, sys, urllib.request

SAMPLES = {
    "zh-CN": "离开舰首了。祝你在星环里好运。你现在身处一艘探索型科学研究星舰上，见习生。这里的每个人都是从最底层做起的。我也一样。",
    "ru":    "Ты вышел из-под носа корабля. Удачи в кольцах. Ты на борту исследовательского научного звездолёта, стажёр. Здесь все начинают с самых низов. Я тоже когда-то.",
    "es":    "Fuera de la proa. Buena suerte en los anillos. Estás a bordo de una nave estelar de exploración, ciencia e investigación, aprendiz. Aquí todos empiezan desde abajo. Yo también, una vez.",
    "pt-BR": "Livre da proa. Boa sorte nos anéis. Você está a bordo de uma nave estelar de exploração, ciência e pesquisa, trainee. Aqui todo mundo começa de baixo. Eu também comecei, um dia.",
    "de":    "Frei vom Bug. Viel Glück draußen in den Ringen. Du bist an Bord eines Forschungsraumschiffs der Wissenschaft und Erkundung, Auszubildender. Hier fangen alle ganz unten an. Ich auch, einmal.",
    "ko":    "함수에서 벗어났습니다. 고리에서 행운을 빌어요. 당신은 탐사 과학 연구 우주선에 탑승해 있어요, 훈련생. 이곳에서는 모두가 맨 아래에서 시작해요. 저도 그랬어요.",
    "fr":    "Dégagé de la proue. Bonne chance dans les anneaux. Tu es à bord d'un vaisseau d'exploration scientifique et de recherche, stagiaire. Ici, tout le monde commence en bas de l'échelle. Moi aussi, autrefois.",
    "ja":    "艦首を離れました。リングでの幸運を祈ります。あなたは探査科学研究宇宙船に乗っています、訓練生。ここでは誰もが一番下から始めます。私もかつてはそうでした。",
    "tr":    "Pruvadan çıktın. Halkalarda bol şans. Bir keşif, bilim ve araştırma yıldız gemisindesin, stajyer. Burada herkes en alttan başlar. Ben de bir zamanlar öyle başladım.",
    "pl":    "Odejście od dziobu. Powodzenia w pierścieniach. Jesteś na pokładzie badawczego statku kosmicznego, stażysto. Tutaj każdy zaczyna od samego dołu. Ja też kiedyś.",
    "zh-TW": "離開艦首了。祝你在星環裡好運。你現在身處一艘探索型科學研究星艦上，見習生。這裡的每個人都是從最底層做起的。我也一樣。",
}


def call(url, key, body=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None,
                                 headers={"xi-api-key": key, "Content-Type": "application/json"})
    return urllib.request.urlopen(req, timeout=120).read()


ap = argparse.ArgumentParser()
ap.add_argument("--voice", default="lily", help="the start of the voice's name in My Voices, e.g. 'kate 1'")
ap.add_argument("--langs", default=",".join(SAMPLES), help="comma-separated, e.g. es,pt-BR,ko,fr,tr")
a = ap.parse_args()
key = os.environ.get("ELEVENLABS_API_KEY") or getpass.getpass("ElevenLabs API key (hidden, not saved): ").strip()
vs = json.loads(call("https://api.elevenlabs.io/v1/voices", key))["voices"]
lily = [v for v in vs if v["name"].lower().startswith(a.voice.lower())]
if not lily: sys.exit(f"No voice starting '{a.voice}' in My Voices. Add it from the Voice Library first (the + button). Found: "
                      + ", ".join(v["name"] for v in vs))
print(f"Voice: {lily[0]['name']}")
SAMPLES = {k: v for k, v in SAMPLES.items() if k in a.langs.split(",")}
out = os.path.expanduser(f"~/Desktop/inara-language-samples/{a.voice.replace(' ', '-')}"); os.makedirs(out, exist_ok=True)
print(f"{len(SAMPLES)} samples, {sum(map(len, SAMPLES.values())):,} characters.")
for code, text in SAMPLES.items():
    p = os.path.join(out, code + ".mp3")
    if os.path.exists(p): continue
    open(p, "wb").write(call(f"https://api.elevenlabs.io/v1/text-to-speech/{lily[0]['voice_id']}", key,
                             {"text": text, "model_id": "eleven_multilingual_v2"}))
    print(f"  {code}", flush=True)
print(f"Done. Listen in {out}")
