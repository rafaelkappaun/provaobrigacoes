import random, json, sys
from pathlib import Path
from ai.offline_generator import generate_question_offline, SUBJECTS, BANKS

SEED_FILE = Path(__file__).resolve().parent.parent / "database" / "seed_questions.json"
QUESTIONS_PER_SUBJECT = 10

def main():
    existing_ids = set()
    pool = {"questions": []}

    # Carrega questões já existentes para não gerar duplicatas
    if SEED_FILE.exists():
        with open(SEED_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            pool = data
            for q in pool["questions"]:
                existing_ids.add(q["id"])
            print(f"Carregadas {len(pool['questions'])} questões existentes.")

    total_needed = 0
    for subj in SUBJECTS:
        count = sum(1 for q in pool["questions"] if q["subject"] == subj)
        need = max(0, QUESTIONS_PER_SUBJECT - count)
        total_needed += need
        print(f"  {subj}: {count} existentes, precisa de +{need}")

    print(f"\nTotal necessário: {total_needed} novas questões")
    if total_needed == 0:
        print("Todos os assuntos já têm 10+ questões. Nada a gerar.")
        return

    for subj in SUBJECTS:
        count = sum(1 for q in pool["questions"] if q["subject"] == subj)
        need = max(0, QUESTIONS_PER_SUBJECT - count)
        for i in range(need):
            bank = random.choice(BANKS)
            q = generate_question_offline(subj, bank)
            if q["id"] not in existing_ids:
                existing_ids.add(q["id"])
                pool["questions"].append(q)
                print(f"  [{subj}] questão {count + i + 1}/{QUESTIONS_PER_SUBJECT} gerada ({bank})")
            else:
                print(f"  [!] ID duplicado, pulando...")
                # Tenta de novo
                for _ in range(5):
                    q = generate_question_offline(subj, bank)
                    if q["id"] not in existing_ids:
                        existing_ids.add(q["id"])
                        pool["questions"].append(q)
                        print(f"  [{subj}] questão {count + i + 1}/{QUESTIONS_PER_SUBJECT} gerada ({bank})")
                        break

    with open(SEED_FILE, "w", encoding="utf-8") as f:
        json.dump(pool, f, ensure_ascii=False, indent=2)

    total = len(pool["questions"])
    print(f"\nSeed concluído! {total} questões salvas em {SEED_FILE}")
    for subj in SUBJECTS:
        c = sum(1 for q in pool["questions"] if q["subject"] == subj)
        print(f"  {subj}: {c}")

if __name__ == "__main__":
    main()
