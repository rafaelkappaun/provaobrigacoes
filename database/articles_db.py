from typing import List, Dict, Any

# Banco de dados de artigos comentados para a Prova de Contratos (Código Civil)
# Contempla a Escada Ponteana (Planos do Negócio Jurídico), Interpretação, Teoria Geral e Espécies de Contratos
ARTICLES_DATA: List[Dict[str, Any]] = [
    {
        "id": "art_104",
        "number": 104,
        "subject": "Planos do Negócio Jurídico (Escada Ponteana)",
        "text": "Art. 104. A validade do negócio jurídico requer: I - agente capaz; II - objeto lícito, possível, determinado ou determinável; III - forma prescrita ou não defesa em lei.",
        "summary": "Plano da Validade na Escada Ponteana. Para que o negócio existente produza efeitos válidos, exige capacidade do agente, licitude/possibilidade do objeto e observância da forma legal.",
        "tips": "A Escada Ponteana divide o negócio em: 1) Existência (manifestação de vontade, partes, objeto e forma); 2) Validade (adjetivação: capacidade, licitude do objeto e forma prescrita); 3) Eficácia (condição, termo e encargo).",
        "common_errors": "Confundir plano da existência com o da validade. Um contrato celebrado por incapaz existe, porém é nulo ou anulável (plano da validade)."
    },
    {
        "id": "art_112",
        "number": 112,
        "subject": "Interpretação dos Contratos no Direito Brasileiro",
        "text": "Art. 112. Nas declarações de vontade se atenderá mais à intenção nelas consubstanciada do que ao sentido literal da linguagem.",
        "summary": "Princípio da prevalência da vontade real sobre a vontade declarada (teoria subjetiva mitigada). A literalidade cede à verdadeira intenção comum dos contraentes.",
        "tips": "O juiz ou intérprete não pode ficar preso à frieza gramatical das palavras quando o comportamento e intenção das partes evidenciarem outro propósito prático.",
        "common_errors": "Achar que a interpretação gramatical/literal é soberana e inflexível no Direito Civil brasileiro."
    },
    {
        "id": "art_113",
        "number": 113,
        "subject": "Interpretação dos Contratos no Direito Brasileiro",
        "text": "Art. 113. Os negócios jurídicos devem ser interpretados conforme a boa-fé e os usos do lugar de sua celebração. § 1º A interpretação do negócio jurídico deve lhe atribuir o sentido que: I - for confirmado pelo comportamento das partes posterior à celebração; II - corresponder aos usos, costumes e práticas do mercado; III - corresponder à boa-fé; IV - for mais benéfico à parte que não redigiu o dispositivo; V - corresponder a qual seria a razoável negociação das partes sobre a questão.",
        "summary": "Regra áurea de interpretação: boa-fé objetiva, usos e costumes, comportamento posterior e redação contra stipulatorem.",
        "tips": "O § 1º foi incluído pela Lei da Liberdade Econômica (Lei 13.874/2019) e é cobradíssimo em provas recentes por detalhar a hermenêutica contratual.",
        "common_errors": "Esquecer que o comportamento das partes após a assinatura do contrato serve de baliza interpretativa para o juiz."
    },
    {
        "id": "art_114",
        "number": 114,
        "subject": "Interpretação dos Contratos no Direito Brasileiro",
        "text": "Art. 114. Os negócios jurídicos benéficos e a renúncia interpretam-se estritamente.",
        "summary": "Contratos gratuitos/benéficos (como doação e comodato) e atos de renúncia não admitem interpretação extensiva ou ampliativa.",
        "tips": "Como o contratante benemérito transfere patrimônio sem contraprestação, sua liberalidade deve ser interpretada de modo restritivo para protegê-lo.",
        "common_errors": "Achar que se pode presumir renúncia tácita de direitos além do que foi expressa e restritivamente declarado."
    },
    {
        "id": "art_421",
        "number": 421,
        "subject": "Princípios do Direito Contratual",
        "text": "Art. 421. A liberdade contratual será exercida nos limites da função social do contrato. Parágrafo único. Nas relações contratuais privadas, prevalecerão o princípio da intervenção mínima e a excepcionalidade da revisão contratual.",
        "summary": "A liberdade de contratar é balizada pela função social (eficácia interna e externa). A intervenção estatal do Judiciário deve ser mínima e excepcional.",
        "tips": "A função social protege direitos difusos e de terceiros que possam ser atingidos pelo contrato (eficácia externa da função social) e veda cláusulas abusivas que desnaturem a comutatividade.",
        "common_errors": "Pensar que o princípio da função social extinguiu o pacta sunt servanda (força obrigatória); na verdade, ele o redimensiona sob a ótica constitucional."
    },
    {
        "id": "art_421_a",
        "number": 421,
        "subject": "Princípios do Direito Contratual",
        "text": "Art. 421-A. Os contratos civis e empresariais presumem-se paritários e simétricos até a presença de elementos concretos que justifiquem o afastamento dessa presunção, ressalvados os regimes jurídicos previstos em leis especiais, garantido também que: I - as partes negociantes poderão estabelecer parâmetros objetivos para a interpretação das cláusulas negociais e de seus pressupostos de revisão ou de resolução; II - a alocação de riscos definida pelas partes deve ser respeitada e observada; III - a revisão contratual somente ocorrerá de maneira excepcional e limitada.",
        "summary": "Presunção de paridade e simetria nos contratos civis e empresariais, prestigiando a autonomia da vontade e a alocação privada de riscos.",
        "tips": "Diferencia o contrato civil/empresarial do contrato de consumo ou de trabalho, onde a vulnerabilidade de uma das partes é presumida por lei.",
        "common_errors": "Aplicar presunção automática de vulnerabilidade entre dois empresários ou contratantes civis plenamente esclarecidos."
    },
    {
        "id": "art_422",
        "number": 422,
        "subject": "Boa-fé Objetiva e Figuras Parcelares",
        "text": "Art. 422. Os contratantes são obrigados a guardar, assim na conclusão do contrato, como em sua execução, os princípios de probidade e boa-fé.",
        "summary": "Cláusula geral da boa-fé objetiva (deveres anexos de conduta: lealdade, informação, cooperação e sigilo) nas fases pré-contratual, de execução e pós-contratual.",
        "tips": "Da boa-fé objetiva decorrem os conceitos parcelares fundamentais: Venire contra factum proprium (proibição de comportamento contraditório), Supressio (perda do direito pelo não exercício), Surrectio (surgimento de direito pela prática reiterada) e Tu quoque (vedação de exigir o que você mesmo descumpriu).",
        "common_errors": "Confundir boa-fé objetiva (regra ética de conduta leal) com boa-fé subjetiva (estado psicológico de ignorância do vício)."
    },
    {
        "id": "art_423",
        "number": 423,
        "subject": "Classificação dos Contratos",
        "text": "Art. 423. Quando houver no contrato de adesão cláusulas ambíguas ou contraditórias, dever-se-á adotar a interpretação mais favorável ao aderente.",
        "summary": "Regra 'contra stipulatorem' nos contratos de adesão. A ambiguidade na redação beneficia quem aderiu e não teve poder de negociar as cláusulas.",
        "tips": "Contrato de adesão opõe-se ao contrato paritário. Como o estipulante redige unilateralmente, arca com o risco da má redação de suas cláusulas.",
        "common_errors": "Acreditar que a interpretação favorável ao aderente só se aplica no Código de Defesa do Consumidor; o Código Civil a consagra expressamente no art. 423."
    },
    {
        "id": "art_427",
        "number": 427,
        "subject": "Etapas de Formação do Contrato",
        "text": "Art. 427. A proposta de contrato obriga o proponente, se o contrário não resultar dos termos dela, da natureza do negócio, ou das circunstâncias do caso.",
        "summary": "Força vinculante da proposta (policitação). Uma vez emitida de forma séria e precisa, gera dever jurídico para quem a propôs.",
        "tips": "Etapas de formação do contrato: 1) Punctuação (negociações preliminares - não vinculam diretamente, mas exigem boa-fé pré-contratual); 2) Proposta/Policitação (oferta formal que vincula o policitante); 3) Aceitação/Oblação (concordância pura e simples do oblato que conclui o contrato).",
        "common_errors": "Achar que as negociações preliminares já vinculam a celebração do contrato final. Elas vinculam apenas deveres de lealdade e indenização se houver ruptura desleal injustificada."
    },
    {
        "id": "art_428",
        "number": 428,
        "subject": "Etapas de Formação do Contrato",
        "text": "Art. 428. Deixa de ser obrigatória a proposta: I - se, feita sem prazo a pessoa presente, não foi imediatamente aceita; II - se, feita sem prazo a pessoa ausente, tiver decorrido tempo suficiente para chegar a resposta; III - se, feita a pessoa ausente com prazo, a resposta não for expedida dentro dele; IV - se, antes dela, ou simultaneamente, chegar ao conhecimento da outra parte a retratação do proponente.",
        "summary": "Hipóteses legais taxativas em que a proposta perde sua eficácia vinculante entre presentes e ausentes.",
        "tips": "Considera-se presente quem contrata por telefone ou meio de comunicação instantânea em tempo real (ex: WhatsApp/chat com resposta imediata).",
        "common_errors": "Achar que a proposta enviada com prazo para resposta pode ser revogada a qualquer momento; enquanto o prazo não expirar, ela é vinculante, salvo retratação anterior ou simultânea."
    },
    {
        "id": "art_436",
        "number": 436,
        "subject": "Estipulação em Favor de Terceiro",
        "text": "Art. 436. O que estipula em favor de terceiro pode exigir o cumprimento da obrigação. Parágrafo único. Ao terceiro, em favor de quem se estipulou a obrigação, também é permitido exigi-la, ficando, todavia, sujeito às condições e normas do contrato, se a ele anuir, e o estipulante o não houver exonerado.",
        "summary": "Na estipulação em favor de terceiro, o estipulante contrata com o promitente para que este preste benefício patrimonial a um terceiro estranho ao pacto.",
        "tips": "Tanto o estipulante quanto o beneficiário (terceiro) possuem legitimidade ativa para cobrar a prestação do promitente.",
        "common_errors": "Pensar que o terceiro precisa assinar o contrato na data da celebração; basta que ele anua para exigir o cumprimento da vantagem."
    },
    {
        "id": "art_439",
        "number": 439,
        "subject": "Promessa de Fato de Terceiro",
        "text": "Art. 439. Aquele que tiver prometido fato de terceiro responderá por perdas e danos, quando este o não executar. Parágrafo único. Tal responsabilidade não existirá se o terceiro for o cônjuge do promitente, dependendo da sua anuência o ato a ser praticado, e pelo regime de bens a indenização alguma coisa do seu patrimônio possa arrebatar.",
        "summary": "Quem promete que terceiro prestará fato responde objetivamente por perdas e danos perante o credor se o terceiro recusar.",
        "tips": "Se o terceiro anuir e assumir a obrigação, o promitente original fica exonerado (art. 440 do CC), transferindo o vínculo inteiramente ao terceiro.",
        "common_errors": "Achar que o credor pode processar o terceiro para obrigá-lo a cumprir; o terceiro não prometeu nada. O réu da ação indenizatória é o promitente."
    },
    {
        "id": "art_441",
        "number": 441,
        "subject": "Vícios Redibitórios - Conceito e Requisitos",
        "text": "Art. 441. A coisa recebida em virtude de contrato comutativo pode ser enjeitada por vícios ou defeitos ocultos, que a tornem imprópria ao uso a que é destinada, ou lhe diminuam o valor. Parágrafo único. É aplicável a disposição deste artigo às doações onerosas.",
        "summary": "Vício redibitório é o defeito oculto e preexistente em coisa recebida em contrato comutativo ou doação onerosa que diminui seu valor ou inutiliza o bem.",
        "tips": "Requisitos cumulativos: 1) Contrato comutativo ou doação modal/onerosa; 2) Defeito oculto (não perceptível de pronto por pessoa de diligência normal); 3) Gravidade (inutilidade ou desvalorização); 4) Preexistência do vício à tradição da coisa.",
        "common_errors": "Achar que doação puramente gratuita admite ação por vício redibitório. A lei só autoriza em contratos onerosos comutativos e doações onerosas (com encargo)."
    },
    {
        "id": "art_442",
        "number": 442,
        "subject": "Ações Edilícias (Redibitória e Estimatória/Quanti Minoris)",
        "text": "Art. 442. Em vez de rejeitar a coisa, redibindo o contrato (art. 441), pode o adquirente reclamar abatimento no preço.",
        "summary": "Direito potestativo de escolha do adquirente entre as duas Ações Edilícias: 1) Ação Redibitória (resolve o contrato e devolve o preço); 2) Ação Estimatória ou Quanti Minoris (conserva o negócio e pede abatimento proporcional).",
        "tips": "O adquirente escolhe livremente uma ou outra ação, não podendo cumular ambas simultaneamente para o mesmo pedido em relação ao mesmo bem.",
        "common_errors": "Achar que o vendedor escolhe se quer consertar, devolver o dinheiro ou dar desconto; a opção entre redibir ou pleitear abatimento pertence exclusivamente ao adquirente."
    },
    {
        "id": "art_443",
        "number": 443,
        "subject": "Efeitos da Boa-fé e Má-fé do Alienante no Vício",
        "text": "Art. 443. Se o alienante conhecia o vício ou defeito da coisa, restituirá o que recebeu com perdas e danos; se o não conhecia, tão-somente restituirá o valor recebido, mais as despesas do contrato.",
        "summary": "Diferença vital: se o alienante agiu de má-fé (sabia do vício), paga restituição + perdas e danos. Se agiu de boa-fé (ignorava o vício), apenas restitui o valor + despesas contratuais.",
        "tips": "Pergunta clássica de prova: A ignorância do alienante exclui a responsabilidade pelo vício redibitório? RESPOSTA: NÃO! Ele ainda responde desfazendo o negócio ou dando abatimento, mas fica isento de pagar perdas e danos adicionais.",
        "common_errors": "Achar que a boa-fé do vendedor afasta a responsabilidade redibitória. A responsabilidade por vício redibitório é de garantia objetiva, variando apenas as perdas e danos."
    },
    {
        "id": "art_445",
        "number": 445,
        "subject": "Prazos Decadenciais dos Vícios Redibitórios",
        "text": "Art. 445. O adquirente decai do direito de obter a redibição ou abatimento no preço no prazo de trinta dias se a coisa for móvel, e de um ano se for imóvel, contado da entrega efetiva; se já estava na posse, o prazo conta-se da alienação, reduzido à metade. § 1º Quando o vício, por sua natureza, só puder ser conhecido mais tarde, o prazo contar-se-á do momento em que dele tiver ciência, até o prazo máximo de cento e oitenta dias, em se tratando de bens móveis; e de um ano, para os imóveis.",
        "summary": "Prazos decadenciais: Móveis = 30 dias; Imóveis = 1 ano. Já estava na posse = metade do prazo. Vício ocultíssimo: conta da ciência, tendo como teto 180 dias (móveis) e 1 ano (imóveis).",
        "tips": "Trata-se de prazo decadencial, não prescricional, pois visa ao exercício de um direito potestativo edilício.",
        "common_errors": "Confundir prazo de móvel (30 dias) com prazo de imóvel (1 ano) ou aplicar o prazo de 90 dias do CDC (art. 26) para relações puramente civis."
    },
    {
        "id": "art_458",
        "number": 458,
        "subject": "Contrato Aleatório: Emptio Spei",
        "text": "Art. 458. Se o contrato for aleatório, por dizer respeito a coisas ou fatos futuros, cujo risco de não virem a existir um dos contratantes assuma, terá o outro direito de receber integralmente o que lhe foi prometido, desde que de sua parte não tenha havido dolo ou culpa, ainda que nada venha a existir.",
        "summary": "Emptio Spei (Venda da Esperança): O comprador assume o risco de a coisa sequer vir a existir. Deve pagar 100% do preço acordado, salvo dolo ou desídia do vendedor.",
        "tips": "Exemplo clássico: Compra do resultado de um lance de rede de pesca por R$ 500,00; mesmo que o pescador lance a rede e não venha nenhum peixe, o valor é devido integralmente.",
        "common_errors": "Confundir com Emptio Rei Speratae. Na emptio spei o risco é da própria existência do objeto (tudo ou nada)."
    },
    {
        "id": "art_459",
        "number": 459,
        "subject": "Contrato Aleatório: Emptio Rei Speratae",
        "text": "Art. 459. Se for aleatório, por serem objeto dele coisas futuras, tomando o adquirente a si o risco de virem a existir em qualquer quantidade, terá também direito o alienante a todo o preço, desde que de sua parte não tiver concorrido culpa, ainda que a coisa venha a existir em quantidade inferior à esperada. Parágrafo único. Mas, se da coisa nada vier a existir, alienação não haverá, e o alienante restituirá o preço recebido.",
        "summary": "Emptio Rei Speratae (Venda da Coisa Esperada): O comprador assume o risco apenas sobre a quantidade, mas não sobre a existência. Deve vir alguma quantidade; se nada existir, o contrato é nulo/resolvido e o preço é devolvido.",
        "tips": "Exemplo: Compra da safra futura de soja de uma fazenda por preço fechado; se colher apenas 10 sacas ao invés de 1.000 sacas devido a seca sem culpa do agricultor, o preço é devido. Porém se não colher nada (zero), o contrato fica sem efeito e devolve-se o valor.",
        "common_errors": "Achar que na emptio rei speratae o alienante fica com o dinheiro mesmo que nenhuma unidade da coisa venha a existir."
    },
    {
        "id": "art_460",
        "number": 460,
        "subject": "Contrato Aleatório: Coisas Existentes Expostas a Risco",
        "text": "Art. 460. Se for aleatório o contrato, por se referir a coisas existentes, mas expostas a risco, assumido pelo adquirente, terá igualmente direito o alienante a todo o preço, posto que a coisa já não existisse, em parte, ou de todo, no dia do contrato.",
        "summary": "Risco de coisas expostas a perigo iminente ou transporte arriscado. O adquirente assume o risco da perda pretérita ou futura desde que o alienante não soubesse do sinistro.",
        "tips": "O art. 461 complementa: a alienação aleatória a risco pode ser anulada como dolosa pelo prejudicado se provar que o outro contratante não ignorava a consumação do risco.",
        "common_errors": "Ignorar que a boa-fé do alienante é condição sine qua non da validade desse contrato aleatório."
    },
    {
        "id": "art_462",
        "number": 462,
        "subject": "Contrato Preliminar / Promessa de Contratar",
        "text": "Art. 462. O contrato preliminar, exceto quanto à forma, deve conter todos os requisitos essenciais ao contrato a ser celebrado.",
        "summary": "Princípio da atração mitigada: o pré-contrato exige capacidade, objeto lícito e determinação das cláusulas essenciais, mas NÃO exige a solenidade formal do definitivo.",
        "tips": "Uma promessa de compra e venda de imóvel de alto valor pode ser feita por instrumento particular, mesmo que a escritura definitiva exija forma pública (art. 108 do CC).",
        "common_errors": "Achar que o contrato preliminar exige exatamente a mesma forma e solenidade pública exigida para o contrato definitivo."
    },
    {
        "id": "art_467",
        "number": 467,
        "subject": "Contrato com Pessoa a Declarar",
        "text": "Art. 467. No momento da conclusão do contrato, pode uma das partes reservar-se a faculdade de indicar a pessoa que deve adquirir os direitos e assumir as obrigações dele decorrentes.",
        "summary": "Pactum de persona declaranda (electio amici). Uma parte se reserva o direito de nomear terceiro que entrará retroativamente na sua posição jurídica.",
        "tips": "O prazo legal para a declaração/indicação do terceiro, salvo estipulação em contrário das partes, é de 5 (cinco) dias (art. 468 do CC). A aceitação do nomeado deve seguir a mesma forma do contrato.",
        "common_errors": "Confundir com mandato ou representação. No contrato com pessoa a declarar, a parte celebra em nome próprio com faculdade resolutiva de substituição ex tunc."
    },
    {
        "id": "art_474",
        "number": 474,
        "subject": "Extinção dos Contratos - Resolução e Cláusula Resolutiva",
        "text": "Art. 474. A cláusula resolutiva expressa opera de pleno direito; a tácita depende de interpelação judicial.",
        "summary": "Cláusula resolutiva: Expressa opera automaticamente pelo inadimplemento contratual; Tácita decorre de lei e necessita de interpelação judicial prévia.",
        "tips": "Em contratos bilaterais e comutativos, a cláusula resolutiva tácita é ínsita a todos os contratos bilaterais (art. 475 do CC).",
        "common_errors": "Achar que mesmo tendo cláusula resolutiva expressa é obrigatório ingressar com ação para constituir o devedor em mora em qualquer situação civil genérica."
    },
    {
        "id": "art_476",
        "number": 476,
        "subject": "Exceção do Contrato Não Cumprido e Onerosidade Excessiva",
        "text": "Art. 476. Nos contratos bilaterais, nenhum dos contratantes, antes de cumprida a sua obrigação, pode exigir o implemento da do outro.",
        "summary": "Exceptio non adimpleti contractus. Meio de defesa substancial nos contratos bilaterais: quem não pagou/entregou não pode exigir a prestação do outro.",
        "tips": "Aplica-se também a exceção do contrato parcialmente cumprido (exceptio non rite adimpleti contractus), que autoriza reter pagamento equivalente ao que faltou.",
        "common_errors": "Tentar invocar a exceção do contrato não cumprido em contratos unilaterais, onde apenas uma das partes suporta obrigação."
    }
]
