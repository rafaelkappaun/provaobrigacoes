import json
import uuid

with open("database/seed_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

existing = data.get("questions", [])

MORE_QUESTIONS = [
    # 1. PLANOS DO NEGÓCIO JURÍDICO (ESCADA PONTEANA)
    {
        "subject": "Planos do Negócio Jurídico (Escada Ponteana)",
        "bank": "FGV",
        "difficulty": "Difícil",
        "enunciado": "(FGV / Magistratura) Dois amigos, brincando em uma mesa de bar, redigem em um guardanapo a venda da Lua por R$ 10,00. Sob a perspectiva da teoria dos planos do negócio jurídico (Escada Ponteana), o negócio padece no plano:",
        "options": {
            "A": "Da existência, por absoluta ausência de vontade negocial séria (declaração jocosa / animus jocandi) e falta de objeto fático no mundo jurídico.",
            "B": "Da validade exclusivamente, sendo anulável por lesão patrimonial de 50%.",
            "C": "Da eficácia, por estar sujeito a condição puramente potestativa.",
            "D": "É negócio jurídico válido e eficaz de execução diferida."
        },
        "gabarito": "A",
        "article": "Doutrina de Pontes de Miranda e Art. 104 do CC",
        "legal_basis": "Teoria Geral do Negócio Jurídico (Pontes de Miranda).",
        "explanation": "A manifestação de vontade com animus contrahendi (vontade negocial séria) é elemento substantivo do Plano da Existência. Declarações em gracejo (animus jocandi) não chegam a ingressar no mundo jurídico, sendo negócios inexistentes."
    },
    # 3. BOA-FÉ OBJETIVA E FIGURAS PARCELARES
    {
        "subject": "Boa-fé Objetiva e Figuras Parcelares",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) O princípio do 'Venire contra factum proprium' veda o comportamento contraditório que frustra legítimas expectativas. São pressupostos doutrinários para a caracterização do venire contra factum proprium:",
        "options": {
            "A": "Uma conduta inicial (factum proprium); a legítima confiança gerada na contraparte; um comportamento posterior contraditório; e o potencial de causar dano patrimonial ou moral a quem confiou.",
            "B": "Apenas a presença de dolo específico com intuito de fraudar a execução fiscal.",
            "C": "A existência de cláusula penal expressa com estipulação de arras penitenciais.",
            "D": "A prévia propositura de ação de interdito proibitório com pedido liminar."
        },
        "gabarito": "A",
        "article": "Art. 422 do Código Civil",
        "legal_basis": "Art. 422 do Código Civil e Enunciado 362 da IV Jornada de Direito Civil.",
        "explanation": "São quatro os elementos do venire: 1) Um fato próprio (conduta inicial); 2) Confiança legítima despertada; 3) Comportamento posterior em contradição direta; 4) Prejuízo ou quebra da estabilidade das relações."
    },
    # 6. ETAPAS DE FORMAÇÃO DO CONTRATO
    {
        "subject": "Etapas de Formação do Contrato",
        "bank": "FCC",
        "difficulty": "Médio",
        "enunciado": "(FCC / Procurador) A proposta de contrato feita sem prazo a pessoa presente, se não for imediatamente aceita, segundo o Art. 428, inciso I, do Código Civil:",
        "options": {
            "A": "Deixa de ser obrigatória de imediato.",
            "B": "Permanece obrigatória pelo prazo legal de 30 dias úteis.",
            "C": "Converte-se em proposta entre ausentes automaticamente.",
            "D": "Gera responsabilidade civil objetiva para o oblato por perdas e danos."
        },
        "gabarito": "A",
        "article": "Art. 428, I do Código Civil",
        "legal_basis": "Art. 428, I do Código Civil.",
        "explanation": "Art. 428, I do CC: Deixa de ser obrigatória a proposta 'se, feita sem prazo a pessoa presente, não foi imediatamente aceita'. Considera-se presente também quem contrata por telefone ou meio de comunicação instantânea."
    },
    # 7. ESTIPULAÇÃO EM FAVOR DE TERCEIRO
    {
        "subject": "Estipulação em Favor de Terceiro",
        "bank": "CESPE",
        "difficulty": "Médio",
        "enunciado": "(CESPE / Doutrina) Em caso de morte do estipulante em contrato com estipulação em favor de terceiro, o direito de exigir o cumprimento da obrigação pelo promitente:",
        "options": {
            "A": "Transmite-se aos herdeiros do estipulante, mantendo-se também hígido o direito conferido ao terceiro beneficiário (art. 436, parágrafo único do CC).",
            "B": "Extingue-se automaticamente por ser direito personalíssimo e intransmissível.",
            "C": "Transfere-se compulsoriamente para a Fazenda Pública do Estado.",
            "D": "Depende de alvará judicial com intervenção obrigatória do Ministério Público."
        },
        "gabarito": "A",
        "article": "Art. 436 do Código Civil",
        "legal_basis": "Art. 436 e parágrafo único do Código Civil.",
        "explanation": "O direito de exigir o cumprimento tem natureza patrimonial e transfere-se aos sucessores do estipulante, subsistindo paralelamente o direito do terceiro beneficiário de exigir a obrigação."
    },
    # 8. PROMESSA DE FATO DE TERCEIRO
    {
        "subject": "Promessa de Fato de Terceiro",
        "bank": "VUNESP",
        "difficulty": "Médio",
        "enunciado": "(VUNESP / TJ) Um empresário comprometeu-se com um patrocinador afirmando que seu irmão, famoso conferencista internacional, ministraria palestra de encerramento em evento empresarial. O conferencista não anuiu e não compareceu. O empresário alegou caso fortuito. Nesse contexto:",
        "options": {
            "A": "O empresário responde integralmente por perdas e danos perante o patrocinador, pois aquele que promete fato de terceiro assume obrigação de garantia e resultado.",
            "B": "O patrocinador deve penhorar os bens do conferencista que se recusou a palestrar.",
            "C": "O contrato é nulo de pleno direito por vício social de simulação.",
            "D": "O empresário só responde se for comprovado que agiu com dolo preordenado de estelionato."
        },
        "gabarito": "A",
        "article": "Art. 439 do Código Civil",
        "legal_basis": "Art. 439 do Código Civil.",
        "explanation": "Quem promete fato de terceiro assume o risco e garante o resultado. Se o terceiro não cumpre, o promitente responde por perdas e danos contratuais (art. 439, CC)."
    },
    # 10. CONTRATO ALEATÓRIO: EMPTIO SPEI
    {
        "subject": "Contrato Aleatório: Emptio Spei",
        "bank": "CESPE",
        "difficulty": "Difícil",
        "enunciado": "(CESPE / Magistratura) Na Emptio Spei (Art. 458 do Código Civil), diz-se que o contrato tem por objeto a 'spes' (a esperança da existência). Qual elemento afasta a exigibilidade do preço pelo alienante caso o objeto venha a não existir?",
        "options": {
            "A": "A ocorrência de dolo ou culpa por parte do próprio alienante para a frustração da coisa futura.",
            "B": "A mera verificação de que o valor de mercado caiu mais de 20%.",
            "C": "A recusa imotivada do comprador em retirar a coisa inexistente.",
            "D": "A superveniência de feriado nacional no dia pactuado para a entrega."
        },
        "gabarito": "A",
        "article": "Art. 458 do Código Civil",
        "legal_basis": "Art. 458 do Código Civil ('...desde que de sua parte não tenha havido dolo ou culpa...').",
        "explanation": "Se o alienante der causa culposa ou dolosa para que nada venha a existir (ex: não fertilizou a terra, não lançou a rede, não alimentou os animais), perde o direito de exigir o preço e responde por perdas e danos."
    },
    # 11. CONTRATO ALEATÓRIO: EMPTIO REI SPERATAE
    {
        "subject": "Contrato Aleatório: Emptio Rei Speratae",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) A distinção central entre a 'Emptio Spei' e a 'Emptio Rei Speratae' no Código Civil reside no fato de que:",
        "options": {
            "A": "Na emptio spei o adquirente assume o risco da própria existência da coisa (se nada existir, o preço ainda é devido); na emptio rei speratae o risco é apenas da quantidade (deve vir alguma quantidade; se nada existir, o contrato é ineficaz e o preço é devolvido).",
            "B": "A emptio spei só pode ser celebrada por pessoas jurídicas, enquanto a emptio rei speratae é restrita a pessoas físicas.",
            "C": "A emptio rei speratae exige outorga uxória sob pena de nulidade.",
            "D": "Ambas as modalidades geram devolução em dobro do preço se a colheita for inferior à metade."
        },
        "gabarito": "A",
        "article": "Art. 458 e Art. 459 do Código Civil",
        "legal_basis": "Arts. 458 e 459 do Código Civil.",
        "explanation": "Emptio Spei = risco da existência (tudo ou nada). Emptio Rei Speratae = risco da quantidade (deve existir ao menos uma unidade; se nada existir, desfaz-se o negócio)."
    },
    # 13. CONTRATO PRELIMINAR / PROMESSA DE CONTRATAR
    {
        "subject": "Contrato Preliminar / Promessa de Contratar",
        "bank": "VUNESP",
        "difficulty": "Médio",
        "enunciado": "(VUNESP / TJ) Se no contrato preliminar de promessa de compra e venda as partes inseriram expressa cláusula de arrependimento (com estipulação de arras penitenciais), a recusa de uma das partes em concluir o definitivo:",
        "options": {
            "A": "Gera unicamente a perda das arras (ou devolução em dobro por quem as recebeu), impedindo a execução compulsória ou a adjudicação do imóvel.",
            "B": "Autoriza a adjudicação compulsória forçada do bem pelo juiz de direito.",
            "C": "Torna o contrato nulo no plano da existência com eficácia ex tunc.",
            "D": "Obriga o promitente a pagar indenização suplementar ilimitada."
        },
        "gabarito": "A",
        "article": "Art. 420 e Art. 463 do Código Civil",
        "legal_basis": "Arts. 420 e 463 ('desde que dele não conste cláusula de arrependimento') do Código Civil.",
        "explanation": "O art. 463 condiciona a exigibilidade da celebração definitiva à inexistência de cláusula de arrependimento. Havendo cláusula de arrependimento, o direito potestativo resolve-se pelas arras penitenciais (art. 420)."
    },
    # 14. CONTRATO COM PESSOA A DECLARAR
    {
        "subject": "Contrato com Pessoa a Declarar",
        "bank": "FCC",
        "difficulty": "Médio",
        "enunciado": "(FCC / PGE) Aceita a nomeação da pessoa a declarar nos termos e forma exigidos pela lei, a pessoa nomeada:",
        "options": {
            "A": "Adquire os direitos e assume as obrigações decorrentes do contrato, a partir do momento em que este foi celebrado (efeito retroativo ex tunc).",
            "B": "Assume as obrigações apenas para o futuro (efeito ex nunc da declaração), ficando o estipulante originário solidariamente obrigado.",
            "C": "Responde apenas subsidiariamente com benefício de ordem.",
            "D": "Pode anular as cláusulas do contrato celebrado pelo estipulante originário sem prévia concordância do vendedor."
        },
        "gabarito": "A",
        "article": "Art. 469 do Código Civil",
        "legal_basis": "Art. 469 do Código Civil.",
        "explanation": "Art. 469 do CC: 'A pessoa, nomeada de conformidade com os artigos antecedentes, adquire os direitos e assume as obrigações decorrentes do contrato, a partir do momento em que este foi celebrado' (eficácia ex tunc)."
    },
    # 15. CONTRATO COM PESSOA A DECLARAR VS. OUTROS CONTRATOS
    {
        "subject": "Contrato com Pessoa a Declarar vs. Outros Contratos",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) Se a pessoa indicada no contrato com pessoa a declarar recusar a nomeação ou for absolutamente incapaz e o outro contratante ignorava, o contrato:",
        "options": {
            "A": "Produzirá seus efeitos unicamente entre os contraentes originários (o próprio estipulante e o vendedor).",
            "B": "Será extinto de pleno direito sem qualquer dever para os participantes.",
            "C": "Será considerado nulo por fraude à lei contra credores.",
            "D": "Será transferido forçadamente aos fiadores da pessoa recusante."
        },
        "gabarito": "A",
        "article": "Art. 470 do Código Civil",
        "legal_basis": "Art. 470, incisos I e II do Código Civil.",
        "explanation": "Art. 470: 'O contrato produzirá os seus efeitos unicamente entre os contratantes originários: I - se não houver indicação de pessoa, ou se a nomeada recusar; II - se a pessoa nomeada era incapaz ou insolvente no momento da nomeação'."
    },
    # 16. VÍCIOS REDIBITÓRIOS - CONCEITO E REQUISITOS
    {
        "subject": "Vícios Redibitórios - Conceito e Requisitos",
        "bank": "CESPE",
        "difficulty": "Médio",
        "enunciado": "(CESPE / Juiz) Em relação aos vícios redibitórios em alienações judiciais (bens arrematados em leilão ou hasta pública):",
        "options": {
            "A": "Aplica-se a garantia contra vícios redibitórios também às vendas efetuadas em hasta pública (alienações judiciais), conforme entendimento pacífico da doutrina e art. 441 do CC.",
            "B": "A hasta pública exonera de forma irrestrita qualquer responsabilidade por defeitos ocultos do bem.",
            "C": "O arrematante não possui qualquer ação edilícia, devendo suportar integralmente o prejuízo.",
            "D": "O juiz da execução responde pessoalmente com seu patrimônio pelos vícios da coisa praceada."
        },
        "gabarito": "A",
        "article": "Art. 441 do Código Civil",
        "legal_basis": "Art. 441 do Código Civil e Jurisprudência do STJ.",
        "explanation": "A jurisprudência do STJ e o Enunciado 28 da Jornada de Direito Civil pacificaram que o arrematante em hasta pública faz jus à garantia dos vícios redibitórios, podendo deduzir pretensão edilícia contra o credor ou executado."
    },
    # 17. EFEITOS DA BOA-FÉ E MÁ-FÉ DO ALIENANTE NO VÍCIO
    {
        "subject": "Efeitos da Boa-fé e Má-fé do Alienante no Vício",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) A ignorância do alienante sobre o vício redibitório oculto da coisa na data da venda:",
        "options": {
            "A": "Não o exime da garantia legal de redibir o contrato ou conceder abatimento no preço, mas afasta a sua condenação ao pagamento de perdas e danos.",
            "B": "Exime o alienante de qualquer obrigação, mantendo o negócio hígido e inalterado.",
            "C": "Transfere o dever de indenizar para o fabricante originário da matéria-prima.",
            "D": "Reduz o prazo decadencial para setenta e duas horas."
        },
        "gabarito": "A",
        "article": "Art. 443 do Código Civil",
        "legal_basis": "Art. 443 do Código Civil.",
        "explanation": "Art. 443: A garantia por vício redibitório independe de culpa. O vendedor de boa-fé apenas não paga perdas e danos adicionais, mas restitui o que recebeu mais as despesas do contrato."
    },
    # 18. AÇÕES EDILÍCIAS (REDIBITÓRIA E ESTIMATÓRIA/QUANTI MINORIS)
    {
        "subject": "Ações Edilícias (Redibitória e Estimatória/Quanti Minoris)",
        "bank": "FCC",
        "difficulty": "Médio",
        "enunciado": "(FCC / Magistratura) A característica preponderante que distingue a Ação Redibitória da Ação Estimatória (quanti minoris) é que:",
        "options": {
            "A": "A ação redibitória tem natureza desconstitutiva/resolutória (desfaz o contrato e devolve a coisa), ao passo que a ação estimatória tem natureza condenatória/modificativa (conserva o contrato e abate proporcionalmente o preço).",
            "B": "A ação redibitória exige prova de dolo, enquanto a ação estimatória exige prova de coação moral.",
            "C": "A ação estimatória só pode ser ajuizada se o bem for um imóvel rural.",
            "D": "A ação redibitória prescreve em 20 anos pelo Código Civil."
        },
        "gabarito": "A",
        "article": "Arts. 441 e 442 do Código Civil",
        "legal_basis": "Arts. 441 e 442 do Código Civil.",
        "explanation": "Ação Redibitória: resolução do contrato (desconstituição do vínculo com restituição mútua). Ação Estimatória (quanti minoris): manutenção do vínculo negocial com redução proporcional do montante pecuniário (princípio da conservação dos contratos)."
    },
    # 19. VÍCIO REDIBITÓRIO VS. ENTREGA DE COISA DIVERSA (ALIUD PRO ALIO)
    {
        "subject": "Vício Redibitório vs. Entrega de Coisa Diversa (Aliud Pro Alio)",
        "bank": "VUNESP",
        "difficulty": "Difícil",
        "enunciado": "(VUNESP / Magistratura) Considere as duas situações: I) João comprou um imóvel residencial e descobriu que as tubulações internas de esgoto estavam corroídas e rompidas (defeito oculto de engenharia); II) Maria comprou o lote 10 da quadra B, mas o vendedor entregou-lhe a posse do lote 10 da quadra C. Juridicamente, os casos tratam, respectivamente, de:",
        "options": {
            "A": "I - Vício redibitório (ação edilícia com prazo decadencial do art. 445); II - Entrega de coisa diversa / aliud pro alio (inadimplemento de obrigação de dar com prazo prescricional decenal).",
            "B": "I - Aliud pro alio; II - Vício redibitório.",
            "C": "Ambos tratam de evicção judicial.",
            "D": "Ambos tratam de vícios redibitórios subordinados à decadência de 30 dias."
        },
        "gabarito": "A",
        "article": "Arts. 389, 441 e 445 do Código Civil",
        "legal_basis": "Arts. 389, 441 e 445 do Código Civil e Jurisprudência do STJ.",
        "explanation": "No caso I, a coisa entregue é a mesma contratada, mas com defeito oculto funcional (vício redibitório). No caso II, entregou-se coisa diversa da avençada (aliud pro alio), gerando inadimplemento absoluto de obrigação de dar."
    },
    # 20. PRAZOS DECADENCIAIS DOS VÍCIOS REDIBITÓRIOS
    {
        "subject": "Prazos Decadenciais dos Vícios Redibitórios",
        "bank": "CESPE",
        "difficulty": "Médio",
        "enunciado": "(CESPE / Notário) Se o adquirente de bem móvel já estava na posse da coisa na data em que celebrou a compra e venda definitiva (ex: locatário que decide comprar o bem alugado), o prazo para redibir ou pedir abatimento por vício redibitório ostensivo:",
        "options": {
            "A": "Conta-se da alienação, reduzido à metade, ou seja, no prazo de 15 (quinze) dias (art. 445 do CC).",
            "B": "Passa a ser de 60 dias úteis a contar da tradição originária da locação.",
            "C": "Extingue-se de plano por renúncia tácita à garantia edilícia.",
            "D": "Equipara-se ao prazo decenal de responsabilidade civil extracontratual."
        },
        "gabarito": "A",
        "article": "Art. 445 do Código Civil",
        "legal_basis": "Art. 445, parte final ('...se já estava na posse, o prazo conta-se da alienação, reduzido à metade').",
        "explanation": "Para móveis, a regra geral é 30 dias da entrega. Se o comprador já estava na posse da coisa, o prazo corre da data da alienação (do contrato) e reduz-se pela metade (15 dias para móveis, 6 meses para imóveis)."
    },
    # 21. EXTINÇÃO DOS CONTRATOS - RESOLUÇÃO E CLÁUSULA RESOLUTIVA
    {
        "subject": "Extinção dos Contratos - Resolução e Cláusula Resolutiva",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) A resolução do contrato por inadimplemento voluntário (culposo) imputável ao devedor acarreta:",
        "options": {
            "A": "A extinção da relação contratual com retorno das partes ao status quo ante, acrescida da condenação do devedor ao pagamento de perdas e danos (danos emergentes e lucros cessantes).",
            "B": "Apenas o dever de desculpas formais sem qualquer repercussão indenizatória.",
            "C": "A conversão forçada de todas as dívidas civis em obrigações naturais inexigíveis.",
            "D": "A exoneração automática do devedor de todas as despesas processuais."
        },
        "gabarito": "A",
        "article": "Art. 475 do Código Civil",
        "legal_basis": "Art. 475 do Código Civil.",
        "explanation": "Art. 475 do CC: 'A parte lesada pelo inadimplemento pode pedir a resolução do contrato, se não preferir exigir-lhe o cumprimento, cabendo, em qualquer dos casos, indenização por perdas e danos'."
    },
    # 22. EXCEÇÃO DO CONTRATO NÃO CUMPRIDO E ONEROSIDADE EXCESSIVA
    {
        "subject": "Exceção do Contrato Não Cumprido e Onerosidade Excessiva",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) Nos contratos de execução continuada ou diferida, se a prestação de uma das partes se tornar excessivamente onerosa, com extrema vantagem para a outra, em virtude de acontecimentos extraordinários e imprevisíveis (Art. 478 do Código Civil):",
        "options": {
            "A": "Poderá o devedor pedir a resolução do contrato, podendo o réu evitar a resolução oferecendo-se a modificar equitativamente as condições do contrato (art. 479 do CC).",
            "B": "O contrato torna-se nulo de pleno direito no plano da existência.",
            "C": "O credor pode executar imediatamente a penhora de todos os bens de família do devedor.",
            "D": "O juiz é proibido de acolher proposta de renegociação consensual das partes."
        },
        "gabarito": "A",
        "article": "Art. 478 e Art. 479 do Código Civil",
        "legal_basis": "Arts. 478 e 479 do Código Civil.",
        "explanation": "Teoria da Imprevisão / Onerosidade Excessiva (art. 478). O devedor pode pleitear a resolução do pacto. Porém, em homenagem à conservação do negócio, o art. 479 autoriza o réu a evitar o desfazimento oferecendo revisão equitativa das bases contratuais."
    }
]

for q in MORE_QUESTIONS:
    if "id" not in q:
        q["id"] = str(uuid.uuid4())
    existing.append(q)

data["questions"] = existing

with open("database/seed_questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Sucesso absoluto! Total acumulado de questões no seed pool: {len(existing)}")
