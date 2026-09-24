import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SPECIFIC_FIXES_BY_PREFIX = {
    "7396e256": { # Q[06] - Boa-fé Objetiva e Figuras Parcelares
        "A": "Tu quoque, segundo o qual a parte que violou determinada cláusula contratual ou dever anexo perde a legitimidade para exigir o adimplemento estrito da contraprestação alheia.",
        "B": "Supressio, caracterizada pela perda de um direito subjetivo em decorrência do seu não exercício prolongado no tempo, gerando na contraparte a legítima expectativa de não cobrança.",
        "C": "Surrectio, consubstanciada no surgimento superveniente de um direito subjetivo contratual em favor de uma parte, decorrente de uma prática reiterada mantida sem oposição recíproca.",
        "D": "Duty to mitigate the loss, consistente no dever imposto ao credor de mitigar os próprios prejuízos sofridos, abstendo-se de praticar atos que agravem desnecessariamente o dano final."
    },
    "051c94f6": { # Q[15] - Promessa de Fato de Terceiro
        "A": "José pode propor ação judicial cominatória de obrigação de fazer contra Clara para compeli-la judicialmente ao cumprimento da prestação artística ajustada.",
        "B": "José deve acionar Mário para pleitear perdas e danos pelo inadimplemento, visto que Clara não anuiu nem se vinculou ao contrato originário firmado.",
        "C": "Mário e Clara respondem de forma estritamente solidária por todos os prejuízos e lucros cessantes perante José, em virtude da teoria da aparência contratual.",
        "D": "O negócio jurídico é nulo de pleno direito no plano da validade por ilicitude do objeto, ficando Mário e Clara integralmente desobrigados de indenizar José."
    },
    "dda2d9a4": { # Q[16] - Promessa de Fato de Terceiro
        "A": "No momento em que o terceiro expressamente aceitar e se comprometer perante o credor a executar a obrigação prometida.",
        "B": "Apenas após a conclusão integral e o adimplemento perfeito da prestação contratada pelo terceiro perante o credor originário.",
        "C": "No prazo decadencial de trinta dias úteis a contar da celebração da promessa, presumindo-se a anuência tácita do terceiro indicado.",
        "D": "A responsabilidade civil do promitente jamais cessa, permanecendo este na condição de fiador legal e devedor solidário perpétuo da obrigação."
    },
    "f92f139f": { # Q[19] - Contrato Aleatório: Emptio Rei Speratae
        "A": "O contrato é nulo de pleno direito, devendo o alienante restituir integralmente os valores pagos pelo comprador em virtude da frustração total do objeto.",
        "B": "O comprador deve pagar o preço integralmente ajustado, assumindo o risco absoluto tanto da existência quanto da quantidade da colheita futura esperada.",
        "C": "O comprador responde apenas por metade do preço convencionado, operando-se a divisão equitativa dos prejuízos entre os contratantes por força da lei.",
        "D": "O negócio converte-se compulsoriamente em comodato mercantil de exploração rural, ficando o alienante obrigado a ceder a terra por duas safras subsequentes."
    },
    "a278678e": { # Q[20] - Contrato Aleatório: Coisas Existentes Expostas a Risco
        "A": "O alienante não tenha agido com dolo, ignorando a consumação do sinistro ao tempo da celebração do contrato de compra e venda mercantil.",
        "B": "O adquirente renuncie previamente perante tabelião público à garantia legal da evicção e aos direitos de indenização por enriquecimento sem causa.",
        "C": "O instrumento contratual seja registrado no cartório competente de títulos e documentos no prazo decadencial de trinta dias da sua celebração.",
        "D": "O risco de perda ou deterioração do bem seja integralmente garantido por apólice securitária obrigatória contratada pelo poder público competente."
    },
    "6f7243a4": { # Q[21] - Contrato Preliminar / Promessa de Contratar
        "A": "O contrato preliminar, exceto quanto à forma, deve conter todos os requisitos essenciais ao contrato a ser celebrado pelas partes.",
        "B": "O contrato preliminar exige obrigatoriamente a mesma forma solene prescrita em lei para o contrato definitivo sob pena de nulidade.",
        "C": "As partes não podem estipular cláusula de arrependimento em nenhuma espécie de contrato preliminar celebrado no direito brasileiro.",
        "D": "A eficácia e a validade jurídica do contrato preliminar entre as partes dependem de prévio e obrigatório registro no cartório imobiliário."
    },
    "e8f0fcd4": { # Q[22] - Contrato Preliminar / Promessa de Contratar
        "A": "Exigir a celebração do contrato definitivo ou requerer que o juiz supra a vontade do inadimplente, conferindo caráter definitivo ao contrato.",
        "B": "Apenas pleitear a rescisão culposa com perda de sinal ou retenção de arras, vedada categoricamente a concessão de tutela jurisdicional específica.",
        "C": "Promover execução por quantia certa contra a fazenda pública para que esta desaproprie compulsoriamente o imóvel objeto da promessa inadimplida.",
        "D": "Exigir a conversão automática do compromisso preliminar em doação remuneratória irrevogável, com incidência de astreintes diárias ilimitadas."
    },
    "92f662cd": { # Q[26] - Efeitos da Boa-fé e Má-fé do Alienante no Vício
        "A": "Restituirá o valor recebido acrescido de perdas e danos materiais e morais, em razão da ilicitude e da má-fé contratual constatada.",
        "B": "Ficará obrigado unicamente a restituir o valor recebido mais as despesas do contrato, ficando isento de indenizar perdas e danos suplementares.",
        "C": "Deverá pagar multa civil equivalente ao dobro do valor do contrato ao adquirente, independentemente de comprovação de danos materiais suportados.",
        "D": "Ficará isento de qualquer restituição pecuniária caso comprove que o adquirente realizou inspeção visual sumária do automóvel antes da tradição."
    },
    "a08e90ed": { # Q[44] - Contrato Aleatório: Emptio Spei
        "A": "O pescador terá direito a receber todo o preço ajustado, desde que não tenha incorrido em dolo ou culpa pela frustração total da pescaria.",
        "B": "O comprador estará dispensado de pagar qualquer quantia pecuniária, extinguindo-se o negócio por perecimento superveniente do objeto essencial.",
        "C": "O negócio converter-se-á compulsoriamente em sociedade em conta de participação, dividindo-se os custos operacionais do barco igualmente entre ambos.",
        "D": "O adquirente poderá exigir em juízo abatimento proporcional de noventa por cento no valor contratado, pagando apenas as despesas do combustível."
    },
    "50eb5089": { # Q[46] - Contrato Aleatório: Coisas Existentes Expostas a Risco
        "A": "É plenamente válida, tendo o alienante direito a todo o preço caso ignorasse a consumação do risco à data do negócio firmado entre as partes.",
        "B": "É vedada pelo Código Civil sob pena de nulidade absoluta, por configurar cláusula leonina incompatível com o princípio da função social da empresa.",
        "C": "Transfere o dever de indenizar para os órgãos governamentais de regulação, desonerando o comprador de arcar com o pagamento do preço convencionado.",
        "D": "Impõe ao vendedor o dever legal de restituir o preço em dobro caso a coisa pereça durante o transporte, mesmo tendo agido com estrita boa-fé."
    },
    "ba9bcf85": { # Q[56] - Exceção do Contrato Não Cumprido e Onerosidade Excessiva
        "A": "A resolução do contrato ou a modificação equitativa das condições contratuais, demonstrando acontecimentos extraordinários e imprevisíveis.",
        "B": "A decretação sumária de insolvência civil com extinção de pleno direito de todos os contratos bilaterais pendentes de adimplemento da sociedade.",
        "C": "A conversão compulsória da dívida em cotas societárias pelo Poder Judiciário, vedada expressamente a revisão ou a extinção do pacto originário.",
        "D": "A suspensão permanente da obrigação principal por prazo indeterminado, sem que o contratante necessite comprovar fato imprevisível ou onerosidade."
    },
    "a0b3d5d2": { # Q[62] - Contrato Aleatório: Emptio Spei
        "A": "O adquirente comprove que a ausência total de produção decorreu de negligência, imperícia ou conduta culposa/dolosa do agricultor alienante.",
        "B": "O adquirente comprove que o preço de mercado da soja oscilou negativamente em percentual superior a vinte por cento no período da colheita.",
        "C": "O alienante não tenha comunicado por notificação extrajudicial em cartório a ocorrência de condições climáticas adversas na região produtora.",
        "D": "A colheita tenha sido frustrada por evento decorrente de força maior ou caso fortuito típico, como seca prolongada ou geada extemporânea."
    },
    "bbc19f60": { # Q[64] - Contrato Preliminar / Promessa de Contratar
        "A": "Apenas exigir o cumprimento da promessa sob pena de perdas e danos, sem direito a requerer judicialmente a adjudicação compulsória do bem.",
        "B": "Requerer a adjudicação compulsória do imóvel em juízo, tendo em vista que a cláusula de arrependimento é nula de pleno direito nas promessas.",
        "C": "Impor a conversão automática da promessa em contrato definitivo de doação onerosa, com incidência de multa cominatória diária contra o promitente.",
        "D": "Promover a anulação da promessa no plano da existência jurídica, desconstituindo a manifestação de vontade emitida pelos contratantes desde a origem."
    },
    "23e04ffd": { # Q[66] - Contrato com Pessoa a Declarar vs. Outros Contratos
        "A": "Produzirá todos os seus efeitos regulares exclusivamente entre os contratantes originários que celebraram o negócio jurídico preliminar.",
        "B": "Será extinto de pleno direito por carência superveniente de pressuposto de validade, liberando os contratantes originários de qualquer prestação.",
        "C": "Será considerado nulo de pleno direito por caracterizar fraude contra credores e simulação relativa no plano de eficácia do negócio jurídico.",
        "D": "Terá seus efeitos transferidos compulsoriamente aos mandatários ou intermediários que participaram das tratativas preliminares da avença."
    },
    "470ce0fd": { # Q[71] - Prazos Decadenciais dos Vícios Redibitórios
        "A": "Conta-se a partir da alienação definitiva do bem, porém o prazo legal de decadência fica reduzido exatamente à metade pelo Código Civil.",
        "B": "Inicia-se normalmente da data em que o locatário ingressou na posse precária do imóvel, sem qualquer redução temporal sobre o prazo ânuo legal.",
        "C": "Converte-se em prazo prescricional trienal comum de reparação civil, afastando-se a disciplina especial dos prazos das ações edilícias do Código.",
        "D": "Extingue-se de pleno direito no momento da assinatura da compra e venda, presumindo a lei que a posse anterior convalidou os vícios ocultos."
    }
}

def apply():
    file_path = BASE_DIR / "database" / "seed_questions.json"
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    questions = data.get("questions", [])
    applied = 0
    for q in questions:
        qid = str(q.get("id", ""))[:8]
        if qid in SPECIFIC_FIXES_BY_PREFIX:
            q["options"] = SPECIFIC_FIXES_BY_PREFIX[qid]
            applied += 1

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Fixes aplicados a {applied} questões por prefixo em seed_questions.json.")

if __name__ == "__main__":
    apply()
