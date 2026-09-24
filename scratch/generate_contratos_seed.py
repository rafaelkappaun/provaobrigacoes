import json
import uuid

# Banco completo e minucioso de questões de prova (OAB, FGV, CESPE, FCC, VUNESP e Doutrina)
# Mapeado 100% no Questionário da Prova de Contratos (itens 1 ao 22)

QUESTIONS = [
    # 1. PLANOS DO NEGÓCIO JURÍDICO (ESCADA PONTEANA)
    {
        "subject": "Planos do Negócio Jurídico (Escada Ponteana)",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) Segundo a clássica Teoria da Escada Ponteana formulada por Pontes de Miranda, a estrutura do negócio jurídico é analisada em três planos distintos: existência, validade e eficácia. A respeito dessa divisão tricotômica, assinale a afirmativa correta.",
        "options": {
            "A": "A capacidade do agente e a licitude do objeto são elementos situados no plano da existência do negócio jurídico.",
            "B": "A manifestação de vontade, as partes, o objeto e a forma integram o plano da existência; enquanto a capacidade do agente, a licitude do objeto e a forma prescrita ou não defesa em lei integram o plano da validade.",
            "C": "O plano da eficácia diz respeito unicamente à nulidade absoluta do negócio jurídico por vício de consentimento.",
            "D": "Um negócio jurídico nulo por incapacidade absoluta do agente é inexistente de pleno direito, não adentrando no mundo fático."
        },
        "gabarito": "B",
        "article": "Art. 104 do Código Civil",
        "legal_basis": "Art. 104 do Código Civil e Teoria Pontiana do Negócio Jurídico.",
        "explanation": "Na Escada Ponteana: 1) Plano da Existência (substantivos: partes, vontade, objeto e forma); 2) Plano da Validade (adjetivos qualificadores: agente capaz, vontade livre, objeto lícito/possível/determinado e forma prescrita em lei - art. 104); 3) Plano da Eficácia (elementos acidentais: condição, termo e encargo, além da produção de efeitos concretos)."
    },
    {
        "subject": "Planos do Negócio Jurídico (Escada Ponteana)",
        "bank": "CESPE",
        "difficulty": "Difícil",
        "enunciado": "(CESPE / Doutrina) A respeito da distinção entre os planos de existência, validade e eficácia do negócio jurídico, assinale a opção correta.",
        "options": {
            "A": "A condição suspensiva, enquanto pendente, impede a existência do negócio jurídico.",
            "B": "A condição suspensiva subordina a eficácia do negócio jurídico a evento futuro e incerto, não impedindo que o negócio já exista e seja válido.",
            "C": "A incapacidade relativa do agente impede que o negócio jurídico atinja o plano da existência.",
            "D": "Todo negócio jurídico válido é imediata e necessariamente eficaz, sendo incompatível a existência de negócio válido mas ineficaz."
        },
        "gabarito": "B",
        "article": "Art. 121 e Art. 125 do Código Civil",
        "legal_basis": "Arts. 104, 121 e 125 do Código Civil.",
        "explanation": "A condição suspensiva atua exclusivamente no Plano da Eficácia (3º degrau). O negócio jurídico sob condição suspensiva já existe e já é válido; apenas a produção dos seus efeitos (exigibilidade do direito) fica suspensa até o implemento do evento futuro e incerto (art. 125, CC)."
    },
    {
        "subject": "Planos do Negócio Jurídico (Escada Ponteana)",
        "bank": "FCC",
        "difficulty": "Médio",
        "enunciado": "(FCC / Magistratura) Um contrato de compra e venda de imóvel de elevado valor foi firmado por instrumento particular, desrespeitando a solenidade de escritura pública exigida pelo art. 108 do Código Civil. Sob a ótica da Escada Ponteana, esse negócio jurídico:",
        "options": {
            "A": "É inexistente, pois a forma é elemento ontológico do plano da existência que não se aperfeiçoou.",
            "B": "Existe no mundo dos fatos, porém é nulo no plano da validade por preterição de solenidade essencial que a lei considera para a sua validade.",
            "C": "É plenamente válido, bastando termo aditivo posterior para ratificar a forma.",
            "D": "É negócio com eficácia plena entre as partes, mas ineficaz perante terceiros."
        },
        "gabarito": "B",
        "article": "Art. 104, III e Art. 166, IV e V do Código Civil",
        "legal_basis": "Arts. 104, III, 108 e 166, IV e V do Código Civil.",
        "explanation": "A forma em si é elemento de existência. Já a forma legalmente prescrita ou pública (solenidade) é requisito do Plano da Validade (Art. 104, III). O desrespeito à forma legal torna o negócio nulo (Art. 166, IV), mas ele existe no plano fático."
    },

    # 2. PRINCÍPIOS DO DIREITO CONTRATUAL
    {
        "subject": "Princípios do Direito Contratual",
        "bank": "FGV",
        "difficulty": "Médio",
        "enunciado": "(FGV / OAB) Duas sociedades empresárias celebraram contrato paritário com expressa previsão de alocação de riscos climáticos. Sobre a função social do contrato e a liberdade contratual após a Lei da Liberdade Econômica (Lei 13.874/2019), assinale a afirmativa correta.",
        "options": {
            "A": "A função social do contrato autoriza a intervenção judicial irrestrita para anular qualquer cláusula livremente ajustada entre empresários.",
            "B": "Nas relações contratuais privadas, prevalecerão o princípio da intervenção mínima e a excepcionalidade da revisão contratual, presumindo-se paritários e simétricos os contratos civis e empresariais.",
            "C": "O princípio do pacta sunt servanda foi integralmente abolido do ordenamento jurídico brasileiro.",
            "D": "A alocação de riscos definida pelas partes não vincula o Poder Judiciário, devendo o juiz impor a repartição igualitária dos prejuízos."
        },
        "gabarito": "B",
        "article": "Art. 421 e Art. 421-A do Código Civil",
        "legal_basis": "Arts. 421, parágrafo único e 421-A do Código Civil (incluídos pela Lei 13.874/2019).",
        "explanation": "A Lei da Liberdade Econômica positivou expressamente a presunção de paridade e simetria nos contratos civis e empresariais (art. 421-A), o princípio da intervenção mínima e a excepcionalidade da revisão contratual (art. 421, parágrafo único)."
    },
    {
        "subject": "Princípios do Direito Contratual",
        "bank": "VUNESP",
        "difficulty": "Médio",
        "enunciado": "(VUNESP / Notário) O princípio da relatividade dos efeitos do contrato sofre importante mitigação na ordem jurídica contemporânea em virtude:",
        "options": {
            "A": "Da tutela externa do crédito e da eficácia transubjetiva da função social do contrato, que veda que o contrato prejudique terceiros ou que terceiros lesem o contrato.",
            "B": "Da vedação absoluta à celebração de contratos preliminares.",
            "C": "Da aplicação da exceptio non adimpleti contractus aos contratos unilaterais benéficos.",
            "D": "Da exigência de escritura pública para qualquer espécie de avença comercial."
        },
        "gabarito": "A",
        "article": "Art. 421 do Código Civil",
        "legal_basis": "Art. 421 do Código Civil e Enunciado 21 da Jornada de Direito Civil.",
        "explanation": "A eficácia externa da função social mitiga o princípio da relatividade dos efeitos contratuais (que restringia os efeitos apenas aos signatários), reconhecendo a tutela externa do crédito (o terceiro não pode cumpliciar-se com o inadimplemento) e impedindo que o contrato lese a coletividade."
    },

    # 3. BOA-FÉ OBJETIVA E FIGURAS PARCELARES
    {
        "subject": "Boa-fé Objetiva e Figuras Parcelares",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) Caio celebrou contrato de locação com Tício, comprometendo-se a pagar o aluguel até o dia 5 de cada mês. No entanto, durante 3 anos consecutivos, Caio pagou no dia 20, sem qualquer oposição de Tício. Inesperadamente, Tício notificou Caio cobrando multa e juros moratórios retroativos de todos os meses. Essa pretensão de Tício é ilegítima em razão do instituto da:",
        "options": {
            "A": "Supressio, que gerou a Surrectio para Caio, vedando o comportamento contraditório (venire contra factum proprium).",
            "B": "Exceptio doli generalis com efeitos extintivos de plano da locação.",
            "C": "Cláusula resolutiva tácita com eficácia ex tunc.",
            "D": "Novação subjetiva passiva compulsória por força de lei."
        },
        "gabarito": "A",
        "article": "Art. 422 e Art. 330 do Código Civil",
        "legal_basis": "Arts. 422 e 330 do Código Civil.",
        "explanation": "O não exercício reiterado de um direito contratual acarreta a perda da pretensão de exigi-lo (supressio) e o nascimento correlato da faculdade para a outra parte (surrectio). Além disso, a cobrança repentina viola o venire contra factum proprium (proibição de comportamento contraditório decorrente da boa-fé objetiva)."
    },
    {
        "subject": "Boa-fé Objetiva e Figuras Parcelares",
        "bank": "CESPE",
        "difficulty": "Difícil",
        "enunciado": "(CESPE / Procuradoria) A boa-fé objetiva desempenha tríplice função no ordenamento civil: interpretativa, integrativa (criação de deveres anexos) e de controle (limite ao exercício de direitos). Dentre os desdobramentos da boa-fé objetiva, a figura que veda a uma das partes exigir da outra uma conduta que ela própria descumpriu é denominada:",
        "options": {
            "A": "Tu quoque.",
            "B": "Supressio.",
            "C": "Surrectio.",
            "D": "Duty to mitigate the loss."
        },
        "gabarito": "A",
        "article": "Art. 422 do Código Civil",
        "legal_basis": "Art. 422 do Código Civil e Doutrina Contratual.",
        "explanation": "O instituto do 'Tu quoque' decorre da boa-fé objetiva e estabelece a regra da reciprocidade ética: ninguém pode invocar uma norma ou cláusula contra outrem se ele próprio descumpriu a regra anteriormente ('até tu?')."
    },

    # 4. INTERPRETAÇÃO DOS CONTRATOS NO DIREITO BRASILEIRO
    {
        "subject": "Interpretação dos Contratos no Direito Brasileiro",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) No que tange às regras de interpretação dos negócios jurídicos e contratos consagradas no Código Civil brasileiro, assinale a opção correta.",
        "options": {
            "A": "Nas declarações de vontade se atenderá mais à intenção nelas consubstanciada do que ao sentido literal da linguagem.",
            "B": "Os negócios jurídicos benéficos e a renúncia interpretam-se ampliativamente em favor do adquirente.",
            "C": "Nos contratos de adesão com cláusulas contraditórias, adota-se a interpretação mais favorável ao estipulante.",
            "D": "O comportamento das partes posterior à celebração do contrato não pode ser utilizado como critério de interpretação."
        },
        "gabarito": "A",
        "article": "Art. 112 do Código Civil",
        "legal_basis": "Arts. 112, 113, § 1º, 114 e 423 do Código Civil.",
        "explanation": "O art. 112 consagra a prevalência da intenção sobre a literalidade estrita. Já os negócios benéficos interpretam-se estritamente (art. 114), e no contrato de adesão a ambiguidade favorece o aderente (art. 423)."
    },
    {
        "subject": "Interpretação dos Contratos no Direito Brasileiro",
        "bank": "FCC",
        "difficulty": "Médio",
        "enunciado": "(FCC / Defensoria) A respeito da interpretação dos negócios benéficos (gratuitos) e dos atos de renúncia de direitos no Código Civil, é correto afirmar que:",
        "options": {
            "A": "Interpretam-se estritamente, sendo vedada a extensão analógica ou ampliativa que crie obrigações ou renúncias não declaradas de forma expressa.",
            "B": "Interpretam-se de forma analógica e extensiva, aplicando-se as mesmas regras dos contratos bilaterais onerosos.",
            "C": "Presume-se a renúncia de direitos patrimoniais sempre que o credor tolerar atraso superior a trinta dias.",
            "D": "São nulos se não contiverem cláusula expressa de arbitragem."
        },
        "gabarito": "A",
        "article": "Art. 114 do Código Civil",
        "legal_basis": "Art. 114 do Código Civil.",
        "explanation": "Art. 114 do CC: 'Os negócios jurídicos benéficos e a renúncia interpretam-se estritamente'. Não se presume doação ou renúncia além do que foi expressa e restritivamente delimitado pelo disponente."
    },

    # 5. CLASSIFICAÇÃO DOS CONTRATOS
    {
        "subject": "Classificação dos Contratos",
        "bank": "VUNESP",
        "difficulty": "Médio",
        "enunciado": "(VUNESP / Magistratura) O contrato de mútuo feneratício (empréstimo de dinheiro com juros) classifica-se tecnicamente como contrato:",
        "options": {
            "A": "Unilateral, oneroso e real.",
            "B": "Bilateral, gratuito e consensual.",
            "C": "Unilateral, gratuito e solene por escritura pública.",
            "D": "Bilateral perfeito, puramente comutativo e solene."
        },
        "gabarito": "A",
        "article": "Arts. 586 a 591 do Código Civil",
        "legal_basis": "Arts. 586 e 591 do Código Civil e Doutrina Contratual.",
        "explanation": "O mútuo é contrato real (só se aperfeiçoa com a efetiva entrega do dinheiro) e unilateral (após a tradição, apenas o mutuário tem obrigação de restituir). Quando prevê juros (feneratício), é também oneroso."
    },
    {
        "subject": "Classificação dos Contratos",
        "bank": "OAB",
        "difficulty": "Fácil",
        "enunciado": "(OAB / FGV) A compra e venda pura de bens móveis com pagamento parcelado é exemplo clássico de contrato:",
        "options": {
            "A": "Bilateral (sinalagmático), oneroso, comutativo e consensual.",
            "B": "Unilateral, gratuito, solene e real.",
            "C": "Aleatório, benéfico, atípico e real.",
            "D": "Bilateral imperfeito, solene por escritura pública e de execução imediata."
        },
        "gabarito": "A",
        "article": "Art. 481 e Art. 482 do Código Civil",
        "legal_basis": "Arts. 481 e 482 do Código Civil.",
        "explanation": "A compra e venda é bilateral (gera obrigações para ambos), onerosa (sacrifício patrimonial recíproco), comutativa (prestações certas e conhecidas) e consensual (aperfeiçoa-se com o simples acordo sobre coisa e preço)."
    },

    # 6. ETAPAS DE FORMAÇÃO DO CONTRATO
    {
        "subject": "Etapas de Formação do Contrato",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) Sobre as etapas de formação do contrato civil (negociações preliminares/punctuação, proposta e aceitação), assinale a afirmativa correta.",
        "options": {
            "A": "A fase de negociações preliminares (punctuação) não gera em nenhuma hipótese dever de indenizar, dada a ampla liberdade contratual.",
            "B": "A proposta séria e precisa vincula o proponente, salvo se o contrário resultar dos termos dela, da natureza do negócio ou das circunstâncias do caso.",
            "C": "A aceitação com modificações ou adições importa conclusão imediata do contrato originário.",
            "D": "Entre ausentes, o contrato só se conclui quando a aceitação é lida pessoalmente pelo proponente."
        },
        "gabarito": "B",
        "article": "Art. 427 e Art. 431 do Código Civil",
        "legal_basis": "Arts. 427, 428, 431 e 434 do Código Civil.",
        "explanation": "A proposta vincula o proponente (art. 427). As negociações preliminares podem gerar dever de indenizar por responsabilidade pré-contratual se violada a boa-fé. A aceitação com adições é nova proposta (art. 431)."
    },
    {
        "subject": "Etapas de Formação do Contrato",
        "bank": "CESPE",
        "difficulty": "Médio",
        "enunciado": "(CESPE / Doutrina) No que diz respeito ao momento da conclusão do contrato entre pessoas ausentes, o Código Civil brasileiro adotou expressamente a Teoria:",
        "options": {
            "A": "Da Agnição, na subespécie da Expedição (art. 434 do CC).",
            "B": "Da Recepção pura, exigindo que o proponente receba a aceitação em seu domicílio.",
            "C": "Da Cognição ou Informação, exigindo que o proponente tome ciência do teor da aceitação.",
            "D": "Da Declaração propriamente dita, bastando a redação da resposta na minuta."
        },
        "gabarito": "A",
        "article": "Art. 434 do Código Civil",
        "legal_basis": "Art. 434 do Código Civil.",
        "explanation": "O Código Civil consagra a Teoria da Expedição: 'Os contratos entre ausentes tornam-se perfeitos desde que a aceitação é expedida' (art. 434), admitindo retratação antes ou concomitante à chegada."
    },

    # 7. ESTIPULAÇÃO EM FAVOR DE TERCEIRO
    {
        "subject": "Estipulação em Favor de Terceiro",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) Na Estipulação em Favor de Terceiro (arts. 436 a 438 do CC), caso o estipulante tenha reservado ao terceiro o direito de reclamar a execução da obrigação:",
        "options": {
            "A": "O estipulante perde a faculdade de exonerar o devedor unilateralmente.",
            "B": "O promitente fica desonerado de prestar qualquer esclarecimento ao terceiro.",
            "C": "O terceiro assume a posição de devedor solidário de todos os custos do negócio.",
            "D": "O estipulante não mais poderá substituir o terceiro sob nenhuma hipótese."
        },
        "gabarito": "A",
        "article": "Art. 437 do Código Civil",
        "legal_basis": "Art. 437 do Código Civil.",
        "explanation": "Art. 437, CC: 'Se ao terceiro, em favor de quem se fez a estipulação, se deixar o direito de reclamar-lhe a execução, não poderá o estipulante exonerar o devedor'."
    },
    {
        "subject": "Estipulação em Favor de Terceiro",
        "bank": "VUNESP",
        "difficulty": "Médio",
        "enunciado": "(VUNESP / Notário) O estipulante pode substituir o terceiro beneficiário designado no contrato?",
        "options": {
            "A": "Sim, pode reservar-se o direito de substituir o terceiro por ato entre vivos ou por disposição de última vontade (testamento), independentemente da anuência do terceiro e do promitente.",
            "B": "Não, a indicação do terceiro é irrevogável após a assinatura do contrato pelas partes originárias.",
            "C": "Apenas com autorização judicial prévia ou consentimento expresso do promitente.",
            "D": "Somente se o terceiro cometer ato de ingratidão previsto nas regras de doação."
        },
        "gabarito": "A",
        "article": "Art. 438 do Código Civil",
        "legal_basis": "Art. 438 e parágrafo único do Código Civil.",
        "explanation": "Art. 438, CC: 'O estipulante pode reservar-se o direito de substituir o terceiro designado no contrato, independentemente da sua anuência e da do outro contratante'."
    },

    # 8. PROMESSA DE FATO DE TERCEIRO
    {
        "subject": "Promessa de Fato de Terceiro",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) Mário prometeu a José que sua irmã Clara, arquiteta premiada, elaboraria gratuitamente o projeto de reforma da casa de José. Todavia, Clara recusou-se veementemente a prestar o serviço, afirmando nada ter contratado com José. À luz do art. 439 do Código Civil:",
        "options": {
            "A": "José pode ajuizar ação de obrigação de fazer contra Clara para compeli-la ao trabalho.",
            "B": "Mário responderá por perdas e danos perante José, em razão da inexecução da obrigação prometida.",
            "C": "Clara e Mário respondem solidariamente por perdas e danos perante José.",
            "D": "O contrato é nulo por ilicitude do objeto, restando as partes desobrigadas."
        },
        "gabarito": "B",
        "article": "Art. 439 do Código Civil",
        "legal_basis": "Art. 439 do Código Civil.",
        "explanation": "Art. 439 do CC: 'Aquele que tiver prometido fato de terceiro responderá por perdas e danos, quando este o não executar'. O terceiro estranho à avença não tem responsabilidade civil."
    },
    {
        "subject": "Promessa de Fato de Terceiro",
        "bank": "FCC",
        "difficulty": "Médio",
        "enunciado": "(FCC / Analista) Quando cessa a responsabilidade daquele que prometeu fato de terceiro, conforme as disposições do Código Civil?",
        "options": {
            "A": "Quando o terceiro se comprometer perante o credor a executar a obrigação, assumindo-a (Art. 440 do CC).",
            "B": "Apenas quando o terceiro concluir integralmente a prestação do fato.",
            "C": "No prazo decadencial de 30 dias contados da celebração da promessa.",
            "D": "Nunca cessa, permanecendo como fiador legal perpétuo do terceiro."
        },
        "gabarito": "A",
        "article": "Art. 440 do Código Civil",
        "legal_basis": "Art. 440 do Código Civil.",
        "explanation": "Art. 440 do CC: 'Nenhuma obrigação haverá para quem se comprometer por outrem, se este, depois de se ter obrigado, faltar à prestação'. Uma vez assumida a obrigação pelo terceiro perante o credor, o promitente fica exonerado."
    },

    # 9. CONTRATOS ALEATÓRIOS - CONCEITO E ESPÉCIES
    {
        "subject": "Contratos Aleatórios - Conceito e Espécies",
        "bank": "CESPE",
        "difficulty": "Médio",
        "enunciado": "(CESPE / Juiz) A respeito da teoria geral dos contratos aleatórios no Código Civil, assinale a opção correta.",
        "options": {
            "A": "Diferenciam-se dos contratos comutativos porque neles a prestação de uma das partes fica subordinada a uma álea (risco de perda ou ganho futuro).",
            "B": "São sempre vedados pelo ordenamento civil quando envolverem produtos agrícolas ou safras futuras.",
            "C": "Permitem que qualquer das partes rescinda imotivadamente o contrato sem pagar o preço acordado caso o evento incerto se concretize.",
            "D": "Classificam-se unicamente como contratos gratuitos e reais."
        },
        "gabarito": "A",
        "article": "Arts. 458 a 461 do Código Civil",
        "legal_basis": "Arts. 458 a 461 do Código Civil e Doutrina Contratual.",
        "explanation": "Nos contratos aleatórios, a incerteza futura (álea) faz parte da causa do contrato, assumindo uma das partes o risco de receber prestação desproporcional ou mesmo nada receber, pagando o preço ajustado."
    },

    # 10. CONTRATO ALEATÓRIO: EMPTIO SPEI
    {
        "subject": "Contrato Aleatório: Emptio Spei",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) Rodrigo comprou de um pescador profissional, pelo valor fechado de R$ 800,00 pago no ato, todo o produto que viesse a ser pescado no próximo lançamento de rede no mar. Ficou ajustado expressamente que Rodrigo assumiria o risco de nada vir a ser capturado (venda da esperança). O pescador lançou a rede adequadamente, mas nenhum peixe foi apanhado. Diante do Art. 458 do Código Civil:",
        "options": {
            "A": "O pescador tem direito de reter o valor integral recebido, desde que de sua parte não tenha havido dolo ou culpa, ainda que nada venha a existir.",
            "B": "O pescador é obrigado a restituir o valor pago, sob pena de enriquecimento sem causa.",
            "C": "O contrato é nulo por ausência de objeto no plano da existência.",
            "D": "O pescador deve lançar a rede até que capture quantidade proporcional aos R$ 800,00 pagos."
        },
        "gabarito": "A",
        "article": "Art. 458 do Código Civil",
        "legal_basis": "Art. 458 do Código Civil.",
        "explanation": "Art. 458 (Emptio Spei): O risco assumido pelo adquirente diz respeito à própria existência da coisa. O alienante tem direito a todo o preço desde que não tenha agido com dolo ou culpa, ainda que nada venha a existir."
    },

    # 11. CONTRATO ALEATÓRIO: EMPTIO REI SPERATAE
    {
        "subject": "Contrato Aleatório: Emptio Rei Speratae",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) Mariana adquiriu do produtor rural Paulo toda a safra futura de tomates de sua fazenda por R$ 30.000,00, ajustando que assumiria o risco sobre a quantidade que viesse a ser colhida (emptio rei speratae). Todavia, por motivos climáticos imprevisíveis e sem culpa de Paulo, a lavoura foi completamente dizimada, não tendo sido colhido um único tomate (quantidade zero). À luz do parágrafo único do Art. 459 do Código Civil:",
        "options": {
            "A": "Alienação não haverá, e o alienante Paulo restituirá integralmente o preço recebido de Mariana.",
            "B": "Mariana deve pagar o valor integral de R$ 30.000,00 tendo em vista a álea contratual assumida.",
            "C": "Paulo deve indenizar Mariana em perdas e danos equivalentes ao lucro que ela obteria no mercado.",
            "D": "O contrato converte-se automaticamente em comodato remunerado."
        },
        "gabarito": "A",
        "article": "Art. 459, parágrafo único do Código Civil",
        "legal_basis": "Art. 459, parágrafo único do Código Civil.",
        "explanation": "Na Emptio Rei Speratae (art. 459), o adquirente assume o risco da quantidade, mas NÃO da existência. 'Se da coisa nada vier a existir, alienação não haverá, e o alienante restituirá o preço recebido'."
    },

    # 12. CONTRATO ALEATÓRIO: COISAS EXISTENTES EXPOSTAS A RISCO
    {
        "subject": "Contrato Aleatório: Coisas Existentes Expostas a Risco",
        "bank": "VUNESP",
        "difficulty": "Difícil",
        "enunciado": "(VUNESP / Magistratura) Nos contratos aleatórios que têm por objeto coisas existentes mas expostas a risco (art. 460 do CC), o alienante terá direito a todo o preço mesmo que a coisa já não existisse no dia do contrato, DESDE QUE:",
        "options": {
            "A": "O alienante estivesse de boa-fé, desconhecendo a consumação do sinistro na data da celebração.",
            "B": "O adquirente renuncie expressamente à garantia de evicção perante tabelião de notas.",
            "C": "O contrato seja firmado exclusivamente por instrumento público registrado em cartório.",
            "D": "A perda da coisa tenha ocorrido por fato do príncipe."
        },
        "gabarito": "A",
        "article": "Art. 460 e Art. 461 do Código Civil",
        "legal_basis": "Arts. 460 e 461 do Código Civil.",
        "explanation": "Art. 461: A alienação aleatória a risco pode ser anulada pelo adquirente se ele provar que o alienante não ignorava a consumação do risco (ou seja, sabia que a coisa já havia perecido e agiu de má-fé)."
    },

    # 13. CONTRATO PRELIMINAR / PROMESSA DE CONTRATAR
    {
        "subject": "Contrato Preliminar / Promessa de Contratar",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) Acerca do contrato preliminar no Código Civil (arts. 462 a 466), assinale a afirmativa correta.",
        "options": {
            "A": "O contrato preliminar deve conter todos os requisitos essenciais ao contrato a ser celebrado, exceto quanto à forma.",
            "B": "O contrato preliminar de compra e venda de imóvel de alto valor exige necessariamente a forma de escritura pública sob pena de nulidade absoluta.",
            "C": "O descumprimento do contrato preliminar gera unicamente direito a perdas e danos, sendo vedada a adjudicação compulsória.",
            "D": "A validade do contrato preliminar depende de registro imobiliário prévio."
        },
        "gabarito": "A",
        "article": "Art. 462 do Código Civil",
        "legal_basis": "Art. 462 do Código Civil.",
        "explanation": "Art. 462 do CC: 'O contrato preliminar, exceto quanto à forma, deve conter todos os requisitos essenciais ao contrato a ser celebrado'. Consagra o princípio da atração mitigada."
    },
    {
        "subject": "Contrato Preliminar / Promessa de Contratar",
        "bank": "FCC",
        "difficulty": "Médio",
        "enunciado": "(FCC / PGE) Concluído o contrato preliminar sem cláusula de arrependimento, se uma das partes se recusar a celebrar o contrato definitivo, a outra parte poderá:",
        "options": {
            "A": "Requerer ao juiz que supra a manifestação de vontade, conferindo à sentença o caráter definitivo do contrato prometido (Art. 464 do CC).",
            "B": "Apenas pleitear rescisão com retenção de arras, sem possibilidade de tutela específica.",
            "C": "Promover a prisão civil do promitente inadimplente por crime de desobediência contratual.",
            "D": "Exigir a conversão forçada do contrato em doação onerosa."
        },
        "gabarito": "A",
        "article": "Art. 464 do Código Civil",
        "legal_basis": "Art. 464 do Código Civil.",
        "explanation": "Art. 464 do CC: 'Esgotado o prazo, poderá o contraente exigir a celebração do definitivo, conferindo o juiz, a pedido da parte, caráter definitivo ao contrato, sendo isso possível pela sua natureza'."
    },

    # 14. CONTRATO COM PESSOA A DECLARAR
    {
        "subject": "Contrato com Pessoa a Declarar",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) No momento da celebração de compra e venda de um imóvel, o comprador reservou-se a faculdade de indicar a pessoa que deve adquirir os direitos e assumir as obrigações dele decorrentes (contrato com pessoa a declarar). O prazo legal para comunicar a indicação (electio amici) à outra parte, se outro não tiver sido estipulado pelos contraentes, é de:",
        "options": {
            "A": "Cinco dias da conclusão do contrato.",
            "B": "Quinze dias da imissão na posse.",
            "C": "Trinta dias da assinatura da escritura.",
            "D": "Seis meses da tradição efetiva."
        },
        "gabarito": "A",
        "article": "Art. 468 do Código Civil",
        "legal_basis": "Art. 468, caput do Código Civil.",
        "explanation": "Art. 468 do CC: 'Essa indicação deve ser comunicada à outra parte no prazo de cinco dias da conclusão do contrato, se outro não tiver sido estipulado pelos contraentes'."
    },

    # 15. CONTRATO COM PESSOA A DECLARAR VS. OUTROS CONTRATOS
    {
        "subject": "Contrato com Pessoa a Declarar vs. Outros Contratos",
        "bank": "CESPE",
        "difficulty": "Difícil",
        "enunciado": "(CESPE / Procuradoria) A respeito da distinção do Contrato com Pessoa a Declarar frente a outras figuras contratuais, assinale a opção correta.",
        "options": {
            "A": "Distingue-se do mandato porque a parte age em nome próprio e, caso a pessoa indicada não aceite a nomeação ou seja insolvente, o contrato produzirá efeitos unicamente entre os contraentes originários.",
            "B": "Equipara-se plenamente à estipulação em favor de terceiro, pois o terceiro nunca assume obrigações pecuniárias.",
            "C": "Configura hipótese de representação direta necessária, exonerando o estipulante originário em qualquer circunstância.",
            "D": "Produz efeitos unicamente ex nunc a partir da declaração da pessoa indicada."
        },
        "gabarito": "A",
        "article": "Art. 469 e Art. 470 do Código Civil",
        "legal_basis": "Arts. 467, 469 e 470 do Código Civil.",
        "explanation": "No contrato com pessoa a declarar, a parte contrata em seu próprio nome. Se a nomeação falhar, for recusada ou recair sobre incapaz/insolvente, o contrato produz seus efeitos originários entre os signatários (art. 470). Além disso, a nomeação válida opera efeitos retroativos ex tunc (art. 469)."
    },

    # 16. VÍCIOS REDIBITÓRIOS - CONCEITO E REQUISITOS
    {
        "subject": "Vícios Redibitórios - Conceito e Requisitos",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) A respeito dos vícios redibitórios disciplinados no Código Civil (arts. 441 a 446), assinale a afirmativa correta.",
        "options": {
            "A": "Aplicam-se aos contratos comutativos onerosos e também às doações onerosas (com encargo).",
            "B": "Configuram-se mesmo diante de defeitos ostensivos e de fácil constatação prévia pelo adquirente.",
            "C": "Podem ser invocados nas doações puras e universais sem qualquer encargo pecuniário.",
            "D": "A responsabilidade por vício redibitório depende sempre da comprovação de culpa ou má-fé do alienante."
        },
        "gabarito": "A",
        "article": "Art. 441 do Código Civil",
        "legal_basis": "Art. 441 e seu parágrafo único do Código Civil.",
        "explanation": "Art. 441: A coisa recebida em contrato comutativo pode ser enjeitada por defeitos ocultos. Parágrafo único: 'É aplicável a disposição deste artigo às doações onerosas'. Nas doações puras não se responde por vício redibitório."
    },

    # 17. EFEITOS DA BOA-FÉ E MÁ-FÉ DO ALIENANTE NO VÍCIO
    {
        "subject": "Efeitos da Boa-fé e Má-fé do Alienante no Vício",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) Pedro vendeu a Lucas um veículo seminovo que possuía grave defeito no bloco do motor, oculto e preexistente. Comprovou-se em juízo que Pedro tinha plena ciência do vício e o ocultou de Lucas. Consoante o Art. 443 do Código Civil, qual a consequência da má-fé do alienante?",
        "options": {
            "A": "Restituirá o que recebeu com perdas e danos.",
            "B": "Restituirá apenas o valor recebido e as despesas do contrato, ficando isento de perdas e danos.",
            "C": "Ficará isento de qualquer obrigação civil se o comprador tiver feito test drive.",
            "D": "O contrato será convalidado mediante pagamento de multa civil de 2% ao Estado."
        },
        "gabarito": "A",
        "article": "Art. 443 do Código Civil",
        "legal_basis": "Art. 443 do Código Civil.",
        "explanation": "Art. 443 do CC: 'Se o alienante conhecia o vício ou defeito da coisa, restituirá o que recebeu com perdas e danos; se o não conhecia, tão-somente restituirá o valor recebido, mais as despesas do contrato'."
    },
    {
        "subject": "Efeitos da Boa-fé e Má-fé do Alienante no Vício",
        "bank": "FCC",
        "difficulty": "Médio",
        "enunciado": "(FCC / Magistratura) O alienante que desconhecia o vício oculto da coisa na data da venda (alienante de boa-fé):",
        "options": {
            "A": "Continua responsável pela garantia legal, devendo restituir o valor recebido mais as despesas do contrato, mas fica isento de pagar perdas e danos.",
            "B": "Fica totalmente desonerado da obrigação de restituir o preço recebido.",
            "C": "Responde por lucros cessantes presumidos fixados pelo juiz.",
            "D": "Pode exigir que o adquirente arque com 50% dos custos do conserto."
        },
        "gabarito": "A",
        "article": "Art. 443 do Código Civil",
        "legal_basis": "Art. 443, 2ª parte do Código Civil.",
        "explanation": "A garantia do vício redibitório é objetiva: mesmo quem ignorava o defeito deve aceitar o desfazimento do negócio ou o abatimento do preço e pagar despesas contratuais; a boa-fé apenas o exonera de perdas e danos."
    },

    # 18. AÇÕES EDILÍCIAS (REDIBITÓRIA E ESTIMATÓRIA/QUANTI MINORIS)
    {
        "subject": "Ações Edilícias (Redibitória e Estimatória/Quanti Minoris)",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) Constatado o vício redibitório em negócio de compra e venda civil, o adquirente dispõe das denominadas ações edilícias. A esse respeito, assinale a opção correta.",
        "options": {
            "A": "O adquirente tem o direito potestativo de optar entre enjeitar a coisa, redibindo o contrato (ação redibitória), ou pleitear abatimento proporcional do preço (ação estimatória ou quanti minoris).",
            "B": "O vendedor é quem possui a prerrogativa exclusiva de escolher se devolve o dinheiro ou concede abatimento no preço.",
            "C": "O comprador pode cumular no mesmo processo o pedido de rescisão contratual com devolução do bem e o abatimento de 50% do valor.",
            "D": "A ação redibitória prescreve em 10 anos pelo prazo geral de responsabilidade civil."
        },
        "gabarito": "A",
        "article": "Art. 442 do Código Civil",
        "legal_basis": "Arts. 441 e 442 do Código Civil.",
        "explanation": "As ações edilícias são disjuntivas/alternativas. O adquirente tem a opção potestativa: rejeitar a coisa rescidindo o contrato (ação redibitória) ou ficar com ela pedindo abatimento no preço (ação estimatória/quanti minoris)."
    },

    # 19. VÍCIO REDIBITÓRIO VS. ENTREGA DE COISA DIVERSA (ALIUD PRO ALIO)
    {
        "subject": "Vício Redibitório vs. Entrega de Coisa Diversa (Aliud Pro Alio)",
        "bank": "CESPE",
        "difficulty": "Difícil",
        "enunciado": "(CESPE / Magistratura) A entrega de coisa diversa da contratada (aliud pro alio), como a entrega de um trator agrícola quando o pactuado foi uma colheitadeira de grãos:",
        "options": {
            "A": "Não constitui vício redibitório, mas sim inadimplemento absoluto da obrigação de dar, subordinando-se às regras do inadimplemento e aos prazos prescricionais gerais.",
            "B": "Constitui modalidade de vício redibitório extrínseco, submetida ao prazo decadencial de trinta dias do art. 445 do CC.",
            "C": "Equipara-se à evicção parcial presumida por lei civil.",
            "D": "Importa em novação objetiva tácita irrevogável."
        },
        "gabarito": "A",
        "article": "Arts. 389 e 441 do Código Civil",
        "legal_basis": "Arts. 389, 441 e 475 do Código Civil e Doutrina Contratual.",
        "explanation": "Entregar coisa diversa da contratada (aliud pro alio) é descumprimento total da prestação (inadimplemento absoluto da obrigação de dar). Vício redibitório pressupõe que a coisa entregue é a mesma contratada, porém afetada por defeito oculto funcional."
    },

    # 20. PRAZOS DECADENCIAIS DOS VÍCIOS REDIBITÓRIOS
    {
        "subject": "Prazos Decadenciais dos Vícios Redibitórios",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) No tocante aos prazos decadenciais para obter a redibição ou abatimento no preço em contratos regulados pelo Código Civil (art. 445), assinale a opção correta.",
        "options": {
            "A": "O prazo é de trinta dias se a coisa for móvel, e de um ano se for imóvel, contado da entrega efetiva; se o adquirente já estava na posse da coisa, o prazo conta-se da alienação, reduzido à metade.",
            "B": "O prazo é prescricional de noventa dias para móveis e cinco anos para imóveis, equiparando-se ao Código de Defesa do Consumidor.",
            "C": "Quando o vício só puder ser conhecido mais tarde, o prazo para móveis passa a ser decadencial de três anos.",
            "D": "O prazo decadencial não flui contra pessoas absolutamente incapazes nos negócios civis imobiliários."
        },
        "gabarito": "A",
        "article": "Art. 445 do Código Civil",
        "legal_basis": "Art. 445, caput e § 1º do Código Civil.",
        "explanation": "Art. 445, CC: Prazos de decadência: 30 dias (móveis) e 1 ano (imóveis), da entrega efetiva. Já estando na posse, conta da alienação pela metade (15 dias móvel, 6 meses imóvel)."
    },

    # 21. EXTINÇÃO DOS CONTRATOS - RESOLUÇÃO E CLÁUSULA RESOLUTIVA
    {
        "subject": "Extinção dos Contratos - Resolução e Cláusula Resolutiva",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) A respeito das formas de extinção do contrato e da disciplina da cláusula resolutiva no Código Civil (arts. 474 e 475), é correto afirmar:",
        "options": {
            "A": "A cláusula resolutiva expressa opera de pleno direito; a tácita depende de interpelação judicial.",
            "B": "A cláusula resolutiva expressa é nula de pleno direito por afastar a intervenção jurisdicional.",
            "C": "A cláusula resolutiva tácita opera automaticamente, independentemente de interpelação do devedor.",
            "D": "A parte lesada pelo inadimplemento só pode pedir perdas e danos se não pleitear a resolução do negócio."
        },
        "gabarito": "A",
        "article": "Art. 474 do Código Civil",
        "legal_basis": "Art. 474 e Art. 475 do Código Civil.",
        "explanation": "Art. 474, CC: 'A cláusula resolutiva expressa opera de pleno direito; a tácita depende de interpelação judicial'. Art. 475: A parte lesada pode pedir a resolução ou exigir o cumprimento, cabendo indenização em qualquer caso."
    },

    # 22. EXCEÇÃO DO CONTRATO NÃO CUMPRIDO E ONEROSIDADE EXCESSIVA
    {
        "subject": "Exceção do Contrato Não Cumprido e Onerosidade Excessiva",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB / FGV) Em contrato de compra e venda mercantil com obrigações recíprocas e simultâneas, o vendedor deixou de entregar os produtos pactuados e, ato contínuo, ajuizou ação cobrando o preço do comprador. Em contestação, o comprador alegou a exceção do contrato não cumprido. Nos termos do Art. 476 do Código Civil:",
        "options": {
            "A": "A alegação do comprador é legítima, pois nos contratos bilaterais nenhum dos contratantes, antes de cumprida a sua obrigação, pode exigir o implemento da do outro.",
            "B": "A exceção do contrato não cumprido só pode ser veiculada por meio de reconvenção autônoma.",
            "C": "O comprador deve efetuar o depósito judicial do valor integral da dívida antes de suscitar a exceção substancial.",
            "D": "A exceptio non adimpleti contractus é privativa dos contratos de adesão celebrados com consumidores."
        },
        "gabarito": "A",
        "article": "Art. 476 do Código Civil",
        "legal_basis": "Art. 476 do Código Civil.",
        "explanation": "Art. 476 do CC: 'Nos contratos bilaterais, nenhum dos contratantes, antes de cumprida a sua obrigação, pode exigir o implemento da do outro'. É a clássica exceptio non adimpleti contractus."
    }
]

# Adiciona UUID único para cada questão
for q in QUESTIONS:
    if "id" not in q:
        q["id"] = str(uuid.uuid4())

data = {"questions": QUESTIONS}

with open("database/seed_questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Sucesso! Geradas {len(QUESTIONS)} questões seminais completas para os 22 temas do questionário de Contratos.")
