import random
import uuid
from typing import Dict, Any, List

# Os 22 assuntos oficiais alinhados 100% ao Questionário da Prova de Contratos (sem evicção)
SUBJECTS = [
    "Planos do Negócio Jurídico (Escada Ponteana)",
    "Princípios do Direito Contratual",
    "Boa-fé Objetiva e Figuras Parcelares",
    "Interpretação dos Contratos no Direito Brasileiro",
    "Classificação dos Contratos",
    "Etapas de Formação do Contrato",
    "Estipulação em Favor de Terceiro",
    "Promessa de Fato de Terceiro",
    "Contratos Aleatórios - Conceito e Espécies",
    "Contrato Aleatório: Emptio Spei",
    "Contrato Aleatório: Emptio Rei Speratae",
    "Contrato Aleatório: Coisas Existentes Expostas a Risco",
    "Contrato Preliminar / Promessa de Contratar",
    "Contrato com Pessoa a Declarar",
    "Contrato com Pessoa a Declarar vs. Outros Contratos",
    "Vícios Redibitórios - Conceito e Requisitos",
    "Efeitos da Boa-fé e Má-fé do Alienante no Vício",
    "Ações Edilícias (Redibitória e Estimatória/Quanti Minoris)",
    "Vício Redibitório vs. Entrega de Coisa Diversa (Aliud Pro Alio)",
    "Prazos Decadenciais dos Vícios Redibitórios",
    "Extinção dos Contratos - Resolução e Cláusula Resolutiva",
    "Exceção do Contrato Não Cumprido e Onerosidade Excessiva",
]

BANKS = ["OAB", "FGV", "CESPE", "FCC", "VUNESP", "Doutrina"]

NOMES_A = ["Carlos", "Roberto", "Mariana", "Juliana", "Eduardo", "Patrícia", "Fernando", "Beatriz", "Ricardo", "Camila", "Rodrigo", "Larissa", "Gustavo", "Fernanda", "Thiago", "Letícia"]
NOMES_B = ["Lucas", "Bruno", "Ana Paula", "Aline", "Felipe", "Vanessa", "Henrique", "Natália", "Vinícius", "Amanda", "Diego", "Carolina", "Leonardo", "Michele", "Alexandre", "Daniela"]
NOMES_TERCEIRO = ["Sérgio", "Gabriel", "Marcelo", "Renato", "Daniel", "André", "Mateus", "Vitor", "Fábio", "Leandro", "Jorge", "Márcio", "Flávio", "Paulo", "Cristiano", "Guilherme"]
CIDADES = ["São Paulo/SP", "Rio de Janeiro/RJ", "Belo Horizonte/MG", "Curitiba/PR", "Porto Alegre/RS", "Salvador/BA", "Recife/PE", "Brasília/DF", "Goiânia/GO", "Florianópolis/SC"]
VALORES = ["R$ 15.000,00", "R$ 45.000,00", "R$ 90.000,00", "R$ 180.000,00", "R$ 350.000,00", "R$ 600.000,00"]

def _rnd(lst: List[Any]) -> Any:
    return random.choice(lst)

def generate_question_offline(subject: str, bank: str = "FGV", difficulty: str = "Médio") -> Dict[str, Any]:
    """Gera proceduralmente questões de alto nível técnico sobre cada um dos 22 temas do questionário de Contratos"""
    if subject not in SUBJECTS:
        subject = _rnd(SUBJECTS)
    if bank not in BANKS:
        bank = _rnd(BANKS)
        
    p1 = _rnd(NOMES_A)
    p2 = _rnd(NOMES_B)
    terceiro = _rnd(NOMES_TERCEIRO)
    cidade = _rnd(CIDADES)
    valor = _rnd(VALORES)
    
    # 1. PLANOS DO NEGÓCIO JURÍDICO (ESCADA PONTEANA)
    if subject == "Planos do Negócio Jurídico (Escada Ponteana)":
        enunciado = (
            f"({bank}) {p1}, empresário em {cidade}, celebrou com {p2} um negócio jurídico no qual transferiu um imóvel de {valor}. "
            f"Posteriormente, verificou-se que {p1} era absolutamente incapaz por causa transitória na data da assinatura, embora o negócio "
            f"contivesse objeto material e declaração formal. À luz da Teoria Dualista de Pontes de Miranda (Escada Ponteana), "
            f"é correto afirmar que:"
        )
        opts = {
            "A": "O negócio jurídico é inexistente, visto que a incapacidade do agente impede a passagem pelo primeiro degrau da Escada Ponteana.",
            "B": "O negócio jurídico existe no mundo fático, mas padece de invalidade (nulidade absoluta) no plano da validade, requerendo declaração judicial.",
            "C": "O negócio jurídico é plenamente válido, operando no plano da eficácia mediante mera aposição de termo suspensivo.",
            "D": "A capacidade das partes integra o plano da existência, de modo que a falta de discernimento impede a produção de qualquer reflexo civil."
        }
        gabarito = "B"
        art = "Art. 104, I e Art. 166, I do Código Civil"
        basis = "No plano da existência constam os elementos essenciais: partes, manifestação de vontade, objeto e forma. No plano da validade esses elementos são qualificados: capacidade do agente, licitude do objeto e forma prescrita em lei."
        expl = "A capacidade é requisito adjetivo do Plano da Validade (Art. 104, I, CC). Um negócio firmado por incapaz existe no mundo fático, porém é inválido (nulo ou anulável). Não se confunde existência com validade."

    # 2. PRINCÍPIOS DO DIREITO CONTRATUAL
    elif subject == "Princípios do Direito Contratual":
        enunciado = (
            f"({bank}) {p1} e {p2}, duas sociedades empresárias em {cidade}, pactuaram contrato de fornecimento no valor de {valor}, "
            f"estipulando livremente a repartição dos riscos decorrentes de oscilações climáticas no frete. Diante de leve oscilação, {p1} "
            f"acionou o Poder Judiciário requerendo a revisão das cláusulas com base na função social do contrato. À luz do Art. 421 e 421-A do Código Civil, "
            f"assinale a afirmativa correta:"
        )
        opts = {
            "A": "O juiz deve intervir prontamente no contrato, haja vista que a função social autoriza a desconsideração da alocação privada de riscos em qualquer caso.",
            "B": "Os contratos civis e empresariais presumem-se paritários e simétricos, devendo prevalecer o princípio da intervenção mínima e a observância da alocação de riscos acordada pelas partes.",
            "C": "A função social do contrato revogou a autonomia privada e a força vinculante das convenções no direito brasileiro contemporâneo.",
            "D": "A presunção de vulnerabilidade se aplica automaticamente aos contratos entre sociedades empresárias, viabilizando a alteração equitativa do preço pelo juiz."
        }
        gabarito = "B"
        art = "Art. 421 e Art. 421-A do Código Civil"
        basis = "Nas relações contratuais privadas prevalecerão o princípio da intervenção mínima e a excepcionalidade da revisão contratual. Os contratos civis e empresariais presumem-se paritários e simétricos."
        expl = "A Lei da Liberdade Econômica introduziu o parágrafo único do art. 421 e o art. 421-A no Código Civil, prestigiando a paridade entre empresários e determinando o respeito estrito à alocação de riscos contratada."

    # 3. BOA-FÉ OBJETIVA E FIGURAS PARCELARES
    elif subject == "Boa-fé Objetiva e Figuras Parcelares":
        enunciado = (
            f"({bank}) Em contrato de locação firmado em {cidade}, o locador {p1} pactuou que o pagamento deveria ocorrer no dia 05 de cada mês. "
            f"Todavia, durante 4 anos consecutivos, {p1} aceitou sem ressalvas nem juros o pagamento realizado no dia 20 por {p2}. "
            f"De repente, {p1} notificou {p2} cobrando multa moratória retroativa de todos os meses anteriores. O comportamento de {p1} caracteriza violação da boa-fé objetiva por meio de:"
        )
        opts = {
            "A": "Supressio (perda da faculdade de cobrar a multa) correlata à Surrectio (direito de pagar dia 20), além de Venire Contra Factum Proprium (comportamento contraditório).",
            "B": "Exceptio Doli exclusivamente, permitindo ao credor cobrar a dívida com atualização monetária e juros compostos.",
            "C": "Tu Quoque absoluto, porquanto o locatário agiu com dolo manifestamente ilícito ao pagar no dia 20.",
            "D": "Exercício regular de direito estrito, já que a tolerância tácita nunca altera cláusula expressa de vencimento contratual."
        }
        gabarito = "A"
        art = "Art. 422 e Art. 330 do Código Civil"
        basis = "A boa-fé objetiva impõe lealdade e veda condutas contraditórias. A tolerância reiterada gera a perda de uma pretensão (supressio) e o nascimento de nova faculdade para o outro (surrectio)."
        expl = "Venire contra factum proprium proíbe o comportamento contraditório que quebra a legítima confiança gerada. Supressio é a perda do direito pelo não exercício continuado, enquanto surrectio é o surgimento correlato da faculdade para a outra parte."

    # 4. INTERPRETAÇÃO DOS CONTRATOS NO DIREITO BRASILEIRO
    elif subject == "Interpretação dos Contratos no Direito Brasileiro":
        enunciado = (
            f"({bank}) Na análise hermenêutica dos contratos e declarações de vontade no direito civil brasileiro, "
            f"considere as regras dispostas nos arts. 112, 113 e 114 do Código Civil. É correto afirmar que:"
        )
        opts = {
            "A": "Nas declarações de vontade se atenderá mais à intenção nelas consubstanciada do que ao sentido literal da linguagem, interpretando-se estritamente os negócios benéficos e a renúncia.",
            "B": "A interpretação gramatical e literal das palavras prevalece invariavelmente sobre a intenção comum manifestada pelas partes negociantes.",
            "C": "Os negócios jurídicos benéficos e os atos de renúncia admitem interpretação extensiva e analógica em favor do donatário ou beneficiário.",
            "D": "O comportamento das partes posterior à celebração do contrato não possui qualquer relevância para a fixação do sentido das cláusulas contratuais."
        }
        gabarito = "A"
        art = "Arts. 112, 113 e 114 do Código Civil"
        basis = "Art. 112: Prevalência da intenção sobre a literalidade. Art. 113, § 1º, I: Comportamento posterior serve como critério. Art. 114: Negócios benéficos e renúncia interpretam-se estritamente."
        expl = "O ordenamento brasileiro adota a teoria subjetiva mitigada: a vontade real prevalece sobre a literalidade estrita (art. 112) e os atos gratuitos/benéficos não podem ser estendidos além do texto expresso (art. 114)."

    # 5. CLASSIFICAÇÃO DOS CONTRATOS
    elif subject == "Classificação dos Contratos":
        enunciado = (
            f"({bank}) Quanto à classificação científica dos contratos no Direito Civil, assinale a opção correta a respeito da "
            f"distinção entre contratos consensuais e reais, e entre comutativos e aleatórios:"
        )
        opts = {
            "A": "Os contratos consensuais exigem a entrega efetiva da coisa para se aperfeiçoarem, ao passo que os reais bastam o consentimento mútuo.",
            "B": "Nos contratos comutativos as partes conhecem antecipadamente suas vantagens e prestações equivalentes, enquanto nos aleatórios há risco assumido (álea) quanto à existência ou quantidade do objeto.",
            "C": "A compra e venda é exemplo típico de contrato real e unilateral, enquanto o comodato é contrato bilateral e consensual.",
            "D": "O contrato de mútuo é negócio bilateral perfeito, comutativo e solene por escritura pública em todos os casos."
        }
        gabarito = "B"
        art = "Doutrina Contratual e Arts. 458 a 461 do Código Civil"
        basis = "Contratos consensuais perfazem-se pelo simples acordo de vontades; contratos reais exigem a tradição da coisa. Contratos comutativos possuem prestações certas; aleatórios envolvem álea/incerteza futura."
        expl = "No contrato comutativo, as prestações são certas e determinadas desde a celebração. No aleatório, pelo menos uma das prestações depende de fato incerto (sorte/álea)."

    # 6. ETAPAS DE FORMAÇÃO DO CONTRATO
    elif subject == "Etapas de Formação do Contrato":
        enunciado = (
            f"({bank}) {p1} enviou proposta formal de venda de um veículo a {p2}, residente em outra comarca, concedendo prazo de 10 dias para resposta. "
            f"No 3º dia, {p1} enviou mensagem retratando-se da proposta, mas a retratação chegou a {p2} dois dias DEPOIS de {p2} já ter expedido sua aceitação formal. "
            f"Diante das regras de formação dos contratos entre ausentes (arts. 427 e 434 do CC):"
        )
        opts = {
            "A": "O contrato não se formou, pois o proponente goza do direito potestativo de desistir até que receba fisicamente a carta de aceitação.",
            "B": "O contrato reputa-se concluído no momento em que a aceitação foi expedida por {p2}, pois a retratação não chegou antes ou simultaneamente com a proposta ou aceitação.",
            "C": "O contrato é nulo de pleno direito, pois a teoria da recepção vigora de modo absoluto e irrestrito no direito civil brasileiro.",
            "D": "A proposta não possuía eficácia vinculante, de sorte que a retratação do proponente surte efeitos a qualquer momento antes do pagamento."
        }
        gabarito = "B"
        art = "Art. 427, Art. 428, IV e Art. 434 do Código Civil"
        basis = "Os contratos entre ausentes tornam-se perfeitos desde que a aceitação é expedida (Teoria da Expedição), salvo se antes ou com a aceitação chegar a retratação do aceitante."
        expl = "O Código Civil adota a Teoria da Expedição (art. 434). A proposta vincula o proponente (art. 427) e a aceitação expedida conclui o negócio, tornando ineficaz a revogação tardia."

    # 7. ESTIPULAÇÃO EM FAVOR DE TERCEIRO
    elif subject == "Estipulação em Favor de Terceiro":
        enunciado = (
            f"({bank}) {p1} (estipulante) celebrou contrato com {p2} (promitente), no qual este se obrigou a prestar consultoria técnica gratuita a {terceiro} (beneficiário/terceiro). "
            f"No instrumento, não foi conferida autorização para {p1} exonerar o devedor unilateralmente. "
            f"Sobre a Estipulação em Favor de Terceiro (arts. 436 a 438 do Código Civil), é correto afirmar:"
        )
        opts = {
            "A": "Apenas o estipulante pode exigir o cumprimento da obrigação, sendo vedado ao terceiro beneficiário acionar judicialmente o promitente.",
            "B": "Tanto o estipulante quanto o terceiro beneficiário têm legitimidade para exigir o cumprimento da prestação; e se ao terceiro foi dado o direito de reclamar a execução, o estipulante não pode exonerar o devedor.",
            "C": "O terceiro beneficiário torna-se pessoalmente responsável pelas dívidas e contraprestações originárias assumidas pelo estipulante.",
            "D": "A substituição do terceiro beneficiário depende obrigatoriamente do consentimento expresso do promitente contratado."
        }
        gabarito = "B"
        art = "Art. 436 e Art. 437 do Código Civil"
        basis = "Art. 436: O estipulante e o terceiro podem exigir a obrigação. Art. 437: Se ao terceiro for deixado o direito de reclamar a execução, o estipulante não pode exonerar o devedor."
        expl = "O art. 436 autoriza tanto o estipulante quanto o beneficiário a exigirem a prestação. O art. 437 impede o estipulante de perdoar ou exonerar a dívida se ao terceiro foi deferido o poder de cobrança direta."

    # 8. PROMESSA DE FATO DE TERCEIRO
    elif subject == "Promessa de Fato de Terceiro":
        enunciado = (
            f"({bank}) {p1}, renomado agente musical em {cidade}, contratou com {p2} que o consagrado cantor {terceiro} realizaria um show no casamento de {p2} pelo cachê de {valor}. "
            f"Contudo, chegado o dia do evento, {terceiro} recusou-se a comparecer, afirmando que sequer tinha conhecimento da negociação. "
            f"Nos termos do Art. 439 do Código Civil:"
        )
        opts = {
            "A": "{p2} deve ajuizar ação de obrigação de fazer diretamente contra {terceiro}, compelindo-o judicialmente a cantar.",
            "B": "{p1} responderá por perdas e danos perante {p2}, pois aquele que tiver prometido fato de terceiro responde patrimonialmente quando este não o executar.",
            "C": "O contrato é nulo por vício insanável de objeto impossível, restando as partes desobrigadas sem qualquer dever indenizatório.",
            "D": "{p1} fica exonerado de qualquer responsabilidade civil desde que comprove que agiu de boa-fé e enviou mensagens ao terceiro."
        }
        gabarito = "B"
        art = "Art. 439 do Código Civil"
        basis = "Aquele que tiver prometido fato de terceiro responderá por perdas e danos, quando este o não executar (Art. 439, CC)."
        expl = "Quem promete fato de terceiro assume obrigação de resultado. Se o terceiro não anui e não cumpre, quem prometeu responde pessoal e integralmente por perdas e danos."

    # 9. CONTRATOS ALEATÓRIOS - CONCEITO E ESPÉCIES
    elif subject == "Contratos Aleatórios - Conceito e Espécies":
        enunciado = (
            f"({bank}) Sobre os contratos aleatórios no Direito Civil brasileiro, no que concerne à distinção entre contratos "
            f"aleatórios por natureza e contratos acidentalmente aleatórios, assinale a opção correta:"
        )
        opts = {
            "A": "Os contratos de seguro e de jogo/aposta são exemplos de contratos acidentalmente aleatórios, ao passo que a compra e venda de safra é aleatória por natureza.",
            "B": "Nos contratos aleatórios por natureza, a incerteza é elemento intrínseco da espécie negocial; nos acidentalmente aleatórios, um contrato tipicamente comutativo passa a envolver risco por estipulação expressa das partes.",
            "C": "Qualquer contrato civil pode ser considerado aleatório por presunção legal, dispensando-se manifestação de vontade expressa das partes nesse sentido.",
            "D": "O Código Civil proíbe a pactuação de contratos comutativos que envolvam álea sobre a existência ou quantidade de bens futuros."
        }
        gabarito = "B"
        art = "Arts. 458 a 461 do Código Civil e Doutrina Contratual"
        basis = "O contrato aleatório por natureza traz o risco em sua própria estrutura típica (seguro). O acidentalmente aleatório é negócio originalmente comutativo (venda) que assume risco por cláusula volitiva."
        expl = "A compra e venda é originalmente comutativa. Quando as partes acordam que o comprador assume o risco da existência (emptio spei) ou da quantidade (emptio rei speratae), ela torna-se acidentalmente aleatória."

    # 10. CONTRATO ALEATÓRIO: EMPTIO SPEI
    elif subject == "Contrato Aleatório: Emptio Spei":
        enunciado = (
            f"({bank}) {p1} comprou de {p2}, por {valor} pago à vista, todo o produto que viesse a ser apanhado em um único lance de rede de pesca "
            f"no mar de {cidade}. As partes acordaram expressamente que o adquirente assumiria o risco integral da existência da coisa futura (Emptio Spei). "
            f"{p2} lançou a rede com a devida técnica, mas nenhum peixe foi capturado. À luz do Art. 458 do Código Civil:"
        )
        opts = {
            "A": "{p2} é obrigado a devolver o valor integral recebido, pois a inexistência total do objeto acarreta a nulidade absoluta da compra e venda.",
            "B": "{p2} tem direito de reter integralmente o preço recebido, desde que de sua parte não tenha havido dolo ou culpa, ainda que nada venha a existir.",
            "C": "O valor pago deve ser dividido em partes iguais entre as partes, aplicando-se a teoria da base objetiva do negócio.",
            "D": "O contrato converte-se automaticamente em doação com encargo, incidindo perdas e danos compensatórios contra {p2}."
        }
        gabarito = "B"
        art = "Art. 458 do Código Civil"
        basis = "Se o contrato for aleatório por dizer respeito a coisas futuras cujo risco de não virem a existir o adquirente assuma (emptio spei), o alienante terá direito a todo o preço, se não agiu com dolo ou culpa, ainda que nada venha a existir."
        expl = "Na Emptio Spei (venda da esperança), o comprador assume o risco de tudo ou nada. Se nada vier a existir por circunstâncias naturais e sem culpa do vendedor, o preço é devido integralmente."

    # 11. CONTRATO ALEATÓRIO: EMPTIO REI SPERATAE
    elif subject == "Contrato Aleatório: Emptio Rei Speratae":
        enunciado = (
            f"({bank}) {p1} celebrou contrato aleatório de compra e venda de safra de café com o agricultor {p2}, tomando para si o risco de as coisas futuras "
            f"virem a existir em qualquer quantidade (Emptio Rei Speratae), pelo valor fixado de {valor}. Em virtude de geada imprevisível, sem culpa de {p2}, "
            f"a colheita rendeu ZERO sacas de café (nada veio a existir). Consoante o Art. 459, parágrafo único, do Código Civil:"
        )
        opts = {
            "A": "{p1} continua obrigado a pagar todo o preço, tendo em vista que assumiu integralmente a álea contratual na modalidade emptio spei.",
            "B": "Alienação não haverá, e o alienante {p2} restituirá o preço recebido, pois na emptio rei speratae exige-se que ao menos alguma quantidade venha a existir.",
            "C": "O contrato é rescindido com condenação de {p2} em perdas e danos equivalentes ao dobro do valor do contrato.",
            "D": "O alienante tem direito a 50% do valor ajustado a título de remuneração pelo trabalho agrícola desempenhado."
        }
        gabarito = "B"
        art = "Art. 459, parágrafo único do Código Civil"
        basis = "Art. 459. Parágrafo único: Mas, se da coisa nada vier a existir, alienação não haverá, e o alienante restituirá o preço recebido."
        expl = "Na Emptio Rei Speratae o risco é da quantidade, não da existência. Deve vir ao menos uma unidade mínima. Se nada existir (quantidade zero), o contrato desfaz-se e o valor deve ser devolvido ao comprador."

    # 12. CONTRATO ALEATÓRIO: COISAS EXISTENTES EXPOSTAS A RISCO
    elif subject == "Contrato Aleatório: Coisas Existentes Expostas a Risco":
        enunciado = (
            f"({bank}) {p1} adquiriu de {p2} um lote de mercadorias no valor de {valor}, ciente de que a carga se encontrava em trânsito marítimo "
            f"em área de tempestade violenta, assumindo contratualmente o risco de perda ou deterioração da coisa existente. "
            f"Constatou-se depois que a carga já havia naufragado antes da assinatura do contrato. Nos termos dos arts. 460 e 461 do Código Civil:"
        )
        opts = {
            "A": "O alienante tem direito a todo o preço se agiu de boa-fé; contudo, a alienação pode ser anulada pelo adquirente se provar que o alienante não ignorava a consumação do sinistro.",
            "B": "A venda de coisa exposta a risco pretérito é nula ipso facto, independentemente da boa ou má-fé dos contratantes.",
            "C": "O adquirente nunca poderá anular o contrato, pois a assunção de risco transfere responsabilidade absoluta e irretratável.",
            "D": "O alienante só terá direito ao preço caso a mercadoria resgatada mantenha seu valor originário integral sem nenhuma depreciação."
        }
        gabarito = "A"
        art = "Arts. 460 e 461 do Código Civil"
        basis = "Art. 460 autoriza o alienante a receber o preço de coisa exposta a risco mesmo que ela já não existisse; Art. 461 dispõe que a alienação pode ser anulada como dolosa se o alienante sabia do sinistro."
        expl = "A validade dessa modalidade aleatória apoia-se na boa-fé subjetiva: se o alienante sabia que a carga já havia afundado e ocultou o fato, o contrato é anulável por dolo."

    # 13. CONTRATO PRELIMINAR / PROMESSA DE CONTRATAR
    elif subject == "Contrato Preliminar / Promessa de Contratar":
        enunciado = (
            f"({bank}) {p1} e {p2} celebraram por instrumento particular um contrato preliminar de promessa de compra e venda de um imóvel "
            f"residencial em {cidade}, no valor de {valor}, estipulando todas as cláusulas essenciais, preço e forma de pagamento, sem cláusula de arrependimento. "
            f"No momento da outorga da escritura, {p1} recusou-se a assinar o contrato definitivo. Com base nos arts. 462 a 464 do Código Civil:"
        )
        opts = {
            "A": "O contrato preliminar é nulo de pleno direito no plano da validade, pois a promessa de compra e venda imobiliária atrai obrigatoriamente a forma solene pública da escritura do art. 108 do Código Civil.",
            "B": "O contrato preliminar é plenamente válido, pois, exceto quanto à forma, deve conter os requisitos essenciais do definitivo; {p2} pode exigir a celebração do definitivo ou obter sentença com efeito de adjudicação compulsória.",
            "C": "{p2} tem direito exclusivamente a exigir perdas e danos compensatórios pelo inadimplemento, sendo defeso ao juiz proferir decisão judicial com efeito substitutivo da manifestação de vontade recusada.",
            "D": "O contrato preliminar é ineficaz entre as partes signatárias enquanto não for averbado junto à matrícula do Registro Imobiliário competente para fins de publicidade e oponibilidade erga omnes."
        }
        gabarito = "B"
        art = "Arts. 462, 463 e 464 do Código Civil"
        basis = "Art. 462: O contrato preliminar, exceto quanto à forma, deve conter todos os requisitos essenciais ao contrato a ser celebrado. Art. 464: O juiz pode conferir caráter definitivo ao contrato preliminar não cumprido."
        expl = "A forma pública não é requisito do pré-contrato imobiliário (princípio da atração mitigada). Não havendo cláusula de arrependimento, o adquirente pode ingressar com adjudicação compulsória."

    # 14. CONTRATO COM PESSOA A DECLARAR
    elif subject == "Contrato com Pessoa a Declarar":
        enunciado = (
            f"({bank}) {p1}, atuando como intermediário, celebrou contrato de compra e venda de imóvel com {p2} em {cidade}, reservando-se a faculdade "
            f"de indicar a pessoa que adquiriria os direitos e assumiria as obrigações dele decorrentes (cláusula 'pro amico'). "
            f"Não havendo estipulação contratual expressa sobre prazo, a indicação da pessoa (electio amici) deve ser comunicada à outra parte no prazo de:"
        )
        opts = {
            "A": "5 (cinco) dias da data da conclusão do negócio, devendo a aceitação da pessoa nomeada revestir rigorosamente a mesma forma solene que foi empregada para a celebração do contrato preliminar.",
            "B": "15 (quinze) dias da imissão provisória na posse do bem, mediante expedição obrigatória de notificação premonitória judicial ou extrajudicial para a ratificação expressa das partes contratantes.",
            "C": "30 (trinta) dias úteis a contar do pagamento da primeira parcela ajustada, operando a indicação efeitos estritamente prospectivos (ex nunc) a partir da lavratura da escritura pública definitiva.",
            "D": "1 (um) ano contado da celebração da avença, sob pena de extinção peremptória do direito potestativo de nomeação e conversão compulsória do estipulante em mandatário com poderes especiais."
        }
        gabarito = "A"
        art = "Art. 468 do Código Civil"
        basis = "Essa indicação deve ser comunicada à outra parte no prazo de cinco dias da conclusão do contrato, se outro não tiver sido estipulado pelos contraentes (Art. 468, caput, CC)."
        expl = "O prazo legal supletivo do art. 468 é de 5 dias. A aceitação do nomeado deve observar a mesma forma utilizada no contrato celebrado."

    # 15. CONTRATO COM PESSOA A DECLARAR VS. OUTROS CONTRATOS
    elif subject == "Contrato com Pessoa a Declarar vs. Outros Contratos":
        enunciado = (
            f"({bank}) No estudo comparativo das figuras contratuais que envolvem intervenção de terceiros, "
            f"o Contrato com Pessoa a Declarar distingue-se do Mandato e da Estipulação em Favor de Terceiro porque:"
        )
        opts = {
            "A": "No Contrato com Pessoa a Declarar, o estipulante contrata em nome próprio e permanece vinculado se a indicação for ineficaz, passando o terceiro nomeado a assumir a posição de contratante retroativamente.",
            "B": "Na Estipulação em Favor de Terceiro, o terceiro beneficiário assume automaticamente a posição passiva de devedor solidário de todos os encargos e despesas decorrentes da execução continuada do contrato.",
            "C": "No Mandato, o mandatário age sempre em nome próprio e por sua conta e risco perante terceiros, assumindo pessoalmente a garantia integral contra a insolvência e o inadimplemento culposo do mandante.",
            "D": "O Contrato com Pessoa a Declarar consubstancia cessão ordinária de posição contratual que opera efeitos prospectivos (ex nunc), prescindindo de expressa anuência ou homologação do contratante originário."
        }
        gabarito = "A"
        art = "Arts. 467 a 471 e Art. 436 do Código Civil"
        basis = "No contrato com pessoa a declarar a parte age em nome próprio com faculdade de substituição ex tunc. Na estipulação o terceiro apenas aufere benefício creditício."
        expl = "Se a pessoa a declarar não aceitar a nomeação ou for insolvente, o contrato produz efeitos unicamente entre os signatários originários (art. 470, CC), demonstrando que o estipulante não é mero mandatário."

    # 16. VÍCIOS REDIBITÓRIOS - CONCEITO E REQUISITOS
    elif subject == "Vícios Redibitórios - Conceito e Requisitos":
        enunciado = (
            f"({bank}) {p1} adquiriu de {p2}, mediante contrato comutativo e oneroso de compra e venda pelo valor de {valor}, uma máquina industrial seminova. "
            f"Após a entrega, constatou que a máquina apresentava defeito interno no motor, oculto e preexistente à tradição, que a tornava imprestável "
            f"para o funcionamento fabril a que se destinava. Sobre a configuração do vício redibitório (art. 441 do CC), assinale a correta:"
        )
        opts = {
            "A": "O vício redibitório exige que o contrato seja oneroso e comutativo (ou doação onerosa), que o defeito seja grave, oculto e preexistente à entrega da coisa, sendo ignorado pelo comprador.",
            "B": "A responsabilidade por vícios redibitórios subsiste mesmo nas doações puras e desprovidas de encargo, em virtude da solidariedade social.",
            "C": "Se o defeito era ostensivo e facilmente perceptível por simples inspeção visual ordinária na data do negócio, ainda assim configura vício redibitório.",
            "D": "A responsabilidade do alienante por vício redibitório depende necessariamente da demonstração de sua culpa ou má-fé subjetiva."
        }
        gabarito = "A"
        art = "Art. 441 do Código Civil"
        basis = "Art. 441: A coisa recebida em virtude de contrato comutativo pode ser enjeitada por vícios ou defeitos ocultos, que a tornem imprópria ao uso a que é destinada, ou lhe diminuam o valor."
        expl = "São requisitos: contrato comutativo oneroso (ou doação onerosa), vício oculto, gravidade do defeito e preexistência à tradição. Não se exige prova de culpa do alienante para o desfazimento do negócio."

    # 17. EFEITOS DA BOA-FÉ E MÁ-FÉ DO ALIENANTE NO VÍCIO
    elif subject == "Efeitos da Boa-fé e Má-fé do Alienante no Vício":
        enunciado = (
            f"({bank}) Em matéria de responsabilidade por vícios redibitórios, a ciência prévia do defeito por parte do alienante "
            f"produz reflexos diretos na extensão de sua responsabilidade jurídica. Conforme prevê expressamente o Art. 443 do Código Civil:"
        )
        opts = {
            "A": "A boa-fé do alienante isenta-o totalmente de qualquer responsabilidade patrimonial, impedindo a rescisão do contrato ou a devolução de qualquer valor.",
            "B": "Se o alienante conhecia o vício da coisa (má-fé), restituirá o que recebeu acrescido de perdas e danos; se não o conhecia (boa-fé), restituirá o valor recebido com as despesas do contrato, sem perdas e danos.",
            "C": "O alienante de má-fé responde apenas criminalmente por estelionato, não respondendo por perdas e danos na esfera civil contratual.",
            "D": "O alienante de boa-fé é obrigado a indenizar lucros cessantes e danos morais punitivos em favor do adquirente prejudicado."
        }
        gabarito = "B"
        art = "Art. 443 do Código Civil"
        basis = "Art. 443. Se o alienante conhecia o vício ou defeito da coisa, restituirá o que recebeu com perdas e danos; se o não conhecia, tão-somente restituirá o valor recebido, mais as despesas do contrato."
        expl = "A garantia por vício redibitório é objetiva (independe de culpa). Porém, a má-fé acarreta o dever adicional de indenizar perdas e danos integrais."

    # 18. AÇÕES EDILÍCIAS (REDIBITÓRIA E ESTIMATÓRIA/QUANTI MINORIS)
    elif subject == "Ações Edilícias (Redibitória e Estimatória/Quanti Minoris)":
        enunciado = (
            f"({bank}) Constatado o vício redibitório oculto e grave na coisa recebida em contrato de compra e venda comutativo, "
            f"o adquirente pode valer-se das ações edilícias (arts. 441 e 442 do CC). Sobre essas ações, assinale a opção correta:"
        )
        opts = {
            "A": "O adquirente tem o direito potestativo de optar entre a Ação Redibitória (para enjeitar a coisa e rescindir o contrato) e a Ação Estimatória (para obter abatimento proporcional no preço ajustado).",
            "B": "Cabe privativamente ao alienante a faculdade discricionária de escolher entre restituir o preço ou autorizar o abatimento proporcional do valor, visando privilegiar a conservação do negócio jurídico.",
            "C": "O adquirente pode cumular a Ação Redibitória de devolução com a Ação Quanti Minoris de abatimento sobre o mesmo bem, pleiteando concomitantemente a resolução integral e a manutenção do contrato.",
            "D": "A Ação Redibitória restringe-se à imposição de obrigação de fazer consistente no conserto ou substituição das peças viciadas no prazo judicial cominatório de até trinta dias úteis."
        }
        gabarito = "A"
        art = "Arts. 441 e 442 do Código Civil"
        basis = "Art. 442: Em vez de rejeitar a coisa, redibindo o contrato (art. 441), pode o adquirente reclamar abatimento no preço."
        expl = "As ações edilícias são disjuntivas (alternativas à escolha do adquirente): ou ele rejeita a coisa rescindindo o contrato (redibitória), ou conserva a coisa pedindo abatimento do preço (quanti minoris/estimatória)."

    # 19. VÍCIO REDIBITÓRIO VS. ENTREGA DE COISA DIVERSA (ALIUD PRO ALIO)
    elif subject == "Vício Redibitório vs. Entrega de Coisa Diversa (Aliud Pro Alio)":
        enunciado = (
            f"({bank}) {p1} comprou de {p2} um lote de café em grãos arábica tipo exportação, mas recebeu no depósito sacas contendo cevada torrada. "
            f"Em outro caso, {terceiro} comprou um touro reprodutor que veio exatamente o animal identificado, mas estéril (defeito interno). "
            f"Sobre a distinção entre Vício Redibitório e Entrega de Coisa Diversa ('Aliud pro alio'), é correto afirmar:"
        )
        opts = {
            "A": "Ambos os casos configuram vícios redibitórios intrínsecos típicos da coisa recebida, sujeitando-se com rigor aos exíguos prazos decadenciais previstos no art. 445 do Código Civil brasileiro.",
            "B": "A entrega de coisa diversa (aliud pro alio) consubstancia inadimplemento com prazos prescricionais gerais, ao passo que o vício redibitório é defeito oculto na própria coisa contratada e entregue.",
            "C": "A entrega de cevada por café caracteriza vício redibitório oculto na mercadoria, aplicando-se o prazo prescricional trienal de reparação civil regulado no art. 206, § 3º, V, do Código Civil.",
            "D": "A esterilidade do touro reprodutor configura entrega de coisa diversa (aliud pro alio), retirando do adquirente a possibilidade de pleitear a resolução ou o abatimento de preço por ação edilícia."
        }
        gabarito = "B"
        art = "Arts. 389, 441 e 475 do Código Civil e Doutrina"
        basis = "Aliud pro alio é o inadimplemento absoluto da obrigação de dar (entrega de coisa distinta). Vício redibitório é vício intrínseco na própria coisa contratada e entregue."
        expl = "No aliud pro alio há violação substancial da identidade da prestação (entregar uma coisa por outra), aplicando-se as regras do inadimplemento e prescrição geral. No vício redibitório, a coisa é a contratada, mas porta defeito oculto funcional."

    # 20. PRAZOS DECADENCIAIS DOS VÍCIOS REDIBITÓRIOS
    elif subject == "Prazos Decadenciais dos Vícios Redibitórios":
        enunciado = (
            f"({bank}) {p1} comprou um imóvel residencial de {p2} em {cidade}, tendo recebido as chaves no dia 10 de janeiro. "
            f"Seis meses depois, surgiu grave vício oculto estrutural de fundação que, por sua natureza, só podia ser conhecido com o período de chuvas. "
            f"De acordo com o Art. 445 do Código Civil, o prazo para {p1} ajuizar ação edilícia:"
        )
        opts = {
            "A": "O prazo é de natureza prescricional e decenal, fundado na responsabilidade civil genérica por inadimplemento culposo, contando-se a partir da imissão do adquirente na posse efetiva do bem imóvel.",
            "B": "O prazo é decadencial de trinta dias úteis a contar da tradição originária das chaves, sendo peremptório e insuscetível de dilação mesmo diante de defeito oculto de conhecimento tardio.",
            "C": "O prazo é decadencial de 1 ano contado da ciência do defeito, respeitado o prazo máximo de garantia legal de até 1 ano da posse para que o vício oculto por sua natureza venha a se manifestar.",
            "D": "O prazo é decadencial de cinco anos contados da expedição do habite-se municipal, aplicando-se o regime da garantia legal contra defeitos de solidez e segurança previstos para a empreitada."
        }
        gabarito = "C"
        art = "Art. 445 e seu § 1º do Código Civil"
        basis = "Art. 445. O adquirente decai do direito de obter a redibição ou abatimento no preço no prazo de 30 dias (móvel) e 1 ano (imóvel). § 1º Quando o vício só puder ser conhecido mais tarde, o prazo conta-se da ciência até o máximo de 180 dias (móveis) e 1 ano (imóveis)."
        expl = "Trata-se de prazo decadencial. Para imóveis, a regra geral é 1 ano da entrega; se o vício é oculto por sua natureza, o prazo de 1 ano corre da ciência, contanto que o vício se revele no prazo máximo de 1 ano."

    # 21. EXTINÇÃO DOS CONTRATOS - RESOLUÇÃO E CLÁUSULA RESOLUTIVA
    elif subject == "Extinção dos Contratos - Resolução e Cláusula Resolutiva":
        enunciado = (
            f"({bank}) Em contrato de prestação de serviços celebrado em {cidade}, foi inserida cláusula prevendo que 'o inadimplemento "
            f"de qualquer parcela acarretará a rescisão imediata e automática do contrato, independentemente de notificação'. "
            f"Conforme o Art. 474 do Código Civil, a respeito das cláusulas resolutivas expressa e tácita:"
        )
        opts = {
            "A": "A cláusula resolutiva expressa opera de pleno direito; a tácita depende de interpelação judicial.",
            "B": "A cláusula resolutiva expressa é ilícita e abusiva nas relações civis, dependendo sempre de prévia autorização judicial.",
            "C": "A cláusula resolutiva tácita opera automaticamente, dispensando interpelação judicial para constituir o devedor em mora.",
            "D": "Ambas as cláusulas necessitam obrigatoriamente de ação judicial com trânsito em julgado para dissolver o vínculo contratual."
        }
        gabarito = "A"
        art = "Art. 474 do Código Civil"
        basis = "Art. 474. A cláusula resolutiva expressa opera de pleno direito; a tácita depende de interpelação judicial."
        expl = "A cláusula resolutiva expressa opera de pleno direito com o inadimplemento. A tácita é inerente aos contratos bilaterais (art. 475), mas exige interpelação judicial prévia."

    # 22. EXCEÇÃO DO CONTRATO NÃO CUMPRIDO E ONEROSIDADE EXCESSIVA
    else:
        enunciado = (
            f"({bank}) {p1} e {p2} celebraram contrato bilateral no qual {p1} deveria entregar equipamentos no valor de {valor} "
            f"e {p2} deveria pagar o preço no ato da entrega. {p1} não entregou os equipamentos, mas ajuizou ação de cobrança contra {p2}. "
            f"Na sua defesa, {p2} invocou a 'Exceptio Non Adimpleti Contractus' (Art. 476 do Código Civil). Assinale a opção correta:"
        )
        opts = {
            "A": "A exceção do contrato não cumprido é defesa de direito material legítima: nos contratos bilaterais, nenhum dos contratantes, antes de cumprida a sua obrigação, pode exigir o implemento da do outro.",
            "B": "A exceção do contrato não cumprido só pode ser arguida em contratos unilaterais gratuitos, não sendo aplicável aos contratos bilaterais onerosos.",
            "C": "O juiz deve condenar {p2} ao pagamento compulsório imediato, devendo {p2} ajuizar ação autônoma posterior para cobrar a entrega dos bens.",
            "D": "A exceptio non adimpleti contractus acarreta a nulidade absoluta e originária do contrato com efeitos ex tunc."
        }
        gabarito = "A"
        art = "Art. 476 do Código Civil"
        basis = "Art. 476. Nos contratos bilaterais, nenhum dos contratantes, antes de cumprida a sua obrigação, pode exigir o implemento da do outro."
        expl = "A exceção do contrato não cumprido decorre da interdependência e reciprocidade das prestações no contrato sinalagmático. Quem não adimpliu não pode cobrar a prestação alheia."

    # Embaralha alternativas mantendo consistência do gabarito
    keys = ["A", "B", "C", "D"]
    correct_text = opts[gabarito]
    other_texts = [opts[k] for k in keys if k != gabarito]
    random.shuffle(other_texts)
    
    new_correct_key = _rnd(keys)
    new_options = {}
    other_idx = 0
    for k in keys:
        if k == new_correct_key:
            new_options[k] = correct_text
        else:
            new_options[k] = other_texts[other_idx]
            other_idx += 1
            
    return {
        "id": f"q_off_{uuid.uuid4().hex[:12]}",
        "subject": subject,
        "bank": bank,
        "difficulty": difficulty,
        "enunciado": enunciado,
        "options": new_options,
        "gabarito": new_correct_key,
        "article": art,
        "legal_basis": basis,
        "explanation": expl
    }
