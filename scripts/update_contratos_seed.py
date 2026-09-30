# -*- coding: utf-8 -*-
"""
Script para atualizar seed_questions.json:
1. Remove todas as referências e prefixos de bancas de concurso (FGV, CESPE, etc.).
2. Normaliza bank para 'Revisão Oficial - Contratos'.
3. Exclui questões do tema Evicção (alinhado aos 22 temas do questionário).
"""
import json
import re
from pathlib import Path

def clean_enunciado(text: str) -> str:
    # Remove prefixos como (FGV / OAB), (CESPE / Defensoria), etc.
    cleaned = re.sub(r'^\s*\([A-Z0-9\s/–-]+\)\s*', '', text)
    return cleaned.strip()

def main():
    target_path = Path(__file__).resolve().parent.parent / "database" / "seed_questions.json"
    with open(target_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    questions = data.get("questions", [])
    updated_questions = []
    
    for q in questions:
        # Pula questões de Evicção
        if q.get("subject") == "Evicção - Conceito, Requisitos e Efeitos" or str(q.get("id", "")).startswith("contratos_23_"):
            continue
        q["bank"] = "Revisão Oficial - Contratos"
        q["enunciado"] = clean_enunciado(q.get("enunciado", ""))
        updated_questions.append(q)
        
    data["questions"] = updated_questions
    data["description"] = "Banco oficial de questões de Direito dos Contratos alinhado 100% aos 22 temas do Questionário da Prova, sem menção a bancas de concurso e com casos práticos."
    data["version"] = "3.1.0"
    
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"Sucesso! Atualizadas {len(updated_questions)} questões de Contratos em {target_path}")

if __name__ == "__main__":
    main()
