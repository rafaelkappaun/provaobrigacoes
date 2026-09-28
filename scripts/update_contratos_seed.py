# -*- coding: utf-8 -*-
"""
Script para atualizar seed_questions.json:
1. Remove todas as referências e prefixos de bancas de concurso (FGV, CESPE, etc.).
2. Normaliza bank para 'Revisão Oficial - Contratos'.
3. Adiciona 4 questões completas e inéditas com nomes de pessoas para o 23º tema (Evicção).
"""
import json
import re
from pathlib import Path

def clean_enunciado(text: str) -> str:
    # Remove prefixos como (FGV / OAB), (CESPE / Defensoria), etc.
    cleaned = re.sub(r'^\s*\([A-Z0-9\s/–-]+\)\s*', '', text)
    return cleaned.strip()

eviccao_questions = [
    {
        "id": "contratos_23_a_eviccao_conceito",
        "subject": "Evicção - Conceito, Requisitos e Efeitos",
        "bank": "Revisão Oficial - Contratos",
        "difficulty": "Médio",
        "enunciado": "Roberto comprou de Carlos um caminhão de carga pelo valor de R$ 180.000,00. Seis meses após a tradição, Roberto foi citado em ação reivindicatória movida por Mariana, verdadeira proprietária que teve o bem furtado por terceiros antes da venda. O juiz proferiu sentença transitada em julgado determinando a entrega do veículo a Mariana. Diante da perda do bem por decisão judicial fundada em causa jurídica preexistente, Roberto sofreu:",
        "options": {
            "A": "Evicção, garantia legal típica dos contratos onerosos pela qual o alienante Carlos deve responder pela perda da posse ou propriedade sofrida pelo adquirente Roberto em virtude de direito preexistente de terceiro.",
            "B": "Vício redibitório intrínseco, cabendo unicamente a ação estimatória para abatimento de 10% no preço.",
            "C": "Aliud pro alio de natureza penal, que exime o vendedor Carlos de qualquer obrigação de indenizar.",
            "D": "Inadimplemento fortuito por fato do príncipe, suportando Roberto integralmente os prejuízos da perda sem direito de regresso."
        },
        "gabarito": "A",
        "article": "Art. 447 do Código Civil",
        "legal_basis": "Art. 447. Nos contratos onerosos, o alienante responde pela evicção. Subsiste esta garantia ainda que a aquisição se tenha realizado em hasta pública.",
        "explanation": "A evicção é a perda total ou parcial da coisa adquirida em contrato oneroso em razão de decisão judicial ou ato administrativo que reconhece direito anterior de terceiro."
    },
    {
        "id": "contratos_23_b_clausula_nao_eviccao",
        "subject": "Evicção - Conceito, Requisitos e Efeitos",
        "bank": "Revisão Oficial - Contratos",
        "difficulty": "Difícil",
        "enunciado": "Eduardo comprou uma fazenda de Juliana. No contrato, as partes inseriram cláusula genérica declarando que 'a vendedora não responderá pela evicção em nenhuma hipótese'. Ocorre que Eduardo não foi informado e não sabia do risco específico de que pendia ação demarcatória contra a área, tampouco assumiu expressamente tal risco. Perdida a terra por decisão judicial para um terceiro confrontante, Eduardo terá direito a:",
        "options": {
            "A": "Recobrar o preço que pagou pela fazenda evicta, pois a cláusula de não responder pela evicção, sem que o adquirente tenha sido informado do risco da evicção e o assumido expressamente, não o priva de recobrar o valor pago (Art. 449 do Código Civil).",
            "B": "Nada receber, visto que a cláusula de exoneração da evicção possui eficácia extintiva absoluta automática em qualquer hipótese no direito civil.",
            "C": "Exigir a prisão civil de Juliana por descumprimento de obrigação líquida e certa.",
            "D": "Compensar o prejuízo retendo tributos federais devidos à Receita Federal."
        },
        "gabarito": "A",
        "article": "Art. 449 do Código Civil",
        "legal_basis": "Art. 449. Não obstante a cláusula que exclui a garantia contra a evicção, se esta se der, tem direito o evicto a recobrar o preço que pagou pela coisa evicta, se não soube do risco da evicção, ou, dele informado, não o assumiu.",
        "explanation": "Para exonerar totalmente o alienante (inclusive do preço), exige-se tríplice requisito: cláusula expressa, ciência específica do risco e assunção expressa do risco pelo comprador."
    },
    {
        "id": "contratos_23_c_eviccao_parcial_consideravel",
        "subject": "Evicção - Conceito, Requisitos e Efeitos",
        "bank": "Revisão Oficial - Contratos",
        "difficulty": "Médio",
        "enunciado": "Patrícia comprou um imóvel com área de 1.000 m² para construir uma clínica médica. Meses depois, uma sentença judicial reconheceu que 600 m² da área (fração de grande vulto e onde seria erguido o centro cirúrgico) pertenciam licitamente a um vizinho com título imobiliário anterior. Constatada a evicção parcial de parcela considerável do bem, o artigo 455 do Código Civil faculta a Patrícia:",
        "options": {
            "A": "Optar entre a rescisão total do contrato (com restituição de tudo o que pagou) ou a conservação da área remanescente com abatimento proporcional do preço.",
            "B": "Apenas conformar-se com a área que sobrou, sendo vedada qualquer pretensão rescisória ou indenizatória.",
            "C": "Exigir compulsoriamente a desapropriação da terra do vizinho pelo poder público municipal.",
            "D": "Anular o casamento civil dos vendedores com fundamento no vício redibitório societário."
        },
        "gabarito": "A",
        "article": "Art. 455 do Código Civil",
        "legal_basis": "Art. 455. Se parcial, mas considerável, for a evicção, poderá o evicto optar entre a rescisão do contrato e a restituição da parte do preço correspondente ao desfalque sofrido.",
        "explanation": "Sendo a evicção parcial considerável, o evicto pode rescindir o contrato integralmente ou ficar com o que sobrou exigindo a devolução proporcional do preço."
    },
    {
        "id": "contratos_23_d_verbas_indenizatorias",
        "subject": "Evicção - Conceito, Requisitos e Efeitos",
        "bank": "Revisão Oficial - Contratos",
        "difficulty": "Médio",
        "enunciado": "Fernando sofreu evicção total de um imóvel comercial adquirido onerosamente de Rodrigo. Ao pleitear a indenização devida pela garantia da evicção perante o alienante, nos moldes expressos do artigo 450 do Código Civil, Fernando terá direito, além da restituição integral do preço ou valor pago, a:",
        "options": {
            "A": "Indenização dos frutos que tiver sido obrigado a restituir, ressarcimento das despesas do contrato e prejuízos que diretamente da evicção resultarem, além das custas judiciais e honorários advocatícios.",
            "B": "Apenas metade do valor pago sem correção monetária ou juros legais.",
            "C": "Uma pensão alimentícia mensal perpétua fixada em salários mínimos.",
            "D": "Exclusivamente indenização por danos estéticos apurados por junta médica do tribunal."
        },
        "gabarito": "A",
        "article": "Art. 450 do Código Civil",
        "legal_basis": "Art. 450. Salvo estipulação em contrário, tem direito o evicto, além da restituição integral do preço ou das quantias que pagou: I - à indenização dos frutos; II - à indenização das despesas contratuais e prejuízos diretos; III - às custas judiciais e honorários.",
        "explanation": "O art. 450 do CC assegura a reparação integral do evicto, englobando preço integral, despesas contratuais, frutos restituídos, prejuízos diretos, custas e honorários."
    }
]

def main():
    target_path = Path(__file__).resolve().parent.parent / "database" / "seed_questions.json"
    with open(target_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    questions = data.get("questions", [])
    updated_questions = []
    
    for q in questions:
        q["bank"] = "Revisão Oficial - Contratos"
        q["enunciado"] = clean_enunciado(q.get("enunciado", ""))
        updated_questions.append(q)
        
    # Adiciona as 4 questões de Evicção se ainda não estiverem presentes
    existing_ids = {q["id"] for q in updated_questions}
    for eq in eviccao_questions:
        if eq["id"] not in existing_ids:
            updated_questions.append(eq)
            
    data["questions"] = updated_questions
    data["description"] = "Banco oficial de questões de Direito dos Contratos alinhado 100% aos 23 temas do Questionário da Prova, sem menção a bancas de concurso e com casos práticos."
    data["version"] = "3.0.0"
    
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"Sucesso! Atualizadas {len(updated_questions)} questões de Contratos em {target_path}")

if __name__ == "__main__":
    main()
