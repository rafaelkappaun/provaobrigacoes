import json
from collections import defaultdict

# Check which questions in add_seed_questions.py would be duplicates
with open('database/seed_questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
existing = data['questions']

# Now check add_seed_questions.py for questions that already exist
# We need to parse the add_seed_questions.py file to extract the questions
import ast, re

with open('scratch/add_seed_questions.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the new_questions list
start = content.find('new_questions = [')
end = content.rfind(']')
list_str = content[start:end+1]

# Parse it
try:
    new_questions = ast.literal_eval(list_str)
except:
    print("Could not parse add_seed_questions.py directly")
    new_questions = []

print(f"Questions in add_seed_questions.py: {len(new_questions)}")

# For each new question, check if same content exists in seed
print(f"\n=== Questions in add_seed_questions.py that ALREADY EXIST in seed_questions.json ===")
found = 0
for nq in new_questions:
    for eq in existing:
        # Compare key fields (ignore id)
        match = (
            nq['subject'] == eq['subject'] and
            nq['bank'] == eq['bank'] and
            nq.get('enunciado', '').strip() == eq.get('enunciado', '').strip() and
            json.dumps(nq['options'], sort_keys=True) == json.dumps(eq['options'], sort_keys=True) and
            nq['gabarito'] == eq['gabarito']
        )
        if match:
            found += 1
            print(f"\nDuplicate #{found}:")
            print(f"  subject={nq['subject']}, bank={nq['bank']}")
            print(f"  enunc={nq['enunciado'][:80]}...")
            print(f"  Existing id: {eq['id'][:12]}")
            break

if found == 0:
    print("None found")

# Also check gabarito patterns in offline_generator.py
print(f"\n\n=== GABARITO ANALYSIS in offline_generator.py ===")
print("Subjects where BOTH variants have same gabarito (predictable answers):")
print()
print("Subject | Var0 | Var1")
print("--------|------|------")
print("Pagamento - Geral      | C | A")
print("Quem deve pagar        | B | B  <-- SAME")
print("A quem se deve pagar   | B | B  <-- SAME")
print("Objeto do pagamento    | C | A")
print("Lugar do pagamento     | B | B  <-- SAME")
print("Tempo do pagamento     | A | B")
print("Consignação            | B | A")
print("Pagamento c/ sub-rogação | A | A  <-- SAME")
print("Imputação do pagamento | B | B  <-- SAME")
print("Dação em pagamento     | B | B  <-- SAME")
print("Novação                | B | B  <-- SAME")
print("Compensação            | A | A  <-- SAME")
print("Confusão               | A | B")
print("Remissão das dívidas   | B | B  <-- SAME")
print("Mora - Geral           | A | A  <-- SAME")
print("Mora do devedor        | A | B")
print("Mora do credor         | B | B  <-- SAME")
print("Inadimplemento - Geral | B | A")
print("Inadimplemento absoluto | A | A  <-- SAME")
print("Perdas e danos         | A | B")
print("Juros legais           | B | A")
print("Cláusula penal         | B | A")
print("Arras ou sinal         | A | B")
