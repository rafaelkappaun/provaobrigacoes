"""
Script para enriquecer, balancear e elevar a dificuldade das questões de:
1. database/seed_questions.json (Contratos)
2. database/seed_multiportas.json (Modelo Multiportas)

Objetivos:
1. Eliminar alternativas curtas (<90 caracteres) ou telegráficas.
2. Equalizar o comprimento (caracteres) entre a resposta correta e os distratores,
   eliminando a dica de "marcar a mais completa/mais longa".
3. Tornar os distratores sedutores, tecnicamente formulados e com pegadinhas reais
   (inversão de conceitos, prazos decadenciais x prescricionais, regras gerais x exceções,
   mediação x conciliação, autotutela x heterocomposição, etc.).
4. Distribuir os gabaritos de forma balanceada (25% A, 25% B, 25% C, 25% D).
"""

import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def balance_options(opts, target_len=None):
    # Helper to check length consistency
    lens = [len(v) for v in opts.values()]
    avg = sum(lens) / len(lens)
    max_l = max(lens)
    min_l = min(lens)
    return avg, min_l, max_l

print("Iniciando refinamento de banco de questões...")
