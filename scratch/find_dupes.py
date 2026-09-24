import json
from collections import defaultdict

with open('database/seed_questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

questions = data['questions']
print(f'Total questions in seed_questions.json: {len(questions)}')

# Same subject + options + gabarito
exact = defaultdict(list)
for i, q in enumerate(questions):
    key = (q['subject'], json.dumps(q['options'], sort_keys=True), q['gabarito'])
    exact[key].append(i)

print(f'\n=== EXACT DUPLICATES (same subject + options + gabarito) ===')
found = 0
for key, indices in exact.items():
    if len(indices) > 1:
        found += 1
        print(f'\nDuplicate #{found}: Subject="{key[0]}"')
        for idx in indices:
            q = questions[idx]
            print(f'  Index {idx}: id={q["id"][:12]} bank={q["bank"]} enunc={q["enunciado"][:70]}')
if found == 0:
    print('None found')

# Cross-subject: different subject, same options+gabarito
cross = defaultdict(list)
for i, q in enumerate(questions):
    key = (json.dumps(q['options'], sort_keys=True), q['gabarito'])
    cross[key].append(i)

print(f'\n=== CROSS-SUBJECT DUPLICATES (same options+gabarito, diff subject) ===')
found_cross = 0
for key, indices in cross.items():
    subjects = set(questions[i]['subject'] for i in indices)
    if len(subjects) > 1:
        found_cross += 1
        print(f'\nCross-duplicate #{found_cross}:')
        for idx in indices:
            q = questions[idx]
            print(f'  Subject="{q["subject"]}" bank={q["bank"]} enunc={q["enunciado"][:60]}')
if found_cross == 0:
    print('None found')

# Check questions that are exact copy except for subject
print(f'\n=== ENUNCIADO DUPLICATES (same enunciado text) ===')
by_enunc = defaultdict(list)
for i, q in enumerate(questions):
    by_enunc[q['enunciado'].strip()].append(i)

for enunc, indices in by_enunc.items():
    if len(indices) > 1:
        print(f'\nSame enunciado ({len(indices)}x):')
        for idx in indices:
            q = questions[idx]
            print(f'  Index {idx}: subject="{q["subject"]}" bank={q["bank"]} gabarito={q["gabarito"]}')
