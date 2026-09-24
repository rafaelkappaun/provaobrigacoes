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
        "articles": "Art. 165, §§ 2º e 3º do CPC/2015 e Art. 1.210, §1º do CC",
        "key_concept": "Adequação prática: Mediação para conflitos relacionais continuados (família, vizinhança, societário); Conciliação para litígios pontuais sem vínculo prévio (consumo, batida de carro); Arbitragem para disputas técnicas e empresariais patrimoniais; Autotutela para desforço possessório imediato.",
        "trap": "Usar conciliação em disputa familiar complexa agrava o conflito; a lei determina expressamente a mediação quando houver vínculo anterior entre as partes (art. 165, § 3º, CPC)."
    },
    "Processos Autocompositivos vs. Heterocompositivos": {
        "articles": "Teoria Geral dos Conflitos e CPC/2015",
        "key_concept": "Autocomposição: solução construída pelas partes, empoderamento, foco no futuro (ganha-ganha), confidencialidade e maior taxa de cumprimento espontâneo. Heterocomposição: decisão imposta de cima para baixo, foco no passado (ganha-perde), dependência de coerção estatal.",
        "trap": "Na heterocomposição a sentença muitas vezes encerra o processo, mas não encerra o conflito sociológico subjacente entre as partes."
    },
    "Princípios da Resolução de Conflitos e Acesso à Justiça": {
        "articles": "Art. 5º, XXXV e LXXVIII da CF/88, Art. 166 do CPC e Art. 2º da Lei 13.140/15",
        "key_concept": "Princípios fundamentais: Confidencialidade, Imparcialidade, Independência, Autonomia da vontade das partes, Oralidade, Informalidade, Boa-fé, Razoável duração do processo e Acesso à Ordem Jurídica Justa.",
        "trap": "O dever de confidencialidade vincula mediadores, conciliadores e partes: informações reveladas na sessão não podem ser usadas como prova em futuro processo judicial (art. 166, § 1º, CPC)."
    },
    "Evolução Histórica dos Métodos Consensuais": {
        "articles": "Doutrina Internacional e Frank Sander (Pound Conference, 1976)",
        "key_concept": "Relatório Cappelletti e Garth (Três Ondas Renovatórias de Acesso à Justiça: 1ª Assistência jurídica aos pobres, 2ª Direitos difusos/coletivos, 3ª Abordagem ampla com métodos alternativos). Frank Sander na Conferência de Pound (1976) concebe a Justiça Multiportas.",
        "trap": "A Terceira Onda de Cappelletti e Garth é exatamente o enfoque no aperfeiçoamento dos métodos de solução e representação adequada dos conflitos."
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

NOMES = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo", "Helena", "Igor", "Juliana", "Lucas", "Mariana", "Rodrigo", "Tatiana"]
EMPRESAS = ["Alfa Engenharia", "Beta Logística", "Gama Cosméticos", "Delta Tecnologia", "Ômega Varejo", "Solaris Construtora"]

def generate_multiportas_question_offline(subject: str, bank: str = "FGV", difficulty: str = "Médio") -> Dict[str, Any]:
    """Gera proceduralmente questões técnicas completas sobre os 14 temas do questionário de Modelo Multiportas"""
    if subject not in MULTIPORTAS_SUBJECTS:
        subject = random.choice(MULTIPORTAS_SUBJECTS)
    if bank not in MULTIPORTAS_BANKS:
        bank = random.choice(MULTIPORTAS_BANKS)

    p1 = random.choice(NOMES)
    p2 = random.choice([n for n in NOMES if n != p1])
    emp1 = random.choice(EMPRESAS)
    emp2 = random.choice([e for e in EMPRESAS if e != emp1])

    # 1. NOÇÃO DE CONFLITO DE DIREITO E CONFLITO SOCIAL
    if subject == "Noção de Conflito de Direito e Conflito Social":
        enunciado = (
            f"({bank}) {p1} e {p2} são vizinhos em um condomínio residencial e divergem reiteradamente sobre ruídos noturnos, "
            f"gerando animosidade pessoal. Após meses de tensão, {p1} ingressa com ação de obrigação de não fazer com pedido indenizatório. "
            f"À luz da Teoria Geral dos Conflitos e da lição clássica de Francesco Carnelutti sobre a lide, assinale a afirmativa correta:"
        )
        options = {
            "A": "O conflito social e a lide jurídica são termos sinônimos, pois qualquer insatisfação interpessoal constitui automaticamente pretensão jurídica processável.",
            "B": "O conflito social é o substrato sociológico da convivência humana, ao passo que a lide é o conflito de interesses qualificado por uma pretensão resistida com relevância jurídica.",
            "C": "A jurisdição estatal tem por função exclusiva solucionar conflitos psicológicos internos, sendo irrelevante a existência de pretensão jurídica.",
            "D": "Para haver lide, basta a manifestação unilateral de vontade de uma parte, dispensando-se a resistência da parte adversa."
        }
        gabarito = "B"
        article = "Teoria Geral do Processo (Francesco Carnelutti) e CPC/2015"
        legal_basis = "A lide é o conflito de interesses qualificado por uma pretensão resistida. O conflito social precede a lide e nem sempre possui enquadramento jurídico direto."
        explanation = "Segundo a clássica doutrina carneluttiana, a lide exige um conflito intersubjetivo em que há pretensão de uma parte subordinar o interesse alheio ao seu, com resistência da outra. O conflito social é mais amplo e sociológico."

    # 2. ENFRENTAMENTO DOS CONFLITOS VS. JURISDIÇÃO
    elif subject == "Enfrentamento dos Conflitos vs. Jurisdição":
        enunciado = (
            f"({bank}) Diante do expressivo aumento no acervo de processos pendentes de julgamento no Judiciário brasileiro, "
            f"doutrina e jurisprudência debatem a crise do modelo contencioso tradicional. Sobre a evolução do enfrentamento de conflitos "
            f"em contraposição ao modelo tradicional de jurisdição estatal, é correto afirmar que:"
        )
        options = {
            "A": "O CPC/2015 consagrou o princípio do monopólio estrito da jurisdição estatal, vedando a atuação de terceiros particulares na solução de controvérsias civis.",
            "B": "O modelo multiportas propõe a substituição da 'cultura da sentença' pela 'cultura da pacificação', na qual o Judiciário e a sociedade estimulam métodos consensuais e adequados a cada litígio.",
            "C": "A sentença judicial tradicional é reconhecida como o único mecanismo capaz de restaurar os laços sociais fraturados entre as partes conflitantes.",
            "D": "O acesso à justiça previsto na Constituição de 1988 restringe-se estritamente ao direito de receber uma sentença proferida por juiz togado."
        }
        gabarito = "B"
        article = "Art. 3º do CPC/2015 e Art. 5º, XXXV da CF/88"
        legal_basis = "O Estado promoverá, sempre que possível, a solução consensual dos conflitos. A conciliação, a mediação e outros métodos de solução consensual de conflitos deverão ser estimulados por juízes, advogados, defensores e promotores."
        explanation = "A superação da 'cultura da sentença' visa transformar o Judiciário em um centro distribuidor de justiça multiportas, onde a solução consensual é incentivada como meio prioritário de pacificação efetiva (Art. 3º, §§ 2º e 3º, CPC)."

    # 3. CONSTRUÇÃO LEGISLATIVA NO ENFRENTAMENTO DE CONFLITOS
    elif subject == "Construção Legislativa no Enfrentamento de Conflitos":
        enunciado = (
            f"({bank}) A disciplina da resolução adequada de conflitos no Brasil passou por importante evolução legislativa e normativa "
            f"nas últimas décadas. Assinale a alternativa que descreve CORRETAMENTE os principais marcos dessa evolução:"
        )
        options = {
            "A": "A Resolução 125/2010 do CNJ instituiu a Política Judiciária Nacional de Tratamento Adequado dos Conflitos, marco posteriormente consolidado pelo CPC/2015 e pela Lei de Mediação (Lei nº 13.140/2015).",
            "B": "A mediação e a conciliação só foram autorizadas no ordenamento brasileiro após a entrada em vigor da Emenda Constitucional nº 45/2004.",
            "C": "O CPC de 2015 revogou a Lei de Arbitragem (Lei nº 9.307/1996), unificando todos os métodos de resolução de conflitos na jurisdição estatal.",
            "D": "A Lei dos Juizados Especiais (Lei nº 9.099/1995) estabeleceu a obrigatoriedade da arbitragem em todas as causas de menor complexidade."
        }
        gabarito = "A"
        article = "Resolução CNJ nº 125/2010, CPC/2015 e Lei nº 13.140/2015"
        legal_basis = "A Resolução CNJ 125/2010 estabeleceu as bases dos Centros Judiciários de Solução de Conflitos (CEJUSCs), que foram recepcionadas e aprofundadas pelo CPC/2015 e pela Lei de Mediação."
        explanation = "A Resolução 125/2010 do CNJ é o divisor de águas institucional no Brasil, determinando a criação dos CEJUSCs e a formação padronizada de conciliadores e mediadores, recepcionada em lei pelo CPC/15 e Lei 13.140/15."

    # 4. PRINCIPAIS FORMAS DE RESOLUÇÃO DE CONFLITOS
    elif subject == "Principais Formas de Resolução de Conflitos":
        enunciado = (
            f"({bank}) No estudo da Teoria Geral dos Conflitos, as formas de resolução são tradicionalmente categorizadas em "
            f"autotutela, autocomposição e heterocomposição. A respeito dessas categorias, assinale a afirmativa correta:"
        )
        options = {
            "A": "A autotutela caracteriza-se pela presença de um terceiro investido de poder para impor sua decisão soberana sobre os litigantes.",
            "B": "Na autocomposição, a solução do litígio é alcançada pelas próprias partes interessadas, seja diretamente ou com auxílio de terceiro facilitador neutro.",
            "C": "A heterocomposição restringe-se exclusivamente aos litígios decididos perante a Justiça do Trabalho, não se aplicando ao juízo arbitral.",
            "D": "A autocomposição é vedada em conflitos que envolvam direitos patrimoniais disponíveis entre sujeitos capazes."
        }
        gabarito = "B"
        article = "Teoria Geral dos Métodos de Resolução de Conflitos"
        legal_basis = "A autocomposição se distingue pelo protagonismo das partes na construção do desfecho do conflito (ex: negociação, conciliação e mediação), enquanto a heterocomposição se pauta na decisão imposta por terceiro (juiz ou árbitro)."
        explanation = "Na autocomposição, são os próprios titulares do conflito que constroem a decisão (por transação, submissão ou renúncia). Já na heterocomposição, o poder de decidir é delegado ao juiz ou árbitro."

    # 5. MÉTODOS ALTERNATIVOS DE RESOLUÇÃO DE CONFLITOS (MASCS/ADRS)
    elif subject == "Métodos Alternativos de Resolução de Conflitos (MASCs/ADRs)":
        enunciado = (
            f"({bank}) {p1} e {p2} divergem sobre o cumprimento de um contrato de prestação de serviços. Buscando solucionar a controvérsia, "
            f"consultam um advogado sobre as diferenças entre os Métodos Adequados de Solução de Conflitos (MASCs). "
            f"À luz do CPC/2015 (art. 165) e da Lei nº 13.140/2015, assinale a opção correta quanto ao papel de cada condutor:"
        )
        options = {
            "A": "O mediador atua preferencialmente onde houver vínculo anterior entre as partes e não propõe soluções, auxiliando os envolvidos a identificar seus interesses; o conciliador pode sugerir soluções para o litígio.",
            "B": "O mediador tem o dever de redigir propostas impositivas e forçar o acordo, ao passo que o conciliador tem função meramente consultiva.",
            "C": "O árbitro e o mediador exercem funções idênticas, ambos com poder de proferir sentença irrecorrível vinculante para as partes.",
            "D": "A negociação exige obrigatoriamente a presença de um conciliador credenciado junto ao Tribunal de Justiça para possuir validade jurídica."
        }
        gabarito = "A"
        article = "Art. 165, §§ 2º e 3º do CPC/2015"
        legal_basis = "O conciliador, que atuará preferencialmente nos casos em que não houver vínculo anterior, poderá sugerir soluções. O mediador, que atuará nos casos com vínculo anterior, auxiliará aos interessados a compreender as questões e identificar soluções consensuais."
        explanation = "Diferença central do CPC/2015: Mediação (vínculo prévio continuado, sem sugestão de propostas pelo terceiro); Conciliação (litígio pontual, sem vínculo prévio, sendo lícito sugerir soluções neutras)."

    # 6. FORMAS DE AUTOCOMPOSIÇÃO E FUNDAMENTOS
    elif subject == "Formas de Autocomposição e Fundamentos":
        enunciado = (
            f"({bank}) Em audiência realizada no CEJUSC, {p1} e {p2} decidem pôr fim à ação de cobrança mediante concessões mútuas, "
            f"ajustando o pagamento parcelado de 70% do valor originalmente pleiteado. Sob o ponto de vista das formas de autocomposição "
            f"e dos efeitos processuais (Art. 487 do CPC), esse ato configura:"
        )
        options = {
            "A": "Submissão, que acarreta a extinção do processo sem julgamento de mérito por carência da ação.",
            "B": "Transação, modalidade autocompositiva bilateral que dá ensejo à extinção do processo com resolução do mérito.",
            "C": "Renúncia unilateral ao direito sobre o qual se funda a ação, dependente de homologação pelo Ministério Público.",
            "D": "Desistência da ação, mantendo aberta a possibilidade de repropositura da mesma demanda em até 2 anos."
        }
        gabarito = "B"
        article = "Art. 487, III, 'b' do CPC/2015 e Art. 840 do Código Civil"
        legal_basis = "Haverá resolução de mérito quando o juiz homologar a transação (art. 487, III, 'b'). É lícito aos interessados prevenirem ou terminarem o litígio mediante concessões mútuas (art. 840 CC)."
        explanation = "A transação é negócio jurídico bilateral no qual as partes fazem concessões recíprocas para extinguir o litígio, produzindo coisa julgada material após homologação judicial."

    # 7. FORMAS DE HETEROCOMPOSIÇÃO E FUNDAMENTOS
    elif subject == "Formas de Heterocomposição e Fundamentos":
        enunciado = (
            f"({bank}) {emp1} e {emp2} celebraram contrato de fornecimento internacional e inseriram cláusula compromissória arbitral. "
            f"Surgindo controvérsia de grande vulto patrimonial, optaram por instituir o tribunal arbitral nos termos da Lei nº 9.307/1996. "
            f"Sobre a heterocomposição e a natureza jurídica da decisão arbitral, assinale a afirmativa correta:"
        )
        options = {
            "A": "A arbitragem é modalidade autocompositiva, pois o árbitro necessita da concordância expressa de ambas as partes para homologar seu relatório.",
            "B": "A sentença arbitral é ato de heterocomposição que produz, entre as partes e seus sucessores, os mesmos efeitos da sentença judicial e constitui título executivo judicial.",
            "C": "A sentença arbitral carece de qualquer eficácia jurídica até que seja homologada por um juiz de direito de primeira instância.",
            "D": "Apenas o Supremo Tribunal Federal possui competência para instituir tribunais arbitrais em matéria empresarial privada."
        }
        gabarito = "B"
        article = "Art. 31 da Lei nº 9.307/1996 e Art. 515, VII do CPC/2015"
        legal_basis = "A sentença arbitral produz, entre as partes e seus sucessores, os mesmos efeitos da sentença proferida pelos órgãos do Poder Judiciário e, sendo condenatória, constitui título executivo."
        explanation = "A arbitragem é heterocomposição privada. O árbitro decide com poder vinculante e sua sentença é título executivo judicial autônomo, dispensando qualquer homologação judicial prévia (art. 31 da Lei 9.307/96)."

    # 8. CASOS PRÁTICOS E ADEQUAÇÃO DOS MÉTODOS (AUTOTUTELA, HETERO E AUTO)
    elif subject == "Casos Práticos e Adequação dos Métodos (Autotutela, Hetero e Auto)":
        enunciado = (
            f"({bank}) Analise as seguintes hipóteses práticas de conflito:\n"
            f"I. Disputa de guarda de filhos menores entre ex-cônjuges com histórico de mágoas e desgaste afetivo acumulado.\n"
            f"II. Invasão violenta e repentina de fazenda rural, com reação imediata e comedida do possuidor para restituir a posse.\n"
            f"III. Controvérsia técnica de engenharia sobre cálculo de royalties entre duas grandes multinacionais de energia.\n"
            f"De acordo com a teoria da adequação dos métodos de resolução de conflitos, os mecanismos mais adequados para os casos I, II e III são, respectivamente:"
        )
        options = {
            "A": "I - Arbitragem compulsória de família; II - Conciliação prévia em juizado especial cível; III - Autotutela judicial de urgência privativa do Estado.",
            "B": "I - Mediação (foco nas relações continuadas); II - Autotutela lícita (desforço possessório imediato e proporcional); III - Arbitragem (expertise técnica e sigilo).",
            "C": "I - Conciliação direta sem vínculo continuado; II - Mediação comunitária protelatória; III - Jurisdição estatal contenciosa obrigatória sem juízo arbitral.",
            "D": "I - Autotutela das partes mediante coação legítima; II - Jurisdição estatal privativa de urgência; III - Mediação informal sem força executiva vinculante."
        }
        gabarito = "B"
        article = "Art. 165 CPC/2015, Art. 1.210, §1º do CC e Lei 9.307/1996"
        legal_basis = "Mediação para relações continuadas de família (I); Autotutela possessória expressamente autorizada em lei no desforço imediato (II); Arbitragem para matérias técnicas e patrimoniais disponíveis (III)."
        explanation = "No caso I, há relação prévia continuada (mediação); no caso II, a lei autoriza autotutela moderada e incontinenti (art. 1.210, § 1º, CC); no caso III, litígio técnico patrimonial com partes empresariais (arbitragem)."

    # 9. PROCESSOS AUTOCOMPOSITIVOS VS. HETEROCOMPOSITIVOS
    elif subject == "Processos Autocompositivos vs. Heterocompositivos":
        enunciado = (
            f"({bank}) No contraponto analítico entre os processos autocompositivos (mediação e conciliação) e os processos "
            f"heterocompositivos (jurisdição estatal e arbitragem), assinale a afirmativa INCORRETA:"
        )
        options = {
            "A": "Nos processos autocompositivos a lógica predominante é a do 'ganha-ganha' (integração de interesses), enquanto na heterocomposição a lógica costuma ser 'ganha-perde'.",
            "B": "Os processos autocompositivos oferecem maior índice de cumprimento espontâneo do acordo porque a solução decorre da vontade dos próprios litigantes.",
            "C": "Tanto nos processos autocompositivos quanto nos heterocompositivos, a solução final é outorgada e imposta por um terceiro munido de poder decisório coercitivo.",
            "D": "A heterocomposição analisa predominantemente os fatos passados para atribuir a razão jurídica, enquanto a mediação foca na preservação das relações para o futuro."
        }
        gabarito = "C"
        article = "Teoria Geral dos Conflitos e Métodos Adequados"
        legal_basis = "Na autocomposição o terceiro NÃO possui poder decisório coercitivo; seu papel limita-se a facilitar a comunicação ou sugerir alternativas sem imposição."
        explanation = "A afirmativa C é incorreta (logo, o gabarito pretendido), pois na autocomposição o terceiro jamais impõe a decisão — quem decide são as próprias partes."

    # 10. PRINCÍPIOS DA RESOLUÇÃO DE CONFLITOS E ACESSO À JUSTIÇA
    elif subject == "Princípios da Resolução de Conflitos e Acesso à Justiça":
        enunciado = (
            f"({bank}) Durante uma sessão de mediação judicial promovida em um CEJUSC, {p1} revelou fatos comprometedores sobre suas finanças "
            f"na tentativa de viabilizar uma proposta de composição. Não havendo acordo, {p2} arrolou o mediador como testemunha e juntou "
            f"as anotações da sessão na ação principal. À luz do art. 166 do CPC e da Lei nº 13.140/2015, assinale a opção correta:"
        )
        options = {
            "A": "O mediador é obrigado a testemunhar em juízo relatando todas as confissões ouvidas, prevalecendo a busca da verdade real sobre o segredo da mediação.",
            "B": "A conduta de {p2} viola o princípio da confidencialidade, sendo inadmissíveis no processo judicial informações, propostas ou documentos produzidos na sessão de mediação.",
            "C": "O princípio da publicidade absoluta dos atos processuais impede qualquer modalidade de sigilo em sessões realizadas dentro de órgãos do Poder Judiciário.",
            "D": "A confidencialidade só protege as sessões de conciliação, aplicando-se o princípio da ampla publicidade às mediações."
        }
        gabarito = "B"
        article = "Art. 166, §§ 1º e 2º do CPC/2015 e Art. 30 da Lei nº 13.140/2015"
        legal_basis = "A confidencialidade estende-se a todas as informações produzidas no curso do procedimento, cujo teor não poderá ser utilizado para fim diverso daquele previsto por expressa deliberação das partes."
        explanation = "O princípio da confidencialidade é pilar da autocomposição. O mediador não pode atuar como testemunha nem as propostas podem ser usadas como confissão no processo (art. 166, CPC)."

    # 11. EVOLUÇÃO HISTÓRICA DOS MÉTODOS CONSENSUAIS
    elif subject == "Evolução Histórica dos Métodos Consensuais":
        enunciado = (
            f"({bank}) No contexto da evolução histórica do acesso à justiça no direito comparado e no Brasil, o renomado estudo de "
            f"Mauro Cappelletti e Bryant Garth identificou as chamadas 'Três Ondas Renovatórias de Acesso à Justiça'. "
            f"Assinale a alternativa que identifica CORRETAMENTE a Terceira Onda Renovatória:"
        )
        options = {
            "A": "Primeira Onda: voltada precipuamente à criação de defensorias públicas para garantir assistência judiciária integral e gratuita aos necessitados.",
            "B": "Segunda Onda: orientada à representação processual dos interesses difusos e coletivos, materializada pela disciplina da ação civil pública.",
            "C": "Terceira Onda: centrada no novo enfoque do acesso à ordem jurídica justa através do estímulo aos métodos adequados de resolução de litígios (ADRs).",
            "D": "Quarta Onda: direcionada exclusivamente à virtualização e à informatização integral da tramitação do processo judicial eletrônico."
        }
        gabarito = "C"
        article = "Doutrina de Acesso à Justiça (Mauro Cappelletti e Bryant Garth)"
        legal_basis = "1ª Onda: assistência judiciária aos pobres; 2ª Onda: representação dos interesses difusos; 3ª Onda: novo enfoque no acesso à justiça através dos métodos adequados de resolução de disputas."
        explanation = "A Terceira Onda de Cappelletti e Garth preconiza uma abordagem ampla sobre o acesso à ordem jurídica justa, com o surgimento e valorização das ADRs (mediação, conciliação e arbitragem)."

    # 12. OBJETIVOS DO MODELO MULTIPORTAS
    elif subject == "Objetivos do Modelo Multiportas":
        enunciado = (
            f"({bank}) A expressão 'Tribunal Multiportas' (Multi-door Courthouse), formulada pelo jurista Frank Sander na Conferência de Pound (1976), "
            f"fundamenta a política judiciária contemporânea adotada pelo CPC/2015 e pelo CNJ. O objetivo central deste modelo é:"
        )
        options = {
            "A": "Privatizar integralmente o Poder Judiciário estatal, transferindo as demandas patrimoniais para escritórios privados de cobrança.",
            "B": "Estruturar o Judiciário como um centro integrador de justiça, que analisa a controvérsia e a direciona para a via de solução mais adequada e célere.",
            "C": "Impedir que qualquer litígio cível tenha acesso à decisão de um juiz togado antes de decorridos três anos de tentativas infrutíferas de acordo.",
            "D": "Impor cobrança de custas em dobro contra o autor que ajuizar ação judicial sem prévia tentativa comprovada de mediação extrajudicial."
        }
        gabarito = "B"
        article = "Conferência de Pound (Frank Sander, 1976) e Res. CNJ nº 125/2010"
        legal_basis = "O modelo multiportas preconiza que para cada litígio há uma 'porta' mais adequada (negociação, conciliação, mediação, arbitragem ou processo judicial tradicional), garantindo a resposta mais eficaz."
        explanation = "Frank Sander propôs que o tribunal não tivesse apenas uma porta (a do julgamento contencioso pelo juiz), mas múltiplas portas onde o conflito é triado e submetido ao mecanismo mais apropriado."

    # 13. EVOLUÇÃO HISTÓRICA E LEGISLATIVA DOS JUIZADOS ESPECIAIS
    elif subject == "Evolução Histórica e Legislativa dos Juizados Especiais":
        enunciado = (
            f"({bank}) Os Juizados Especiais representam um dos mais expressivos instrumentos de democratização do acesso à justiça no Brasil. "
            f"Sobre a trajetória legislativa e os princípios fundamentais da Lei nº 9.099/1995 (Art. 2º), assinale a afirmativa correta:"
        )
        options = {
            "A": "Os Juizados Especiais foram criados pelo CPC de 2015, o qual extinguiu integralmente a sistemática autônoma da Lei nº 9.099/1995.",
            "B": "O processo perante os Juizados orienta-se pela oralidade, simplicidade, informalidade, economia processual e celeridade, buscando a conciliação.",
            "C": "A Lei nº 9.099/1995 veda a realização de audiência conciliatória nas causas cujo valor controvertido ultrapasse dez salários mínimos.",
            "D": "A Constituição Federal de 1988 vedou a atuação de juízes leigos e conciliadores, exigindo presença privativa de magistrados togados vitalícios."
        }
        gabarito = "B"
        article = "Art. 2º da Lei nº 9.099/1995 e Art. 98, I da CF/88"
        legal_basis = "O processo orientar-se-á pelos critérios da oralidade, simplicidade, informalidade, economia processual e celeridade, buscando, sempre que possível, a conciliação ou a transação."
        explanation = "O art. 2º da Lei 9.099/95 estabelece os vetores principiológicos dos Juizados Especiais, priorizando de forma imperativa a autocomposição em sua fase inaugural."

    # 14. EVOLUÇÃO HISTÓRICA E LEGISLATIVA DA ARBITRAGEM NO BRASIL
    else:
        enunciado = (
            f"({bank}) A arbitragem no direito brasileiro experimentou profunda transformação com a promulgação da Lei nº 9.307/1996 "
            f"(Lei Marco Maciel) e a consolidação de sua constitucionalidade pelo Supremo Tribunal Federal (STF). "
            f"A esse respeito, assinale a opção correta:"
        )
        options = {
            "A": "A convenção de arbitragem possui eficácia vinculante negativa, obrigando o juiz togado a extinguir o processo sem julgamento do mérito.",
            "B": "O STF declarou inconstitucional a Lei nº 9.307/1996 por entender que a decisão arbitral fere o princípio da inafastabilidade da jurisdição.",
            "C": "A arbitragem no Brasil é permitida para dirimir quaisquer espécies de controvérsias, inclusive crimes graves e estado de filiação civil.",
            "D": "A Lei nº 13.129/2015 revogou a possibilidade de entes da Administração Pública direta utilizarem a arbitragem em contratos administrativos."
        }
        gabarito = "A"
        article = "Art. 485, VII do CPC/2015 e Lei nº 9.307/1996 (AgRg na SE 5.206/STF)"
        legal_basis = "A convenção de arbitragem afasta a jurisdição estatal, ensejando a extinção do processo sem resolução de mérito pelo juiz togado (art. 485, VII, CPC)."
        explanation = "Com a constitucionalidade afirmada pelo STF no AgRg na SE 5.206, a convenção de arbitragem possui eficácia vinculante negativa, impedindo o julgamento da causa pelo Judiciário estatal."

    # Embaralha alternativas mantendo consistência do gabarito
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
        "id": f"q_multi_{uuid.uuid4().hex[:12]}",
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
