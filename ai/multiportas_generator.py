import random
import uuid
from typing import Dict, Any, List

# Os 14 assuntos oficiais alinhados 100% ao Questionário de Revisão da Prova 01 de Modelo Multiportas
MULTIPORTAS_SUBJECTS = [
    "Noção de Conflito de Direito e Conflito Social",
    "Enfrentamento dos Conflitos vs. Jurisdição",
    "Construção Legislativa no Enfrentamento de Conflitos",
    "Principais Formas de Resolução de Conflitos",
    "Métodos Alternativos de Resolução de Conflitos (MASCs/ADRs)",
    "Formas de Autocomposição e Fundamentos",
    "Formas de Heterocomposição e Fundamentos",
    "Casos Práticos e Adequação dos Métodos (Autotutela, Hetero e Auto)",
    "Processos Autocompositivos vs. Heterocompositivos",
    "Princípios da Resolução de Conflitos e Acesso à Justiça",
    "Evolução Histórica dos Métodos Consensuais",
    "Objetivos do Modelo Multiportas",
    "Evolução Histórica e Legislativa dos Juizados Especiais",
    "Evolução Histórica e Legislativa da Arbitragem no Brasil"
]

MULTIPORTAS_BANKS = ["OAB", "FGV", "CESPE", "FCC", "VUNESP", "Doutrina"]

MULTIPORTAS_STUDY_GUIDE: Dict[str, Dict[str, str]] = {
    "Noção de Conflito de Direito e Conflito Social": {
        "articles": "Teoria Geral do Processo / Doutrina (Carnelutti e Kazuo Watanabe)",
        "key_concept": "O conflito social é fenômeno natural decorrente da convivência em sociedade e da escassez de bens. Transforma-se em conflito de direito (lide) quando há uma pretensão resistida qualificada por interesse juridicamente tutelado (Carnelutti).",
        "trap": "Nem todo conflito social é conflito de direito; apenas adquire relevância jurídica quando atinge normas ou bens tutelados pelo ordenamento."
    },
    "Enfrentamento dos Conflitos vs. Jurisdição": {
        "articles": "Art. 5º, XXXV da CF/88 e Art. 3º do CPC/2015",
        "key_concept": "Crise da jurisdição tradicional estatal: sobrecarga de processos, morosidade e 'cultura da sentença'. A jurisdição estatal não possui mais o monopólio exclusivo; promove-se a 'cultura da pacificação' e da solução adequada.",
        "trap": "A jurisdição estatal não foi abolida; o modelo multiportas convive harmonicamente com ela, sendo o juiz obrigado a estimular métodos consensuais (art. 3º, § 3º, CPC)."
    },
    "Construção Legislativa no Enfrentamento de Conflitos": {
        "articles": "Art. 3º do CPC/2015, Lei 13.140/2015 e Resolução CNJ 125/2010",
        "key_concept": "Marco histórico-normativo: CF/88 (art. 98, I), Lei dos Juizados (9.099/95), Lei de Arbitragem (9.307/96), Resolução CNJ 125/2010 (Política Judiciária Nacional de Tratamento Adequado dos Conflitos), CPC/2015 e Lei de Mediação (13.140/15).",
        "trap": "A Resolução 125/2010 do CNJ institucionalizou os CEJUSCs e a capacitação obrigatória de mediadores antes mesmo do CPC/2015 e da Lei de Mediação."
    },
    "Principais Formas de Resolução de Conflitos": {
        "articles": "Doutrina e Código Civil (ex: art. 1.210, §1º)",
        "key_concept": "Tríade clássica: 1) Autotutela (imposição pela força própria - excepcional e tipificada em lei); 2) Autocomposição (as próprias partes constroem a solução); 3) Heterocomposição (terceiro imparcial decide de forma impositiva).",
        "trap": "A autotutela é regra geral ilícita (crime de exercício arbitrário das próprias razões - art. 345 CP), sendo admitida apenas em exceções estritas como legítima defesa e desforço imediato."
    },
    "Métodos Alternativos de Resolução de Conflitos (MASCs/ADRs)": {
        "articles": "Arts. 165 a 175 do CPC/2015 e Lei 13.140/2015",
        "key_concept": "Negociação (direta entre as partes, sem terceiro); Mediação (terceiro neutro facilita o diálogo sem propor soluções); Conciliação (terceiro pode sugerir soluções práticas); Arbitragem (terceiro profere sentença com força executiva).",
        "trap": "O mediador NUNCA sugere propostas nem pressiona por acordo; quem constrói a solução são as próprias partes. O conciliador PODE sugerir soluções (art. 165, §§ 2º e 3º, CPC)."
    },
    "Formas de Autocomposição e Fundamentos": {
        "articles": "Arts. 165 a 175, 334 e 487, III do CPC/2015",
        "key_concept": "Modalidades: 1) Transação (concessões mútuas bilaterais); 2) Renúncia ao direito (unilateral pelo credor); 3) Submissão/Reconhecimento da procedência do pedido (unilateral pelo réu). Extingue o processo com resolução de mérito (art. 487, III, CPC).",
        "trap": "A desistência da ação extingue o processo sem resolução de mérito (art. 485, VIII); a renúncia extingue COM resolução de mérito (art. 487, III, 'c')."
    },
    "Formas de Heterocomposição e Fundamentos": {
        "articles": "Lei 9.307/1996 (Arbitragem) e CPC/2015 (Jurisdição)",
        "key_concept": "Duas grandes espécies: 1) Jurisdição Estatal (exercida pelo Poder Judiciário investido de iurisdictio e imperium); 2) Arbitragem (exercida por árbitro privado escolhido pelas partes para direitos patrimoniais disponíveis).",
        "trap": "A sentença arbitral tem a mesma eficácia da sentença judicial e constitui título executivo judicial (art. 515, VII, CPC), dispensando homologação pelo Judiciário."
    },
    "Casos Práticos e Adequação dos Métodos (Autotutela, Hetero e Auto)": {
        "articles": "Art. 165 do CPC/2015, Art. 1.210 do CC e Lei 9.307/1996",
        "key_concept": "Critérios de adequação: vínculos relacionais prévios e duradouros exigem Mediação; relações pontuais sem vínculo prévio exigem Conciliação; direitos patrimoniais empresariais com sigilo e especialidade exigem Arbitragem; ameaça injusta iminente à posse exige Autotutela proporcional.",
        "trap": "Não existe método universalmente superior: a escolha do método adequado deve respeitar a natureza do conflito e a relação das partes."
    },
    "Processos Autocompositivos vs. Heterocompositivos": {
        "articles": "Doutrina de Métodos Adequados e Resolução CNJ 125/2010",
        "key_concept": "Autocomposição: solução consensual construída pelas partes (ganha-ganha), preserva relações futuras e tem altíssimo cumprimento voluntário. Heterocomposição: imposição coercitiva por terceiro juiz/árbitro (ganha-perde), foco no passado e na culpa.",
        "trap": "Na autocomposição o terceiro jamais profere juízo condenatório nem impõe sanção; a autoridade decorre da concordância de vontades das partes."
    },
    "Princípios da Resolução de Conflitos e Acesso à Justiça": {
        "articles": "Art. 166 do CPC/2015 e Lei 13.140/2015",
        "key_concept": "Princípios cardeais: independência, imparcialidade da intervenção, autonomia da vontade das partes, confidencialidade absoluta, oralidade, informalidade e decisão informada.",
        "trap": "A confidencialidade é ampla: nenhuma informação ou proposta revelada em sessão de mediação pode servir de prova em processo judicial futuro (art. 166, §§ 1º e 2º, CPC)."
    },
    "Evolução Histórica dos Métodos Consensuais": {
        "articles": "Doutrina de Mauro Cappelletti e Bryant Garth (Acesso à Justiça)",
        "key_concept": "Ondas de Cappelletti: 1ª Onda (Assistência Judiciária aos hipossuficientes financeiramente); 2ª Onda (Tutela e representação dos Direitos Difusos e Coletivos); 3ª Onda (Enfoque integral de acesso à ordem jurídica justa através das ADRs).",
        "trap": "A terceira onda renovatória não descarta a via judicial, mas amplia o espectro de portas adequadas para entrega de pacificação efetiva."
    },
    "Objetivos do Modelo Multiportas": {
        "articles": "Resolução CNJ 125/2010 e Art. 3º do CPC/2015",
        "key_concept": "O Judiciário como um centro integrador de justiça ('Multi-door Courthouse'): oferecer a porta mais adequada a cada conflito (Appropriate Dispute Resolution), promovendo pacificação social duradoura, desjudicialização seletiva e redução da litigiosidade patológica.",
        "trap": "Multiportas não significa forçar acordo a qualquer custo para diminuir estatística de juiz, mas garantir que o cidadão receba o tratamento metodológico mais eficaz para sua controvérsia."
    },
    "Evolução Histórica e Legislativa dos Juizados Especiais": {
        "articles": "Art. 98, I da CF/88, Lei 7.244/1984 e Lei 9.099/1995",
        "key_concept": "Evolução: Lei 7.244/84 (Juizados de Pequenas Causas); CF/88 (art. 98, I prevendo juizados especiais cíveis e criminais providos por juízes togados ou togados e leigos); Lei 9.099/95. Princípios: oralidade, simplicidade, informalidade, economia processual e celeridade.",
        "trap": "A conciliação nos Juizados Especiais é fase obrigatória que antecede a audiência de instrução e julgamento (arts. 21 e seguintes da Lei 9.099/95)."
    },
    "Evolução Histórica e Legislativa da Arbitragem no Brasil": {
        "articles": "Lei 9.307/1996, Lei 13.129/2015 e STF (SE 5.206/Espanha)",
        "key_concept": "Constituição Imperial de 1824 e Código Comercial de 1850 já previam a arbitragem. O marco moderno foi a Lei Marco Maciel (Lei 9.307/96), declarada plenamente constitucional pelo STF em 2001. Atualizada pela Lei 13.129/15 (permitindo arbitragem na Administração Pública).",
        "trap": "A convenção de arbitragem (cláusula compromissória ou compromisso arbitral) tem efeito negativo: afasta a jurisdição estatal, devendo o juiz extinguir o processo sem resolução de mérito (art. 485, VII, CPC)."
    }
}

NOMES = ["Adriano", "Beatriz", "Caio", "Débora", "Estêvão", "Flávia", "Gabriel", "Heloísa", "Ismael", "Júlia", "Leandro", "Manuela", "Otávio", "Priscila", "Renato", "Sabrina", "Tiago", "Valéria"]
EMPRESAS = ["Alfa Logística", "Beta Softwares", "Gama Biofarmacêutica", "Delta Agrícola", "Ômega Energia Solar", "Titan Infraestrutura", "Vértice Construtora", "Horizonte Alimentos"]

def generate_multiportas_question_offline(subject: str, bank: str = "FGV", difficulty: str = "Médio") -> Dict[str, Any]:
    """
    Gera proceduralmente questões técnicas sobre os 14 temas de Modelo Multiportas.
    Possui múltiplos cenários factuais distintos por assunto (garantindo diversidade e zero repetições idênticas).
    """
    if subject not in MULTIPORTAS_SUBJECTS:
        subject = random.choice(MULTIPORTAS_SUBJECTS)
    if bank not in MULTIPORTAS_BANKS:
        bank = random.choice(MULTIPORTAS_BANKS)

    p1 = random.choice(NOMES)
    p2 = random.choice([n for n in NOMES if n != p1])
    emp1 = random.choice(EMPRESAS)
    emp2 = random.choice([e for e in EMPRESAS if e != emp1])
    scenario_idx = random.choice([0, 1, 2])

    # 1. NOÇÃO DE CONFLITO DE DIREITO E CONFLITO SOCIAL
    if subject == "Noção de Conflito de Direito e Conflito Social":
        if scenario_idx == 0:
            enunciado = (
                f"({bank}) {p1} e {p2} fundaram uma sociedade de tecnologia da informação e, após divergências estratégicas, "
                f"passaram a nutrir forte animosidade interpessoal mútua. Em determinado momento, {p1} notificou formalmente {p2} "
                f"exigindo apuração de haveres e pagamento de sua participação societária, pretensão expressamente recusada por {p2}. "
                f"À luz da Teoria Geral dos Conflitos e da clássica lição de Francesco Carnelutti, é correto afirmar:"
            )
        elif scenario_idx == 1:
            enunciado = (
                f"({bank}) {emp1} e {emp2} mantinham parceria comercial no agronegócio regional. Em razão de quebra de safra, "
                f"instaurou-se um clima de insatisfação mútua no relacionamento empresarial. A controvérsia adquiriu status de lide jurídica "
                f"apenas quando {emp1} demandou a retenção de maquinários e {emp2} opôs resistência formal fundada em cláusula de força maior. "
                f"Sobre a transição entre conflito social e lide de direito (Carnelutti), assinale a afirmativa correta:"
            )
        else:
            enunciado = (
                f"({bank}) Dois cirurgiões cooperados em um hospital privado, {p1} e {p2}, desenvolveram divergências sobre a escala "
                f"de plantões cirúrgicos, gerando tensão relacional continuada. A questão desbordou do âmbito meramente social e configurou "
                f"lide jurídica no instante em que {p1} postulou indenização por danos materiais e {p2} recusou categoricamente a pretensão. "
                f"Considerando a lição de Carnelutti sobre o conceito de lide, assinale a opção correta:"
            )
        options = {
            "A": "O conflito social e a lide jurídica coincidem rigorosamente no plano fático, pois qualquer mal-estar interpessoal autoriza a tutela jurisdicional contenciosa imediata.",
            "B": "O conflito social decorre da convivência coletiva e da escassez de bens, enquanto a lide jurídica exige um conflito de interesses qualificado por pretensão resistida juridicamente tutelada.",
            "C": "A lide jurídica prescinde de resistência do adversário, bastando a manifestação de insatisfação moral unilateral de qualquer interessado perante o Poder Judiciário.",
            "D": "O ordenamento jurídico processual veda a autocomposição em situações decorrentes de conflitos interpessoais puros desprovidos de previsão típica expressa em lei civil."
        }
        gabarito = "B"
        article = "Teoria Geral do Processo (Francesco Carnelutti) e CPC/2015"
        legal_basis = "A lide é o conflito de interesses qualificado por uma pretensão resistida. O conflito social precede a lide e nem sempre possui enquadramento jurídico direto."
        explanation = "Segundo a clássica doutrina carneluttiana, a lide exige um conflito intersubjetivo qualificado por pretensão que encontra resistência da parte contrária. O conflito social é amplo e sociológico."

    # 2. ENFRENTAMENTO DOS CONFLITOS VS. JURISDIÇÃO
    elif subject == "Enfrentamento dos Conflitos vs. Jurisdição":
        if scenario_idx == 0:
            enunciado = (
                f"({bank}) O Poder Judiciário brasileiro enfrenta histórico congestionamento processual, decorrente da arraigada "
                f"'cultura da sentença', onde litígios civis rotineiros são massivamente judicializados. Sobre a transformação paradigmática "
                f"do enfrentamento de conflitos trazida pelo CPC/2015 em contraposição à jurisdição tradicional, assinale a afirmativa correta:"
            )
        elif scenario_idx == 1:
            enunciado = (
                f"({bank}) No contexto da moderna teoria do Direito Processual Civil, discute-se a superação do monopólio estatal absoluto "
                f"da prestação jurisdicional e a afirmação de modelos cooperativos de pacificação social (Art. 3º do CPC). "
                f"A respeito desse novo modelo de enfrentamento dos litígios, é correto assinalar:"
            )
        else:
            enunciado = (
                f"({bank}) Ao analisar a prestação da tutela jurídica contemporânea, juristas sustentam que a adjudicação formal por sentença "
                f"estatal frequentemente declara vencedores e perdedores, mas não dissolve a animosidade subjacente entre os cidadãos. "
                f"Diante dessa realidade, o modelo multiportas propõe:"
            )
        options = {
            "A": "O restabelecimento do monopólio jurisdicional absoluto pelo Estado, vedando a autotutela mitigada e a via arbitral em litígios patrimoniais privados.",
            "B": "A substituição gradativa da 'cultura da sentença' pela 'cultura da pacificação', onde o Estado e os operadores estimulam ativamente métodos consensuais adequados ao litígio.",
            "C": "A supressão do direito constitucional de ação judicial para cidadãos que recusarem submeter controvérsias cíveis a câmaras privadas de mediação prévia.",
            "D": "A atribuição de poder decisório coercitivo imediato a mediadores comunitários para proferir sentenças com trânsito em julgado material sem controle judicial."
        }
        gabarito = "B"
        article = "Art. 3º do CPC/2015 e Art. 5º, XXXV da CF/88"
        legal_basis = "O Estado promoverá, sempre que possível, a solução consensual dos conflitos. A conciliação, a mediação e outros métodos deverão ser estimulados por juízes, advogados, defensores e promotores."
        explanation = "A transição da 'cultura da sentença' para a 'cultura da pacificação' descentraliza a resposta judicial contenciosa, incentivando vias autocompositivas e métodos adequados (Art. 3º, §§ 2º e 3º, CPC)."

    # 3. CONSTRUÇÃO LEGISLATIVA NO ENFRENTAMENTO DE CONFLITOS
    elif subject == "Construção Legislativa no Enfrentamento de Conflitos":
        if scenario_idx == 0:
            enunciado = (
                f"({bank}) A construção do arcabouço normativo brasileiro voltado ao tratamento adequado dos conflitos "
                f"consolidou-se por marcos históricos interligados entre 1995 e 2015. Assinale a alternativa que descreve "
                f"CORRETAMENTE esse itinerário legislativo e normativo:"
            )
        elif scenario_idx == 1:
            enunciado = (
                f"({bank}) Ao examinar a Política Judiciária Nacional instituída pelo Conselho Nacional de Justiça (CNJ), "
                f"doutrinadores apontam uma norma precursora que organizou os Centros Judiciários de Solução de Conflitos e Cidadania (CEJUSCs). "
                f"Essa norma pioneira e seu desdobramento legal consistem em:"
            )
        else:
            enunciado = (
                f"({bank}) As reformas legislativas do processo civil brasileiro culminaram na consagração expressa dos métodos "
                f"consensuais no CPC/2015 e na Lei Federal nº 13.140/2015. A respeito da integração legislativa nesse campo, assinale a opção correta:"
            )
        options = {
            "A": "A Resolução CNJ nº 125/2010 instituiu a Política Judiciária Nacional de Tratamento Adequado dos Conflitos, marco regulatório posteriormente absorvido pelo CPC/2015 e pela Lei nº 13.140/2015.",
            "B": "A Lei nº 9.099/1995 extinguiu a exigência de tentativa de conciliação prévia, tornando privativa do juiz togado a homologação de qualquer manifestação de vontade.",
            "C": "O Código de Processo Civil de 2015 revogou tacitamente a Lei de Arbitragem (Lei nº 9.307/1996), unificando a solução de conflitos na via estatal pública.",
            "D": "A prática da mediação extrajudicial e judicial no Brasil dependia exclusivamente de provimento individual de cada juiz de primeira instância até o ano de 2022."
        }
        gabarito = "A"
        article = "Resolução CNJ nº 125/2010, CPC/2015 e Lei nº 13.140/2015"
        legal_basis = "A Resolução CNJ 125/2010 estabeleceu as diretrizes dos CEJUSCs e a capacitação obrigatória de mediadores, sendo recepcionada e complementada pelo CPC/2015 e pela Lei de Mediação."
        explanation = "A Resolução 125/2010 foi o marco normativo institucional no Brasil, determinando a instalação dos CEJUSCs e a formação qualificada, confirmada em sede legal pelo CPC/2015 e pela Lei 13.140/2015."

    # 4. PRINCIPAIS FORMAS DE RESOLUÇÃO DE CONFLITOS
    elif subject == "Principais Formas de Resolução de Conflitos":
        if scenario_idx == 0:
            enunciado = (
                f"({bank}) Na sistematização doutrinária das formas de resolução de controvérsias (autotutela, autocomposição e heterocomposição), "
                f"o ordenamento jurídico estabelece balizas estritas para o uso da força física própria e para a atuação de facilitadores. "
                f"Sobre essas modalidades fundamentais, assinale a afirmativa correta:"
            )
        elif scenario_idx == 1:
            enunciado = (
                f"({bank}) {p1}, titular de direito de crédito vencido e não pago por {p2}, cogita os caminhos legais admitidos para obter "
                f"a satisfação de seu interesse econômico. Ao consultar seu advogado sobre as modalidades clássicas de enfrentamento de litígios, "
                f"recebe a orientação correta de que:"
            )
        else:
            enunciado = (
                f"({bank}) A doutrina processual classifica a solução de litígios em autotutela, autocomposição e heterocomposição. "
                f"Em relação à legitimidade e características operacionais dessas três espécies, é correto afirmar:"
            )
        options = {
            "A": "A autotutela é a regra geral no direito privado moderno, podendo o credor apreender bens móveis do devedor sem previsão legal nem intervenção policial.",
            "B": "Na autocomposição, o resultado decisório é emanado diretamente das próprias partes litigantes, que constroem a pacificação por via autônoma direta ou auxiliadas por terceiro.",
            "C": "A heterocomposição depende imperativamente da manifestação favorável de ambos os litigantes quanto ao teor substancial da sentença proferida pelo juiz togado.",
            "D": "A autocomposição é expressamente proibida em litígios patrimoniais civis que tramitam em varas cíveis da Justiça Comum Estadual."
        }
        gabarito = "B"
        article = "Teoria Geral dos Conflitos e Código Civil"
        legal_basis = "Na autocomposição, os próprios litigantes constroem o desfecho do conflito. Já na heterocomposição, a decisão vinculante cabe a terceiro investido (juiz ou árbitro)."
        explanation = "O cerne da autocomposição é o protagonismo das partes no desfecho da lide. A autotutela é excepcional e tipificada (ex: desforço possessório imediato - art. 1.210, §1º CC)."

    # 5. MÉTODOS ALTERNATIVOS DE RESOLUÇÃO DE CONFLITOS (MASCS/ADRS)
    elif subject == "Métodos Alternativos de Resolução de Conflitos (MASCs/ADRs)":
        if scenario_idx == 0:
            enunciado = (
                f"({bank}) Dois herdeiros de quotas societárias de uma empresa familiar em {emp1} estão em litígio duradouro. "
                f"Paralelamente, a transportadora {emp2} cobra uma fatura isolada e incontroversa de frete contra um cliente eventual. "
                f"Considerando a diretriz do Art. 165 do CPC/2015 sobre as figuras do mediador e do conciliador, assinale a opção correta:"
            )
        elif scenario_idx == 1:
            enunciado = (
                f"({bank}) {p1} e {p2} questionam a atuação prática de mediadores e conciliadores no âmbito do Poder Judiciário. "
                f"À luz do art. 165, §§ 2º e 3º do CPC/2015 e da Lei nº 13.140/2015, assinale a afirmativa correta sobre as atribuições técnicas de cada função:"
            )
        else:
            enunciado = (
                f"({bank}) No campo dos Métodos Adequados de Solução de Conflitos (MASCs), a distinção metodológica entre mediação, "
                f"conciliação, negociação e arbitragem orienta a adequada triagem dos litígios no Judiciário. A esse propósito, é correto afirmar:"
            )
        options = {
            "A": "O mediador atua preferencialmente em casos com vínculo relacional anterior entre as partes, facilitando o diálogo sem sugerir soluções; o conciliador atua sem vínculo prévio e pode propor soluções.",
            "B": "O mediador tem o poder legal de proferir sentença condenatória impositiva se as partes recusarem a primeira proposta conciliatória em audiência.",
            "C": "O conciliador é terminantemente proibido pela legislação processual civil de apresentar qualquer proposta, cabendo tal função exclusivamente ao árbitro privado.",
            "D": "A negociação direta entre advogados requer prévia homologação pelo Ministério Público para ter validade e gerar quitação civil."
        }
        gabarito = "A"
        article = "Art. 165, §§ 2º e 3º do CPC/2015"
        legal_basis = "O conciliador poderá sugerir soluções (casos sem vínculo prévio). O mediador auxiliará os interessados a compreender as questões e identificar soluções consensuais (casos com vínculo prévio)."
        explanation = "A distinção técnica do CPC/2015 reside no vínculo prévio continuado (mediação, sem proposição de soluções pelo terceiro) versus relação pontual sem vínculo prévio (conciliação, onde sugestões são permitidas)."

    # 6. FORMAS DE AUTOCOMPOSIÇÃO E FUNDAMENTOS
    elif subject == "Formas de Autocomposição e Fundamentos":
        if scenario_idx == 0:
            enunciado = (
                f"({bank}) Em audiência de conciliação perante vara cível, o réu {p1}, convencido das provas documentais apresentadas, "
                f"declara formalmente concordar com todos os pedidos deduzidos na petição inicial por {p2}. "
                f"Sob o ângulo das modalidades autocompositivas e dos efeitos processuais (Art. 487 do CPC), essa manifestação constitui:"
            )
        elif scenario_idx == 1:
            enunciado = (
                f"({bank}) Durante sessão conduzida no CEJUSC, {p1} e {p2} resolvem extinguir litígio contratual mediante recíprocas concessões: "
                f"{p1} concede desconto financeiro no saldo devedor e {p2} antecipa o pagamento à vista. Esse negócio jurídico autocompositivo representa:"
            )
        else:
            enunciado = (
                f"({bank}) {p1}, autora de ação de indenização por perdas e danos contra {emp1}, protocola petição abrindo mão definitiva "
                f"do próprio direito material sobre o qual se funda a pretensão, desonerando a empresa de qualquer obrigação futura. Esse ato configura:"
            )
        options = {
            "A": "Desistência unilateral da demanda, que enseja a extinção do processo sem julgamento do mérito e autoriza a propositura de nova ação.",
            "B": "Modalidade autocompositiva com resolução de mérito (Art. 487, III do CPC), vinculando as partes e operando coisa julgada material após homologação.",
            "C": "Autotutela jurisdicional reflexa, que necessita de intervenção em dobro da Defensoria Pública para produzir eficácia perante terceiros.",
            "D": "Perempção superveniente compulsória, que afasta a incidência dos princípios do contraditório e da ampla defesa."
        }
        gabarito = "B"
        article = "Art. 487, III do CPC/2015 e Art. 840 do Código Civil"
        legal_basis = "Haverá resolução de mérito quando o juiz homologar o reconhecimento da procedência do pedido, a transação ou a renúncia à pretensão (art. 487, III, CPC)."
        explanation = "As três grandes formas de autocomposição com resolução de mérito no CPC são a transação (concessões recíprocas), a renúncia (pelo autor) e o reconhecimento da procedência/submissão (pelo réu)."

    # 7. FORMAS DE HETEROCOMPOSIÇÃO E FUNDAMENTOS
    elif subject == "Formas de Heterocomposição e Fundamentos":
        if scenario_idx == 0:
            enunciado = (
                f"({bank}) Duas concessionárias de infraestrutura rodoviária, {emp1} e {emp2}, celebraram contrato com cláusula compromissória "
                f"arbitral para dirimir litígios de reequilíbrio econômico-financeiro. Surgido o conflito, submeteram a controvérsia a um tribunal arbitral. "
                f"A respeito da eficácia jurídica da sentença arbitral proferida nos termos da Lei nº 9.307/1996, assinale a afirmativa correta:"
            )
        elif scenario_idx == 1:
            enunciado = (
                f"({bank}) A heterocomposição se caracteriza pela intervenção de terceiro investido de autoridade decisória impositiva. "
                f"Ao comparar a jurisdição estatal com a arbitragem privada no ordenamento brasileiro, é correto assinalar que:"
            )
        else:
            enunciado = (
                f"({bank}) Um investidor e uma construtora litigam perante juízo arbitral em razão de atraso na conclusão de empreendimento comercial. "
                f"O árbitro profere sentença condenando a construtora ao pagamento de multa contratual líquida. Sobre a executoriedade dessa decisão, é correto afirmar:"
            )
        options = {
            "A": "A sentença arbitral é mero parecer consultivo desprovido de força executiva, necessitando de processo autônomo de conhecimento no Judiciário para ser executada.",
            "B": "A sentença arbitral tem a mesma eficácia da sentença judicial e constitui título executivo judicial autônomo (Art. 515, VII, CPC), dispensando homologação pelo Judiciário.",
            "C": "O laudo arbitral só adquire validade após prévia e expressa ratificação por câmara especializada do Tribunal de Justiça competente.",
            "D": "A heterocomposição privada por arbitragem é restrita a causas criminais e de estado familiar de incapazes."
        }
        gabarito = "B"
        article = "Art. 31 da Lei nº 9.307/1996 e Art. 515, VII do CPC/2015"
        legal_basis = "A sentença arbitral produz, entre as partes e seus sucessores, os mesmos efeitos da sentença judicial e, sendo condenatória, constitui título executivo (art. 31 Lei 9.307/96)."
        explanation = "A arbitragem é modalidade plena de heterocomposição. Sua sentença equipara-se à judicial, constituindo título executivo judicial que dispensa homologação do Judiciário."

    # 8. CASOS PRÁTICOS E ADEQUAÇÃO DOS MÉTODOS (AUTOTUTELA, HETERO E AUTO)
    elif subject == "Casos Práticos e Adequação dos Métodos (Autotutela, Hetero e Auto)":
        if scenario_idx == 0:
            enunciado = (
                f"({bank}) Considere os seguintes cenários fáticos:\n"
                f"I. Disputa de visitas e convivência familiar de filho menor entre pais que nutrem mágoas afetivas recíprocas.\n"
                f"II. Invasão noturna e violenta de fazenda produtiva, com desforço físico imediato e moderado do possuidor para repelir os invasores.\n"
                f"III. Controvérsia técnica e sigilosa sobre patentes de biotecnologia entre multinacionais de grande capacidade financeira.\n"
                f"Segundo a teoria da adequação dos métodos de resolução de litígios, os mecanismos mais adequados para I, II e III são, respectivamente:"
            )
        elif scenario_idx == 1:
            enunciado = (
                f"({bank}) Analise as seguintes situações concretas:\n"
                f"1. Cobrança de indenização por colisão de trânsito entre motoristas desconhecidos sem relação pretérita nem interesse em contato futuro.\n"
                f"2. Conflito sucessório de partilha entre irmãos coproprietários de empresa familiar centenária com histórico afetivo complexo.\n"
                f"3. Tentativa de turbação recente de imóvel rural com reação incontinenti e proporcional de segurança própria do proprietário.\n"
                f"Os métodos recomendados segundo o CPC/2015 e a teoria da resolução adequada são:"
            )
        else:
            enunciado = (
                f"({bank}) A correta triagem e o encaminhamento do litígio à 'porta' apropriada constituem o pilar do modelo multiportas. "
                f"Acerca da correspondência entre a natureza do litígio e o método de resolução recomendado, assinale a afirmativa correta:"
            )
        options = {
            "A": "Vínculos relacionais duradouros recomendam Mediação; disputas pontuais patrimoniais recomendam Conciliação; matérias societárias de alta especialidade e sigilo recomendam Arbitragem.",
            "B": "A autotutela violenta sem limites temporais é o método prioritário recomendado pelo CPC para conflitos societários de grande envergadura econômica.",
            "C": "Litígios com forte carga afetiva familiar devem ser obrigatoriamente submetidos a arbitragem privada compulsória irrecorrível.",
            "D": "O modelo multiportas determina que todas as ações indenizatórias sem vínculo prévio devem ser processadas por mediação obrigatória de 12 meses."
        }
        gabarito = "A"
        article = "Art. 165 do CPC/2015, Art. 1.210 do CC e Lei 9.307/1996"
        legal_basis = "Mediação para vínculos continuados; Conciliação para litígios sem vínculo prévio; Arbitragem para direitos patrimoniais disponíveis técnicos com sigilo; Autotutela apenas em hipóteses estritas como desforço imediato."
        explanation = "A teoria da adequação avalia o método mais eficaz de acordo com as peculiaridades de cada litígio (foco relacional vs. foco pontual no objeto)."

    # 9. PROCESSOS AUTOCOMPOSITIVOS VS. HETEROCOMPOSITIVOS
    elif subject == "Processos Autocompositivos vs. Heterocompositivos":
        if scenario_idx == 0:
            enunciado = (
                f"({bank}) Estudos empíricos de jurimetria evidenciam que os acordos construídos em procedimentos autocompositivos "
                f"apresentam índice de cumprimento espontâneo significativamente superior ao das sentenças condenatórias impostas pelo juiz togado. "
                f"Essa maior efetividade prática da autocomposição decorre precipuamente de:"
            )
        elif scenario_idx == 1:
            enunciado = (
                f"({bank}) Ao contrastar a dinâmica dos processos autocompositivos (conciliação e mediação) com os heterocompositivos "
                f"(jurisdição estatal e arbitragem), a doutrina aponta diferenças estruturais sobre a abordagem do conflito. Assinale a afirmativa correta:"
            )
        else:
            enunciado = (
                f"({bank}) Em relação aos paradigmas 'ganha-ganha' e 'ganha-perde' na resolução de controvérsias jurídicas, "
                f"assinale a opção que reflete fielmente o contraponto entre processos autocompositivos e heterocompositivos:"
            )
        options = {
            "A": "Os processos autocompositivos operam na lógica de integração de interesses mútuos ('ganha-ganha'), promovendo o cumprimento voluntário porque as obrigações foram pactuadas pelos próprios envolvidos.",
            "B": "A heterocomposição estatal estimula a restauração espontânea da convivência harmônica entre os litigantes, eliminando qualquer sentimento de derrota por parte do réu sucumbente.",
            "C": "Nos processos autocompositivos a decisão final é imposta de modo coercitivo pelo mediador, que atua como juiz com poderes sancionatórios plenos.",
            "D": "Os processos heterocompositivos dispensam a aplicação de normas jurídicas positivas, decidindo causas cíveis invariavelmente por critérios de equidade fática arbitrária."
        }
        gabarito = "A"
        article = "Teoria dos Conflitos e Resolução CNJ nº 125/2010"
        legal_basis = "A autocomposição privilegia a autonomia privada e a construção consensual da solução pelas partes (lógica ganha-ganha), favorecendo o adimplemento voluntário."
        explanation = "Como a solução autocompositiva é fruto da vontade construída pelas próprias partes e não imposta de fora, ela tem adesão psicológica e fática superior, garantindo maior cumprimento voluntário."

    # 10. PRINCÍPIOS DA RESOLUÇÃO DE CONFLITOS E ACESSO À JUSTIÇA
    elif subject == "Princípios da Resolução de Conflitos e Acesso à Justiça":
        if scenario_idx == 0:
            enunciado = (
                f"({bank}) Durante sessão de mediação judicial realizada no CEJUSC, {p1} revelou informações estratégicas de faturamento "
                f"visando viabilizar proposta de composição com {p2}. Frustrado o acordo, o advogado de {p2} arrolou o mediador como testemunha "
                f"e requereu a juntada do rascunho de contas da mediação aos autos judiciais. À luz do art. 166 do CPC e da Lei nº 13.140/2015, assinale a opção correta:"
            )
        elif scenario_idx == 1:
            enunciado = (
                f"({bank}) O art. 166 do CPC/2015 estabelece os princípios fundamentais da conciliação e da mediação. "
                f"Entre os princípios expressamente tutelados, destaca-se a confidencialidade das comunicações. Sobre esse princípio, é correto afirmar:"
            )
        else:
            enunciado = (
                f"({bank}) Em procedimento de mediação envolvendo dissolução de vínculo contratual entre {p1} e {emp1}, as partes debatem "
                f"propostas sob compromisso ético e legal de sigilo. A respeito da extensão e limites da confidencialidade na autocomposição, assinale a afirmativa correta:"
            )
        options = {
            "A": "O princípio da publicidade absoluta impõe que todas as confidências reveladas na mediação sejam encaminhadas de ofício ao juiz da causa para fundamentar a sentença.",
            "B": "A confidencialidade abrange todas as informações produzidas na sessão, sendo vedado às partes e ao mediador utilizá-las como elemento de prova no processo judicial.",
            "C": "O mediador é juridicamente obrigado a prestar testemunho em juízo sempre que for intimado pela parte que tiver interesse em provar culpa do adversário.",
            "D": "A regra da confidencialidade se aplica exclusivamente a sessões extrajudiciais de arbitragem, vigorando a publicidade irrestrita nos CEJUSCs."
        }
        gabarito = "B"
        article = "Art. 166, §§ 1º e 2º do CPC/2015 e Art. 30 da Lei nº 13.140/2015"
        legal_basis = "A confidencialidade estende-se a todas as informações produzidas no curso do procedimento, cujo teor não poderá ser utilizado para fim diverso daquele previsto por expressa deliberação das partes."
        explanation = "O mediador e as partes estão submetidos ao sigilo profissional e processual; manifestações, propostas e relatos ouvidos na sessão não podem ser usados como prova no processo (art. 166, CPC)."

    # 11. EVOLUÇÃO HISTÓRICA DOS MÉTODOS CONSENSUAIS
    elif subject == "Evolução Histórica dos Métodos Consensuais":
        if scenario_idx == 0:
            enunciado = (
                f"({bank}) No clássico estudo sobre os movimentos globais de reforma judiciária conduzido por Mauro Cappelletti e Bryant Garth "
                f"(Projeto de Florença), foram sistematizadas as chamadas 'Três Ondas Renovatórias de Acesso à Justiça'. "
                f"Sobre a Terceira Onda Renovatória, assinale a afirmativa correta:"
            )
        elif scenario_idx == 1:
            enunciado = (
                f"({bank}) A democratização do acesso à justiça evoluiu ao longo do século XX com sucessivos aprimoramentos descritos pela doutrina "
                f"de Cappelletti e Garth. Assinale a alternativa que correlaciona CORRETAMENTE o objeto da Terceira Onda Renovatória:"
            )
        else:
            enunciado = (
                f"({bank}) Ao analisar o acesso à ordem jurídica justa, juristas contemporâneos fundamentam a valorização das MASCs "
                f"na doutrina das ondas de acesso à justiça. Assinale a opção que identifica com precisão as três ondas:"
            )
        options = {
            "A": "A Terceira Onda enfoca o acesso à ordem jurídica justa através de um novo olhar sobre o procedimento, incentivando métodos adequados de resolução de litígios (ADRs).",
            "B": "A Terceira Onda visava primordialmente à instituição da Defensoria Pública para assegurar gratuidade judiciária a pessoas hipossuficientes financeiramente.",
            "C": "A Terceira Onda restringiu-se à criação da ação civil pública para tutela dos interesses metaindividuais difusos e coletivos.",
            "D": "A Primeira Onda preconizou a substituição completa dos juizados togados por tribunais de inteligência artificial desprovidos de intervenção humana."
        }
        gabarito = "A"
        article = "Doutrina de Acesso à Justiça (Mauro Cappelletti e Bryant Garth)"
        legal_basis = "1ª Onda: assistência judiciária aos hipossuficientes; 2ª Onda: representação de interesses difusos/coletivos; 3ª Onda: novo enfoque no acesso à justiça por métodos adequados e simplificação de procedimentos."
        explanation = "A Terceira Onda de Cappelletti e Garth é o fundamento teórico moderno que dá legitimidade ao modelo multiportas e à valorização dos métodos consensuais como formas autênticas de pacificação social."

    # 12. OBJETIVOS DO MODELO MULTIPORTAS
    elif subject == "Objetivos do Modelo Multiportas":
        if scenario_idx == 0:
            enunciado = (
                f"({bank}) O conceito de 'Tribunal Multiportas' (Multi-door Courthouse), formulado originalmente pelo professor Frank Sander "
                f"na Conferência de Pound (1976), inspirou as diretrizes da Resolução CNJ nº 125/2010 e do CPC/2015. O objetivo primordial desse modelo consiste em:"
            )
        elif scenario_idx == 1:
            enunciado = (
                f"({bank}) A expressão 'Resolução Adequada de Disputas' substitui contemporaneamente o termo 'Métodos Alternativos', "
                f"reforçando o papel central do modelo multiportas. Sob a ótica do acesso qualificado à justiça, esse modelo tem por meta:"
            )
        else:
            enunciado = (
                f"({bank}) Diante de litígios complexos no âmbito civil e empresarial, o modelo multiportas atua como um sistema integrador. "
                f"A esse respeito, assinale a opção que expressa o verdadeiro propósito deste paradigma de justiça:"
            )
        options = {
            "A": "Estruturar o Judiciário como um centro inteligente de triagem, que analisa o perfil da lide e a encaminha à via de pacificação mais adequada e eficaz.",
            "B": "Privatizar as varas de execução judicial, retirando do Poder Judiciário o monopólio da coerção e do cumprimento de sentenças cíveis.",
            "C": "Impedir o ajuizamento de ações por consumidores enquanto não comprovarem pagamento de taxa de adesão a plataformas privadas de negociação.",
            "D": "Eliminar definitivamente a presença de advogados nos processos cíveis para reduzir custos de honorários contratuais e sucumbenciais."
        }
        gabarito = "A"
        article = "Conferência de Pound (Frank Sander, 1976) e Resolução CNJ nº 125/2010"
        legal_basis = "O modelo multiportas propõe que o Judiciário ofereça múltiplas portas (conciliação, mediação, arbitragem, adjudicação), direcionando cada caso ao mecanismo metodológico mais compatível."
        explanation = "O Tribunal Multiportas de Frank Sander concebe o Judiciário como um complexo de portas de acesso onde o litígio é acolhido e encaminhado ao método mais adequado (Appropriate Dispute Resolution)."

    # 13. EVOLUÇÃO HISTÓRICA E LEGISLATIVA DOS JUIZADOS ESPECIAIS
    elif subject == "Evolução Histórica e Legislativa dos Juizados Especiais":
        if scenario_idx == 0:
            enunciado = (
                f"({bank}) A criação dos Juizados Especiais Cíveis consolidou um novo marco na democratização da justiça no Brasil, "
                f"partindo da Lei nº 7.244/1984 e alcançando respaldo constitucional no Art. 98, I da CF/88 e na Lei nº 9.099/1995. "
                f"Sobre a principiologia e o procedimento inaugural desses órgãos, assinale a afirmativa correta:"
            )
        elif scenario_idx == 1:
            enunciado = (
                f"({bank}) Nos termos do Art. 2º da Lei Federal nº 9.099/1995, o processo perante os Juizados Especiais é informado "
                f"por critérios axiológicos direcionados à efetividade da tutela. Assinale a opção que elenca CORRETAMENTE esses critérios:"
            )
        else:
            enunciado = (
                f"({bank}) A Lei nº 9.099/1995 estruturou uma sistemática processual orientada à rápida solução das causas de menor complexidade. "
                f"A respeito da primazia da composição consensual no rito dos Juizados Especiais, é correto afirmar:"
            )
        options = {
            "A": "O rito rege-se pelos critérios da oralidade, simplicidade, informalidade, economia processual e celeridade, buscando, sempre que possível, a conciliação ou a transação.",
            "B": "A realização de audiência de conciliação nos Juizados Especiais é ato meramente facultativo que só ocorre caso o magistrado togado considere conveniente.",
            "C": "A Lei nº 9.099/1995 revogou a possibilidade de atuação de conciliadores leigos, exigindo presença privativa e indelegável de juízes de carreira vitalícios.",
            "D": "Os Juizados Especiais exigem petição inicial rígida com citação prévia por edital e aplicação obrigatória de revelia automática sem audiência inaugural."
        }
        gabarito = "A"
        article = "Art. 2º da Lei nº 9.099/1995 e Art. 98, I da CF/88"
        legal_basis = "O processo orientar-se-á pelos critérios da oralidade, simplicidade, informalidade, economia processual e celeridade, buscando, sempre que possível, a conciliação ou a transação."
        explanation = "O art. 2º da Lei 9.099/95 elenca expressamente os princípios fundamentais dos Juizados Especiais, com imperativa busca prioritária pela conciliação e transação."

    # 14. EVOLUÇÃO HISTÓRICA E LEGISLATIVA DA ARBITRAGEM NO BRASIL
    else:
        if scenario_idx == 0:
            enunciado = (
                f"({bank}) A Lei nº 9.307/1996 (Lei Marco Maciel) inaugurou a era moderna da arbitragem no Brasil, consolidada pelo Supremo Tribunal Federal "
                f"(STF) no histórico julgamento do AgRg na Sentença Estrangeira Contestada nº 5.206/Espanha. A respeito da eficácia da convenção de arbitragem, assinale a opção correta:"
            )
        elif scenario_idx == 1:
            enunciado = (
                f"({bank}) A inserção de convenção de arbitragem (cláusula compromissória ou compromisso arbitral) em contratos civis ou empresariais "
                f"produz relevantes efeitos perante a jurisdição estatal. À luz do CPC/2015 (Art. 485, VII) e da Lei nº 9.307/1996, é correto afirmar:"
            )
        else:
            enunciado = (
                f"({bank}) Com as atualizações introduzidas pela Lei Federal nº 13.129/2015 na Lei de Arbitragem brasileira, "
                f"o ordenamento jurídico ampliou a segurança jurídica e o campo de aplicação do instituto. Sobre essas inovações, assinale a afirmativa correta:"
            )
        options = {
            "A": "A convenção de arbitragem tem eficácia vinculante negativa, ensejando a extinção do processo estatal sem julgamento do mérito caso a parte invoque a cláusula perante o juiz togado.",
            "B": "O STF declarou inconstitucional a Lei nº 9.307/1996 por ofensa ao princípio da inafastabilidade da jurisdição previsto no Art. 5º, XXXV da Constituição Federal.",
            "C": "A arbitragem é terminantemente vedada para entes da Administração Pública direta ou indireta, mesmo após a edição da Lei nº 13.129/2015.",
            "D": "A celebração de compromisso arbitral não afasta a jurisdição do juiz estatal, que pode reexaminar livremente o mérito do laudo arbitral a qualquer tempo."
        }
        gabarito = "A"
        article = "Art. 485, VII do CPC/2015 e Lei nº 9.307/1996 (AgRg na SE 5.206/STF)"
        legal_basis = "A convenção de arbitragem possui efeito negativo vinculante, obrigando o juiz estatal a extinguir o processo sem resolução do mérito (art. 485, VII, CPC)."
        explanation = "A convenção de arbitragem vincula os contratantes e afasta a competência do Judiciário togado para apreciar o mérito da lide, tendo sua constitucionalidade chancelada pelo STF."

    # Embaralha alternativas de forma uniforme e balanceada
    keys = ["A", "B", "C", "D"]
    correct_text = options[gabarito]
    other_texts = [options[k] for k in keys if k != gabarito]
    random.shuffle(other_texts)

    new_correct_key = random.choice(keys)
    new_options = {}
    other_idx = 0
    for k in keys:
        if k == new_correct_key:
            new_options[k] = correct_text
        else:
            new_options[k] = other_texts[other_idx]
            other_idx += 1

    return {
        "id": f"q_multi_proc_{uuid.uuid4().hex[:12]}",
        "subject": subject,
        "bank": bank,
        "difficulty": difficulty,
        "enunciado": enunciado,
        "options": new_options,
        "gabarito": new_correct_key,
        "article": article,
        "legal_basis": legal_basis,
        "explanation": explanation
    }
