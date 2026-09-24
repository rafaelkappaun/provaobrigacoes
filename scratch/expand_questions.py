import json
import uuid

with open("database/seed_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

existing = data.get("questions", [])

ADDITIONAL_QUESTIONS = [
    # 1. PLANOS DO NEGÓCIO JURÍDICO (ESCADA PONTEANA)
    {
        "subject": "Planos do Negócio Jurídico (Escada Ponteana)",
        "bank": "VUNESP",
        "difficulty": "Médio",
        "enunciado": "(VUNESP / Delegado) No plano da eficácia do negócio jurídico, a aposição de um encargo (ou modo) em uma doação de bem imóvel:",
        "options": {
            "A": "Suspende a aquisição e o exercício do direito pelo donatário até que o encargo seja cumprido.",
            "B": "Não suspende a aquisição nem o exercício do direito, salvo quando expressamente imposto no negócio como condição suspensiva pelo disponente.",
            "C": "Torna o negócio jurídico juridicamente inexistente enquanto não homologado por sentença judicial.",
            "D": "Macula o negócio no plano da validade com vício de simulação absoluta."
        },
        "gabarito": "B",
        "article": "Art. 136 do Código Civil",
        "legal_basis": "Art. 136 do Código Civil.",
        "explanation": "Art. 136 do CC: 'O encargo não suspende a aquisição nem o exercício do direito, salvo quando expressamente imposto no negócio, pelo disponente, como condição suspensiva'. Atua no plano da eficácia."
    },
    {
        "subject": "Planos do Negócio Jurídico (Escada Ponteana)",
        "bank": "CESPE",
        "difficulty": "Médio",
        "enunciado": "(CESPE / Doutrina) Um contrato foi celebrado mediante coação moral irresistível exercida sobre uma das partes. Sob a ótica da Escada Ponteana:",
        "options": {
            "A": "O negócio existe, porém padece de vício no plano da validade, sendo classificado como ato anulável (art. 171, II do CC).",
            "B": "O negócio é nulo de pleno direito no plano da existência, não chegando ao mundo jurídico.",
            "C": "O negócio é inexistente por ausência total de manifestação da vontade humana.",
            "D": "O negócio é válido, operando no plano da eficácia apenas contra terceiros de má-fé."
        },
        "gabarito": "A",
        "article": "Art. 171, II do Código Civil",
        "legal_basis": "Art. 171, II do Código Civil e Escada Ponteana.",
        "explanation": "A coação moral (vis compulsiva) não exclui a existência da manifestação de vontade, mas contamina sua liberdade, situando-se no Plano da Validade como causa de anulabilidade (art. 171, II)."
    },

    # 2. PRINCÍPIOS DO DIREITO CONTRATUAL
    {
        "subject": "Princípios do Direito Contratual",
        "bank": "FCC",
        "difficulty": "Médio",
        "enunciado": "(FCC / DPE) O princípio da força obrigatória dos contratos (pacta sunt servanda) no direito civil contemporâneo:",
        "options": {
            "A": "Permanece como postulado de segurança jurídica, sendo todavia relativizado pela função social, pela boa-fé objetiva e pela Teoria da Imprevisão / Onerosidade Excessiva.",
            "B": "Foi inteiramente revogado pelo Código Civil de 2002, cabendo ao juiz redefinir livremente todas as cláusulas e preços das convenções privadas.",
            "C": "Aplica-se unicamente aos contratos unilaterais regidos pelo direito administrativo.",
            "D": "Impede em qualquer circunstância a resolução contratual por eventos imprevisíveis e extraordinários."
        },
        "gabarito": "A",
        "article": "Arts. 421, 422 e 478 do Código Civil",
        "legal_basis": "Arts. 421, 422 e 478 do Código Civil.",
        "explanation": "O pacta sunt servanda continua em pleno vigor, mas sob feição social: subordina-se à função social (art. 421), à boa-fé objetiva (art. 422) e à revisão por onerosidade excessiva imprevisível (art. 478)."
    },

    # 3. BOA-FÉ OBJETIVA E FIGURAS PARCELARES
    {
        "subject": "Boa-fé Objetiva e Figuras Parcelares",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB / FGV) A doutrina e a jurisprudência consagram o 'Duty to mitigate the loss' (dever do credor de mitigar o próprio prejuízo) como figura parcelar da boa-fé objetiva. Esse dever impõe ao credor:",
        "options": {
            "A": "A obrigação ética e jurídica de adotar medidas razoáveis para não agravar o dano patrimonial decorrente do inadimplemento do devedor, sob pena de redução da indenização.",
            "B": "A obrigação de renunciar tacitamente aos juros moratórios vencidos há mais de 30 dias.",
            "C": "O dever de pagar integralmente as custas processuais do devedor inadimplente.",
            "D": "A proibição de ajuizar qualquer ação de execução antes de 5 anos de inadimplência."
        },
        "gabarito": "A",
        "article": "Art. 422 do Código Civil",
        "legal_basis": "Art. 422 do Código Civil e Enunciado 169 da III Jornada de Direito Civil.",
        "explanation": "O 'duty to mitigate the loss' decorre da boa-fé objetiva (art. 422): o credor não pode permanecer inerte assistindo à dívida e ao dano crescerem indefinidamente para cobrar indenização astronômica posterior."
    },
    {
        "subject": "Boa-fé Objetiva e Figuras Parcelares",
        "bank": "VUNESP",
        "difficulty": "Médio",
        "enunciado": "(VUNESP / TJ) Os deveres anexos, laterais ou instrumentais de conduta decorrentes da cláusula geral de boa-fé objetiva (art. 422 do CC):",
        "options": {
            "A": "Existem independentemente de previsão expressa no instrumento contratual e compreendem os deveres de lealdade, informação, proteção, cooperação e sigilo.",
            "B": "Dependem de cláusula penal escrita expressa para gerarem qualquer efeito vinculante.",
            "C": "Expiram de pleno direito imediatamente no momento em que as assinaturas do contrato são lançadas.",
            "D": "Aplicam-se apenas aos contratos de consumo regulados pelo Procon."
        },
        "gabarito": "A",
        "article": "Art. 422 do Código Civil",
        "legal_basis": "Art. 422 do Código Civil e Doutrina de Judith Martins-Costa.",
        "explanation": "Os deveres anexos decorrem da própria lei e da eticidade, vinculando os contratantes antes, durante e após o cumprimento do contrato (fases pré, de cumprimento e pós-contratual)."
    },

    # 4. INTERPRETAÇÃO DOS CONTRATOS NO DIREITO BRASILEIRO
    {
        "subject": "Interpretação dos Contratos no Direito Brasileiro",
        "bank": "CESPE",
        "difficulty": "Médio",
        "enunciado": "(CESPE / Analista) De acordo com as diretrizes do Art. 113, § 1º do Código Civil (incluído pela Lei 13.874/2019), a interpretação do negócio jurídico deve lhe atribuir o sentido que:",
        "options": {
            "A": "For confirmado pelo comportamento das partes posterior à celebração e for mais benéfico à parte que não redigiu o dispositivo contratual.",
            "B": "Sempre prestigie a parte que redigiu a cláusula por haver investido nos custos de elaboração.",
            "C": "Desconsidere categoricamente os usos e costumes do local onde o contrato foi celebrado.",
            "D": "Invalide de ofício qualquer contrato que não tenha sido lavrado em notas de tabelião."
        },
        "gabarito": "A",
        "article": "Art. 113, § 1º do Código Civil",
        "legal_basis": "Art. 113, § 1º, incisos I a V do Código Civil.",
        "explanation": "O § 1º do art. 113 estabelece critérios objetivos: comportamento posterior das partes, usos e costumes do mercado, razoabilidade da negociação e interpretação contra proferentem (em favor de quem não redigiu a cláusula)."
    },

    # 5. CLASSIFICAÇÃO DOS CONTRATOS
    {
        "subject": "Classificação dos Contratos",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) A respeito da classificação dos contratos, quanto à presença ou ausência de solenidade e quanto ao momento do cumprimento das prestações, assinale a opção correta.",
        "options": {
            "A": "Os contratos solenes são aqueles para os quais a lei exige forma determinada como requisito de validade (ad solemnitatem), como a escritura pública na compra e venda de imóvel de valor superior a 30 salários mínimos.",
            "B": "Os contratos de execução continuada (ou de trato sucessivo) cumprem-se em um único ato instantâneo imediatamente após a manifestação do consentimento.",
            "C": "O contrato de adesão permite que o aderente altere substancialmente as cláusulas nucleares do negócio em mesa paritária de negociação.",
            "D": "Todo contrato oneroso é necessariamente solene e formal."
        },
        "gabarito": "A",
        "article": "Art. 107 e Art. 108 do Código Civil",
        "legal_basis": "Arts. 107 e 108 do Código Civil.",
        "explanation": "Contratos solenes exigem forma estrita da lei para valerem (art. 108: escritura pública para imóveis acima de 30 salários mínimos). Contratos de trato sucessivo têm cumprimento diferido e repetido no tempo."
    },

    # 6. ETAPAS DE FORMAÇÃO DO CONTRATO
    {
        "subject": "Etapas de Formação do Contrato",
        "bank": "VUNESP",
        "difficulty": "Médio",
        "enunciado": "(VUNESP / Notário) Se a aceitação da proposta for expedida com prazo, mas chegar tardiamente ao proponente por circunstâncias imprevistas, nos termos do Art. 430 do Código Civil:",
        "options": {
            "A": "O proponente deverá comunicar imediatamente o fato ao aceitante, sob pena de responder por perdas e danos.",
            "B": "O contrato se considera nulo de pleno direito, dispensando qualquer comunicação ao aceitante.",
            "C": "A aceitação tardia converte-se automaticamente em contrato definitivo concluído sem ressalvas.",
            "D": "O aceitante decai de todos os seus direitos civis patrimoniais."
        },
        "gabarito": "A",
        "article": "Art. 430 do Código Civil",
        "legal_basis": "Art. 430 do Código Civil.",
        "explanation": "Art. 430 do CC: 'Se a aceitação, por circunstância imprevista, chegar tarde ao conhecimento do proponente, este, sob pena de responder por perdas e danos, deverá comunicá-lo imediatamente ao aceitante'."
    },

    # 7. ESTIPULAÇÃO EM FAVOR DE TERCEIRO
    {
        "subject": "Estipulação em Favor de Terceiro",
        "bank": "FCC",
        "difficulty": "Médio",
        "enunciado": "(FCC / Procurador) Na Estipulação em Favor de Terceiro disciplinada pelo Código Civil:",
        "options": {
            "A": "O estipulante pode exonerar o devedor promitente, salvo se ao terceiro beneficiário foi deixado expressamente o direito de reclamar a execução do contrato.",
            "B": "O promitente pode unilateralmente indicar outro credor sem conhecimento das partes.",
            "C": "A morte do terceiro beneficiário antes do vencimento extingue automaticamente a obrigação do promitente.",
            "D": "O terceiro é obrigado a remunerar o estipulante em comissão de corretagem obrigatória."
        },
        "gabarito": "A",
        "article": "Art. 437 do Código Civil",
        "legal_basis": "Art. 437 do Código Civil.",
        "explanation": "O estipulante pode liberar o devedor/promitente se não tiver transferido de forma irrevogável o direito de cobrança direta ao terceiro (art. 437)."
    },

    # 8. PROMESSA DE FATO DE TERCEIRO
    {
        "subject": "Promessa de Fato de Terceiro",
        "bank": "CESPE",
        "difficulty": "Difícil",
        "enunciado": "(CESPE / Doutrina) O parágrafo único do Art. 439 do Código Civil estabelece uma causa especial de exoneração da responsabilidade de quem prometeu fato de terceiro. Essa responsabilidade NÃO existirá se:",
        "options": {
            "A": "O terceiro for o cônjuge do promitente, dependendo da sua anuência o ato a ser praticado, e pelo regime de bens a indenização alguma coisa do seu patrimônio possa arrebatar.",
            "B": "O terceiro for amigo de infância do promitente.",
            "C": "O promitente comprovar que o terceiro viajou para o exterior em férias.",
            "D": "O credor tiver patrimônio líquido superior ao do promitente."
        },
        "gabarito": "A",
        "article": "Art. 439, parágrafo único do Código Civil",
        "legal_basis": "Art. 439, parágrafo único do Código Civil.",
        "explanation": "Art. 439, parágrafo único: Exclui a indenização se o terceiro for o cônjuge do promitente e o pagamento da indenização atingir o patrimônio do próprio terceiro em razão da meação/comunhão de bens."
    },

    # 9. CONTRATOS ALEATÓRIOS - CONCEITO E ESPÉCIES
    {
        "subject": "Contratos Aleatórios - Conceito e Espécies",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) No contrato aleatório, a equivalência subjetiva das prestações cede espaço à álea assumida pelos contratantes. Por tal razão, em regra, nos contratos aleatórios:",
        "options": {
            "A": "Não se admite a rescisão por lesão com fundamento na mera desproporção do resultado advindo da sorte (álea) contratada, salvo dolo da outra parte.",
            "B": "É vedada a fixação de preço em moeda corrente nacional.",
            "C": "As partes são obrigadas a registrar o contrato perante a Bolsa de Valores.",
            "D": "A morte de qualquer dos contratantes invalida retroativamente a álea."
        },
        "gabarito": "A",
        "article": "Art. 157 e Art. 458 do Código Civil",
        "legal_basis": "Arts. 157 e 458 do Código Civil e Doutrina Contratual.",
        "explanation": "Na lesão (art. 157) exige-se desproporção manifesta originária na comutatividade. Nos contratos aleatórios, como o desequilíbrio potencial é da própria essência do risco assumido, a álea normal não enseja vício de lesão."
    },

    # 10. CONTRATO ALEATÓRIO: EMPTIO SPEI
    {
        "subject": "Contrato Aleatório: Emptio Spei",
        "bank": "FCC",
        "difficulty": "Médio",
        "enunciado": "(FCC / Magistratura) Na venda de coisas futuras na modalidade Emptio Spei (Art. 458 do Código Civil), caso o alienante venha a agir com dolo ou culpa comprovada para a frustração do objeto:",
        "options": {
            "A": "Perderá o direito de receber o preço e deverá indenizar perdas e danos, pois a álea não acoberta a desídia ou a má-fé do contratante.",
            "B": "Continuará tendo direito ao preço integral, pois o risco assumido pelo adquirente é absoluto e incondicionado.",
            "C": "O contrato converter-se-á compulsoriamente em sociedade em conta de participação.",
            "D": "O comprador poderá apenas exigir abatimento de 10% no valor contratado."
        },
        "gabarito": "A",
        "article": "Art. 458 do Código Civil",
        "legal_basis": "Art. 458 ('...desde que de sua parte não tenha havido dolo ou culpa...').",
        "explanation": "O art. 458 é categórico: o alienante só recebe o preço integral se de sua parte não tiver havido dolo ou culpa na frustração da coisa futura."
    },

    # 11. CONTRATO ALEATÓRIO: EMPTIO REI SPERATAE
    {
        "subject": "Contrato Aleatório: Emptio Rei Speratae",
        "bank": "VUNESP",
        "difficulty": "Médio",
        "enunciado": "(VUNESP / TJ) Um comprador pactuou contrato aleatório de compra de colheita de laranjas assumindo o risco quanto à quantidade (Emptio Rei Speratae). O pomar sofreu praga natural sem culpa do agricultor e colheu apenas 1% do volume ordinário esperado. Nesse caso:",
        "options": {
            "A": "O comprador é obrigado a pagar a totalidade do preço convencionado, tendo em vista que alguma quantidade veio a existir e a álea assumida dizia respeito à quantidade.",
            "B": "O comprador não deve pagar nada, pois a quantidade foi irrisória e descaracteriza a comutatividade.",
            "C": "O agricultor deve pagar indenização ao comprador para compensar a perda.",
            "D": "O contrato é nulo de pleno direito por quebra da base objetiva."
        },
        "gabarito": "A",
        "article": "Art. 459 do Código Civil",
        "legal_basis": "Art. 459, caput do Código Civil.",
        "explanation": "Conforme o art. 459, caput, na emptio rei speratae o alienante tem direito a todo o preço ainda que a coisa venha a existir em quantidade inferior à esperada. Só se nada vier a existir é que o negócio desfaz-se (parágrafo único)."
    },

    # 12. CONTRATO ALEATÓRIO: COISAS EXISTENTES EXPOSTAS A RISCO
    {
        "subject": "Contrato Aleatório: Coisas Existentes Expostas a Risco",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) A compra e venda aleatória de carga em transporte que se encontra exposta a alto risco no momento do contrato (arts. 460 e 461 do CC):",
        "options": {
            "A": "Pode ser anulada como dolosa pelo prejudicado se este provar que o outro contratante não ignorava a consumação prévia do risco.",
            "B": "É proibida pelo direito brasileiro como contrato usurário.",
            "C": "Transfere os riscos exclusivamente para a seguradora pública da União.",
            "D": "Obriga o alienante a devolver em dobro o preço caso a coisa pereça no trajeto."
        },
        "gabarito": "A",
        "article": "Art. 461 do Código Civil",
        "legal_basis": "Art. 461 do Código Civil.",
        "explanation": "Art. 461: Se o alienante já sabia que a carga havia sido destruída ou naufragado, sua omissão dolosa autoriza a anulação do contrato pelo comprador."
    },

    # 13. CONTRATO PRELIMINAR / PROMESSA DE CONTRATAR
    {
        "subject": "Contrato Preliminar / Promessa de Contratar",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) Sobre o registro do compromisso de compra e venda de imóvel no Cartório de Registro de Imóveis, consoante a Súmula 239 do Superior Tribunal de Justiça (STJ):",
        "options": {
            "A": "O direito à adjudicação compulsória não se condiciona ao registro do compromisso de compra e venda no cartório de imóveis perante o promitente vendedor.",
            "B": "A ausência de registro torna o compromisso de compra e venda absolutamente inexistente no plano material.",
            "C": "Apenas os contratos registrados por escritura pública conferem direito a perdas e danos.",
            "D": "O registro do contrato preliminar é pressuposto de existência na Escada Ponteana."
        },
        "gabarito": "A",
        "article": "Art. 463 do Código Civil e Súmula 239 do STJ",
        "legal_basis": "Súmula 239 do STJ e Art. 463 do Código Civil.",
        "explanation": "A Súmula 239 do STJ sedimentou que o promitente comprador pode exigir do vendedor a adjudicação compulsória mesmo sem registro imobiliário do compromisso. O registro confere eficácia erga omnes perante terceiros (direito real de aquisição - art. 1.417), mas inter partes a pretensão existe."
    },

    # 14. CONTRATO COM PESSOA A DECLARAR
    {
        "subject": "Contrato com Pessoa a Declarar",
        "bank": "VUNESP",
        "difficulty": "Médio",
        "enunciado": "(VUNESP / Magistratura) Concluído o contrato com pessoa a declarar (arts. 467 e seguintes do CC), a indicação da pessoa nomeada (electio amici):",
        "options": {
            "A": "Não produzirá efeito se a pessoa nomeada era incapaz ou insolvente no momento da nomeação, hipótese em que o contrato produzirá efeitos unicamente entre os contraentes originários.",
            "B": "Exonera o estipulante originário mesmo se a pessoa indicada recusar formalmente a nomeação.",
            "C": "Transfere a posse da coisa apenas a partir do trânsito em julgado de sentença arbitral.",
            "D": "Depende de nova escrituração pública de dação em pagamento."
        },
        "gabarito": "A",
        "article": "Art. 470, II do Código Civil",
        "legal_basis": "Art. 470, II do Código Civil.",
        "explanation": "Art. 470, II: O contrato produz efeitos exclusivamente entre os contratantes originários se a pessoa nomeada era incapaz ou insolvente na hora da indicação e o outro contratante ignorava."
    },

    # 15. CONTRATO COM PESSOA A DECLARAR VS. OUTROS CONTRATOS
    {
        "subject": "Contrato com Pessoa a Declarar vs. Outros Contratos",
        "bank": "FCC",
        "difficulty": "Difícil",
        "enunciado": "(FCC / PGE) Diferentemente da Cessão da Posição Contratual, o Contrato com Pessoa a Declarar caracteriza-se porque:",
        "options": {
            "A": "A faculdade de substituição subjetiva já é pactuada na origem do próprio negócio com cláusula de eficácia retroativa (ex tunc), ao passo que a cessão é negócio derivado posterior que depende de anuência superveniente do cedido.",
            "B": "O cessionário na cessão adquire apenas direitos, ficando isento de quaisquer dívidas.",
            "C": "O contrato com pessoa a declarar é sempre gratuito, não se admitindo ônus para a pessoa declarada.",
            "D": "A cessão da posição contratual é vedada a pessoas jurídicas de direito privado."
        },
        "gabarito": "A",
        "article": "Art. 467 do Código Civil",
        "legal_basis": "Art. 467 do Código Civil e Doutrina Contratual.",
        "explanation": "No contrato com pessoa a declarar, a cláusula pro amico integra a gênese do contrato e opera efeitos retroativos ex tunc desde a formação. Na cessão de contrato ordinária, há um negócio autônomo posterior de transferência com efeitos normalmente ex nunc."
    },

    # 16. VÍCIOS REDIBITÓRIOS - CONCEITO E REQUISITOS
    {
        "subject": "Vícios Redibitórios - Conceito e Requisitos",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) Se várias coisas forem vendidas conjuntamente por preço global e apenas uma delas apresentar vício redibitório oculto, segundo o Art. 503 do Código Civil:",
        "options": {
            "A": "O defeito oculto de uma delas não autoriza a redibição de todas, mas tão-só a da que estiver viciada, salvo se a viciada for inseparável ou formar um todo unitário com as demais.",
            "B": "Todo o contrato deve ser rescindido compulsoriamente por imposição da boa-fé objetiva.",
            "C": "O adquirente perde o direito a qualquer reclamação edilícia se não provar o dolo do vendedor.",
            "D": "O valor global do contrato é reduzido automaticamente em 50%."
        },
        "gabarito": "A",
        "article": "Art. 503 do Código Civil",
        "legal_basis": "Art. 503 do Código Civil.",
        "explanation": "Art. 503 do CC: 'Nas coisas vendidas conjuntamente, o defeito oculto de uma não autoriza a rejeição de todas, mas tão-somente a da defeituosa' (princípio da conservação dos contratos), salvo se formarem um todo inseparável (ex: junta de bois)."
    },

    # 17. EFEITOS DA BOA-FÉ E MÁ-FÉ DO ALIENANTE NO VÍCIO
    {
        "subject": "Efeitos da Boa-fé e Má-fé do Alienante no Vício",
        "bank": "CESPE",
        "difficulty": "Médio",
        "enunciado": "(CESPE / Defensoria) Se a coisa alienada vier a perecer em poder do adquirente em decorrência direta do próprio vício oculto que já trazia consigo na entrega, nos termos do Art. 444 do Código Civil:",
        "options": {
            "A": "A responsabilidade subsiste para o alienante: se conhecia o vício, responderá pelo valor mais perdas e danos; se não conhecia, ressarcirá o que recebeu mais despesas do contrato.",
            "B": "O alienante fica totalmente isento de responsabilidade com base na regra de que a coisa perece para o dono (res perit domino).",
            "C": "O adquirente deve indenizar o alienante pela perda da oportunidade de consertar o bem.",
            "D": "O contrato é convalidado como dação em pagamento involuntária."
        },
        "gabarito": "A",
        "article": "Art. 444 do Código Civil",
        "legal_basis": "Art. 444 do Código Civil.",
        "explanation": "Art. 444 do CC: 'A responsabilidade do alienante subsiste ainda que a coisa pereça em poder do adquirente, se perecer por vício oculto, constante do tempo da tradição'. A causa da perda foi o defeito anterior entregue."
    },

    # 18. AÇÕES EDILÍCIAS (REDIBITÓRIA E ESTIMATÓRIA/QUANTI MINORIS)
    {
        "subject": "Ações Edilícias (Redibitória e Estimatória/Quanti Minoris)",
        "bank": "VUNESP",
        "difficulty": "Médio",
        "enunciado": "(VUNESP / TJ) Uma vez ajuizada pelo adquirente a Ação Estimatória (quanti minoris) requerendo o abatimento no preço em virtude de vício redibitório:",
        "options": {
            "A": "Opera-se a opção potestativa irretratável pela conservação do contrato com redução proporcional do valor, precluindo o direito de pleitear a devolução da coisa via ação redibitória.",
            "B": "O juiz é obrigado a converter de ofício a petição inicial em ação de reintegração de posse.",
            "C": "O vendedor pode recusar o abatimento e exigir judicialmente a devolução compulsória do bem.",
            "D": "O comprador deve prestar caução no valor de 30% do contrato."
        },
        "gabarito": "A",
        "article": "Art. 442 do Código Civil",
        "legal_basis": "Art. 442 do Código Civil e Doutrina de Nelson Nery Jr.",
        "explanation": "O adquirente dispõe de faculdade de escolha alternativa e disjuntiva entre a redibição e o abatimento no preço (art. 442). Escolhendo a ação estimatória, opta por conservar o contrato abatendo o preço."
    },

    # 19. VÍCIO REDIBITÓRIO VS. ENTREGA DE COISA DIVERSA (ALIUD PRO ALIO)
    {
        "subject": "Vício Redibitório vs. Entrega de Coisa Diversa (Aliud Pro Alio)",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB / FGV) Um laboratório farmacêutico celebrou contrato de compra de insumos químicos para entrega de 500 kg de matéria-prima 'A'. Ao receber a carga, constatou que a fornecedora havia despachado matéria-prima 'B' (composto totalmente diverso). Nessa situação jurídica:",
        "options": {
            "A": "Trata-se de inadimplemento da obrigação de dar por entrega de coisa diversa (aliud pro alio), aplicando-se as regras gerais de perdas e danos e prazo prescricional decenal (art. 205 do CC), e não vício redibitório.",
            "B": "Trata-se de vício redibitório de produto industrial, decaindo o direito do laboratório em trinta dias da entrega.",
            "C": "O contrato é nulo de pleno direito por motivo torpe de ambas as partes.",
            "D": "O comprador só pode recusar a carga se notificar o alienante perante o Conselho de Farmácia em 48 horas."
        },
        "gabarito": "A",
        "article": "Arts. 205, 389 e 441 do Código Civil",
        "legal_basis": "Arts. 205, 389 e 475 do Código Civil e Jurisprudência pacífica do STJ.",
        "explanation": "No aliud pro alio, a prestação executada é ontologicamente diferente da contratada. O STJ firmou que essa hipótese constitui inadimplemento contratual de obrigação de entregar, sujeitando-se ao prazo prescricional de 10 anos (art. 205 do CC), e não à decadência edilícia de vícios redibitórios."
    },

    # 20. PRAZOS DECADENCIAIS DOS VÍCIOS REDIBITÓRIOS
    {
        "subject": "Prazos Decadenciais dos Vícios Redibitórios",
        "bank": "FCC",
        "difficulty": "Médio",
        "enunciado": "(FCC / Magistratura) Conforme o Art. 446 do Código Civil, os prazos de decadência para redibição ou abatimento no preço (art. 445) NÃO correm:",
        "options": {
            "A": "Na constância de cláusula de garantia estipulada pelo alienante; mas o adquirente deve denunciar o defeito ao alienante nos trinta dias seguintes ao seu descobrimento, sob pena de decadência.",
            "B": "Durante o período de férias forenses do Tribunal de Justiça local.",
            "C": "Enquanto o comprador não registrar o veículo no Detran competente.",
            "D": "Se a coisa for objeto de seguro facultativo contra terceiros."
        },
        "gabarito": "A",
        "article": "Art. 446 do Código Civil",
        "legal_basis": "Art. 446 do Código Civil.",
        "explanation": "Art. 446 do CC: 'Não correrão os prazos do artigo antecedente na constância de cláusula de garantia; mas o adquirente deve denunciar o defeito ao alienante nos trinta dias seguintes ao seu descobrimento, sob pena de decadência'."
    },

    # 21. EXTINÇÃO DOS CONTRATOS - RESOLUÇÃO E CLÁUSULA RESOLUTIVA
    {
        "subject": "Extinção dos Contratos - Resolução e Cláusula Resolutiva",
        "bank": "CESPE",
        "difficulty": "Médio",
        "enunciado": "(CESPE / Defensoria) Sobre a extinção dos contratos por resilição bilateral (distrato) e resilição unilateral (denúncia), assinale a afirmativa correta à luz dos arts. 472 e 473 do Código Civil.",
        "options": {
            "A": "O distrato faz-se pela mesma forma exigida para o contrato; e a resilição unilateral, nos casos em que a lei admite, opera mediante denúncia notificada à outra parte.",
            "B": "O distrato pode ser realizado verbalmente mesmo que a lei exija escritura pública para a validade do contrato primitivo.",
            "C": "A resilição unilateral independe de notificação ou aviso prévio em qualquer relação contratual.",
            "D": "O distrato extingue o contrato por vício de dolo congênito à celebração."
        },
        "gabarito": "A",
        "article": "Art. 472 e Art. 473 do Código Civil",
        "legal_basis": "Arts. 472 e 473 do Código Civil.",
        "explanation": "Art. 472: 'O distrato faz-se pela mesma forma exigida para o contrato'. Art. 473: A resilição unilateral opera mediante denúncia notificada. Se uma das partes houver feito investimentos consideráveis, a denúncia só produz efeito depois de transcorrido prazo compatível (art. 473, parágrafo único)."
    },

    # 22. EXCEÇÃO DO CONTRATO NÃO CUMPRIDO E ONEROSIDADE EXCESSIVA
    {
        "subject": "Exceção do Contrato Não Cumprido e Onerosidade Excessiva",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) Se, depois de concluído o contrato bilateral, sobrevier a uma das partes contratantes diminuição em seu patrimônio capaz de comprometer ou tornar duvidosa a prestação pela qual se obrigou, segundo o Art. 477 do Código Civil:",
        "options": {
            "A": "A outra parte pode recusar a prestação que lhe incumbe, até que aquela satisfaça a que lhe cabe ou dê garantia bastante de satisfazê-la.",
            "B": "O contrato é rescindido imediatamente com cobrança compulsória da cláusula penal integral.",
            "C": "O juiz deve decretar a falência sumária do devedor em dificuldade.",
            "D": "A dívida é convertida compulsoriamente em título de crédito ao portador."
        },
        "gabarito": "A",
        "article": "Art. 477 do Código Civil",
        "legal_basis": "Art. 477 do Código Civil.",
        "explanation": "Art. 477 do CC: Consagra a exceção de insegurança da prestação (exceptio ante tempus): se sobrevier diminuição patrimonial duvidosa ao devedor, a outra parte pode reter a sua prestação até que receba garantia idônea."
    }
]

for q in ADDITIONAL_QUESTIONS:
    if "id" not in q:
        q["id"] = str(uuid.uuid4())
    existing.append(q)

data["questions"] = existing

with open("database/seed_questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total de questões no seed pool: {len(existing)}")
