import json
import hashlib
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "database" / "seed_questions.json"
OUTPUT_FILE = BASE_DIR / "database" / "seed_questions.json"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data["questions"]
print(f"Total original questions: {len(questions)}")

def clean_text(text):
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'R\s*\$\s*[\d.,]+', ' VALOR ', text)
    text = re.sub(r'\d+[\d.,]*', ' NUM ', text)
    text = re.sub(r'\b(?:cem|mil|dois|tres|quatro|cinco|seis|sete|oito|nove|dez)\b', ' NUM ', text, flags=re.I)
    text = re.sub(r'[^\w\s]', ' ', text)
    words = text.split()
    cleaned = []
    for w in words:
        if w.istitle() and len(w) > 1:
            cleaned.append('NOME')
        else:
            cleaned.append(w.lower())
    text = ' '.join(cleaned)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

deduped = {}
kept = []

for q in questions:
    opts_str = json.dumps(q["options"], ensure_ascii=False)
    clean_opts = clean_text(opts_str)
    enunc_clean = clean_text(q.get("enunciado", ""))
    key_str = f"{q['subject']}|{clean_opts}|{q['gabarito']}"
    key = hashlib.md5(key_str.encode("utf-8")).hexdigest()

    subj = q["subject"]
    if subj not in deduped:
        deduped[subj] = {}
    if key in deduped[subj]:
        continue
    deduped[subj][key] = True
    kept.append(q)

print(f"Unique questions: {len(kept)}")
print(f"Duplicates removed: {len(questions) - len(kept)}")

subj_counts = {}
for q in kept:
    s = q["subject"]
    subj_counts[s] = subj_counts.get(s, 0) + 1

print("\nQuestions per subject:")
for s, c in sorted(subj_counts.items()):
    print(f"  {s}: {c}")

data["questions"] = kept
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\nDone!")
