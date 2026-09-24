import json

with open('database/seed_questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

q = data['questions']
print(f'Total: {len(q)}')

# Find all FGV questions about Bernardo (inadimplemento)
for i, qi in enumerate(q):
    if 'Bernardo' in qi.get('enunciado', '') and 'nao construir' in qi.get('enunciado', '').lower():
        print(f'Index {i}: id={qi["id"][:12]} subject={qi["subject"]} bank={qi["bank"]}')

# Find all FGV questions about Douglas (juros)
for i, qi in enumerate(q):
    if 'Douglas' in qi.get('enunciado', '') and 'juros' in qi.get('enunciado', '').lower():
        print(f'Index {i}: id={qi["id"][:12]} subject={qi["subject"]} bank={qi["bank"]}')

# Find all FGV questions about Patricia (arras)
for i, qi in enumerate(q):
    if 'Patricia' in qi.get('enunciado', '') and 'Rodrigo' in qi.get('enunciado', ''):
        print(f'Index {i}: id={qi["id"][:12]} subject={qi["subject"]} bank={qi["bank"]}')

# Find all CESPE Bruno about incapaz
for i, qi in enumerate(q):
    if 'Bruno' in qi.get('enunciado', '') and 'incapaz' in qi.get('enunciado', '').lower():
        print(f'Index {i}: id={qi["id"][:12]} subject={qi["subject"]} bank={qi["bank"]}')

# Find all Objeto do pagamento / FMP
for i, qi in enumerate(q):
    if qi.get('subject') == 'Objeto do pagamento e sua prova' and qi.get('bank') == 'FMP':
        print(f'Index {i}: id={qi["id"][:12]} enunc={qi["enunciado"][:60]}')

# Full duplicate detection by content hash
print("\n=== Full content-based duplicate detection ===")
import hashlib

# Group by normalized content
groups = {}
for i, qi in enumerate(q):
    # Create hash of options+gabarito+explanation (ignore id)
    content = json.dumps(qi['options'], sort_keys=True) + qi['gabarito'] + qi.get('explanation', '')
    h = hashlib.md5(content.encode()).hexdigest()
    if h not in groups:
        groups[h] = []
    groups[h].append(i)

for h, indices in groups.items():
    if len(indices) > 1:
        print(f"\nDuplicate group ({len(indices)} entries):")
        for idx in indices:
            qi = q[idx]
            print(f"  Index {idx}: id={qi['id'][:12]} subject={qi['subject']} bank={qi['bank']}")
            print(f"           enunc={qi['enunciado'][:80]}")
