import json
from pathlib import Path

SEED_FILE = Path(__file__).resolve().parent.parent / "database" / "seed_questions.json"

with open(SEED_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data["questions"]
print(f"Total original: {len(questions)}")

# 1. Fix subject labels
subject_fixes = {
    "1987ecec-4d31-45ff-ab2c-e9ded42127e3": "Mora - Geral",
    "0e34e17f-714f-4f32-9334-5ab469fa9788": "Mora - Geral",
}

for q in questions:
    qid = q["id"]
    if qid in subject_fixes:
        old = q["subject"]
        q["subject"] = subject_fixes[qid]
        print(f"  Fix subject [{qid[:8]}...]: '{old}' -> '{q['subject']}'")

# 2. Remove content duplicates (same options + gabarito, keep first occurrence)
seen = {}
duplicates = []
for i, q in enumerate(questions):
    key = (json.dumps(q["options"], sort_keys=True), q["gabarito"])
    if key in seen:
        dup_subject = q["subject"]
        orig_subject = seen[key]["subject"]
        if dup_subject == orig_subject:
            duplicates.append(i)
            print(f"  Remove duplicate [{q['id'][:8]}...] '{q['subject']}' (same subject)")
        else:
            # Keep if different subjects (different topic coverage)
            pass
    else:
        seen[key] = q

for i in reversed(duplicates):
    questions.pop(i)

print(f"Total apos limpeza: {len(questions)}")
print(f"Removidas: {len(duplicates)}")

# Remove duplicates that span different subjects but are clearly the exact same question
# (same options + gabarito + explanation)
seen_exact = {}
exact_dupes = []
for i, q in enumerate(questions):
    key = (json.dumps(q["options"], sort_keys=True), q["gabarito"], q["explanation"])
    if key in seen_exact:
        exact_dupes.append(i)
        print(f"  Remove exact cross-subject duplicate [{q['id'][:8]}...] '{q['subject']}'")
    else:
        seen_exact[key] = q

for i in reversed(exact_dupes):
    questions.pop(i)

print(f"Total final: {len(questions)}")
print(f"Removidas no total: {len(duplicates) + len(exact_dupes)}")

data["questions"] = questions
with open(SEED_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Done!")
