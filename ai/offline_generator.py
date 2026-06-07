import random
import uuid

# Os 23 assuntos obrigatórios baseados nos artigos 304 a 420 do Código Civil
SUBJECTS = [
    "Pagamento - Geral",
    "Quem deve pagar",
    "A quem se deve pagar",
    "Objeto do pagamento e sua prova",
    "Lugar do pagamento",
    "Tempo do pagamento",
    "Consignação em pagamento",
    "Pagamento com sub-rogação",
    "Imputação do pagamento",
    "Dação em pagamento",
    "Novação",
    "Compensação",
    "Confusão",
    "Remissão das dívidas",
    "Inadimplemento - Disposições gerais",
    "Mora - Geral",
    "Mora do devedor",
    "Mora do credor",
    "Inadimplemento absoluto",
    "Perdas e danos",
    "Juros legais",
    "Cláusula penal",
    "Arras ou sinal"
]

BANKS = ["FGV", "OAB", "CESPE", "FCC", "VUNESP", "AOCP", "FMP", "Consulplan"]

NOMES_DEVEDOR = ["João", "Pedro", "Marcos", "Rafael", "Rodrigo", "Gustavo", "Thiago", "Fabiano", "Felipe", "Alexandre", "Henrique", "Vinícius", "Eduardo", "Ricardo", "Murilo", "Diego", "Leonardo", "César", "Alberto", "Fernando"]
NOMES_CREDOR = ["Ana", "Fernanda", "Maria", "Juliana", "Patrícia", "Camila", "Beatriz", "Letícia", "Larissa", "Carolina", "Amanda", "Vanessa", "Natália", "Cristina", "Raquel", "Daniela", "Priscila", "Michele", "Aline", "Gabriela"]
NOMES_TERCEIRO = ["Lucas", "Bruno", "Carlos", "Roberto", "Daniel", "André", "Mateus", "Gabriel", "Vitor", "Fábio", "Marcelo", "Renato", "Leandro", "Sérgio", "Jorge", "Márcio", "Flávio", "Paulo", "Sérgio", "Cristiano"]

PROFISSOES = ["Advogado", "Médico", "Empresário", "Contador", "Engenheiro", "Dentista", "Comerciante", "Arquiteto", "Veterinário", "Professor", "Bancário", "Corretor", "Administrador", "Economista", "Consultor", "Despachante", "Tabelião", "Juiz aposentado", "Empresário rural", "Microempresário"]
CONTRATOS = [
    "compra e venda de um veículo seminovo",
    "locação de um galpão comercial",
    "prestação de serviços de consultoria em TI",
    "financiamento de maquinário industrial",
    "empréstimo de insumos agrícolas",
    "fornecimento de mercadorias para revenda",
    "promessa de compra e venda de imóvel residencial",
    "prestação de serviços advocatícios",
    "contrato de empreitada para reforma",
    "compromisso de cessão de direitos creditórios",
    "mútuo bancário para capital de giro",
    "arrendamento mercantil de equipamentos",
    "contrato de franquia empresarial",
    "prestação de serviços médicos hospitalares",
    "transporte de cargas interestadual",
]
CIDADES = ["São Paulo/SP", "Rio de Janeiro/RJ", "Belo Horizonte/MG", "Curitiba/PR", "Porto Alegre/RS", "Salvador/BA", "Recife/PE", "Fortaleza/CE", "Brasília/DF", "Florianópolis/SC", "Manaus/AM", "Goiânia/GO", "Vitória/ES", "Natal/RN", "Campo Grande/MS", "Cuiabá/MT", "João Pessoa/PB", "Maceió/AL", "São Luís/MA", "Teresina/PI"]
VALORES = ["R$ 10.000,00", "R$ 25.000,00", "R$ 50.000,00", "R$ 120.000,00", "R$ 200.000,00", "R$ 5.000,00", "R$ 8.500,00", "R$ 15.000,00", "R$ 35.000,00", "R$ 75.000,00", "R$ 150.000,00", "R$ 300.000,00", "R$ 3.200,00", "R$ 42.000,00", "R$ 87.500,00"]

def get_random_vars():
    return {
        "devedor": random.choice(NOMES_DEVEDOR),
        "credor": random.choice(NOMES_CREDOR),
        "terceiro": random.choice(NOMES_TERCEIRO),
        "prof_dev": random.choice(PROFISSOES),
        "prof_cred": random.choice(PROFISSOES),
        "prof_terc": random.choice(PROFISSOES),
        "contrato": random.choice(CONTRATOS),
        "cidade": random.choice(CIDADES),
        "valor": random.choice(VALORES),
    }

def generate_question_offline(subject: str = None, bank: str = None) -> dict:
    if not subject or subject not in SUBJECTS:
        subject = random.choice(SUBJECTS)
    if not bank or bank not in BANKS:
        bank = random.choice(BANKS)
        
    v = get_random_vars()
    q_id = str(uuid.uuid4())
    difficulty = random.choice(["Fácil", "Médio", "Difícil"])
    variant = random.randint(0, 1)  # 0 = template original, 1 = variação
    
    # Se a banca for CESPE, geramos no formato Certo/Errado
    is_cespe = (bank == "CESPE")
    
    # Dicionário que guardará os dados finais
    question_data = {
        "id": q_id,
        "subject": subject,
        "bank": bank,
        "difficulty": difficulty,
        "enunciado": "",
        "options": {},
        "gabarito": "",
        "article": "",
        "legal_basis": "",
        "explanation": ""
    }
    
    # -------------------------------------------------------------
    # 1. PAGAMENTO - GERAL (Arts. 304 - 420 - visão geral)
    # -------------------------------------------------------------
    if subject == "Pagamento - Geral":
        question_data["article"] = "Art. 304 e Art. 313 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) Considera-se pagamento, no contexto do Direito das Obrigações, a entrega voluntária da prestação devida pelo devedor "
                f"ao credor, podendo ser realizado por terceiro interessado ou não interessado, desde que observados os requisitos de validade do negócio jurídico."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "A"
            question_data["legal_basis"] = "Arts. 304 e 313 do Código Civil."
            question_data["explanation"] = (
                f"O pagamento é o adimplemento voluntário da obrigação. Qualquer interessado pode pagar (art. 304), e terceiro não interessado também "
                f"pode pagar em nome do devedor (art. 305). O credor não é obrigado a receber prestação diversa (art. 313). Portanto, a afirmação está CERTA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} ({v['prof_dev']}) contraiu obrigação de pagar {v['valor']} a {v['credor']} ({v['prof_cred']}) "
                    f"decorrente de {v['contrato']}. Considerando as disposições gerais sobre pagamento no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"O pagamento deve ser necessariamente realizado pelo próprio devedor {v['devedor']}, sendo vedado o adimplemento por terceiros, ainda que interessados.",
                    "B": f"O credor {v['credor']} é obrigado a aceitar prestação diversa da que lhe é devida, desde que a prestação alternativa seja mais valiosa que a original.",
                    "C": f"O pagamento feito por terceiro juridicamente interessado, como o fiador, extingue a obrigação e opera a sub-rogação legal nos direitos do credor.",
                    "D": f"O pagamento em dinheiro deve ser feito em moeda estrangeira sempre que houver cláusula de escala móvel pactuada entre as partes.",
                    "E": f"A quitação dada pelo credor ao devedor não faz presumir a extinção da obrigação principal, devendo ser comprovada por outros meios jurídicos."
                }
                question_data["gabarito"] = "C"
                question_data["legal_basis"] = "Arts. 304, 305, 313, 314 e 320 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 304 estabelece que 'qualquer interessado na extinção da dívida pode pagá-la'. O terceiro interessado (fiador, avalista, "
                    f"adquirente de imóvel hipotecado) ao pagar a dívida sub-roga-se nos direitos do credor (art. 346, III). O credor não é obrigado "
                    f"a receber prestação diversa (art. 313) nem a receber por partes (art. 314). A moeda de pagamento é a moeda corrente nacional (art. 315)."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['credor']} emprestou {v['valor']} a {v['devedor']} mediante contrato de {v['contrato']} com vencimento em 30 dias. "
                    f"Próximo ao vencimento, sobreveio legislação que reduziu o poder aquisitivo da moeda. {v['devedor']} deseja pagar com correção monetária, "
                    f"mas {v['credor']} exige o valor nominal. À luz do Código Civil sobre pagamento, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"O credor {v['credor']} tem direito ao valor nominal, salvo disposição contratual em contrário, pois o pagamento deve ser feito no valor originalmente contratado.",
                    "B": f"O devedor {v['devedor']} pode exigir a revisão judicial do valor com base na teoria da imprevisão, independentemente de qualquer cláusula contratual.",
                    "C": f"O pagamento em dinheiro deverá ser feito em moeda estrangeira se houver desvalorização superior a 20% da moeda nacional.",
                    "D": f"Se o contrato for omisso quanto à correção, o juiz pode determinar a atualização monetária com base em índices oficiais sempre que houver desequilíbrio econômico.",
                    "E": f"O pagamento pode ser feito em bem imóvel de valor equivalente se o devedor não dispuser de recursos em dinheiro no vencimento."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Arts. 315, 316 e 317 do Código Civil."
                question_data["explanation"] = (
                    f"Pelo art. 315 do CC, o pagamento em dinheiro deve ser feito em moeda corrente nacional pelo valor nominal (princípio do nominalismo). "
                    f"O art. 317 permite a correção judicial apenas em caso de desproporção manifesta entre o valor da prestação e o do dia do pagamento, "
                    f"desde que a parte não tenha assumido o risco cambial. A regra geral, contudo, é o valor nominal."
                )

    # -------------------------------------------------------------
    # 2. QUEM DEVE PAGAR (Arts. 304 - 307)
    # -------------------------------------------------------------
    elif subject == "Quem deve pagar":
        question_data["article"] = "Art. 304 e Art. 305 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) {v['terceiro']}, terceiro não interessado na extinção de dívida decorrente de contrato de {v['contrato']} firmado entre "
                f"{v['devedor']} (devedor) e {v['credor']} (credor), realiza o pagamento integral do débito de {v['valor']} em seu próprio nome, "
                f"sem oposição de {v['devedor']}. Nessa situação, {v['terceiro']} se sub-roga de pleno direito nos privilégios e garantias do credor original."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "B"
            question_data["legal_basis"] = "Art. 305, caput, do Código Civil."
            question_data["explanation"] = (
                f"O terceiro não interessado que paga a dívida em seu próprio nome tem direito a reembolsar-se do que pagar, mas não se sub-roga "
                f"nos direitos do credor (Art. 305, CC). A sub-rogação de pleno direito só ocorre a favor do terceiro interessado ou nas hipóteses "
                f"legais expressas (Art. 346, CC). Portanto, a afirmação está ERRADA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} ({v['prof_dev']}) possuía uma dívida no valor de {v['valor']} decorrente de {v['contrato']} com "
                    f"{v['credor']}. Diante das dificuldades financeiras de {v['devedor']}, seu amigo {v['terceiro']} ({v['prof_terc']}), "
                    f"terceiro juridicamente não interessado, resolveu quitar a obrigação diretamente com o credor. "
                    f"Sobre o pagamento feito por {v['terceiro']} em seu próprio nome, assinale a opção correta à luz do Código Civil:"
                )
                question_data["options"] = {
                    "A": f"O pagamento feito por {v['terceiro']} extingue a dívida e gera sub-rogação imediata em todos os direitos e garantias de {v['credor']}.",
                    "B": f"Por ser terceiro não interessado, {v['terceiro']} tem direito a reembolsar-se do que pagar, mas não se sub-roga nos direitos do credor original.",
                    "C": f"Se {v['terceiro']} tivesse pago a dívida antes de vencida, teria direito ao reembolso imediato, mesmo antes do vencimento do prazo original.",
                    "D": f"O pagamento feito por {v['terceiro']} é considerado nulo, pois somente o devedor ou terceiros juridicamente interessados podem adimplir a obrigação.",
                    "E": f"Caso {v['devedor']} tivesse meios para ilidir (impedir) a ação e desconhecesse o pagamento, {v['terceiro']} ainda assim teria direito ao reembolso total."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 305 e Art. 306 do Código Civil."
                question_data["explanation"] = (
                    f"Conforme o art. 305, caput, do Código Civil, o terceiro não interessado que paga a dívida em seu próprio nome tem direito a "
                    f"reembolsar-se do que pagar, mas não se sub-roga nos direitos do credor. Além disso, o parágrafo único do mesmo artigo prevê que "
                    f"se pagar antes de vencida a dívida, só terá direito ao reembolso no vencimento. O art. 306 dispõe que o pagamento feito por terceiro, "
                    f"com desconhecimento ou oposição do devedor, não obriga a reembolso se este tinha meios para ilidir a ação."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} faleceu antes de quitar a dívida de {v['valor']} que possuía com {v['credor']}. "
                    f"O herdeiro {v['terceiro']} deseja pagar o débito para evitar a execução sobre o patrimônio deixado. "
                    f"Considerando as regras sobre quem deve pagar no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"Os herdeiros não têm legitimidade para pagar dívidas do falecido, devendo o credor {v['credor']} cobrar diretamente do espólio.",
                    "B": f"O interessado na extinção da dívida, como o herdeiro ou fiador, pode pagá-la, sub-rogando-se nos direitos do credor.",
                    "C": f"Apenas o devedor originário pode realizar o pagamento, sendo nulo qualquer pagamento feito por terceiros.",
                    "D": f"O pagamento por terceiro interessado exige autorização judicial prévia para produzir efeitos de extinção da obrigação.",
                    "E": f"O herdeiro que pagar dívida do falecido não tem direito de regresso contra os demais herdeiros, salvo disposição testamentária."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 304 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 304 do CC estabelece que 'qualquer interessado na extinção da dívida pode pagá-la'. O herdeiro é parte interessada "
                    f"diretamente, pois responde pelas dívidas do falecido dentro da força da herança (art. 1.997, CC). Ao pagar, sub-roga-se nos "
                    f"direitos do credor contra os demais herdeiros (art. 346, III, CC)."
                )

    # -------------------------------------------------------------
    # 3. A QUEM SE DEVE PAGAR (Arts. 308 - 312)
    # -------------------------------------------------------------
    elif subject == "A quem se deve pagar":
        question_data["article"] = "Art. 308 e Art. 309 do Código Civil"
        if is_cespe:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} realizou o pagamento do débito de {v['valor']} a {v['terceiro']}, que aparentava de forma convincente ser "
                    f"o legítimo credor (credor putativo). Posteriormente, o verdadeiro credor, {v['credor']}, demonstrou que {v['terceiro']} agia com falsidade. "
                    f"Nessa hipótese, o pagamento feito por {v['devedor']} a {v['terceiro']} é considerado plenamente válido, desde que {v['devedor']} tenha agido de boa-fé."
                )
                question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 309 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 309 do Código Civil consagra a Teoria da Aparência ao dispor que 'o pagamento feito de boa-fé ao credor putativo é válido, "
                    f"ainda provado depois que não era credor'. A boa-fé do devedor é o requisito essencial. Portanto, a afirmação está CERTA."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} pagou o valor de {v['valor']} a {v['terceiro']}, pessoa relativamente incapaz que se apresentava "
                    f"como credor, sem que {v['terceiro']} tivesse capacidade para dar quitação. {v['devedor']} não consegue provar que o valor "
                    f"reverteu em proveito do verdadeiro credor {v['credor']}. Nessa hipótese, o pagamento é válido e extingue a obrigação."
                )
                question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 310 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 310 do CC dispõe: 'Não vale o pagamento feito a quem se mostrava incapaz de quitá-lo, se o devedor não provar "
                    f"que reverteu em proveito do credor'. A incapacidade relativa de {v['terceiro']} para dar quitação invalida o pagamento, "
                    f"a menos que o devedor prove que o valor beneficiou o verdadeiro credor. Portanto, a afirmação está ERRADA."
                )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} contraiu uma obrigação perante {v['credor']} no valor de {v['valor']} referente a {v['contrato']}. "
                    f"No dia do vencimento, {v['devedor']} realizou o pagamento de boa-fé a {v['terceiro']}, pessoa que, por circunstâncias fáticas, "
                    f"apresentava-se socialmente e documentalmente como mandatário de {v['credor']} (credor putativo). Dias depois, {v['credor']} "
                    f"notificou {v['devedor']} exigindo o pagamento, alegando que {v['terceiro']} nunca teve poderes para receber. Diante disso, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"O pagamento é inválido, aplicando-se o brocardo popular 'quem paga mal paga duas vezes', restando a {v['devedor']} apenas pagar novamente a {v['credor']}.",
                    "B": f"O pagamento feito de boa-fé ao credor putativo é válido, restando a {v['credor']} demandar contra {v['terceiro']} para reaver o valor recebido.",
                    "C": f"O pagamento a {v['terceiro']} só seria válido se houvesse expressa autorização judicial prévia.",
                    "D": f"O pagamento é anulável, devendo {v['devedor']} ingressar com ação de anulação do negócio jurídico em face de {v['terceiro']}.",
                    "E": f"O pagamento é válido porque qualquer pagamento realizado a terceiros extingue a obrigação, independentemente de boa-fé."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 309 do Código Civil."
                question_data["explanation"] = (
                    f"De acordo com o art. 309 do CC, o pagamento feito de boa-fé ao credor putativo é perfeitamente válido. A lei protege o devedor "
                    f"que foi induzido a erro escusável pela aparência de credor do receptor. O verdadeiro credor ({v['credor']}) deve buscar o "
                    f"ressarcimento contra quem recebeu indevidamente ({v['terceiro']})."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['credor']} faleceu antes do vencimento da dívida de {v['valor']} que {v['devedor']} havia contraído mediante "
                    f"{v['contrato']}. {v['devedor']} efetuou o pagamento a {v['terceiro']}, irmão de {v['credor']}, que se apresentou como herdeiro e apresentou "
                    f"cópia simples da certidão de óbito. Posteriormente, o verdadeiro administrador do espólio cobrou novamente o valor, alegando que {v['terceiro']} não era o inventariante. "
                    f"À luz das regras sobre 'a quem se deve pagar' no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"O pagamento a {v['terceiro']} é válido, pois o pagamento feito a herdeiro aparente de boa-fé extingue a obrigação.",
                    "B": f"O pagamento é inválido, pois o credor é o espólio representado pelo inventariante, e não um herdeiro individualmente considerado.",
                    "C": f"O pagamento a qualquer parente do credor falecido é válido, independentemente de inventário ou formal de partilha.",
                    "D": f"A cobrança do espólio é abusiva, pois o pagamento feito a herdeiro putativo é sempre considerado quitado.",
                    "E": f"O pagamento só seria válido se {v['terceiro']} fosse o único herdeiro e comprovasse essa condição com certidão de óbito."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 308 e Art. 310 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 308 do CC determina que o pagamento deve ser feito ao credor ou a quem legalmente o represente. Com o falecimento do credor, "
                    f"o espólio, representado pelo inventariante, é quem detém a titularidade do crédito. O art. 310 dispõe que o pagamento feito de boa-fé "
                    f"ao credor putativo é válido, mas isso exige aparência legítima de credor, o que não ocorre com mera apresentação de certidão de óbito."
                )

    # -------------------------------------------------------------
    # 4. OBJETO DO PAGAMENTO E SUA PROVA (Arts. 313 - 326)
    # -------------------------------------------------------------
    elif subject == "Objeto do pagamento e sua prova":
        question_data["article"] = "Art. 313, Art. 314 e Art. 320 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) O credor não é obrigado a receber prestação diversa da que lhe é devida, ainda que mais valiosa, "
                f"salvo se o devedor oferecer garantias reais adicionais que assegurem o cumprimento da prestação original."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "B"
            question_data["legal_basis"] = "Art. 313 do Código Civil."
            question_data["explanation"] = (
                f"O art. 313 do CC determina que 'o credor não é obrigado a receber prestação diversa da que lhe é devida, ainda que mais valiosa'. "
                f"A ressalva sobre garantias reais adicionais não existe no texto legal — a regra é absoluta. Portanto, a afirmação está ERRADA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} firmou contrato de {v['contrato']} com {v['credor']} no valor de {v['valor']}. "
                    f"No momento do adimplemento, {v['devedor']} propõe quitar a dívida de forma não pecuniária. "
                    f"Sobre as regras do objeto do pagamento e sua prova no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"O credor {v['credor']} é obrigado a receber prestação diversa em dinheiro caso o devedor {v['devedor']} ofereça bem imóvel de valor comprovadamente superior ao da dívida.",
                    "B": f"O devedor {v['devedor']} pode exigir que o credor {v['credor']} receba o pagamento parceladamente, mesmo que o contrato tenha previsto pagamento à vista, desde que haja autorização judicial.",
                    "C": f"A quitação (recibo) é o principal meio de prova do pagamento, devendo conter o valor da prestação, o nome do devedor e a assinatura do credor, entre outros requisitos legais.",
                    "D": f"O pagamento feito em moeda estrangeira é plenamente válido se ambas as partes concordarem, independentemente de qualquer condição ou autorização legal.",
                    "E": f"A prova do pagamento pode ser feita exclusivamente por testemunhas, sendo o recibo mera formalidade dispensável para a validade do negócio."
                }
                question_data["gabarito"] = "C"
                question_data["legal_basis"] = "Arts. 313, 314, 315, 316, 317 e 320 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 320 do CC estabelece os requisitos da quitação: 'A quitação, que sempre poderá ser dada por instrumento particular, "
                    f"designará o valor e a espécie da dívida quitada, o nome do devedor, ou quem por este pagou, o tempo e o lugar do pagamento, "
                    f"com a assinatura do credor, ou do seu representante'. O credor não é obrigado a receber prestação diversa (art. 313), nem "
                    f"a receber por partes (art. 314). O pagamento em moeda estrangeira só é válido nos casos expressos em lei (art. 318)."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} deve a {v['credor']} o valor de {v['valor']} em moeda nacional, mas propõe quitar a dívida "
                    f"entregando metade em dinheiro e a outra metade em serviços de sua profissão ({v['prof_dev']}). "
                    f"Considerando as normas do Código Civil sobre objeto do pagamento e sua prova, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"O credor não é obrigado a receber por partes, salvo disposição em contrário; o devedor não pode obrigar o credor a receber prestação diversa, ainda que mais valiosa.",
                    "B": f"O pagamento parcelado é sempre obrigatório se o devedor comprovar dificuldade financeira, por aplicação do princípio da função social do contrato.",
                    "C": f"A quitação por instrumento particular dispensa a assinatura do credor, sendo suficiente a prova testemunhal do pagamento.",
                    "D": f"O pagamento em moeda estrangeira é permitido em qualquer contrato entre particulares, desde que as partes convencionem expressamente.",
                    "E": f"A prova do pagamento por recibo é obrigatória sob pena de nulidade do ato de adimplemento."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 313 e Art. 314 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 313 do CC determina que o credor não é obrigado a receber prestação diversa da que lhe é devida, ainda que mais valiosa. "
                    f"O art. 314, por sua vez, dispõe que o credor não é obrigado a receber o pagamento por partes, salvo disposição em contrário. "
                    f"A quitação (art. 320) exige a assinatura do credor. Moeda estrangeira só é admitida nos casos em que a lei autoriza (art. 318)."
                )

    # -------------------------------------------------------------
    # 5. LUGAR DO PAGAMENTO (Arts. 327 - 330)
    # -------------------------------------------------------------
    elif subject == "Lugar do pagamento":
        question_data["article"] = "Art. 327 e Art. 330 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) Salvo disposição em contrário do contrato ou das circunstâncias da lei, o pagamento de uma dívida de {v['valor']} "
                f"celebrado entre {v['devedor']} e {v['credor']} deve ser efetuado no domicílio do credor, configurando uma obrigação portável (portável)."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "B"
            question_data["legal_basis"] = "Art. 327 do Código Civil."
            question_data["explanation"] = (
                f"Conforme o art. 327, caput, do Código Civil, a regra geral é que o pagamento deve ser efetuado no domicílio do devedor, "
                f"caracterizando a obrigação querível (ou quérable). A obrigação portável (portável, no domicílio do credor) é a exceção e "
                f"exige convenção das partes ou disposição legal em contrário. Portanto, a afirmação está ERRADA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) No contrato de {v['contrato']} firmado entre {v['devedor']} (devedor) e {v['credor']} (credor), não foi estipulado "
                    f"o lugar para a entrega do valor de {v['valor']}. Sabendo que {v['devedor']} reside em {v['cidade']} e {v['credor']} reside em outra localidade, "
                    f"e considerando as regras do Código Civil brasileiro aplicáveis ao lugar do pagamento, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"O pagamento deve ser feito no domicílio de {v['credor']}, pois vigora a regra geral de que as obrigações são portáveis.",
                    "B": f"O pagamento deve ser feito no domicílio de {v['devedor']} ({v['cidade']}), pois rege o princípio geral de que as obrigações são queríveis (quérables).",
                    "C": f"Se houver dois ou mais lugares designados no contrato, cabe exclusivamente ao devedor escolher onde o pagamento será realizado.",
                    "D": f"O pagamento feito reiteradamente em local diverso do avençado não gera qualquer presunção de renúncia do credor.",
                    "E": f"A entrega de imóveis ou prestações relativas a eles deve ocorrer necessariamente no domicílio do credor."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 327 e Art. 330 do Código Civil."
                question_data["explanation"] = (
                    f"Pelo art. 327, caput, a regra geral é que o pagamento ocorra no domicílio do devedor (obrigação querível). O parágrafo único diz "
                    f"que se designados dois ou mais lugares, cabe ao *credor* escolher entre eles (eliminando a letra C). O art. 330 prevê que o pagamento "
                    f"reiteradamente feito em outro lugar faz presumir renúncia do credor relativamente ao previsto no contrato (eliminando a letra D)."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} e {v['credor']} firmaram contrato de {v['contrato']} estipulando que o pagamento de {v['valor']} "
                    f"seria feito no escritório de {v['credor']} em {v['cidade']}. Todavia, nos últimos seis meses, {v['credor']} aceitou "
                    f"reiteradamente o pagamento na residência de {v['devedor']}. Agora, {v['credor']} exige o pagamento em seu escritório, "
                    f"alegando o teor literal do contrato. Sobre o lugar do pagamento, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"O credor {v['credor']} tem razão, pois o contrato faz lei entre as partes, devendo ser cumprido no local avençado.",
                    "B": f"O pagamento reiteradamente feito em local diverso faz presumir renúncia do credor quanto ao lugar convencionado, de modo que {v['credor']} não pode mais exigir o cumprimento no local original.",
                    "C": f"A mudança de local de pagamento exige acordo formal escrito entre as partes, sendo inválida qualquer tolerância tácita.",
                    "D": f"Tratando-se de obrigação portável, o pagamento deve ser feito no domicílio do devedor {v['devedor']} em qualquer hipótese.",
                    "E": f"O credor pode unilateralmente alterar o lugar do pagamento a qualquer tempo, desde que comunique o devedor com 30 dias de antecedência."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 327 e Art. 330 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 330 do CC dispõe que 'o pagamento reiteradamente feito em outro local faz presumir renúncia do credor relativamente ao previsto no contrato'. "
                    f"A regra geral do art. 327 determina que, à falta de estipulação, o pagamento ocorre no domicílio do devedor (obrigação querível). "
                    f"Se o contrato designa local, este vale, mas a tolerância reiterada do credor gera renúncia tácita."
                )

    # -------------------------------------------------------------
    # 6. TEMPO DO PAGAMENTO (Arts. 331 - 333)
    # -------------------------------------------------------------
    elif subject == "Tempo do pagamento":
        question_data["article"] = "Art. 331 e Art. 333 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) Se uma obrigação firmada entre {v['devedor']} e {v['credor']} não contiver prazo assinalado para o seu cumprimento, "
                f"o credor poderá exigir o adimplemento imediatamente, sem a necessidade de prévia constituição em mora."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "A"
            question_data["legal_basis"] = "Art. 331 do Código Civil."
            question_data["explanation"] = (
                f"O art. 331 do CC estabelece: 'Salvo disposição especial deste Código, as obrigações puras e simples, sem prazo assinalado, "
                f"são exigíveis imediatamente'. Portanto, a afirmação está CERTA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} firmou com {v['credor']} um contrato de {v['contrato']} no valor de {v['valor']}. "
                    f"Sobre as regras legais acerca do tempo do pagamento e da cobrança antecipada da dívida, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"Ao credor assiste o direito de cobrar a dívida antes de vencido o prazo contratual se o devedor cair em insolvência ou for declarada sua falência.",
                    "B": f"As obrigações condicionais vencem de pleno direito na data da assinatura do respectivo instrumento, independentemente do implemento da condição.",
                    "C": f"Se não houver prazo estipulado no contrato, o devedor só poderá ser cobrado após interpelação judicial com prazo mínimo de 30 dias.",
                    "D": f"Caso o devedor ofereça garantias reais adicionais que se tornem insuficientes, o credor não poderá exigir reforço de garantia nem antecipar o vencimento.",
                    "E": f"O vencimento antecipado da dívida por insolvência do devedor estende-se automaticamente aos fiadores e codevedores solidários não insolventes."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 333, I, e parágrafo único do Código Civil."
                question_data["explanation"] = (
                    f"O art. 333 do CC autoriza o credor a cobrar a dívida antes de vencido o prazo: I - no caso de falência do devedor, ou de sua insolvência; "
                    f"II - se os bens, hipotecados ou empenhados, forem penhorados por outro credor; III - se cessarem, ou se se tornarem insuficientes, as garantias "
                    f"do débito, e o devedor, intimado, se negar a reforçá-las. O parágrafo único prevê que nos casos de solidariedade passiva, o vencimento antecipado "
                    f"não se propaga aos demais codevedores solventes."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} contraiu obrigação condicional com {v['credor']} no valor de {v['valor']}, cujo implemento "
                    f"da condição ainda não ocorreu. Paralelamente, {v['devedor']} teve bens penhorados por outro credor e suas garantias "
                    f"tornaram-se insuficientes. Considerando a disciplina do tempo do pagamento no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"A obrigação condicional considera-se vencida antes do implemento da condição, podendo o credor {v['credor']} cobrá-la imediatamente.",
                    "B": f"A obrigação condicional não se considera vencida antes do implemento da condição; entretanto, o credor pode cobrar a dívida antes do prazo se os bens dados em garantia se tornarem insuficientes.",
                    "C": f"As garantias tornadas insuficientes não autorizam o vencimento antecipado, pois a lei só admite antecipação por falência ou insolvência do devedor.",
                    "D": f"Se o devedor não tiver prazo assinalado, a obrigação vence 30 dias após a constituição em mora por interpelação judicial.",
                    "E": f"O vencimento antecipado por penhora de bens hipotecados só se aplica a obrigações solidárias."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 331, Art. 332 e Art. 333, I, II, III do Código Civil."
                question_data["explanation"] = (
                    f"O art. 332 do CC dispõe que as obrigações condicionais cumprem-se no implemento da condição, não vencendo antes. Todavia, "
                    f"o art. 333, II, autoriza o vencimento antecipado se 'os bens hipotecados ou empenhados forem penhorados por outro credor'. "
                    f"O inciso III também autoriza se as garantias se tornarem insuficientes. A regra geral é a do art. 331: obrigações sem prazo são exigíveis imediatamente."
                )

    # -------------------------------------------------------------
    # 7. CONSIGNAÇÃO EM PAGAMENTO (Arts. 334 - 345)
    # -------------------------------------------------------------
    elif subject == "Consignação em pagamento":
        question_data["article"] = "Art. 334 e Art. 335 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) O devedor {v['devedor']} poderá exonerar-se da obrigação mediante consignação em pagamento se o credor {v['credor']}, "
                f"sem justa causa, recusar-se a receber o pagamento ou dar a respectiva quitação no tempo e lugar devidos."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "A"
            question_data["legal_basis"] = "Art. 335, I, do Código Civil."
            question_data["explanation"] = (
                f"O art. 335, I, do CC prevê que a consignação tem lugar 'se o credor não puder, ou, sem justa causa, recusar receber o pagamento, "
                f"ou dar quitação na devida forma'. Portanto, a afirmação está CERTA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} pretende adimplir obrigação no valor de {v['valor']} decorrente de {v['contrato']} perante {v['credor']}. "
                    f"Contudo, há séria dúvida sobre quem é o legítimo credor, uma vez que {v['credor']} e {v['terceiro']} disputam judicialmente "
                    f"a titularidade do crédito. Diante desta situação de incerteza, conforme as regras de Consignação em Pagamento do Código Civil:"
                )
                question_data["options"] = {
                    "A": f"{v['devedor']} deve aguardar o trânsito em julgado da disputa entre {v['credor']} e {v['terceiro']}, suspendendo-se os juros moratórios automaticamente.",
                    "B": f"{v['devedor']} pode requerer a consignação em pagamento do valor devido para exonerar-se da obrigação, depositando a quantia em juízo.",
                    "C": f"A consignação é incabível em caso de dúvida sobre a titularidade do credor, devendo o devedor pagar a quem primeiro o interpelar.",
                    "D": f"Mesmo julgada procedente a consignação, as despesas com o depósito judicial correrão por conta do devedor {v['devedor']}.",
                    "E": f"Se {v['devedor']} consignar a importância e posteriormente levantar o depósito com anuência do credor, as garantias reais da dívida permanecerão intactas."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 335, IV, Art. 343 e Art. 344 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 335, IV, do CC estabelece que cabe consignação se ocorrer dúvida sobre quem deva legitimamente receber. As despesas do depósito, "
                    f"se julgado procedente, correm por conta do credor (art. 343). O art. 344 determina que se o devedor levantar o depósito anuído pelo "
                    f"credor, extinguem-se as garantias e desobrigam-se os fiadores."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['credor']} recusa-se a receber o pagamento de {v['valor']} oferecido por {v['devedor']} no tempo e lugar devidos, "
                    f"exigindo que {v['devedor']} pague também uma multa contratual não prevista no instrumento original de {v['contrato']}. "
                    f"{v['devedor']} deseja exonerar-se da obrigação. Com base na disciplina da consignação em pagamento, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"Cabe consignação em pagamento se o credor recusar receber o pagamento ou dar quitação na devida forma, sem justa causa.",
                    "B": f"A consignação só é cabível em caso de dúvida sobre quem deve receber, não se aplicando à recusa simples do credor.",
                    "C": f"O devedor pode reter o pagamento enquanto o credor não desistir da multa indevida, sem necessidade de depositar o valor incontroverso.",
                    "D": f"A consignação extrajudicial é obrigatória antes de qualquer ação judicial, sob pena de extinção do direito de consignar.",
                    "E": f"Consignado o valor, se julgado improcedente o pedido, o devedor responde por perdas e danos independentemente de comprovação de prejuízo."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 335, I, do Código Civil."
                question_data["explanation"] = (
                    f"O art. 335, I, do CC admite a consignação se o credor não puder ou, sem justa causa, recusar receber o pagamento ou dar quitação "
                    f"na devida forma. A consignação extrajudicial é facultativa (art. 539, CPC). Julgado improcedente, o devedor responde pelos prejuízos "
                    f"que comprovadamente causar (art. 342, CC)."
                )

    # -------------------------------------------------------------
    # 8. PAGAMENTO COM SUB-ROGAÇÃO (Arts. 346 - 351)
    # -------------------------------------------------------------
    elif subject == "Pagamento com sub-rogação":
        question_data["article"] = "Art. 346 e Art. 347 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) A sub-rogação é legal (opera-se de pleno direito) em favor do terceiro interessado que paga a dívida pela qual "
                f"era ou podia ser obrigado, como ocorre no caso do fiador que quita o débito do devedor principal."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "A"
            question_data["legal_basis"] = "Art. 346, III, do Código Civil."
            question_data["explanation"] = (
                f"O art. 346, III, do CC prescreve que a sub-rogação opera-se, de pleno direito, em favor 'do terceiro interessado, "
                f"que paga a dívida pela qual era ou podia ser obrigado, no todo ou em parte'. O fiador é o exemplo clássico de terceiro interessado. "
                f"Portanto, a afirmação está CERTA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} possui um débito hipotecário de {v['valor']} com {v['credor']}. O imóvel dado em garantia "
                    f"foi vendido a {v['terceiro']}. Para evitar a excussão da hipoteca e a perda do bem, {v['terceiro']} decide pagar "
                    f"integralmente a dívida a {v['credor']}. À luz do Código Civil, o pagamento efetuado por {v['terceiro']} acarreta:"
                )
                question_data["options"] = {
                    "A": "Sub-rogação legal, operando-se de pleno direito em favor do adquirente do imóvel hipotecado.",
                    "B": "Sub-rogação convencional, dependendo da expressa concordância de do devedor original.",
                    "C": "Mero direito de reembolso simples, sem a transferência das garantias hipotecárias.",
                    "D": "Extinção absoluta da obrigação, restando a terceiro apenas a via da ação de enriquecimento sem causa.",
                    "E": "Nulidade do pagamento por não ser terceiro interessado sob a ótica jurídica."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 346, II, do Código Civil."
                question_data["explanation"] = (
                    f"Conforme o art. 346, II, do CC, a sub-rogação opera-se de pleno direito (sub-rogação legal) em favor do adquirente "
                    f"do imóvel hipotecado, que paga ao credor o débito que onerava o imóvel. Trata-se de hipótese expressa na lei, dispensando "
                    f"acordo das partes."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['terceiro']}, amigo de {v['devedor']}, decide pagar a dívida de {v['valor']} que {v['devedor']} possui "
                    f"com {v['credor']} decorrente de {v['contrato']}. {v['terceiro']} não é fiador nem tem qualquer relação jurídica com a obrigação. "
                    f"Após o pagamento, o credor {v['credor']} cede expressamente seus direitos e ações ao terceiro que pagou. "
                    f"Considerando a disciplina da sub-rogação no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "O terceiro não interessado que paga a dívida em seu próprio nome não se sub-roga, tendo apenas direito de reembolso, salvo se houver cessão expressa de direitos pelo credor (sub-rogação convencional).",
                    "B": "A sub-rogação legal opera-se automaticamente em favor de qualquer terceiro que pague a dívida, independentemente de interesse ou concordância.",
                    "C": "O pagamento por terceiro não interessado extingue a dívida sem qualquer direito de reembolso ou sub-rogação.",
                    "D": "O terceiro não interessado sub-roga-se automaticamente nos direitos do credor, mas não nas garantias reais.",
                    "E": "A sub-rogação convencional exige concordância do devedor, sendo inválida se feita sem seu conhecimento."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 305, Art. 346, I, e Art. 347 do Código Civil."
                question_data["explanation"] = (
                    f"O terceiro não interessado que paga em seu próprio nome tem direito a reembolso (art. 305, CC), mas não se sub-roga nos direitos do credor. "
                    f"Para que haja sub-rogação, é necessário expressa declaração do credor ao transferir seus direitos (sub-rogação convencional, art. 347, I, CC) "
                    f"ou que o terceiro seja juridicamente interessado (sub-rogação legal, art. 346, CC)."
                )

    # -------------------------------------------------------------
    # 9. IMPUTAÇÃO DO PAGAMENTO (Arts. 352 - 355)
    # -------------------------------------------------------------
    elif subject == "Imputação do pagamento":
        question_data["article"] = "Art. 352 e Art. 354 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) Havendo capital e juros vencidos decorrentes de obrigações recíprocas entre {v['devedor']} e {v['credor']}, "
                f"o pagamento imputar-se-á primeiro no capital e, somente após a sua integral quitação, nos juros vencidos, salvo acordo em contrário."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "B"
            question_data["legal_basis"] = "Art. 354 do Código Civil."
            question_data["explanation"] = (
                f"O art. 354 do CC determina o oposto: 'Havendo capital e juros, o pagamento imputar-se-á primeiro nos juros vencidos, "
                f"e depois no capital, salvo estipulação em contrário, ou se o credor passar quitação por conta do capital'. "
                f"Portanto, a afirmação está ERRADA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} possui três débitos vencidos e de mesma natureza perante {v['credor']}, todos líquidos e certos, "
                    f"mas de valores distintos. Ao efetuar um pagamento parcial no valor de {v['valor']}, inferior à soma das três dívidas, "
                    f"{v['devedor']} não declara qual delas deseja quitar. De acordo com as regras de Imputação do Pagamento, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"Se {v['devedor']} não indicar, a escolha passa imediatamente ao credor {v['credor']}, que poderá imputar o pagamento na dívida que bem entender, devendo o devedor aceitar sem ressalvas.",
                    "B": f"Não tendo o devedor imputado, e se na quitação dada por {v['credor']} não constar imputação, o pagamento imputar-se-á nas dívidas líquidas e vencidas em primeiro lugar. Se todas forem vencidas ao mesmo tempo, na mais onerosa.",
                    "C": f"A lei obriga que o pagamento parcial seja rateado proporcionalmente entre as três dívidas.",
                    "D": f"Caso haja juros vencidos em uma das dívidas, o pagamento será obrigatoriamente imputado primeiro no capital de maior valor.",
                    "E": f"A imputação é ato estritamente bilateral, exigindo necessariamente a assinatura de termo aditivo contratual."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 354 e Art. 355 do Código Civil."
                question_data["explanation"] = (
                    f"Se o devedor não exercer o direito de imputação (art. 352) e o credor também não o fizer na quitação (art. 353), aplica-se a "
                    f"imputação legal determinada pelo art. 355: imputar-se-á nas dívidas líquidas e vencidas em primeiro lugar. Se as dívidas forem "
                    f"todas líquidas e vencidas ao mesmo tempo, a imputação far-se-á na mais onerosa."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} deve a {v['credor']} duas importâncias: R$ 10.000,00 de capital e R$ 2.000,00 de juros vencidos. "
                    f"{v['devedor']} efetua um pagamento de R$ 5.000,00 sem declarar em que imputá-lo. "
                    f"De acordo com as regras de imputação do pagamento do Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"O pagamento imputar-se-á primeiro no capital, pois a regra geral protege o credor, e só depois nos juros vencidos.",
                    "B": f"Havendo capital e juros, o pagamento imputar-se-á primeiro nos juros vencidos e depois no capital, salvo estipulação em contrário.",
                    "C": f"Os juros vencidos são considerados acessórios e não podem ser quitados separadamente, devendo o pagamento ser rateado proporcionalmente.",
                    "D": f"A imputação caberá exclusivamente ao credor se o devedor não a fizer, podendo {v['credor']} escolher imputar no capital ou nos juros.",
                    "E": f"O pagamento será considerado sem efeito até que o devedor declare expressamente em qual débito deseja imputá-lo, sob pena de devolução."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 354 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 354 do CC estabelece: 'Havendo capital e juros, o pagamento imputar-se-á primeiro nos juros vencidos, e depois no capital, "
                    f"salvo estipulação em contrário, ou se o credor passar quitação por conta do capital'. Essa regra protege o credor, evitando que "
                    f"o capital seja reduzido enquanto os juros continuam a se acumular."
                )

    # -------------------------------------------------------------
    # 10. DAÇÃO EM PAGAMENTO (Arts. 356 - 359)
    # -------------------------------------------------------------
    elif subject == "Dação em pagamento":
        question_data["article"] = "Art. 356 e Art. 359 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) Se o credor {v['credor']} aceitar receber de {v['devedor']} um lote de terras em substituição à prestação pecuniária "
                f"de {v['valor']}, e posteriormente {v['credor']} perder o imóvel por evicção, restabelecer-se-á a obrigação original, "
                f"ficando sem efeito a quitação dada, ressalvados os direitos de terceiros de boa-fé."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "A"
            question_data["legal_basis"] = "Art. 359 do Código Civil."
            question_data["explanation"] = (
                f"O art. 359 do Código Civil expressamente determina que, se o credor for evicto da coisa recebida em pagamento, restabelecer-se-á "
                f"a obrigação primitiva, ficando sem efeito a quitação dada, ressalvados os direitos de terceiros. Portanto, a afirmação está CERTA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} deve a {v['credor']} a quantia de {v['valor']}. Sem dinheiro para honrar o compromisso, {v['devedor']} "
                    f"oferece a entrega de um veículo de sua propriedade como forma de quitar integralmente o débito. {v['credor']} consente com "
                    f"a substituição. Considerando as normas da dação em pagamento, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "O consentimento de do credor é dispensável, bastando que o bem oferecido pelo devedor tenha valor igual ou superior à dívida original.",
                    "B": "Se o credor for evicto da coisa recebida (perder o veículo por decisão judicial favorável a terceiro), a obrigação original renasce, invalidando a quitação anterior, ressalvados direitos de terceiros de boa-fé.",
                    "C": "Se o devedor entregar coisa com vício redibitório, a obrigação original é considerada extinta de forma definitiva, restando apenas perdas e danos pelo vício.",
                    "D": "A dação em pagamento equipara-se à doação, aplicando-se integralmente as regras do contrato de doação pura.",
                    "E": "Se as partes determinarem o preço da coisa dada em substituição, o negócio jurídico será regido pelas regras do contrato de mútuo."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 356, Art. 357 e Art. 359 do Código Civil."
                question_data["explanation"] = (
                    f"A alternativa B reproduz fielmente a regra da evicção na dação em pagamento (art. 359, CC). A alternativa A está errada porque o "
                    f"credor não é obrigado a receber prestação diversa da que lhe é devida, ainda que mais valiosa (art. 313, CC). A alternativa E está errada "
                    f"pois se determinar o preço da coisa dada, a relação regula-se pelas regras do contrato de compra e venda (art. 357, CC)."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} oferece a {v['credor']} um imóvel para quitar dívida de {v['valor']}. O imóvel apresenta "
                    f"um vício oculto que o torna impróprio para o uso a que se destina. {v['credor']} aceita a dação sem conhecer o vício. "
                    f"Considerando as regras do Código Civil sobre dação em pagamento, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "O vício redibitório não se aplica à dação em pagamento, pois o credor assumiu o risco ao aceitar prestação diversa.",
                    "B": "Se a coisa dada em pagamento for evicta ou tiver vício redibitório, aplicam-se as regras da compra e venda, podendo o credor optar por rejeitar a coisa e recobrar a dívida original.",
                    "C": "O credor que recebe coisa com vício redibitório perde o direito de reclamar a dívida original, cabendo apenas ação de perdas e danos contra o devedor.",
                    "D": "A dação em pagamento com vício redibitório converte-se automaticamente em doação, invalidando a quitação.",
                    "E": "O vício redibitório extingue a dívida original, restando ao credor apenas a ação redibitória para devolver a coisa."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 358 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 358 do CC determina: 'Se for evicta a coisa dada em pagamento, ou se nela forem descobertos vícios redibitórios, "
                    f"assegurado ao credor o direito de reaver a obrigação primitiva'. Aplica-se, portanto, a mesma regra da compra e venda (arts. 441 e ss.), "
                    f"permitindo ao credor optar entre rejeitar a coisa e recobrar o débito original ou mantê-la com abatimento do preço."
                )

    # -------------------------------------------------------------
    # 11. NOVAÇÃO (Arts. 360 - 367)
    # -------------------------------------------------------------
    elif subject == "Novação":
        question_data["article"] = "Art. 360 e Art. 364 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) A novação extingue os acessórios e garantias da dívida antiga sempre que não houver estipulação em contrário. "
                f"Contudo, a garantia prestada por fiador que não anuiu com a novação permanece válida por força da solidariedade legal."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "B"
            question_data["legal_basis"] = "Art. 364 do Código Civil."
            question_data["explanation"] = (
                f"O art. 364 do Código Civil estabelece que a novação extingue os acessórios e garantias da dívida, se não houver estipulação em contrário. "
                f"Além disso, o mesmo artigo deixa claro que 'não aproveitará contudo ao credor ressalvar o penhor, a hipoteca ou a anticrese, se a coisa "
                f"pertencer a terceiro que não foi parte na novação'. Súmula e jurisprudência confirmam que o fiador que não participou da novação "
                f"fica exonerado da fiança (art. 366, CC). Portanto, a afirmação está ERRADA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} possui uma dívida de {v['valor']} com {v['credor']}. Para facilitar o adimplemento, as partes assinam "
                    f"um novo instrumento contratual contratando uma nova obrigação em substituição à anterior, que resta extinta. "
                    f"O contrato original era afiançado por {v['terceiro']}. Sobre os efeitos jurídicos dessa novação, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"A fiança prestada por {v['terceiro']} é transmitida automaticamente para a nova obrigação, independentemente de sua concordância, pois o acessório segue a sorte do principal.",
                    "B": f"A novação extingue a obrigação anterior. Importa a exoneração de {v['terceiro']} (fiador) caso este não tenha anuído expressamente com o novo contrato.",
                    "C": f"Qualquer tipo de modificação de prazo ou alteração de juros importa em novação presumida, mesmo sem a intenção inequívoca de novar (animus novandi).",
                    "D": f"Se a obrigação primitiva novada for nula, a novação é plenamente válida se as partes agiram de boa-fé.",
                    "E": f"A novação subjetiva passiva por expromissão exige obrigatoriamente o consentimento do devedor originário {v['devedor']}."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 360, Art. 361, Art. 362, Art. 366 e Art. 367 do Código Civil."
                question_data["explanation"] = (
                    f"Conforme o art. 366 do CC, importa exoneração do fiador a novação feita sem consenso dele com o devedor. A novação requer "
                    f"ânimo de novar expresso ou inequívoco (art. 361, CC) - eliminando a letra C. Obrigações nulas não podem ser novadas (art. 367, CC) "
                    f"- eliminando a letra D. A expromissão (novação por substituição do devedor) pode ser feita *independentemente* do consentimento "
                    f"do devedor originário (art. 362, CC) - eliminando a letra E."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} deve {v['valor']} a {v['credor']}. {v['terceiro']}, pessoa estranha à relação obrigacional, "
                    f"assume perante {v['credor']} a responsabilidade pela dívida, substituindo {v['devedor']}. {v['devedor']} não concorda "
                    f"com essa substituição e manifesta sua oposição. À luz das regras de novação subjetiva passiva, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "A substituição do devedor é nula sem o consentimento do devedor originário, pois a novação exige acordo trilateral.",
                    "B": "A expromissão (substituição do devedor por iniciativa do terceiro) dispensa o consentimento do devedor originário, mas exige a concordância do credor.",
                    "C": "A delegação (substituição do devedor por iniciativa do devedor originário) exige anuência do credor e do novo devedor, mas dispensa a concordância do delegante.",
                    "D": "Em qualquer modalidade de novação subjetiva passiva, a insolvência do novo devedor autoriza o credor a reclamar do devedor originário, salvo se este agiu de má-fé.",
                    "E": "A novação subjetiva passiva extingue automaticamente todas as garantias prestadas por terceiros, ainda que estes anuam com a substituição."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 362 e Art. 363 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 362 do CC trata da expromissão: 'O terceiro pode assumir a obrigação do devedor, independentemente do consentimento "
                    f"deste, salvo disposição em contrário'. Já o art. 363 trata da delegação, que exige consentimento do devedor. Na expromissão, "
                    f"apenas o consentimento do credor é necessário para a validade."
                )

    # -------------------------------------------------------------
    # 12. COMPENSAÇÃO (Arts. 368 - 380)
    # -------------------------------------------------------------
    elif subject == "Compensação":
        question_data["article"] = "Art. 368 e Art. 369 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) Para que ocorra a compensação legal, exige-se a reciprocidade das obrigações, que as dívidas sejam líquidas, "
                f"vencidas (exigíveis) e de coisas fungíveis da mesma espécie e qualidade."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "A"
            question_data["legal_basis"] = "Art. 368 e Art. 369 do Código Civil."
            question_data["explanation"] = (
                f"De acordo com o art. 368 (reciprocidade) e art. 369 do CC, a compensação legal efetua-se entre dívidas líquidas, vencidas e de "
                f"coisas fungíveis. Portanto, a afirmação está CERTA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} deve {v['valor']} a {v['credor']}. Por sua vez, {v['credor']} deve {v['valor']} a {v['devedor']}. "
                    f"Diante das regras de compensação estatuídas no Código Civil, assinale a opção que apresenta um impedimento à compensação legal:"
                )
                question_data["options"] = {
                    "A": "Uma das dívidas decorrer de comodato, depósito ou alimentos.",
                    "B": "As dívidas possuírem prazos de vencimento diferentes, embora ambas já estejam vencidas.",
                    "C": "Uma das partes ser fiadora da outra e pretender compensar sua dívida com o crédito do devedor principal.",
                    "D": "As obrigações terem sido contraídas em locais de cumprimento distintos, mesmo que deduzidas as despesas de remessa.",
                    "E": "As obrigações decorrerem de relações contratuais de naturezas comerciais diversas."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 373, Art. 371 do Código Civil."
                question_data["explanation"] = (
                    f"A compensação legal não é admitida em certas hipóteses por razões de interesse público ou proteção social. O art. 373 do CC exclui "
                    f"a compensação se a causa de uma das dívidas provier: I - de esbulho, furto ou roubo; II - de comodato, depósito ou alimentos; "
                    f"III - de coisa não suscetível de penhora. O fiador pode compensar sua obrigação com o débito do credor ao devedor principal "
                    f"(art. 371) - logo, a alternativa C não é um impedimento."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} deve R$ 50.000,00 a {v['credor']} por contrato de {v['contrato']}. Por sua vez, {v['credor']} "
                    f"deve R$ 30.000,00 a {v['devedor']} por outro contrato. As dívidas são líquidas, vencidas e de coisas fungíveis. "
                    f"Considerando a disciplina da compensação no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "A compensação opera-se de pleno direito entre as dívidas até o limite de R$ 30.000,00, extinguindo-se ambas no valor correspondente.",
                    "B": "A compensação total das dívidas opera-se automaticamente, extinguindo ambos os débitos por completo.",
                    "C": "A compensação depende de acordo expresso entre as partes, não podendo ser declarada de ofício pelo juiz.",
                    "D": "A compensação legal exige que ambas as dívidas tenham o mesmo valor, sendo incabível se os montantes forem desiguais.",
                    "E": "A compensação convencional só é admitida se as dívidas forem da mesma natureza jurídica."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 368, Art. 369 e Art. 374 do Código Civil."
                question_data["explanation"] = (
                    f"Pelo art. 368 do CC, a compensação efetua-se entre dívidas líquidas, vencidas e de coisas fungíveis. "
                    f"Não sendo iguais os valores, a compensação dar-se-á até o limite do menor (art. 374, CC). O juiz pode declará-la de ofício "
                    f"(art. 369, parágrafo único). A compensação opera-se de pleno direito (art. 368, CC)."
                )

    # -------------------------------------------------------------
    # 13. CONFUSÃO (Arts. 381 - 384)
    # -------------------------------------------------------------
    elif subject == "Confusão":
        question_data["article"] = "Art. 381 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) A confusão opera-se quando na mesma pessoa se reúnem as qualidades de credor e devedor, gerando a extinção automática "
                f"do crédito. Se a confusão for desfeita por causa subsequente, a obrigação anterior não se restabelece, restando apenas perdas e danos."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "B"
            question_data["legal_basis"] = "Art. 381 e Art. 384 do Código Civil."
            question_data["explanation"] = (
                f"O art. 384 do CC prevê exatamente o contrário: 'Cessando a confusão, para logo se restabelece, com todos os seus acessórios, "
                f"a obrigação anterior'. Portanto, a afirmação está ERRADA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} emitiu uma nota promissória a favor de seu tio {v['credor']} no valor de {v['valor']}. "
                    f"Posteriormente, {v['credor']} falece e, em seu testamento, deixa todo o seu patrimônio (incluindo o referido crédito) "
                    f"para seu único herdeiro e sobrinho {v['devedor']}. À luz das regras do Código Civil acerca da confusão, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "A obrigação extingue-se por confusão, posto que as qualidades de credor e devedor reuniram-se na figura de uma única pessoa.",
                    "B": "A obrigação permanece ativa, devendo o devedor pagar a si mesmo e recolher o imposto de transmissão correspondente.",
                    "C": "Trata-se de hipótese de compensação tácita testamentária, pois o devedor herdou o crédito do próprio devedor.",
                    "D": "A confusão, por ser causa de extinção meramente provisória, impede a cobrança de juros mas mantém as garantias prestadas por fiador.",
                    "E": "Se a confusão cessar posteriormente (ex: surgimento de testamento mais recente anulando o anterior), a obrigação original não se restabelece."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 381 e Art. 384 do Código Civil."
                question_data["explanation"] = (
                    f"A reunião das qualidades de credor e devedor na mesma pessoa gera extinção da obrigação por confusão (art. 381, CC). "
                    f"Se a confusão cessar por causa superveniente (como a anulação do inventário/testamento), a obrigação renasce com todos os seus "
                    f"acessórios e garantias (art. 384, CC)."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} é devedor solidário com seu irmão {v['terceiro']} perante {v['credor']} no valor de {v['valor']}. "
                    f"{v['credor']} falece e {v['devedor']} é seu único herdeiro. {v['terceiro']} (codevedor solidário) continua a ser devedor "
                    f"e agora é também credor em parte, pois a herança inclui o crédito. Considerando a disciplina da confusão, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "A confusão extingue integralmente a obrigação, inclusive em relação a todos os codevedores solidários.",
                    "B": "A confusão, na solidariedade passiva, extingue a obrigação apenas até a quota-parte do devedor que se confundiu com o credor, subsistindo o saldo para os demais codevedores.",
                    "C": "A confusão não opera em obrigações solidárias, pois o vínculo obrigacional exige a pluralidade de sujeitos.",
                    "D": "O codevedor solidário que não se confundiu com o credor pode exigir que o herdeiro-credor pague a quota dos demais.",
                    "E": "A confusão transforma a obrigação solidária em obrigação simples, mantendo-se o mesmo devedor remanescente."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 381 e Art. 383 do Código Civil."
                question_data["explanation"] = (
                    f"Nos termos do art. 383 do CC, 'a confusão operada na pessoa do credor ou devedor solidário só extingue a obrigação "
                    f"até a concorrência da respectiva quota, subsistindo quanto ao mais a solidariedade'. Portanto, apenas a quota de {v['devedor']} "
                    f"se extingue, restando a {v['terceiro']} a obrigação pelo saldo remanescente."
                )

    # -------------------------------------------------------------
    # 14. REMISSÃO DAS DÍVIDAS (Arts. 385 - 388)
    # -------------------------------------------------------------
    elif subject == "Remissão das dívidas":
        question_data["article"] = "Art. 385 e Art. 388 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) A remissão da dívida (perdão), aceita pelo devedor, extingue a obrigação, mas não pode prejudicar terceiros, "
                f"como os credores do credor remitente."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "A"
            question_data["legal_basis"] = "Art. 385 do Código Civil."
            question_data["explanation"] = (
                f"O art. 385 do Código Civil dispõe: 'A remissão da dívida, aceita pelo devedor, extingue a obrigação, mas sem prejuízo de terceiro'. "
                f"Logo, credores do remitente prejudicados podem impugnar o ato. Portanto, a afirmação está CERTA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['credor']} resolve perdoar (remitir) a dívida de {v['valor']} contraída por {v['devedor']}. "
                    f"O contrato conta com garantia real de penhor sobre um bem de {v['devedor']}. Com base nas regras sobre a remissão das dívidas no Código Civil, "
                    f"assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "A remissão é ato estritamente unilateral, operando seus efeitos de extinção mesmo se o devedor manifestar recusa expressa ao perdão.",
                    "B": "A devolução voluntária do objeto empenhado (garantia real) pelo credor ao devedor faz presumir a renúncia da garantia, mas não a extinção da dívida principal.",
                    "C": "A remissão concedida a um dos codevedores solidários extingue toda a dívida em relação aos demais codevedores, sem direito de cobrar a quota-parte dos outros.",
                    "D": "O perdão da dívida principal mantém íntegra a garantia real de penhor, a qual subsiste por força de lei.",
                    "E": "A remissão é negócio jurídico nulo por se tratar de doação indireta disfarçada de transação."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 385, Art. 387 e Art. 388 do Código Civil."
                question_data["explanation"] = (
                    f"Pelo art. 387 do CC, 'a restituição voluntária do objeto empenhado prova a renúncia do credor à garantia real, não a remissão da dívida'. "
                    f"A alternativa A está incorreta pois a remissão exige aceitação do devedor (art. 385). A alternativa C está incorreta porque a remissão "
                    f"a um codevedor extingue a dívida apenas até o montante de sua quota, restando aos outros codevedores o saldo deduzido (art. 388)."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['credor']} perdoa a dívida de {v['valor']} de {v['devedor']} mediante declaração expressa. "
                    f"O contrato de {v['contrato']} tinha {v['terceiro']} como fiador. "
                    f"Considerando a disciplina da remissão das dívidas no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "A remissão concedida ao devedor principal extingue a obrigação, mas não exonera o fiador, que continua vinculado pela garantia prestada.",
                    "B": "A remissão da dívida principal extingue a obrigação e exonera o fiador, salvo se este anuir em permanecer garantindo a dívida já remitida.",
                    "C": "O fiador permanece vinculado até que o credor devolva voluntariamente o contrato de fiança ao fiador.",
                    "D": "A remissão é irrevogável após a declaração do credor, independentemente de aceitação do devedor.",
                    "E": "O credor que remite a dívida perde o direito de cobrar de codevedores solidários, salvo se houver expressa ressalva quanto à quota de cada um."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 385 e Art. 388 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 385 do CC dispõe que a remissão extingue a obrigação. Tratando-se de fiança, o acessório segue o principal: "
                    f"extinta a obrigação principal, extingue-se a fiança. O art. 388 determina que a remissão concedida a um codevedor "
                    f"extingue a dívida apenas até o limite de sua quota na solidariedade. A remissão exige aceitação do devedor (art. 385)."
                )

    # -------------------------------------------------------------
    # 15. MORA - GERAL (Arts. 394 - 401)
    # -------------------------------------------------------------
    elif subject == "Mora - Geral":
        question_data["article"] = "Art. 394, Art. 395 e Art. 396 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) Se {v['devedor']} (devedor) incorrer em atraso culposo no cumprimento de obrigação líquida e com prazo certo "
                f"ajustada com {v['credor']}, a mora operar-se-á de pleno direito no vencimento (mora ex re), dispensando-se qualquer notificação judicial."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "A"
            question_data["legal_basis"] = "Art. 397, caput, do Código Civil."
            question_data["explanation"] = (
                f"Segundo o art. 397 do CC, 'o inadimplemento da obrigação, positiva e líquida, no seu termo, constitui de pleno direito em mora o devedor' "
                f"(regra dies interpellat pro homine). A mora ex re dispensa interpelação. Portanto, a afirmação está CERTA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} firmou contrato de {v['contrato']} com {v['credor']}. No vencimento do prazo para entrega do valor de {v['valor']}, "
                    f"{v['devedor']} não realiza o pagamento. Com base na disciplina da mora no Código Civil brasileiro, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "Não havendo fato ou omissão imputável ao devedor (ausência de culpa), este não incorre em mora.",
                    "B": "O devedor em mora responde pela impossibilidade da prestação, exceto se provar que a impossibilidade ocorreria mesmo se tivesse adimplido tempestivamente.",
                    "C": "A mora do credor (mora accipiendi) não isenta o devedor de responsabilidade pela conservação da coisa nem obsta a cobrança de juros moratórios standard.",
                    "D": "Para purgar a mora, basta ao devedor oferecer ao credor a prestação devida no valor principal, independentemente de juros ou perdas e danos.",
                    "E": "Se a obrigação não tiver prazo determinado, a mora do devedor (mora ex persona) ocorre no momento exato do inadimplemento material da prestação."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 396, Art. 399, Art. 400 e Art. 401 do Código Civil."
                question_data["explanation"] = (
                    f"A alternativa A reflete o art. 396 do CC: 'Não havendo fato ou omissão imputável ao devedor, não incorre este em mora'. "
                    f"A mora do devedor exige culpa. A alternativa B está incorreta porque o devedor responde pela impossibilidade *a menos que* prove "
                    f"que o dano sobreviria mesmo com o cumprimento pontual (art. 399). A alternativa C erra porque a mora do credor subtrai o devedor "
                    f"da responsabilidade pela conservação, salvo dolo (art. 400). A alternativa E erra pois se não há termo, a mora exige interpelação (art. 397, parágrafo único)."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} deve {v['valor']} a {v['credor']} sem prazo determinado. {v['credor']} exige o pagamento "
                    f"mediante carta com aviso de recebimento, concedendo prazo de 10 dias. {v['devedor']} não paga. "
                    f"Considerando as regras sobre constituição em mora no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "Nas obrigações sem prazo determinado, a mora constitui-se mediante interpelação judicial ou extrajudicial do devedor (mora ex persona).",
                    "B": "Nas obrigações sem prazo, a mora é automática no momento do inadimplemento (mora ex re), dispensando qualquer intervenção.",
                    "C": "A interpelação extrajudicial não produz efeitos para constituir o devedor em mora, sendo necessária a citação judicial.",
                    "D": "O devedor de obrigação sem prazo não pode ser constituído em mora, pois o credor pode exigir a qualquer tempo.",
                    "E": "A mora ex persona dispensa os requisitos de culpa, bastando o mero retardamento para caracterizá-la."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 397, parágrafo único, do Código Civil."
                question_data["explanation"] = (
                    f"O art. 397, parágrafo único, do CC estabelece: 'Não havendo termo, a mora se constitui mediante interpelação judicial ou extrajudicial'. "
                    f"Isso é a chamada mora ex persona, que exige provocação do credor para constituir o devedor em mora. Diferencia-se da mora ex re "
                    f"(art. 397, caput), que opera-se de pleno direito no vencimento quando a obrigação tem prazo certo."
                )

    # -------------------------------------------------------------
    # 15b. MORA DO DEVEDOR (Arts. 394 - 401)
    # -------------------------------------------------------------
    elif subject == "Mora do devedor":
        question_data["article"] = "Art. 394, Art. 397, Art. 399 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) {v['devedor']}, devedor de obrigação líquida e com prazo certo, deixou de pagar {v['valor']} a {v['credor']} na data ajustada. "
                f"Antes do recebimento da prestação, o bem objeto do contrato pereceu por caso fortuito, sem culpa de {v['devedor']}. "
                f"Nessa hipótese, {v['devedor']} não responde pelo perecimento, exceto se este também ocorresse caso a prestação tivesse sido realizada no vencimento."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "A"
            question_data["legal_basis"] = "Art. 399 do Código Civil."
            question_data["explanation"] = (
                f"O art. 399 do CC dispõe que o devedor em mora responde pela impossibilidade da prestação, exceto se provar que o dano ocorreria "
                f"ainda que a obrigação tivesse sido cumprida no vencimento. Portanto, a afirmação está CERTA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} contraiu obrigação de entregar {v['contrato']} a {v['credor']} até determinada data. "
                    f"Após o vencimento, {v['credor']} exige o cumprimento com acréscimos legais. Considerando a disciplina da mora do devedor no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "Constituído em mora, o devedor responde pela impossibilidade da prestação, ainda que esta decorra de caso fortuito ou força maior, salvo se provar que o dano ocorreria mesmo que cumprisse a obrigação no vencimento.",
                    "B": "A mora do devedor é sempre purgável mediante a simples oferta da prestação principal, independentemente do pagamento de juros ou correção monetária.",
                    "C": "O devedor constituído em mora não responde pelos prejuízos decorrentes de caso fortuito se provar que agiu com diligência na guarda do bem.",
                    "D": "A mora do devedor em obrigação sem prazo determinado constitui-se automaticamente no momento do inadimplemento, sem necessidade de interpelação.",
                    "E": "O credor pode recusar a prestação oferecida pelo devedor em mora se o prejuízo causado pelo atraso exceder o valor da própria obrigação."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 394, Art. 397 e Art. 399 do Código Civil."
                question_data["explanation"] = (
                    f"A alternativa A descreve corretamente a perpetuação da obrigação (art. 399). A alternativa B erra porque a purgação exige o pagamento "
                    f"da prestação acrescida de juros, correção e perdas e danos (art. 401). A alternativa D erra porque obrigação sem prazo exige interpelação "
                    f"(art. 397, parágrafo único). A alternativa C contraria o art. 399, que impõe a responsabilidade objetiva do devedor em mora pelo fortuito."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} em mora há 15 dias em relação à obrigação de pagar {v['valor']} a {v['credor']}. "
                    f"Durante esse período, o objeto da prestação pereceu por força maior, sem culpa de {v['devedor']}. "
                    f"Considerando a disciplina da mora no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"O devedor não responde pelo perecimento, pois caso fortuito ou força maior excluem a responsabilidade, nos termos do art. 393 do CC.",
                    "B": "O devedor em mora responde pela impossibilidade da prestação, salvo se provar que o dano ocorreria ainda que a obrigação tivesse sido cumprida no vencimento.",
                    "C": "A purgação da mora retroage à data do vencimento, eximindo o devedor de qualquer responsabilidade pelo perecimento superveniente.",
                    "D": "O credor que aceitar a prestação após o perecimento renuncia ao direito de cobrar perdas e danos pela mora.",
                    "E": "A mora se extingue com o perecimento da coisa por força maior, operando-se a novação objetiva automática."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 399 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 399 do CC dispõe que 'o devedor em mora responde pela impossibilidade da prestação, embora essa impossibilidade "
                    f"decorra de caso fortuito ou força maior, se estes ocorrerem durante o atraso; salvo se provar que o dano sobreviria ainda "
                    f"quando a obrigação fosse oportunamente desempenhada'. Esta é a teoria da perpetuação da obrigação."
                )

    # -------------------------------------------------------------
    # 15c. MORA DO CREDOR (Arts. 394 - 401)
    # -------------------------------------------------------------
    elif subject == "Mora do credor":
        question_data["article"] = "Art. 394, Art. 400 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) {v['credor']} recusou injustificadamente receber o pagamento de {v['valor']} oferecido por {v['devedor']} no prazo e local ajustados. "
                f"Em razão da mora do credor, {v['devedor']} fica desobrigado de conservar a coisa objeto da prestação, respondendo apenas por dolo, "
                f"e ficam suspensos os juros de mora."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "A"
            question_data["legal_basis"] = "Art. 400 do Código Civil."
            question_data["explanation"] = (
                f"O art. 400 do CC estabelece que 'a mora do credor subtrai o devedor da responsabilidade pela conservação da coisa, "
                f"obriga o credor a pagar as despesas e reduzindo-a, e exime o devedor de pagar juros'. Portanto, a afirmação está CERTA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['credor']} recusou-se, sem justa causa, a receber o valor de {v['valor']} que {v['devedor']} lhe ofereceu no local e data "
                    f"aprazados. Diante da recusa, {v['devedor']} não sabe como proceder para se desonerar. Considerando a disciplina da mora do credor (mora accipiendi) no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "O devedor em mora accipiendi responde pela conservação da coisa enquanto não a consignar, salvo se a recusa do credor o impossibilitar de cumprir a prestação.",
                    "B": "A mora do credor exonera o devedor da responsabilidade pela conservação da coisa, obriga o credor a ressarcir as despesas de guarda e exime o devedor de pagar juros sobre a dívida.",
                    "C": "O credor em mora pode, a qualquer tempo, exigir a prestação, correndo por conta do devedor os riscos pela deterioração da coisa.",
                    "D": "A mora do credor converte automaticamente a obrigação de dar em obrigação de indenizar, liberando o devedor do vínculo obrigacional.",
                    "E": "O devedor pode exigir a purgação da mora do credor mediante consignação extrajudicial, sendo esta suficiente para afastar a mora accipiendi."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 400 do Código Civil."
                question_data["explanation"] = (
                    f"A alternativa B descreve precisamente os efeitos da mora do credor previstos no art. 400 do CC. "
                    f"A alternativa A erra porque o devedor não responde pela conservação (salvo dolo). A alternativa C erra porque os riscos da deterioração "
                    f"correm por conta do credor em mora. A alternativa D erra porque o vínculo não se converte automaticamente em indenização."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} se dispõe a pagar {v['valor']} a {v['credor']} no local e data aprazados. "
                    f"{v['credor']} recusa o pagamento sem justa causa, alegando que {v['devedor']} deveria pagar também uma taxa "
                    f"de serviço que não consta do contrato de {v['contrato']}. Considerando a mora do credor, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "A recusa do credor não caracteriza mora accipiendi, pois o devedor pode pagar a qualquer tempo posterior.",
                    "B": "Configurada a mora do credor, o devedor fica exonerado da responsabilidade pela conservação da coisa e suspensos os juros de mora, podendo o devedor valer-se da consignação em pagamento para se exonerar.",
                    "C": "O devedor deve depositar o valor em juízo independentemente da recusa do credor, sob pena de incorrer em mora.",
                    "D": "A mora do credor converte a obrigação de dar em obrigação de fazer, devendo o devedor prestar serviços equivalentes.",
                    "E": "O devedor responde integralmente pela conservação da coisa até que o credor aceite o pagamento, salvo caso fortuito."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 400 e Art. 335, I, do Código Civil."
                question_data["explanation"] = (
                    f"O art. 400 do CC estabelece os efeitos da mora do credor: subtrai o devedor da responsabilidade pela conservação da coisa, "
                    f"obriga o credor a pagar as despesas e exime o devedor de pagar juros. Além disso, a consignação em pagamento (art. 335, I) "
                    f"é o remédio adequado para o devedor se exonerar quando o credor recusa receber sem justa causa."
                )

    # -------------------------------------------------------------
    # 16a. INADIMPLEMENTO - DISPOSIÇÕES GERAIS (Arts. 389 - 393)
    # -------------------------------------------------------------
    elif subject == "Inadimplemento - Disposições gerais":
        question_data["article"] = "Art. 389, Art. 390, Art. 391, Art. 392, Art. 393 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) {v['devedor']} descumpriu obrigação contratual com {v['credor']} em razão de caso fortuito imprevisível, "
                f"não tendo assumido expressamente o risco por tal evento no contrato. Nessa hipótese, {v['devedor']} não responde pelos prejuízos "
                f"decorrentes do inadimplemento, pois o caso fortuito exclui a responsabilidade, salvo disposição em contrário."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "A"
            question_data["legal_basis"] = "Art. 393 do Código Civil."
            question_data["explanation"] = (
                f"O art. 393 do CC estabelece que 'o devedor não responde pelos prejuízos resultantes de caso fortuito ou força maior, "
                f"se expressamente não se houver por eles responsabilizado'. Portanto, a afirmação está CERTA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} não cumpriu a obrigação assumida no contrato de {v['contrato']} com {v['credor']} no valor de {v['valor']}. "
                    f"Considerando as disposições gerais sobre inadimplemento das obrigações no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "O inadimplemento absoluto ocorre quando a prestação ainda é possível e útil ao credor, autorizando o cumprimento forçado com acréscimos.",
                    "B": "O devedor não responde pelos prejuízos resultantes de caso fortuito ou força maior, se expressamente não se houver por eles responsabilizado.",
                    "C": "Nas obrigações de dar coisa incerta, a escolha pertence ao devedor, que não pode ser obrigado a prestar outra de qualidade superior.",
                    "D": "A mora caracteriza-se pelo descumprimento definitivo da obrigação, tornando inútil a prestação ao credor.",
                    "E": "O credor da obrigação de fazer pode, em qualquer hipótese, mandar executar o fato por terceiro às expensas do devedor."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 389, Art. 390, Art. 391, Art. 392 e Art. 393 do Código Civil."
                question_data["explanation"] = (
                    f"A alternativa B reproduz o art. 393, caput, que exclui a responsabilidade do devedor por caso fortuito ou força maior, "
                    f"salvo assunção expressa. A alternativa A erra ao confundir inadimplemento absoluto (que torna a prestação inútil ao credor) "
                    f"com mora. A alternativa D erra ao inverter os conceitos: mora é atraso (ainda possível); inadimplemento absoluto é impossibilidade definitiva."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} descumpriu obrigação no valor de {v['valor']} decorrente de {v['contrato']}. "
                    f"{v['credor']} pretende executar o patrimônio de {v['devedor']} para satisfazer o crédito. "
                    f"Considerando as disposições gerais sobre inadimplemento, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "Pelo inadimplemento da obrigação, respondem todos os bens do devedor, salvo as restrições estabelecidas em lei ou, sendo a obrigação personalíssima, se o fato personalíssimo não puder ser exigido de terceiro.",
                    "B": "Nas obrigações de fazer, o credor pode sempre mandar executar o fato por terceiro, independentemente da natureza da prestação.",
                    "C": "O inadimplemento por culpa do devedor limita-se ao valor da prestação principal, excluídos lucros cessantes e danos morais.",
                    "D": "A mora e o inadimplemento absoluto produzem os mesmos efeitos jurídicos, diferenciando-se apenas quanto à possibilidade de purgação.",
                    "E": "O descumprimento de obrigação decorrente de caso fortuito autoriza o credor a exigir indenização, salvo cláusula de não indenizar."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 389, Art. 390, Art. 391 e Art. 393 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 391 do CC estabelece: 'Pelo inadimplemento das obrigações respondem todos os bens do devedor'. "
                    f"O art. 389 determina que o devedor responde por perdas e danos, mais juros e correção. O art. 393 exclui a responsabilidade "
                    f"por caso fortuito ou força maior. Nas obrigações de fazer, o credor pode mandar executar por terceiro apenas quando a prestação "
                    f"for fungível (art. 390, CC)."
                )

    # -------------------------------------------------------------
    # 16b. INADIMPLEMENTO ABSOLUTO (Arts. 389 - 393)
    # -------------------------------------------------------------
    elif subject == "Inadimplemento absoluto":
        question_data["article"] = "Art. 389, Art. 391, Art. 395 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) {v['devedor']} deveria entregar {v['contrato']} a {v['credor']} em determinada data, mas o bem pereceu totalmente por culpa exclusiva de {v['devedor']}, "
                f"tornando a prestação impossível. Diante do inadimplemento absoluto, {v['credor']} tem direito de exigir o equivalente econômico "
                f"da prestação acrescido de perdas e danos, sem prejuízo de buscar a resolução do contrato."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "A"
            question_data["legal_basis"] = "Art. 389 do Código Civil."
            question_data["explanation"] = (
                f"O art. 389 do CC dispõe que 'não cumprida a obrigação, responde o devedor por perdas e danos, mais juros e atualização monetária, "
                f"sem prejuízo da resolução do contrato'. A diferença entre inadimplemento absoluto e mora é que no absoluto a prestação tornou-se inútil "
                f"ao credor. Portanto, a afirmação está CERTA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} comprometeu-se a entregar bem específico a {v['credor']} até o dia do vencimento. "
                    f"Após o vencimento, o bem pereceu integralmente por culpa de {v['devedor']}, não sendo mais possível o cumprimento da prestação original. "
                    f"Considerando o inadimplemento absoluto no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "O inadimplemento absoluto distingue-se da mora porque nesta a prestação ainda é possível e útil ao credor, enquanto naquele a prestação tornou-se impossível ou inútil.",
                    "B": "No inadimplemento absoluto, o credor pode exigir o cumprimento forçado da prestação original, pois o vínculo obrigacional persiste integralmente.",
                    "C": "O devedor em inadimplemento absoluto responde apenas pelo valor da prestação, sem incidência de juros, correção ou perdas e danos.",
                    "D": "O inadimplemento absoluto exige necessariamente prévia interpelação judicial ou extrajudicial do devedor para se configurar.",
                    "E": "A purgação do inadimplemento absoluto pode ocorrer a qualquer tempo, desde que o devedor comprove força maior."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 389, art. 394 e art. 395 do Código Civil."
                question_data["explanation"] = (
                    f"A alternativa A diferencia corretamente inadimplemento absoluto (prestação impossível ou inútil ao credor) da mora (atraso culposo "
                    f"em que a prestação ainda é possível e útil). A alternativa B erra porque no inadimplemento absoluto não há mais falar em cumprimento "
                    f"forçado da prestação original (já impossível). A alternativa C erra porque o art. 389 impõe perdas e danos, juros e correção."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} deveria entregar determinado bem a {v['credor']} na data do vencimento, mas deixou de fazê-lo. "
                    f"A prestação ainda é possível. No entanto, {v['credor']} declara que a prestação perdeu a utilidade em razão do atraso. "
                    f"Considerando as regras do Código Civil sobre inadimplemento, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "O credor pode recusar a prestação se esta, por sua utilidade, não mais lhe aproveitar, caso em que o devedor pagará perdas e danos.",
                    "B": "O credor é obrigado a aceitar a prestação em qualquer caso, pois a mora não se converte em inadimplemento absoluto sem autorização judicial.",
                    "C": "O devedor pode purgar a mora a qualquer tempo, independentemente da utilidade da prestação para o credor.",
                    "D": "A inutilidade superveniente da prestação para o credor extingue a obrigação sem responsabilidade para o devedor.",
                    "E": "O inadimplemento absoluto só se configura se houver impossibilidade física, e não mera inutilidade da prestação."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 394 e Art. 395, parágrafo único, do Código Civil."
                question_data["explanation"] = (
                    f"O art. 395, parágrafo único, do CC dispõe: 'Se a prestação, devido ao atraso, se tornar inútil ao credor, este poderá "
                    f"enjeitá-la e exigir perdas e danos'. A mora se converte em inadimplemento absoluto quando a prestação perde a utilidade para o credor."
                )

    # -------------------------------------------------------------
    # 16c. PERDAS E DANOS (Arts. 402 - 405)
    # -------------------------------------------------------------
    elif subject == "Perdas e danos":
        question_data["article"] = "Art. 402, Art. 403, Art. 404, Art. 405 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) Em decorrência do inadimplemento contratual de {v['devedor']}, {v['credor']} sofreu prejuízo de dois tipos: "
                f"(i) desembolsou {v['valor']} para contratar terceiro para concluir o serviço (dano emergente) e (ii) deixou de lucrar {v['valor']} "
                f"em razão do atraso (lucros cessantes). Segundo o Código Civil, ambos os componentes integram as perdas e danos, "
                f"desde que sejam consequência direta e imediata do inadimplemento."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "A"
            question_data["legal_basis"] = "Art. 402 do Código Civil."
            question_data["explanation"] = (
                f"O art. 402 do CC dispõe que 'salvo as exceções expressamente previstas em lei, as perdas e danos devidas ao credor abrangem, "
                f"além do que ele efetivamente perdeu (dano emergente), o que razoavelmente deixou de lucrar (lucros cessantes), desde que sejam "
                f"consequência direta e imediata do inadimplemento'. Portanto, a afirmação está CERTA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} descumpriu contrato de prestação de serviços firmado com {v['credor']} no valor de {v['valor']}. "
                    f"{v['credor']} alega ter sofrido prejuízos materiais e requer indenização. Considerando a disciplina das perdas e danos no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "As perdas e danos abrangem o dano emergente e os lucros cessantes, desde que consequência direta e imediata do inadimplemento ou do fato lesivo, apurados em liquidação de sentença.",
                    "B": "Os lucros cessantes limitam-se ao que o credor deixou de lucrar exclusivamente com a obrigação descumprida, vedada a indenização por oportunidades perdidas além do vínculo contratual.",
                    "C": "O devedor respede por todos os prejuízos sofridos pelo credor, ainda que remotos, desde que decorrentes do inadimplemento.",
                    "D": "Nas perdas e danos decorrentes de responsabilidade contratual, os juros de mora contam-se exclusivamente a partir da citação inicial.",
                    "E": "O valor da indenização por perdas e danos limita-se ao montante da obrigação principal, não podendo excedê-lo."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 402, Art. 403, Art. 404 e Art. 405 do Código Civil."
                question_data["explanation"] = (
                    f"A alternativa A descreve corretamente a composição das perdas e danos (art. 402: dano emergente + lucros cessantes), "
                    f"com apuração em liquidação de sentença (art. 403). A alternativa B erra ao restringir indevidamente os lucros cessantes. "
                    f"A alternativa C erra porque a indenização abrange apenas os danos diretos e imediatos (art. 403), excluindo danos remotos. "
                    f"A alternativa D erra porque os juros de mora contam-se da citação apenas na responsabilidade extracontratual; na contratual, "
                    f"contam-se do vencimento (art. 405)."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) Em decorrência do inadimplemento de {v['devedor']}, {v['credor']} contratou um terceiro para concluir "
                    f"o serviço de {v['contrato']}, ao custo de {v['valor']}, valor superior ao que havia contratado originalmente. "
                    f"Além disso, {v['credor']} alega que deixou de lucrar o equivalente por mês enquanto o serviço não foi concluído. "
                    f"Considerando a disciplina das perdas e danos, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "O credor tem direito apenas ao valor que pagou a terceiro, excluídos lucros cessantes, por se tratar de dano indireto.",
                    "B": "As perdas e danos abrangem o dano emergente e o que o credor razoavelmente deixou de lucrar, desde que consequência direta e imediata do inadimplemento.",
                    "C": "Os juros de mora na responsabilidade contratual contam-se da citação inicial, enquanto na extracontratual contam-se do evento danoso.",
                    "D": "O devedor responde por todos os danos, ainda que remotos, respondendo pela integralidade do prejuízo sofrido pelo credor.",
                    "E": "O lucro cessante exige prova inequívoca do valor que o credor efetivamente teria auferido, sendo vedada a estimativa judicial."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 402 e Art. 403 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 402 do CC define as perdas e danos como o que o credor efetivamente perdeu (dano emergente) e o que razoavelmente deixou de lucrar "
                    f"(lucros cessantes), desde que consequência direta e imediata do inadimplemento (art. 403). Os juros de mora na responsabilidade contratual "
                    f"contam-se do vencimento (art. 405, CC), não da citação."
                )

    # -------------------------------------------------------------
    # 17. JUROS LEGAIS (Arts. 406 - 407)
    # -------------------------------------------------------------
    elif subject == "Juros legais":
        question_data["article"] = "Art. 406 e Art. 407 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) Quando os juros moratórios não forem convencionados no contrato de {v['contrato']} entre {v['devedor']} e {v['credor']}, "
                f"eles deverão ser fixados de acordo com a taxa em vigor para a mora do pagamento de impostos devidos à Fazenda Nacional."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "A"
            question_data["legal_basis"] = "Art. 406 do Código Civil."
            question_data["explanation"] = (
                f"O art. 406 do CC estatui: 'Quando os juros moratórios não forem convencionados, ou o forem sem taxa estipulada, ou provierem "
                f"de determinação da lei, serão fixados segundo a taxa que estiver em vigor para a mora do pagamento de impostos devidos à Fazenda Nacional'. "
                f"Portanto, a afirmação está CERTA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) Em uma ação judicial decorrente do inadimplemento de contrato de prestação de serviços no valor de {v['valor']}, "
                    f"o juiz deve arbitrar os juros de mora incidentes sobre a condenação. Considerando o regramento de juros legais do Código Civil:"
                )
                question_data["options"] = {
                    "A": "Os juros moratórios só são devidos se o credor comprovar que sofreu prejuízo material efetivo com o atraso.",
                    "B": "Ainda que não se alegue prejuízo, o credor tem direito aos juros de mora, que se contam assim às dívidas em dinheiro, como às prestações de outra natureza, uma vez que lhes esteja estimado o valor pecuniário.",
                    "C": "Os juros legais são de no máximo 0,5% ao mês, sendo proibida a aplicação da taxa referencial Selic sob qualquer pretexto.",
                    "D": "Os juros de mora fluem a partir do vencimento apenas nas obrigações decorrentes de ato ilícito extracontratual.",
                    "E": "O credor que receber o pagamento da dívida principal sem ressalva de juros mantém o direito de cobrá-los autonomamente em ação própria posterior."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 407 do Código Civil."
                question_data["explanation"] = (
                    f"Conforme o art. 407 do CC, os juros de mora são devidos independentemente da alegação ou comprovação de prejuízo pelo credor. "
                    f"Aplicam-se a obrigações pecuniárias e a outras obrigações avaliáveis em dinheiro."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['credor']} ajuizou ação contra {v['devedor']} cobrando o valor de {v['valor']} referente a {v['contrato']}, "
                    f"com juros de mora desde o vencimento. O contrato não estipulou taxa de juros moratórios. "
                    f"Considerando as regras de juros legais no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "Os juros de mora serão fixados segundo a taxa em vigor para a mora do pagamento de impostos devidos à Fazenda Nacional (art. 406, CC).",
                    "B": "Na ausência de taxa convencionada, os juros moratórios são de 1% ao mês, conforme a lei de usura.",
                    "C": "Os juros legais são de 6% ao ano, aplicando-se o Código Comercial supletivamente.",
                    "D": "O juiz fixará os juros de mora com base na taxa média de mercado divulgada pelo Banco Central.",
                    "E": "Não havendo taxa estipulada, o credor tem direito apenas à correção monetária, sem incidência de juros."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 406 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 406 do CC determina que, na falta de convenção ou de taxa estipulada, os juros moratórios serão fixados segundo a taxa "
                    f"em vigor para a mora do pagamento de impostos devidos à Fazenda Nacional (atualmente, a taxa Selic para fins de juros moratórios). "
                    f"O art. 407 do CC dispõe que os juros são devidos independentemente de prova de prejuízo."
                )

    # -------------------------------------------------------------
    # 18. CLÁUSULA PENAL (Arts. 408 - 416)
    # -------------------------------------------------------------
    elif subject == "Cláusula penal":
        question_data["article"] = "Art. 408 a Art. 416 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) Se no contrato de {v['contrato']} entre {v['devedor']} e {v['credor']} houver cláusula penal compensatória pactuada, "
                f"o credor poderá exigir cumulativamente o cumprimento da obrigação principal e o pagamento integral da multa em caso de inadimplemento total."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "B"
            question_data["legal_basis"] = "Art. 410 do Código Civil."
            question_data["explanation"] = (
                f"A cláusula penal compensatória serve como pré-fixação de perdas e danos para o inadimplemento total. O art. 410 do CC determina "
                f"que 'quando se estipular a cláusula penal para o caso de total inadimplemento da obrigação, esta converter-se-á em alternativa para o credor', "
                f"sendo vedada a cumulação. A cumulação só é permitida na cláusula penal moratória (art. 411, CC). Portanto, a afirmação está ERRADA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} celebrou contrato de prestação de serviços com {v['credor']} prevendo cláusula penal no montante de R$ 50.000,00 "
                    f"para o caso de inadimplemento absoluto. O valor total da obrigação principal era de R$ 40.000,00. "
                    f"Diante das disposições do Código Civil sobre cláusula penal, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "A cláusula penal pactuada é totalmente válida, uma vez que a autonomia de vontade permite fixar multa em qualquer montante.",
                    "B": "O valor da cláusula penal não pode exceder o da obrigação principal; portanto, o montante da multa deve ser reduzido a R$ 40.000,00.",
                    "C": "O credor pode cobrar perdas e danos excedentes ao valor da cláusula penal compensatória, mesmo sem qualquer previsão contratual nesse sentido.",
                    "D": "A penalidade deve ser reduzida equitativamente pelo juiz se a obrigação principal tiver sido cumprida em parte, ou se o montante for manifestamente excessivo, sendo esta uma faculdade exclusiva do juiz que depende de pedido do réu.",
                    "E": "Incorrido o devedor em mora, o credor deve provar o prejuízo sofrido para fazer jus ao recebimento do valor da cláusula penal."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 412, Art. 413 e Art. 416 do Código Civil."
                question_data["explanation"] = (
                    f"Segundo o art. 412 do CC, 'o valor da cominação imposta na cláusula penal não pode exceder o da obrigação principal'. Logo, "
                    f"a multa compensatória de R$ 50.000,00 deve ser reduzida para R$ 40.000,00. A redução judicial do art. 413 é de ordem pública "
                    f"e deve ser feita de ofício pelo juiz, não sendo mera faculdade (eliminando a letra D). Para exigir a cláusula penal, não é necessário "
                    f"provar prejuízo (art. 416, CC) - eliminando a letra E."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} atrasou o pagamento de {v['contrato']} no valor de {v['valor']} em 20 dias. "
                    f"O contrato prevê cláusula penal moratória de 2% sobre o valor da prestação em atraso. "
                    f"Considerando a diferença entre cláusula penal compensatória e moratória no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": "O credor pode exigir cumulativamente o pagamento da prestação principal e a cláusula penal moratória, pois esta destina-se a punir o retardamento sem prejuízo do adimplemento da obrigação principal.",
                    "B": "O credor deve optar entre a cláusula penal ou o cumprimento forçado, não podendo cumulá-los em nenhuma hipótese.",
                    "C": "A cláusula penal moratória é ilícita, pois o Código Civil só admite a cláusula penal compensatória para o inadimplemento absoluto.",
                    "D": "O valor da cláusula penal, seja compensatória ou moratória, não pode ultrapassar 10% do valor da obrigação principal.",
                    "E": "A cláusula penal compensatória converte a obrigação em alternativa para o credor, que pode exigir a prestação principal ou a multa, mas nunca cumulativamente."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 409, Art. 410 e Art. 411 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 411 do CC estabelece: 'Quando se estipular a cláusula penal para o caso de mora, o credor terá direito de exigir "
                    f"a satisfação da prestação principal e, cumulativamente, a multa estipulada'. Já o art. 410 disciplina a cláusula penal "
                    f"compensatória (para inadimplemento absoluto), que converte a obrigação em alternativa, vedando a cumulação."
                )

    # -------------------------------------------------------------
    # 19. ARRAS OU SINAL (Arts. 417 - 420)
    # -------------------------------------------------------------
    elif subject == "Arras ou sinal":
        question_data["article"] = "Art. 417 a Art. 420 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) Se no contrato de compromisso de compra e venda celebrado entre {v['devedor']} e {v['credor']} for estipulado o direito "
                f"de arrependimento para qualquer das partes, as arras possuem caráter puramente penitencial, servindo de indenização máxima, "
                f"sem direito a indenização suplementar."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "A"
            question_data["legal_basis"] = "Art. 420 do Código Civil."
            question_data["explanation"] = (
                f"O art. 420 do CC prevê que, se no contrato for estipulado o direito de arrependimento, as arras ou sinal terão função unicamente "
                f"indenizatória (arras penitenciais). Quem as deu as perderá em benefício da outra parte; quem as recebeu as devolverá mais o equivalente. "
                f"E o artigo conclui: 'em ambos os casos não haverá direito a indenização suplementar'. Portanto, a afirmação está CERTA."
            )
        else:
            if variant == 0:
                question_data["enunciado"] = (
                    f"({bank}) {v['devedor']} assinou contrato de promessa de compra e venda de imóvel com {v['credor']}, entregando a quantia de R$ 20.000,00 "
                    f"a título de arras confirmatórias. O contrato não prevê direito de arrependimento. Posteriormente, {v['devedor']} (devedor) "
                    f"desiste do negócio e deixa de pagar as parcelas pactuadas, operando o inadimplemento culposo. À luz do Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"{v['credor']} pode reter as arras de R$ 20.000,00 e, caso o prejuízo real seja superior, postular em juízo indenização suplementar.",
                    "B": f"As arras confirmatórias devem ser devolvidas a {v['devedor']} em dobro, respondendo {v['credor']} por perdas e danos.",
                    "C": f"Como o contrato não prevê direito de arrependimento, as arras operam como arras penitenciais, sendo vedado pleitear qualquer valor adicional.",
                    "D": f"Pelo inadimplemento de {v['devedor']}, {v['credor']} é obrigado a aceitar a rescisão contratual sem poder exigir a execução do contrato.",
                    "E": f"Se a parte que deu as arras ({v['devedor']}) der causa ao inadimplemento, a outra ({v['credor']}) terá as arras devolvidas mais o equivalente."
                }
                question_data["gabarito"] = "A"
                question_data["legal_basis"] = "Art. 418 e Art. 419 do Código Civil."
                question_data["explanation"] = (
                    f"Trata-se de arras confirmatórias (art. 418, CC). Se a parte que deu as arras der causa à inexecução, a outra poderá reter as arras "
                    f"(art. 418). E o art. 419 dispõe que a parte inocente pode pedir indenização suplementar, se provar maior prejuízo, valendo as "
                    f"arras como taxa mínima da indenização."
                )
            else:
                question_data["enunciado"] = (
                    f"({bank}) {v['credor']} e {v['devedor']} celebraram contrato de compra e venda, tendo {v['devedor']} entregue "
                    f"R$ 10.000,00 a título de arras, com cláusula expressa de direito de arrependimento para ambas as partes. "
                    f"{v['credor']} exerce o direito de arrependimento. Considerando a disciplina das arras no Código Civil, assinale a opção correta:"
                )
                question_data["options"] = {
                    "A": f"O credor {v['credor']} deve devolver as arras em dobro (R$ 20.000,00), sem direito a indenização suplementar.",
                    "B": f"As arras penitenciais autorizam o arrependimento: quem as deu ({v['devedor']}) perde-as; quem as recebeu ({v['credor']}) restitui-as em dobro, não havendo direito a indenização suplementar.",
                    "C": f"O direito de arrependimento é exclusivo do comprador, não podendo o vendedor {v['credor']} exercê-lo.",
                    "D": f"Com o arrependimento, as arras são perdidas em favor da parte que não se arrependeu, mas esta pode pleitear indenização suplementar se provar prejuízo maior.",
                    "E": f"O exercício do direito de arrependimento extingue o contrato, mas a parte que se arrependeu responde por perdas e danos independentemente das arras."
                }
                question_data["gabarito"] = "B"
                question_data["legal_basis"] = "Art. 420 do Código Civil."
                question_data["explanation"] = (
                    f"O art. 420 do CC dispõe: 'Se no contrato for estipulado o direito de arrependimento para qualquer das partes, as arras ou sinal "
                    f"têm função unicamente indenizatória. Neste caso, quem as deu as perderá em benefício da outra parte; e quem as recebeu as devolverá "
                    f"em dobro, e, em ambos os casos, não haverá direito a indenização suplementar'. Trata-se das arras penitenciais."
                )
            
    # -------------------------------------------------------------
    # 20. DEFAULT / FALLBACK PARA OS DEMAIS TEMAS DO CC (ARTS 304 - 420)
    # -------------------------------------------------------------
    else:
        # Fallback genérico para cobrir qualquer tema faltante com padrão civilista robusto
        question_data["article"] = "Art. 308 e 313 do Código Civil"
        if is_cespe:
            question_data["enunciado"] = (
                f"({bank}) O credor de uma obrigação pecuniária no valor de {v['valor']} é obrigado a receber prestação diversa da que lhe é devida "
                f"caso o bem oferecido pelo devedor {v['devedor']} possua valor de mercado expressamente superior ao do débito contratado."
            )
            question_data["options"] = {"A": "CERTO", "B": "ERRADO"}
            question_data["gabarito"] = "B"
            question_data["legal_basis"] = "Art. 313 do Código Civil."
            question_data["explanation"] = (
                f"De acordo com o art. 313 do Código Civil, 'o credor não pode ser obrigado a receber prestação diversa da que lhe é devida, "
                f"ainda que mais valiosa'. Logo, a obrigação não pode ser alterada unilateralmente pelo devedor. A afirmação está ERRADA."
            )
        else:
            question_data["enunciado"] = (
                f"({bank}) {v['devedor']} firmou com {v['credor']} um contrato de {v['contrato']} com vencimento para o dia de hoje. "
                f"No ato do pagamento, o devedor insiste em entregar um objeto diferente do estipulado originalmente, provando documentalmente "
                f"que o objeto substituto possui valor de mercado muito superior à dívida de {v['valor']}. Conforme o Código Civil:"
            )
            question_data["options"] = {
                "A": f"O credor {v['credor']} é obrigado a aceitar o objeto substituto sob pena de incorrer em mora do credor.",
                "B": f"O credor não pode ser obrigado a receber prestação diversa da que lhe é devida, ainda que mais valiosa.",
                "C": "O pagamento com objeto mais valioso extingue a dívida imediatamente por compensação forçada.",
                "D": "O devedor tem o direito de impor a substituição judicialmente por meio de ação de consignação.",
                "E": "O contrato é rescindido automaticamente por culpa do credor se ele se recusar a receber o bem de maior valor."
            }
            question_data["gabarito"] = "B"
            question_data["legal_basis"] = "Art. 313 do Código Civil."
            question_data["explanation"] = (
                f"O art. 313 consagra o princípio da identidade da coisa devida, estabelecendo expressamente que o credor não é obrigado a aceitar "
                f"prestação diversa da devida, mesmo que de maior valor. O adimplemento exige exatidão no objeto."
            )
            
    return question_data
