import json
import uuid
from pathlib import Path

SEED_FILE = Path(__file__).resolve().parent.parent / "database" / "seed_questions.json"

OAB_QUESTIONS = [
    # ============================================================
    # 1. PAGAMENTO - GERAL (Arts. 304-420 - visão geral)
    # ============================================================
    {
        "subject": "Pagamento - Geral",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB XXXVIII) No tocante ao pagamento, assinale a opção correta.",
        "options": {
            "A": "O pagamento deve ser feito pessoalmente pelo devedor, sendo vedado o pagamento por terceiro, ainda que interessado.",
            "B": "O credor é obrigado a aceitar prestação diversa da que lhe é devida, se a prestação alternativa for mais valiosa.",
            "C": "Se o pagamento for feito por terceiro interessado, extingue-se a obrigação e opera-se a sub-rogação nos direitos do credor.",
            "D": "O pagamento em dinheiro deve ser feito em moeda estrangeira se houver previsão contratual de escala móvel."
        },
        "gabarito": "C",
        "article": "Art. 304 e Art. 313 CC",
        "legal_basis": "Arts. 304, 305, 313, 346, III do Código Civil.",
        "explanation": "O art. 304 autoriza o pagamento por qualquer interessado na extinção da dívida. O terceiro interessado (fiador, avalista) que paga sub-roga-se nos direitos do credor (art. 346, III). O credor não é obrigado a receber prestação diversa (art. 313) e o pagamento em dinheiro deve ser em moeda nacional corrente (art. 315)."
    },
    {
        "subject": "Pagamento - Geral",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB XXXVIII) Em relação ao pagamento por terceiro, assinale a alternativa correta.",
        "options": {
            "A": "O terceiro não interessado que paga a dívida em seu próprio nome sub-roga-se nos direitos do credor.",
            "B": "O terceiro interessado que paga a dívida sub-roga-se nos direitos do credor.",
            "C": "O terceiro não interessado não tem direito de reembolso se pagar a dívida em seu próprio nome.",
            "D": "O pagamento feito por terceiro, independentemente de ser interessado, não admite sub-rogação."
        },
        "gabarito": "B",
        "article": "Art. 304, 305 e 346 CC",
        "legal_basis": "Arts. 304, 305 e 346, III do Código Civil.",
        "explanation": "O terceiro interessado que paga a dívida sub-roga-se de pleno direito nos direitos do credor (art. 346, III). Já o terceiro não interessado que paga em seu próprio nome tem direito a reembolso, mas não se sub-roga (art. 305)."
    },
    {
        "subject": "Pagamento - Geral",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB XXXIX) Assinale a opção que apresenta hipótese de pagamento indevido.",
        "options": {
            "A": "O devedor paga dívida vencida antes de ser cobrado judicialmente.",
            "B": "O devedor paga dívida já prescrita, desconhecendo a prescrição.",
            "C": "O devedor paga ao credor putativo de boa-fé.",
            "D": "O terceiro não interessado paga a dívida em nome próprio, sem oposição do devedor."
        },
        "gabarito": "B",
        "article": "Arts. 876 e 877 CC",
        "legal_basis": "Arts. 876 e 877 do Código Civil.",
        "explanation": "O pagamento indevido ocorre quando se paga o que não é devido (art. 876). O pagamento de dívida prescrita, quando desconhecida a prescrição, é pagamento indevido, pois a prescrição extingue a pretensão. O devedor tem direito de repetir o que pagou indevidamente (ação de repetição do indébito)."
    },
    {
        "subject": "Pagamento - Geral",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB XLII) Sobre as obrigações indivisíveis, assinale a afirmativa correta.",
        "options": {
            "A": "Se houver pluralidade de devedores em obrigação indivisível, cada devedor é obrigado pela dívida toda.",
            "B": "A indivisibilidade se extingue com a opção por perdas e danos, pois a obrigação se converte em divisível.",
            "C": "Em caso de pluralidade de credores em obrigação indivisível, cada credor só pode exigir a sua quota-parte.",
            "D": "O devedor pode escolher pagar a apenas um dos credores, extinguindo parcialmente a obrigação."
        },
        "gabarito": "B",
        "article": "Art. 259 CC",
        "legal_basis": "Art. 259 do Código Civil.",
        "explanation": "Segundo o art. 259, 'se a obrigação for indivisível e houver dois ou mais devedores, cada um será obrigado pela dívida toda'. No entanto, a opção por perdas e danos (quando a indivisibilidade se perde pela conversão em prestação pecuniária) faz cessar a indivisibilidade, tornando a obrigação divisível entre os devedores."
    },
    {
        "subject": "Pagamento - Geral",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB XLI) Em relação à cessão de crédito, assinale a alternativa correta.",
        "options": {
            "A": "A cessão de crédito não produz efeitos em relação ao devedor se não houver notificação, ainda que por cláusula contratual expressa.",
            "B": "O devedor pode opor ao cessionário as exceções que lhe competirem, bem como as que, no momento em que veio a ter conhecimento da cessão, já possuía contra o cedente.",
            "C": "A cessão de crédito transfere ao cessionário apenas o crédito, mantendo-se as garantias com o cedente.",
            "D": "O devedor que paga ao cedente antes da notificação da cessão não se libera, devendo pagar novamente ao cessionário."
        },
        "gabarito": "B",
        "article": "Arts. 286 e 290 CC",
        "legal_basis": "Arts. 286, 290 e 294 do Código Civil.",
        "explanation": "Conforme o art. 290, a cessão não tem eficácia perante o devedor sem sua notificação. O art. 294 permite ao devedor opor ao cessionário as exceções que já tinha contra o cedente antes da cessão. As garantias acompanham o crédito (art. 287). O pagamento feito ao cedente antes da notificação é liberatório (art. 292)."
    },
    {
        "subject": "Pagamento - Geral",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB XXXVI) Sobre a solidariedade ativa e passiva nas obrigações, assinale a opção correta.",
        "options": {
            "A": "Na solidariedade ativa, cada credor pode exigir do devedor a dívida por inteiro, mas o pagamento feito a um dos credores extingue a dívida até o montante do que recebeu.",
            "B": "Na solidariedade passiva, cada devedor é obrigado pela dívida toda, mas o pagamento integral por um deles extingue a solidariedade, subsistindo o direito de regresso.",
            "C": "Na solidariedade passiva, o pagamento parcial feito por um devedor não extingue a solidariedade quanto ao saldo remanescente.",
            "D": "Na solidariedade ativa, se um dos credores remitir a dívida, a obrigação se extingue integralmente, sem direito de regresso dos demais credores."
        },
        "gabarito": "B",
        "article": "Arts. 267 e 275 CC",
        "legal_basis": "Arts. 267, 275, 276 e 277 do Código Civil.",
        "explanation": "Na solidariedade passiva (art. 275), qualquer devedor pode ser cobrado pela dívida toda. O que pagar integralmente extingue a obrigação e tem direito de regresso contra os demais (art. 283). O pagamento parcial não extingue a solidariedade quanto ao saldo (art. 277). Na solidariedade ativa, a remissão feita por um credor extingue apenas sua quota-parte (art. 272)."
    },
    {
        "subject": "Pagamento - Geral",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB XXXVII) Considerando as regras sobre obrigações indivisíveis, assinale a opção correta.",
        "options": {
            "A": "Na obrigação indivisível, a escolha do devedor pelo pagamento em perdas e danos torna a obrigação divisível automaticamente.",
            "B": "O devedor de obrigação indivisível com pluralidade de credores pode pagar a qualquer um deles, mas precisa do consentimento de todos para se liberar.",
            "C": "Se a obrigação indivisível tiver por objeto coisa certa que se perde sem culpa dos devedores, a obrigação se extingue para todos.",
            "D": "O credor de obrigação indivisível pode exigir o cumprimento de apenas parte da prestação, fracionando o objeto."
        },
        "gabarito": "A",
        "article": "Arts. 235, 236, 257 e 259 CC",
        "legal_basis": "Arts. 235, 236 e 259 do Código Civil.",
        "explanation": "O art. 236 dispõe que, convertida a obrigação em perdas e danos, cessa a indivisibilidade. Isso ocorre porque a prestação pecuniária é essencialmente divisível. O art. 235 trata da perda da coisa sem culpa (extingue a obrigação). Nas obrigações indivisíveis com pluralidade de credores, o devedor deve pagar a todos conjuntamente (art. 260)."
    },
    {
        "subject": "Pagamento - Geral",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Em relação ao pagamento e suas regras gerais, assinale a alternativa correta.",
        "options": {
            "A": "O pagamento feito de boa-fé ao credor putativo é válido, ainda que depois se prove que não era credor.",
            "B": "O credor é obrigado a aceitar pagamento antecipado, desde que o devedor ofereça desconto proporcional.",
            "C": "O pagamento feito por terceiro não interessado, sem oposição do devedor, não gera direito a reembolso.",
            "D": "A quitação dada pelo credor ao devedor não faz presumir o pagamento, devendo ser sempre comprovado por outros meios."
        },
        "gabarito": "A",
        "article": "Art. 309 CC",
        "legal_basis": "Art. 309 do Código Civil.",
        "explanation": "O art. 309 do CC consagra a teoria da aparência: 'O pagamento feito de boa-fé ao credor putativo é válido, ainda provado depois que não era credor'. Trata-se de proteção à boa-fé do devedor que se guia pela aparência de legitimidade de quem recebe o pagamento."
    },

    # ============================================================
    # 2. QUEM DEVE PAGAR (Arts. 304 - 307)
    # ============================================================
    {
        "subject": "Quem deve pagar",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre o pagamento por terceiro, assinale a alternativa correta.",
        "options": {
            "A": "Qualquer interessado na extinção da dívida pode pagá-la, sub-rogando-se nos direitos do credor.",
            "B": "O terceiro não interessado que paga a dívida em seu próprio nome tem direito de regresso, mas não se sub-roga nos direitos do credor.",
            "C": "O terceiro não interessado que paga a dívida antes do vencimento tem direito ao reembolso imediato.",
            "D": "O pagamento feito por terceiro, com oposição do devedor, obriga o devedor a reembolsá-lo, desde que o pagamento tenha sido útil."
        },
        "gabarito": "B",
        "article": "Arts. 305 e 306 CC",
        "legal_basis": "Arts. 305 e 306 do Código Civil.",
        "explanation": "O art. 305 estabelece que o terceiro não interessado que paga em seu próprio nome tem direito a se reembolsar, mas não se sub-roga. Se pagar antes do vencimento, só terá direito ao reembolso no vencimento. O art. 306 dispõe que, se o pagamento foi feito com desconhecimento ou oposição do devedor, este não é obrigado a reembolsar se tinha meios de ilidir a ação."
    },
    {
        "subject": "Quem deve pagar",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) O fiador de uma obrigação, diante do inadimplemento do devedor principal, decide pagar a dívida. Sobre essa hipótese, assinale a opção correta.",
        "options": {
            "A": "O fiador, por ser terceiro interessado, pode pagar a dívida e sub-roga-se nos direitos do credor.",
            "B": "O fiador não tem legitimidade para pagar, pois o pagamento é ato pessoal do devedor.",
            "C": "O fiador que paga a dívida não pode cobrar o devedor principal, pois a fiança é mera garantia acessória.",
            "D": "O fiador, por ser terceiro não interessado, tem apenas direito de reembolso, sem sub-rogação."
        },
        "gabarito": "A",
        "article": "Arts. 304 e 346, III CC",
        "legal_basis": "Arts. 304 e 346, III do Código Civil.",
        "explanation": "O fiador é terceiro interessado (art. 304, parágrafo único) e, ao pagar a dívida, sub-roga-se de pleno direito nos direitos do credor (art. 346, III). Pode cobrar do devedor principal o valor pago, com juros e correção, nos termos do art. 831."
    },
    {
        "subject": "Quem deve pagar",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) O avalista de uma dívida quitou integralmente o débito vencido. Sobre essa situação, assinale a alternativa correta.",
        "options": {
            "A": "O avalista, por ser terceiro não interessado, tem direito apenas ao reembolso, sem sub-rogação.",
            "B": "O avalista sub-roga-se nos direitos do credor, podendo executar o devedor principal pelas vias cabíveis.",
            "C": "O avalista não pode pagar a dívida, pois a obrigação cambial é personalíssima.",
            "D": "O pagamento feito pelo avalista não extingue a dívida, que subsiste contra o devedor principal."
        },
        "gabarito": "B",
        "article": "Arts. 304 e 346, III CC",
        "legal_basis": "Arts. 304, 346, III e 837 do Código Civil.",
        "explanation": "O avalista é terceiro interessado na extinção da dívida (art. 304). Ao pagar, sub-roga-se nos direitos do credor (art. 346, III), podendo exercer o direito de regresso contra o devedor principal. O aval é garantia cambiária que segue a mesma lógica da fiança quanto ao pagamento pelo garantidor."
    },
    {
        "subject": "Quem deve pagar",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Considerando as regras sobre o pagamento por terceiros no Código Civil, assinale a alternativa correta.",
        "options": {
            "A": "O terceiro não interessado que paga a dívida em seu próprio nome, com a oposição do devedor, não terá direito a reembolso se o devedor tinha meios de ilidir a ação.",
            "B": "O terceiro interessado que paga a dívida não se sub-roga nos direitos do credor, pois o pagamento extingue a obrigação de forma absoluta.",
            "C": "O devedor pode opor-se ao pagamento feito por terceiro não interessado, e a oposição invalida o pagamento.",
            "D": "O terceiro não interessado que paga a dívida antes do vencimento tem direito ao reembolso imediato do valor atualizado."
        },
        "gabarito": "A",
        "article": "Arts. 305 e 306 CC",
        "legal_basis": "Arts. 305 e 306 do Código Civil.",
        "explanation": "O art. 306 dispõe que 'se o terceiro pagar a dívida antes de ser ouvido o devedor, ou com oposição deste, não terá direito a reembolso, se o devedor tinha meios para ilidir a ação'. O art. 305, parágrafo único, prevê que o pagamento antecipado só dá direito ao reembolso no vencimento."
    },

    # ============================================================
    # 3. A QUEM SE DEVE PAGAR (Arts. 308 - 312)
    # ============================================================
    {
        "subject": "A quem se deve pagar",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Assinale a alternativa correta acerca de a quem se deve pagar.",
        "options": {
            "A": "O pagamento deve ser feito ao credor ou a quem de direito o represente, sendo válido o pagamento feito de boa-fé ao credor putativo.",
            "B": "O pagamento feito a credor incapaz de quitá-lo é sempre nulo, independentemente de prova de reversão em proveito do credor.",
            "C": "O pagamento feito ao credor que está impedido de receber, como na hipótese de penhora do crédito, é sempre ineficaz.",
            "D": "O credor putativo é aquele que, de má-fé, aparenta ser credor para receber indevidamente."
        },
        "gabarito": "A",
        "article": "Arts. 308 e 309 CC",
        "legal_basis": "Arts. 308, 309, 310 do Código Civil.",
        "explanation": "O art. 308 determina que o pagamento deve ser feito ao credor ou a quem o represente. O art. 309 valida o pagamento de boa-fé ao credor putativo. O art. 310 exige prova de reversão em proveito do credor para validar pagamento a incapaz. O art. 312 protege o pagamento de boa-fé a credor impedido de receber."
    },
    {
        "subject": "A quem se deve pagar",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Marcelo deve R$ 50.000,00 a Fernando. Por desconhecer que o crédito de Fernando havia sido penhorado em execução movida por terceiro, Marcelo paga a Fernando diretamente. Considerando essa situação, assinale a opção correta.",
        "options": {
            "A": "O pagamento é válido se Marcelo desconhecia a penhora e agiu de boa-fé.",
            "B": "O pagamento é nulo, pois a penhora torna o credor absolutamente incapaz de receber.",
            "C": "O pagamento só é válido se houver autorização judicial expressa.",
            "D": "O pagamento é anulável, cabendo ao credor penhorante ação anulatória."
        },
        "gabarito": "A",
        "article": "Art. 312 CC",
        "legal_basis": "Art. 312 do Código Civil.",
        "explanation": "O art. 312 dispõe: 'Se o devedor pagar ao credor, ignorando estar este impedido de receber, valerá o pagamento, se o devedor não tinha conhecimento da penhora ou do concurso de credores'. A boa-fé do devedor é protegida pela lei, sendo válido o pagamento."
    },
    {
        "subject": "A quem se deve pagar",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Em relação ao pagamento a credor incapaz, assinale a alternativa correta.",
        "options": {
            "A": "O pagamento feito a credor incapaz é inválido, salvo se o devedor provar que o valor reverteu em proveito do credor.",
            "B": "O pagamento feito a credor incapaz é plenamente válido, pois a capacidade do credor é irrelevante para o adimplemento.",
            "C": "O pagamento feito a credor incapaz é nulo de pleno direito, sem possibilidade de convalidação.",
            "D": "O pagamento feito a credor incapaz é anulável, dependendo de ação própria do representante legal."
        },
        "gabarito": "A",
        "article": "Art. 310 CC",
        "legal_basis": "Art. 310 do Código Civil.",
        "explanation": "Conforme o art. 310, 'Não vale o pagamento feito a quem se mostrava incapaz de quitá-lo, se o devedor não provar que reverteu em proveito do credor'. A regra protege o incapaz, mas admite prova de que o pagamento beneficiou efetivamente o credor."
    },

    # ============================================================
    # 4. OBJETO DO PAGAMENTO E SUA PROVA (Arts. 313 - 326)
    # ============================================================
    {
        "subject": "Objeto do pagamento e sua prova",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Quanto ao objeto do pagamento, assinale a alternativa correta.",
        "options": {
            "A": "O credor não é obrigado a receber prestação diversa da que lhe é devida, ainda que mais valiosa.",
            "B": "O credor é obrigado a aceitar pagamento parcial se o devedor alegar dificuldade financeira.",
            "C": "O devedor pode impor ao credor o recebimento de coisa diversa, desde que de valor equivalente.",
            "D": "O pagamento em dinheiro pode ser feito em moeda estrangeira, a critério do devedor."
        },
        "gabarito": "A",
        "article": "Arts. 313 e 314 CC",
        "legal_basis": "Arts. 313, 314 e 315 do Código Civil.",
        "explanation": "O art. 313 estabelece o princípio da identidade: o credor não é obrigado a receber prestação diversa da devida, ainda que mais valiosa. O art. 314 veda o pagamento parcial, salvo disposição contratual. O art. 315 determina que o pagamento em dinheiro seja feito em moeda corrente nacional."
    },
    {
        "subject": "Objeto do pagamento e sua prova",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Assinale a alternativa correta acerca da quitação no direito das obrigações.",
        "options": {
            "A": "A quitação deve indicar o valor pago, o nome do devedor e o título da dívida, podendo ser dada por instrumento particular.",
            "B": "A quitação dada pelo credor ao devedor não faz presumir o pagamento, que deve ser provado por outros meios.",
            "C": "A quitação é ato personalíssimo do credor, não podendo ser dada por procurador.",
            "D": "A quitação de dívida de alto valor exige escritura pública para sua validade."
        },
        "gabarito": "A",
        "article": "Arts. 319 e 320 CC",
        "legal_basis": "Arts. 319, 320 e 321 do Código Civil.",
        "explanation": "O art. 320 estabelece os requisitos da quitação: valor, nome do devedor, tempo e lugar do pagamento, com assinatura do credor. Pode ser dada por instrumento particular. O art. 319 admite que a quitação seja dada por mandatário. A quitação faz presumir o pagamento (art. 321)."
    },
    {
        "subject": "Objeto do pagamento e sua prova",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Em relação à prova do pagamento, assinale a alternativa correta.",
        "options": {
            "A": "O devedor que tem recibo do pagamento, mas não tem o título de crédito original, não pode exigir a quitação.",
            "B": "A presunção de pagamento decorrente da entrega do título ao devedor é relativa (juris tantum), admitindo prova em contrário.",
            "C": "O credor pode recusar-se a dar quitação, desde que fundamente o motivo.",
            "D": "A quitação é nula se não especificar o valor exato pago, ainda que haja prova testemunhal."
        },
        "gabarito": "B",
        "article": "Arts. 320 e 324 CC",
        "legal_basis": "Arts. 320, 324 do Código Civil.",
        "explanation": "O art. 324 estabelece que a entrega do título ao devedor faz presumir o pagamento. Trata-se de presunção relativa (juris tantum), que admite prova em contrário. A quitação pode ser dada por recibo, e a recusa do credor em dar quitação autoriza o devedor a consignar (art. 335, III)."
    },

    # ============================================================
    # 5. LUGAR DO PAGAMENTO (Arts. 327 - 330)
    # ============================================================
    {
        "subject": "Lugar do pagamento",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre o lugar do pagamento, assinale a opção correta.",
        "options": {
            "A": "Na omissão do contrato, o pagamento deve ser feito no domicílio do devedor (obrigação quesível).",
            "B": "Na omissão do contrato, o pagamento deve ser feito no domicílio do credor (obrigação portável).",
            "C": "O credor pode exigir o pagamento em local diverso do pactuado se houver mudança de domicílio do devedor.",
            "D": "O pagamento em local diverso do convencionado é sempre nulo."
        },
        "gabarito": "A",
        "article": "Arts. 327 e 328 CC",
        "legal_basis": "Arts. 327, 328 e 329 do Código Civil.",
        "explanation": "O art. 327 determina que, na omissão, o pagamento deve ser feito no domicílio do devedor (obrigação quesível - o credor vai buscar). Na obrigação portável, o pagamento é feito no domicílio do credor (o devedor leva). O art. 328 trata de mudança de domicílio do credor. O art. 329 trata de despesas com mudança de local."
    },
    {
        "subject": "Lugar do pagamento",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Em relação ao lugar do pagamento nas obrigações, assinale a alternativa correta.",
        "options": {
            "A": "A obrigação quesível é aquela em que o pagamento deve ser feito no domicílio do credor.",
            "B": "A obrigação portável é aquela em que o pagamento deve ser feito no domicílio do devedor.",
            "C": "Na obrigação quesível, o credor deve procurar o devedor para receber o pagamento.",
            "D": "Se a obrigação for portável e o credor se mudar, o devedor arca com as despesas da mudança."
        },
        "gabarito": "C",
        "article": "Arts. 327 e 328 CC",
        "legal_basis": "Arts. 327 e 328 do Código Civil.",
        "explanation": "Na obrigação quesível, o pagamento é feito no domicílio do devedor - o credor vai buscar (art. 327). Na obrigação portável, o pagamento é feito no domicílio do credor - o devedor leva. Se o credor se muda, as despesas são por conta dele (art. 328)."
    },
    {
        "subject": "Lugar do pagamento",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Contrato de compra e venda estabelece que o pagamento será feito 'no domicílio do comprador'. O comprador mudou-se para outra cidade antes do vencimento. Assinale a alternativa correta.",
        "options": {
            "A": "O pagamento deve ser feito no novo domicílio do devedor, por conta deste as despesas adicionais.",
            "B": "O pagamento deve ser feito no novo domicílio do devedor, por conta do credor as despesas adicionais.",
            "C": "O pagamento deve ser feito no domicílio anterior do devedor, pois o local foi convencionado.",
            "D": "O credor pode exigir o pagamento no seu próprio domicílio, independentemente da mudança."
        },
        "gabarito": "B",
        "article": "Arts. 327 e 328 CC",
        "legal_basis": "Arts. 327 e 328 do Código Civil.",
        "explanation": "Tratando-se de obrigação quesível (pagamento no domicílio do devedor), se o devedor se muda, a obrigação continua sendo quesível, mas as despesas com a mudança correm por conta do credor (art. 328). O credor não pode se beneficiar da mudança do devedor para impor-lhe custos adicionais."
    },

    # ============================================================
    # 6. TEMPO DO PAGAMENTO (Arts. 331 - 333)
    # ============================================================
    {
        "subject": "Tempo do pagamento",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre o tempo do pagamento, assinale a alternativa correta.",
        "options": {
            "A": "O devedor pode pagar antes do vencimento, salvo se houver estipulação de prazo em benefício do credor.",
            "B": "O devedor não pode pagar antes do vencimento em nenhuma hipótese.",
            "C": "O credor pode exigir o pagamento antes do vencimento se houver fundado receio de insolvência do devedor.",
            "D": "O prazo estabelecido em benefício do devedor pode ser renunciado pelo credor a qualquer tempo."
        },
        "gabarito": "A",
        "article": "Arts. 331 e 332 CC",
        "legal_basis": "Arts. 331 e 332 do Código Civil.",
        "explanation": "O art. 331 estabelece que o devedor pode pagar antes do vencimento, salvo se o prazo foi estipulado em benefício exclusivo do credor ou de ambos (art. 332). Se o prazo for em benefício do devedor, este pode renunciá-lo e pagar antecipadamente. O credor só pode exigir antecipação nas hipóteses legais (art. 333)."
    },
    {
        "subject": "Tempo do pagamento",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Assinale a alternativa correta acerca do vencimento da obrigação.",
        "options": {
            "A": "O vencimento da obrigação pode ser antecipado nos casos de insolvência do devedor ou falência.",
            "B": "O prazo estabelecido em benefício do credor pode ser renunciado pelo devedor.",
            "C": "A obrigação sem prazo é inexigível até que o credor a declare vencida.",
            "D": "A antecipação do vencimento depende de autorização judicial em qualquer hipótese."
        },
        "gabarito": "A",
        "article": "Arts. 331, 332 e 333 CC",
        "legal_basis": "Arts. 331, 332 e 333 do Código Civil.",
        "explanation": "O art. 333 prevê hipóteses de vencimento antecipado: falência ou insolvência do devedor, garantias deterioradas sem reforço etc. Sem prazo, a obrigação é exigível de imediato (art. 331). O prazo em benefício do credor não pode ser renunciado pelo devedor (art. 332)."
    },
    {
        "subject": "Tempo do pagamento",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) A respeito do vencimento antecipado das obrigações, assinale a opção correta.",
        "options": {
            "A": "A insolvência do devedor não autoriza o vencimento antecipado, pois o patrimônio ainda responde pela dívida.",
            "B": "A deterioração das garantias reais, sem culpa do devedor, autoriza o credor a exigir o vencimento antecipado.",
            "C": "A cessão de crédito transfere automaticamente o benefício do prazo ao cessionário, independentemente de notificação.",
            "D": "O prazo estabelecido em favor do devedor pode ser renunciado pelo credor a qualquer momento."
        },
        "gabarito": "B",
        "article": "Arts. 332 e 333 CC",
        "legal_basis": "Arts. 332 e 333 do Código Civil.",
        "explanation": "O art. 333, II, autoriza o vencimento antecipado se 'diminuídas por ato do devedor as garantias reais ou fidejussórias'. A insolvência também autoriza a antecipação (art. 333, I). O prazo em benefício do devedor só pode ser renunciado por ele. A cessão do crédito não altera o prazo (art. 286)."
    },

    # ============================================================
    # 7. CONSIGNAÇÃO EM PAGAMENTO (Arts. 334 - 345)
    # ============================================================
    {
        "subject": "Consignação em pagamento",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB XXXVII) Sobre a consignação em pagamento, assinale a alternativa correta.",
        "options": {
            "A": "A consignação em pagamento é cabível quando o credor não quiser receber o pagamento, recusar dar quitação ou estiver ausente.",
            "B": "A consignação só pode ser feita mediante depósito judicial, sendo vedado o depósito extrajudicial em banco oficial.",
            "C": "A consignação extingue a obrigação apenas após sentença judicial transitada em julgado.",
            "D": "A consignação não é cabível se houver dúvida sobre quem deve receber o pagamento."
        },
        "gabarito": "A",
        "article": "Art. 335 CC e art. 547 CPC",
        "legal_basis": "Art. 335 do Código Civil e arts. 539 e ss. do CPC.",
        "explanation": "O art. 335 do CC elenca as hipóteses de cabimento: I - credor não quiser receber; II - credor não der quitação; III - credor for desconhecido ou ausente; IV - houver dúvida sobre quem receber; V - pender litígio sobre o crédito. Admite-se consignação extrajudicial (art. 539 CPC) quando o débito for em dinheiro."
    },
    {
        "subject": "Consignação em pagamento",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Assinale a alternativa que apresenta hipótese de cabimento da consignação em pagamento.",
        "options": {
            "A": "O credor se recusa a receber o pagamento e a dar quitação na forma regular.",
            "B": "O devedor deseja pagar antes do vencimento, mas o credor exige o valor integral.",
            "C": "O credor deseja cobrar juros maiores que os contratados, e o devedor prefere consignar.",
            "D": "O devedor não concorda com a correção monetária aplicada pelo credor."
        },
        "gabarito": "A",
        "article": "Art. 335 CC",
        "legal_basis": "Art. 335, I e II do Código Civil.",
        "explanation": "O art. 335, I e II, autoriza a consignação quando o credor se recusa a receber ou não dá quitação. As demais hipóteses (III - ausência/desconhecimento; IV - dúvida; V - litígio) também autorizam. A mera divergência sobre valores não autoriza consignação - é necessário que o credor se recuse a receber o que é devido."
    },
    {
        "subject": "Consignação em pagamento",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Efetuada a consignação em pagamento, o credor é citado para levantar o depósito ou contestar. Sobre os efeitos, assinale a opção correta.",
        "options": {
            "A": "A consignação produz efeitos de pagamento desde a data do depósito em juízo.",
            "B": "A consignação só produz efeitos após o trânsito em julgado da sentença que a julgar procedente.",
            "C": "Enquanto não houver sentença, o devedor continua sujeito à mora e aos juros.",
            "D": "A consignação não extingue a obrigação se o credor não levantar o depósito."
        },
        "gabarito": "A",
        "article": "Art. 336 e 337 CC",
        "legal_basis": "Arts. 336, 337, 338 e 340 do Código Civil.",
        "explanation": "O art. 336 dispõe que a consignação extingue a obrigação. O art. 337 trata dos requisitos. O depósito judicial substitui o pagamento, liberando o devedor da mora desde a data do depósito (art. 338). O credor que não aceita nem contesta tem 30 dias para se manifestar (art. 340)."
    },

    # ============================================================
    # 8. PAGAMENTO COM SUB-ROGAÇÃO (Arts. 346 - 351)
    # ============================================================
    {
        "subject": "Pagamento com sub-rogação",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Assinale a alternativa correta acerca da sub-rogação legal no pagamento.",
        "options": {
            "A": "O terceiro interessado que paga a dívida sub-roga-se de pleno direito nos direitos do credor.",
            "B": "A sub-rogação legal depende de acordo entre as partes, não operando automaticamente.",
            "C": "O devedor que paga dívida de terceiro com garantia real não se sub-roga nos direitos do credor.",
            "D": "A sub-rogação legal transfere o crédito com todos os seus acessórios, exceto as garantias."
        },
        "gabarito": "A",
        "article": "Art. 346 CC",
        "legal_basis": "Art. 346 do Código Civil.",
        "explanation": "O art. 346 enumera as hipóteses de sub-rogação legal de pleno direito: I - credor que paga dívida do devedor comum; II - herdeiro que paga dívida do espólio; III - terceiro interessado que paga dívida pela qual era responsável. A sub-rogação opera automaticamente, transferindo crédito, garantias e acessórios (art. 349)."
    },
    {
        "subject": "Pagamento com sub-rogação",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre a sub-rogação convencional, assinale a alternativa correta.",
        "options": {
            "A": "A sub-rogação convencional depende de acordo expresso entre as partes, com declaração do devedor.",
            "B": "A sub-rogação convencional transfere ao novo credor todos os direitos, ações e garantias do crédito original.",
            "C": "A sub-rogação convencional não admite pagamento parcial, devendo o crédito ser integral.",
            "D": "A sub-rogação convencional não se aplica a obrigações de dar coisa certa."
        },
        "gabarito": "B",
        "article": "Art. 347 CC",
        "legal_basis": "Arts. 347 e 348 do Código Civil.",
        "explanation": "O art. 347 trata da sub-rogação convencional, que pode ser: I - pactuada entre credor e terceiro; II - declarada pelo devedor ao contratar novo empréstimo. A sub-rogação transfere ao sub-rogado todos os direitos, ações, privilégios e garantias do credor original (art. 349). O pagamento parcial é admitido (art. 351)."
    },
    {
        "subject": "Pagamento com sub-rogação",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Em relação à sub-rogação, assinale a alternativa correta.",
        "options": {
            "A": "Na sub-rogação legal, o pagamento parcial não sub-roga o pagador nos direitos do credor quanto à parte paga.",
            "B": "Havendo sub-rogação parcial, o credor original e o sub-rogado concorrem como credores, cada qual com seus respectivos direitos.",
            "C": "A sub-rogação convencional depende de autorização judicial para produzir efeitos.",
            "D": "A sub-rogação extingue o crédito original, criando nova obrigação entre devedor e sub-rogado."
        },
        "gabarito": "B",
        "article": "Arts. 348 e 351 CC",
        "legal_basis": "Arts. 348, 349 e 351 do Código Civil.",
        "explanation": "O art. 351 admite a sub-rogação parcial: 'O credor original, só em parte reembolsado, terá preferência ao sub-rogado, na cobrança do débito restante, se os bens do devedor não bastarem para saldar inteiramente o que a cada um se deve'. Na sub-rogação parcial, credor e sub-rogado concorrem como credores."
    },

    # ============================================================
    # 9. IMPUTAÇÃO DO PAGAMENTO (Arts. 352 - 355)
    # ============================================================
    {
        "subject": "Imputação do pagamento",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre a imputação do pagamento, assinale a alternativa correta.",
        "options": {
            "A": "A imputação do pagamento é direito do devedor, que pode indicar qual dívida quer pagar, se todas forem líquidas e vencidas.",
            "B": "A imputação do pagamento é sempre feita pelo credor, independentemente da vontade do devedor.",
            "C": "O devedor não pode imputar o pagamento em dívida líquida se houver dívida ilíquida.",
            "D": "A imputação do pagamento não admite regras legais subsidiárias, devendo ser sempre pactuada."
        },
        "gabarito": "A",
        "article": "Arts. 352 e 353 CC",
        "legal_basis": "Arts. 352 e 353 do Código Civil.",
        "explanation": "O art. 352 confere ao devedor o direito de imputar o pagamento, indicando qual dívida quer extinguir entre dívidas líquidas e vencidas do mesmo credor. Se o devedor não imputar, a imputação caberá ao credor (art. 353). As regras subsidiárias dos arts. 354 e 355 aplicam-se na falta de ambos."
    },
    {
        "subject": "Imputação do pagamento",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) O devedor, sem imputar o pagamento, paga parte das dívidas que possui com o mesmo credor. As dívidas são: uma com juros, uma com garantia real e uma mais antiga. Assinale a alternativa correta quanto à imputação legal.",
        "options": {
            "A": "A imputação recai primeiro sobre a dívida vencida mais antiga, depois a mais onerosa.",
            "B": "A imputação recai primeiro sobre a dívida mais onerosa entre as vencidas.",
            "C": "A imputação recai proporcionalmente sobre todas as dívidas existentes.",
            "D": "A imputação recai primeiro sobre a dívida com garantia real, depois a mais antiga."
        },
        "gabarito": "B",
        "article": "Arts. 354 e 355 CC",
        "legal_basis": "Arts. 354 e 355 do Código Civil.",
        "explanation": "Na falta de imputação pelo devedor e pelo credor, aplicam-se as regras legais: primeiro, imputa-se na dívida vencida mais antiga (art. 355); se forem da mesma natureza, proporcionalmente. O art. 354 determina que, entre dívidas vencidas, a imputação recai primeiro na mais onerosa (juros, garantia real)."
    },
    {
        "subject": "Imputação do pagamento",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Assinale a alternativa correta acerca da imputação do pagamento.",
        "options": {
            "A": "Se o devedor não imputar e a quitação for omissa quanto à imputação, esta recairá na dívida que o credor escolher entre as líquidas e vencidas.",
            "B": "A imputação feita pelo devedor não pode ser contestada pelo credor, sendo direito absoluto do devedor.",
            "C": "A imputação deve recair primeiro sobre o principal, depois sobre os juros e acessórios.",
            "D": "Não é possível imputar o pagamento em dívida ilíquida, mesmo que todas as partes concordem."
        },
        "gabarito": "C",
        "article": "Arts. 352 e 354 CC",
        "legal_basis": "Arts. 352, 353, 354 do Código Civil.",
        "explanation": "Conforme o art. 354, 'havendo capital e juros, a imputação primeiramente nos juros vencidos, e depois no capital, salvo estipulação em contrário'. O devedor imputa primeiro (art. 352), se não o fizer, o credor imputa (art. 353). Se ambos omitirem, aplicam-se as regras subsidiárias do art. 355."
    },

    # ============================================================
    # 10. DAÇÃO EM PAGAMENTO (Arts. 356 - 359)
    # ============================================================
    {
        "subject": "Dação em pagamento",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre a dação em pagamento, assinale a alternativa correta.",
        "options": {
            "A": "A dação em pagamento é o ato pelo qual o credor consente em receber prestação diversa da que lhe é devida.",
            "B": "A dação em pagamento independe da concordância do credor, sendo direito potestativo do devedor.",
            "C": "Na dação em pagamento, a entrega de coisa diversa não precisa de avaliação ou determinação de valor.",
            "D": "A dação em pagamento extingue a obrigação, mas o devedor responde pela evicção da coisa dada."
        },
        "gabarito": "A",
        "article": "Arts. 356 e 357 CC",
        "legal_basis": "Arts. 356, 357, 358 do Código Civil.",
        "explanation": "O art. 356 define: 'O credor pode consentir em receber prestação diversa da que lhe é devida'. A dação depende de acordo de vontades (não é direito potestativo). O art. 357 estabelece que, se a coisa sofrer evicção, restabelece-se a obrigação primitiva. O valor deve ser determinado (art. 358)."
    },
    {
        "subject": "Dação em pagamento",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Em relação à dação em pagamento, assinale a opção correta.",
        "options": {
            "A": "Ocorrendo evicção da coisa dada em pagamento, restabelece-se a obrigação primitiva, com todos os seus acessórios.",
            "B": "O credor é obrigado a aceitar a dação em pagamento se o devedor oferecer bem de valor equivalente.",
            "C": "A dação em pagamento pode ser unilateral, sem necessidade de aceitação do credor.",
            "D": "A dação em pagamento de imóvel exige escritura pública, sob pena de nulidade."
        },
        "gabarito": "A",
        "article": "Arts. 356 e 359 CC",
        "legal_basis": "Arts. 356, 357, 358 e 359 do Código Civil.",
        "explanation": "O art. 359 dispõe: 'Se a coisa dada em pagamento for evicta, restabelece-se a obrigação primitiva, ficando sem efeito a quitação dada'. A dação depende de consentimento do credor (art. 356). O valor deve ser estimado (art. 358). A forma depende da natureza do bem."
    },
    {
        "subject": "Dação em pagamento",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Em uma dação em pagamento, assinale a alternativa correta.",
        "options": {
            "A": "Se a coisa dada em pagamento for evicta, o devedor pode optar entre restabelecer a obrigação primitiva ou dar outra coisa.",
            "B": "A dação em pagamento é nula se não houver avaliação do bem pelo mesmo valor da dívida.",
            "C": "O credor não pode exercer o direito de preferência sobre a coisa recebida em dação.",
            "D": "A dação em pagamento importa em novação da obrigação, por substituir o objeto."
        },
        "gabarito": "A",
        "article": "Arts. 357 e 359 CC",
        "legal_basis": "Arts. 357 e 359 do Código Civil.",
        "explanation": "O art. 357 estabelece que, na evicção, o devedor pode optar: 'o credor pode reaver o valor da dívida, ou exigir a restituição da coisa' (na verdade, a obrigação primitiva se restaura - art. 359). A dação não é novação, pois não cria nova dívida - apenas altera o objeto. O valor deve ser estimado (art. 358)."
    },

    # ============================================================
    # 11. NOVAÇÃO (Arts. 360 - 367)
    # ============================================================
    {
        "subject": "Novação",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre a novação, assinale a alternativa correta.",
        "options": {
            "A": "A novação subjetiva passiva opera-se pela substituição do devedor, independentemente do consentimento do credor.",
            "B": "A novação extingue a obrigação anterior, criando-se nova obrigação em seu lugar.",
            "C": "A novação objetiva depende de alteração do sujeito da obrigação, mantendo-se o objeto.",
            "D": "A novação não admite a declaração expressa de intenção de novar, bastando a incompatibilidade entre as obrigações."
        },
        "gabarito": "B",
        "article": "Arts. 360 e 361 CC",
        "legal_basis": "Arts. 360, 361 e 362 do Código Civil.",
        "explanation": "O art. 360 define a novação como a criação de nova obrigação para substituir e extinguir a anterior. Pode ser: I - objetiva (mudança no objeto); II - subjetiva ativa (mudança de credor); III - subjetiva passiva (mudança de devedor). Depende de declaração expressa da intenção de novar (animus novandi - art. 361)."
    },
    {
        "subject": "Novação",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Assinale a alternativa correta em relação à novação subjetiva passiva.",
        "options": {
            "A": "A novação subjetiva passiva independe do consentimento do devedor originário, que é automaticamente exonerado.",
            "B": "A novação subjetiva passiva (expromissão) opera-se pela substituição do devedor, com consentimento do credor.",
            "C": "Na novação subjetiva passiva, o devedor originário fica solidariamente responsável com o novo devedor.",
            "D": "A novação subjetiva passiva exige que o novo devedor seja incapaz, para proteção do crédito."
        },
        "gabarito": "B",
        "article": "Arts. 362 e 363 CC",
        "legal_basis": "Arts. 362, 363 do Código Civil.",
        "explanation": "A novação subjetiva passiva pode ser por expromissão (art. 362) - o novo devedor assume a dívida com consentimento do credor, exonerando o devedor originário - ou por delegação (art. 363) - o devedor originário indica novo devedor com consentimento do credor. Em ambos os casos, o devedor originário é exonerado, salvo pacto de solidariedade."
    },
    {
        "subject": "Novação",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Em relação à novação, assinale a alternativa correta.",
        "options": {
            "A": "A novação subjetiva ativa é a substituição do credor, que independe do consentimento do devedor.",
            "B": "A novação objetiva ocorre quando se modifica o objeto da prestação, exigindo-se a intenção expressa de novar.",
            "C": "A novação extingue as garantias da dívida originária, salvo se as partes acordarem em mantê-las.",
            "D": "A novação não pode ser parcial, devendo abranger a totalidade da obrigação anterior."
        },
        "gabarito": "C",
        "article": "Arts. 360, 361 e 364 CC",
        "legal_basis": "Arts. 360, 361, 364 e 366 do Código Civil.",
        "explanation": "O art. 364 dispõe que a novação extingue os acessórios e garantias, salvo disposição em contrário. A novação subjetiva ativa exige consentimento do devedor (art. 360). Exige-se animus novandi expresso ou inequívoco (art. 361). Pode ser parcial (art. 365)."
    },

    # ============================================================
    # 12. COMPENSAÇÃO (Arts. 368 - 380)
    # ============================================================
    {
        "subject": "Compensação",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB XXXIV) Sobre a compensação, assinale a alternativa correta.",
        "options": {
            "A": "A compensação opera de pleno direito entre dívidas líquidas, vencidas e de coisas fungíveis.",
            "B": "A compensação é sempre convencional, dependendo de acordo entre as partes para operar efeitos.",
            "C": "A compensação não admite que as partes excluam sua incidência por acordo contratual.",
            "D": "A compensação exige autorização judicial, não operando automaticamente entre as partes."
        },
        "gabarito": "A",
        "article": "Art. 369 CC",
        "legal_basis": "Arts. 369, 370, 371 do Código Civil.",
        "explanation": "O art. 369 estabelece a compensação legal: 'A compensação efetua-se entre dívidas líquidas, vencidas e de coisas fungíveis'. Opera automaticamente (ipso iure), independentemente de acordo - as partes podem, contudo, excluí-la convencionalmente. Também existe a compensação convencional (art. 375) e a facultativa."
    },
    {
        "subject": "Compensação",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre os requisitos da compensação legal, assinale a alternativa correta.",
        "options": {
            "A": "A compensação legal exige que as dívidas sejam líquidas, vencidas e de coisas fungíveis entre pessoas reciprocamente credoras e devedoras.",
            "B": "A compensação legal pode ser afastada por vontade das partes, que podem excluí-la contratualmente.",
            "C": "A compensação legal não exige que as dívidas sejam vencidas, bastando que sejam líquidas e fungíveis.",
            "D": "A compensação legal se efetiva mediante declaração unilateral do credor, sem necessidade de aceitação."
        },
        "gabarito": "B",
        "article": "Arts. 369, 370, 371, 375 CC",
        "legal_basis": "Arts. 369, 370, 371 e 375 do Código Civil.",
        "explanation": "O art. 369 exige: liquidez, vencimento e fungibilidade. O art. 375 admite que as partes afastem a compensação por acordo. O art. 370 trata da compensação de dívidas ilíquidas. O art. 371 exclui a compensação em caso de culpa ou dolo. A compensação opera-se ipso iure, independentemente de declaração expressa."
    },
    {
        "subject": "Compensação",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Assinale a alternativa que apresenta hipótese em que a compensação NÃO é admitida pelo Código Civil.",
        "options": {
            "A": "Dívidas de coisas fungíveis da mesma qualidade, líquidas e vencidas.",
            "B": "Dívida de alimentos e dívida de locação entre as mesmas partes.",
            "C": "Dívidas em que uma delas decorre de ato ilícito doloso.",
            "D": "Dívidas em que uma das partes é credora e devedora simultaneamente."
        },
        "gabarito": "C",
        "article": "Art. 371, 373 CC",
        "legal_basis": "Arts. 371 e 373 do Código Civil.",
        "explanation": "O art. 371 exclui a compensação: 'Embora sejam do mesmo gênero e qualidade, não se compensarão as dívidas, se uma delas provier de culpa ou dolo'. O art. 373 veda a compensação de dívida alimentar. O art. 372 trata da compensação em caso de renúncia."
    },

    # ============================================================
    # 13. CONFUSÃO (Arts. 381 - 384)
    # ============================================================
    {
        "subject": "Confusão",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre a confusão, assinale a alternativa correta.",
        "options": {
            "A": "A confusão opera-se quando na mesma pessoa se confundem as qualidades de credor e devedor, extinguindo a obrigação.",
            "B": "A confusão é forma de pagamento indireto que depende de acordo entre as partes.",
            "C": "A confusão extingue a obrigação, mas mantém as garantias prestadas por terceiros.",
            "D": "A confusão não se aplica às obrigações solidárias, pois a solidariedade impede a confusão."
        },
        "gabarito": "A",
        "article": "Art. 381 CC",
        "legal_basis": "Arts. 381, 382, 383 do Código Civil.",
        "explanation": "O art. 381 define: 'Extingue-se a obrigação, desde que na mesma pessoa se confundam as qualidades de credor e devedor'. A confusão opera de pleno direito. No caso de solidariedade, a confusão extingue a obrigação apenas quanto ao devedor/credor confundido (art. 383). Extingue as garantias (art. 384)."
    },
    {
        "subject": "Confusão",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Em relação à confusão nas obrigações solidárias, assinale a opção correta.",
        "options": {
            "A": "Na solidariedade passiva, a confusão entre um dos devedores e o credor extingue a dívida em relação a todos os devedores.",
            "B": "Na solidariedade ativa, a confusão entre um dos credores e o devedor extingue a obrigação apenas quanto à parte daquele credor.",
            "C": "A confusão não pode ser parcial, devendo abranger a totalidade do crédito.",
            "D": "Na solidariedade passiva, a confusão entre um devedor e o credor extingue a dívida em relação a todos os coobrigados."
        },
        "gabarito": "B",
        "article": "Art. 383 CC",
        "legal_basis": "Art. 383, parágrafo único, do Código Civil.",
        "explanation": "O art. 383 dispõe que, na solidariedade ativa, 'a confusão operada quanto a um dos credores solidários não extingue a obrigação senão até a concorrência da respectiva parte'. Na solidariedade passiva, a confusão quanto a um devedor extingue a dívida proporcionalmente à sua parte, subsistindo para os demais."
    },
    {
        "subject": "Confusão",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Sobre os efeitos da confusão, assinale a alternativa correta.",
        "options": {
            "A": "A confusão extingue a obrigação principal e todas as garantias, inclusive as prestadas por terceiros.",
            "B": "A confusão extingue a obrigação principal, mas não as garantias prestadas por terceiros, salvo se estes anuírem.",
            "C": "A confusão opera efeitos retroativos à data da constituição da obrigação.",
            "D": "A confusão é causa de suspensão, e não de extinção da obrigação."
        },
        "gabarito": "B",
        "article": "Art. 384 CC",
        "legal_basis": "Art. 384 do Código Civil.",
        "explanation": "O art. 384 dispõe: 'A confusão pode verificar-se a respeito da dívida principal ou de prestação acessória, mas não extingue as garantias prestadas por terceiros'. Portanto, as garantias fidejussórias ou reais prestadas por terceiros subsistem, pois o terceiro garantidor não se beneficia da confusão."
    },

    # ============================================================
    # 14. REMISSÃO DAS DÍVIDAS (Arts. 385 - 388)
    # ============================================================
    {
        "subject": "Remissão das dívidas",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre a remissão das dívidas, assinale a alternativa correta.",
        "options": {
            "A": "A remissão (perdão da dívida) depende da aceitação do devedor para produzir efeitos.",
            "B": "A remissão é ato unilateral do credor que independe da aceitação do devedor.",
            "C": "A remissão só pode ser expressa, não se admitindo remissão tácita.",
            "D": "A remissão parcial da dívida é nula, pois o perdão deve abranger a totalidade do crédito."
        },
        "gabarito": "B",
        "article": "Arts. 385 e 386 CC",
        "legal_basis": "Arts. 385, 386, 387 do Código Civil.",
        "explanation": "O art. 385 dispõe que a remissão é ato unilateral do credor que independe da aceitação do devedor (diferencia-se da renúncia ao direito). O art. 386 admite a remissão tácita (ex.: entrega voluntária do título ao devedor). Pode ser parcial (art. 387). A remissão a um dos devedores solidários extingue a dívida na parte correspondente (art. 388)."
    },
    {
        "subject": "Remissão das dívidas",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Assinale a alternativa que configura hipótese de remissão tácita.",
        "options": {
            "A": "O credor entrega voluntariamente o título da dívida ao devedor.",
            "B": "O credor notifica o devedor informando que perdoa a dívida.",
            "C": "O credor deixa de cobrar a dívida por mais de 5 anos.",
            "D": "O credor renova o contrato com novas condições de pagamento."
        },
        "gabarito": "A",
        "article": "Art. 386 CC",
        "legal_basis": "Art. 386 do Código Civil.",
        "explanation": "O art. 386 estabelece: 'A remissão tanto pode ser expressa como tácita'. A remissão tácita decorre de atos incompatíveis com a vontade de receber o crédito, como a entrega voluntária do título ao devedor. O simples não exercício do direito de cobrar não configura remissão - exige-se ato inequívoco de liberalidade."
    },
    {
        "subject": "Remissão das dívidas",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Em relação à remissão nas obrigações solidárias, assinale a alternativa correta.",
        "options": {
            "A": "A remissão concedida a um dos devedores solidários extingue a dívida por inteiro para todos os devedores.",
            "B": "A remissão concedida a um dos devedores solidários extingue a dívida apenas até a sua parte, subsistindo para os demais.",
            "C": "A remissão na solidariedade ativa extingue integralmente o crédito dos demais credores.",
            "D": "A remissão não é admitida nas obrigações solidárias, por incompatibilidade com o regime de solidariedade."
        },
        "gabarito": "B",
        "article": "Art. 388 CC",
        "legal_basis": "Art. 388 do Código Civil.",
        "explanation": "O art. 388 dispõe: 'A remissão concedida a um dos devedores solidários extingue a dívida na parte a ele correspondente; se for solidária, exonera-o, mas os outros devedores continuam obrigados pelo saldo'. A remissão não prejudica os demais devedores solidários."
    },

    # ============================================================
    # 15. INADIMPLEMENTO - DISPOSIÇÕES GERAIS (Arts. 389 - 393)
    # ============================================================
    {
        "subject": "Inadimplemento - Disposições gerais",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre o inadimplemento das obrigações, assinale a alternativa correta.",
        "options": {
            "A": "O inadimplemento absoluto ocorre quando a prestação ainda é possível e útil ao credor.",
            "B": "O inadimplemento do devedor o obriga a perdas e danos, mais juros e correção monetária.",
            "C": "O devedor respede pelos prejuízos mesmo em caso de caso fortuito ou força maior, salvo se houver cláusula de exclusão.",
            "D": "O inadimplemento só gera perdas e danos se houver dolo do devedor."
        },
        "gabarito": "B",
        "article": "Arts. 389 e 393 CC",
        "legal_basis": "Arts. 389, 390, 391, 392, 393 do Código Civil.",
        "explanation": "O art. 389 estabelece: 'Não cumprida a obrigação, responde o devedor por perdas e danos, mais juros e atualização monetária'. O art. 393 exclui a responsabilidade por caso fortuito e força maior. O art. 391 consagra a responsabilidade patrimonial geral. O art. 392 trata da responsabilidade nas obrigações de meio e resultado."
    },
    {
        "subject": "Inadimplemento - Disposições gerais",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Assinale a alternativa correta acerca da responsabilidade do devedor no inadimplemento.",
        "options": {
            "A": "O devedor não respede pelos prejuízos resultantes de caso fortuito ou força maior, salvo se por estes se responsabilizou.",
            "B": "O devedor respede sempre pelos prejuízos, independentemente de culpa, nas obrigações de resultado.",
            "C": "A culpa do devedor é sempre presumida, cabendo a ele provar que não agiu com negligência.",
            "D": "O devedor respede objetivamente pelo inadimplemento, bastando a demonstração do descumprimento."
        },
        "gabarito": "A",
        "article": "Art. 393 CC",
        "legal_basis": "Arts. 389, 391, 393 do Código Civil.",
        "explanation": "O art. 393 estabelece: 'O devedor não respede pelos prejuízos resultantes de caso fortuito ou força maior, se expressamente não se houver por eles responsabilizado'. A responsabilidade do devedor é subjetiva (depende de culpa) nas obrigações de meio, e objetiva nas obrigações de resultado. O parágrafo único do art. 393 define o caso fortuito e a força maior."
    },
    {
        "subject": "Inadimplemento - Disposições gerais",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Em relação ao inadimplemento das obrigações, assinale a opção correta.",
        "options": {
            "A": "Nas obrigações de resultado, a culpa do devedor é presumida, invertendo-se o ônus da prova.",
            "B": "Nas obrigações de meio, o devedor se obriga a atingir um resultado específico, respondendo objetivamente.",
            "C": "O inadimplemento absoluto autoriza o credor a rescindir o contrato e exigir perdas e danos.",
            "D": "O inadimplemento parcial da obrigação indivisível converte a prestação em perdas e danos automaticamente."
        },
        "gabarito": "A",
        "article": "Arts. 389 e 392 CC",
        "legal_basis": "Arts. 389, 391, 392, 393 do Código Civil.",
        "explanation": "Nas obrigações de resultado, o devedor se compromete a alcançar um fim específico. Se não o alcança, presume-se sua culpa (inversão do ônus da prova). Nas obrigações de meio, o devedor se obriga a empregar diligência, e o credor deve provar a culpa. O inadimplemento absoluto impede o adimplemento útil."
    },

    # ============================================================
    # 16. MORA - GERAL (Arts. 394 - 401, visão geral)
    # ============================================================
    {
        "subject": "Mora - Geral",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre a mora, assinale a alternativa correta.",
        "options": {
            "A": "A mora do devedor se caracteriza pelo não pagamento no tempo, lugar e forma convencionados, independentemente de culpa.",
            "B": "A mora do credor ocorre quando este se recusa a receber o pagamento nas condições pactuadas.",
            "C": "A mora pode ser purgada pelo devedor com o pagamento da prestação acrescida de juros e correção, a qualquer tempo.",
            "D": "A mora exige interpelação judicial ou extrajudicial do credor para se configurar em todos os casos."
        },
        "gabarito": "B",
        "article": "Arts. 394 e 400 CC",
        "legal_basis": "Arts. 394, 397, 398, 400 do Código Civil.",
        "explanation": "A mora do devedor (arts. 394-399) é o descumprimento culposo no tempo, lugar e forma devidos. A mora do credor (art. 400) ocorre quando o credor se recusa a receber. A mora exige culpa (art. 394). O devedor pode purgar a mora enquanto não houver prejuízo ao credor (art. 401). A mora ex re (art. 397) dispensa interpelação; a ex personae (art. 398) exige."
    },
    {
        "subject": "Mora - Geral",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Assinale a alternativa correta acerca da purgação da mora.",
        "options": {
            "A": "A purgação da mora pelo devedor exige o pagamento da prestação acrescida de juros, correção monetária e honorários advocatícios.",
            "B": "A purgação da mora pelo devedor consiste no cumprimento da prestação acrescida dos prejuízos decorrentes do atraso.",
            "C": "A purgação da mora não é admitida depois de constituída em mora, sendo irreversível.",
            "D": "A purgação da mora pelo credor se dá com a aceitação tardia do pagamento."
        },
        "gabarito": "B",
        "article": "Art. 401 CC",
        "legal_basis": "Art. 401, I e II do Código Civil.",
        "explanation": "O art. 401 permite a purgação da mora: I - pelo devedor, pagando a prestação com juros e correção; II - pelo credor, oferecendo-se a receber e depositando os prejuízos a que está obrigado. A purgação é possível enquanto não houver prejuízo irreversível ou enquanto o credor não tiver exigido perdas e danos."
    },
    {
        "subject": "Mora - Geral",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Em relação à constituição em mora, assinale a opção correta.",
        "options": {
            "A": "A mora é constituída de pleno direito (ex re) nas obrigações com prazo certo, dispensando interpelação.",
            "B": "A mora exige sempre interpelação judicial ou extrajudicial do devedor para se constituir.",
            "C": "A mora do devedor se constitui automaticamente com o simples inadimplemento, independentemente de prazo.",
            "D": "A interpelação judicial é o único meio de constituir o devedor em mora nas obrigações sem termo."
        },
        "gabarito": "A",
        "article": "Arts. 397 e 398 CC",
        "legal_basis": "Arts. 397 e 398 do Código Civil.",
        "explanation": "O art. 397 estabelece a mora ex re: 'O inadimplemento da obrigação, positiva e líquida, no seu termo, constitui de pleno direito em mora o devedor'. Dispensa interpelação. O art. 398 trata da mora ex personae: nas obrigações sem prazo, a mora se constitui mediante interpelação judicial ou extrajudicial."
    },

    # ============================================================
    # 17. MORA DO DEVEDOR (Arts. 394 - 399)
    # ============================================================
    {
        "subject": "Mora do devedor",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB XXXIX) Assinale a opção correta acerca da mora do devedor com perecimento da coisa.",
        "options": {
            "A": "Se a coisa se perder por caso fortuito antes da constituição em mora, o devedor responde pelo valor equivalente.",
            "B": "Se a coisa se perder por caso fortuito durante a mora do devedor, este responde pelo equivalente mais perdas e danos.",
            "C": "O perecimento da coisa durante a mora do devedor sempre exonera o devedor de responsabilidade.",
            "D": "A mora do devedor é purgada com a simples entrega da coisa, independentemente de juros e correção."
        },
        "gabarito": "B",
        "article": "Arts. 239 e 399 CC",
        "legal_basis": "Arts. 239 e 399 do Código Civil.",
        "explanation": "O art. 399 dispõe: 'O devedor em mora responde pela impossibilidade da prestação, embora essa impossibilidade decorra de caso fortuito ou de força maior, se estas ocorrerem durante o atraso'. Aplica-se a responsabilidade agravada: o devedor em mora responde até por caso fortuito e força maior."
    },
    {
        "subject": "Mora do devedor",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB XXVI) Sobre a mora do devedor no contrato de comodato, assinale a alternativa correta.",
        "options": {
            "A": "O comodatário constituído em mora responde pela impossibilidade de restituição da coisa, ainda que decorrente de caso fortuito.",
            "B": "O comodatário em mora não responde por caso fortuito ou força maior, pois a mora não agrava sua responsabilidade.",
            "C": "A mora do comodatário se purga com a simples restituição da coisa, sem necessidade de pagamento de perdas e danos.",
            "D": "O comodante deve provar culpa do comodatário para constituí-lo em mora."
        },
        "gabarito": "A",
        "article": "Arts. 399, 582 e 583 CC",
        "legal_basis": "Arts. 399, 582, 583 do Código Civil.",
        "explanation": "Com fundamento no art. 399, o comodatário em mora responde pela impossibilidade da prestação, mesmo decorrente de caso fortuito. O comodato é mútuo de uso (art. 579). Se o comodatário não devolve a coisa no prazo, constitui-se em mora e assume o risco pelo perecimento, ainda que por caso fortuito."
    },
    {
        "subject": "Mora do devedor",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Quanto à mora do devedor, assinale a alternativa correta.",
        "options": {
            "A": "Nas obrigações negativas, o devedor se constitui em mora desde o dia em que executar o ato que deveria omitir.",
            "B": "A mora do devedor nas obrigações positivas exige sempre interpelação judicial.",
            "C": "O devedor em mora não responde pelos juros de mora se provar que o atraso não causou prejuízo ao credor.",
            "D": "A mora do devedor cessa com a oferta de pagamento, mesmo que incompleto."
        },
        "gabarito": "A",
        "article": "Arts. 394, 397, 398 CC",
        "legal_basis": "Arts. 394, 397, 398 do Código Civil.",
        "explanation": "O art. 390 trata das obrigações negativas: 'Se a obrigação for de não fazer, o devedor é constituído em mora desde o dia em que executar o ato de que deveria abster-se'. Nas obrigações positivas com prazo, a mora é ex re (art. 397). Nas sem prazo, é ex personae (art. 398). Juros fluem automaticamente na mora (art. 407)."
    },

    # ============================================================
    # 18. MORA DO CREDOR (Arts. 400 - 401)
    # ============================================================
    {
        "subject": "Mora do credor",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre a mora do credor, assinale a alternativa correta.",
        "options": {
            "A": "O credor em mora não pode exigir do devedor juros de mora pelos dias de atraso, pois o retardamento é imputável a ele.",
            "B": "O credor em mora pode exigir a correção monetária do valor, pois a mora do credor não interfere nos encargos.",
            "C": "O credor em mora responde pelos prejuízos causados ao devedor, incluindo o pagamento de honorários advocatícios.",
            "D": "A mora do credor se purga com a simples oferta de receber o pagamento, independentemente de despesas."
        },
        "gabarito": "A",
        "article": "Art. 400 CC",
        "legal_basis": "Art. 400 do Código Civil.",
        "explanation": "O art. 400 dispõe: 'A mora do credor consiste em não querer receber a prestação no tempo, lugar e forma devidos'. Efeitos: o devedor não responde por juros de mora (pois o atraso é imputável ao credor), pode consignar e exigir a quitação. O credor em mora responde pela conservação da coisa (art. 400, parte final)."
    },
    {
        "subject": "Mora do credor",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Assinale a alternativa que apresenta efeito da mora do credor.",
        "options": {
            "A": "O devedor fica desobrigado de pagar juros de mora, pois o retardamento é imputável ao credor.",
            "B": "O devedor pode exigir que o credor pague juros compensatórios pelo atraso no recebimento.",
            "C": "A mora do credor extingue automaticamente a dívida, liberando o devedor.",
            "D": "O devedor pode resolver o contrato independentemente de notificação judicial."
        },
        "gabarito": "A",
        "article": "Art. 400 CC",
        "legal_basis": "Art. 400 do Código Civil.",
        "explanation": "O art. 400 estabelece que na mora do credor: o devedor não responde por juros; o credor responde pela conservação da coisa; o devedor pode consignar. Entretanto, a dívida não se extingue - o devedor continua obrigado, mas pode depositar em consignação para se liberar (art. 335, I)."
    },
    {
        "subject": "Mora do credor",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Na mora do credor, assinale a alternativa correta.",
        "options": {
            "A": "O credor responde pela conservação da coisa, podendo o devedor exigir-lhe a devida indenização pelas despesas de guarda e conservação.",
            "B": "O devedor pode extinguir unilateralmente a obrigação, liberando-se sem consignação.",
            "C": "O credor em mora tem direito a exigir juros de mora se o devedor atrasar o pagamento depois de purgada a mora.",
            "D": "A mora do credor converte a obrigação em perdas e danos automaticamente."
        },
        "gabarito": "A",
        "article": "Art. 400 CC",
        "legal_basis": "Art. 400 do Código Civil.",
        "explanation": "O art. 400 estabelece que o credor em mora responde pela conservação da coisa. O devedor tem direito ao reembolso das despesas de guarda e conservação. O devedor não se libera automaticamente - deve consignar. A mora do credor não extingue a obrigação, apenas a modifica em benefício do devedor."
    },

    # ============================================================
    # 19. INADIMPLEMENTO ABSOLUTO (Arts. 389 e ss.)
    # ============================================================
    {
        "subject": "Inadimplemento absoluto",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Assinale a alternativa que caracteriza inadimplemento absoluto.",
        "options": {
            "A": "O devedor atrasa o pagamento por 15 dias, mas a prestação ainda é útil ao credor.",
            "B": "A coisa certa e determinada, que constituía o objeto da prestação, pereceu sem culpa do devedor.",
            "C": "O devedor não entrega a coisa no prazo, mas o credor ainda tem interesse no recebimento.",
            "D": "O pagamento é feito a menor, faltando pequena parcela do valor devido."
        },
        "gabarito": "B",
        "article": "Arts. 234, 235, 236 CC",
        "legal_basis": "Arts. 234, 235, 236, 389 do Código Civil.",
        "explanation": "O inadimplemento absoluto ocorre quando a prestação não pode mais ser cumprida ou perdeu a utilidade para o credor. A impossibilidade da prestação (caso fortuito, perecimento da coisa sem culpa) extingue a obrigação para ambas as partes (art. 235). Diferencia-se da mora, que é o retardamento temporário com possibilidade de cumprimento posterior."
    },
    {
        "subject": "Inadimplemento absoluto",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre o inadimplemento absoluto e a mora, assinale a opção correta.",
        "options": {
            "A": "No inadimplemento absoluto, o credor pode exigir o cumprimento forçado da prestação.",
            "B": "Na mora, o credor pode recusar o recebimento se a prestação perdeu a utilidade, convertendo-se em inadimplemento absoluto.",
            "C": "No inadimplemento absoluto, a prestação ainda é possível, mas o devedor se recusa a cumpri-la.",
            "D": "A mora se converte em inadimplemento absoluto quando o credor não aceita o pagamento em atraso."
        },
        "gabarito": "B",
        "article": "Arts. 389 e 394 CC",
        "legal_basis": "Arts. 389, 394, 395, 475 do Código Civil.",
        "explanation": "Se a prestação perder a utilidade para o credor, a mora se converte em inadimplemento absoluto (art. 395, parágrafo único). No inadimplemento absoluto, o credor pode resolver o contrato e exigir perdas e danos (art. 475). Na mora pura, o devedor pode ainda cumprir a prestação com os acréscimos."
    },
    {
        "subject": "Inadimplemento absoluto",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Caracterizada a perda de utilidade da prestação para o credor, assinale a alternativa correta.",
        "options": {
            "A": "A mora se converte em inadimplemento absoluto, podendo o credor exigir perdas e danos.",
            "B": "A obrigação se extingue automaticamente, sem direito a indenização para qualquer das partes.",
            "C": "O devedor pode purgar a mora pagando a prestação com juros, mesmo perdida a utilidade.",
            "D": "O credor é obrigado a aceitar o pagamento em atraso, perdendo o direito de exigir indenização."
        },
        "gabarito": "A",
        "article": "Art. 395, parágrafo único CC",
        "legal_basis": "Art. 395, parágrafo único, e art. 475 do Código Civil.",
        "explanation": "Conforme o art. 395, parágrafo único, 'se a prestação, devido ao atraso, se tornar inútil ao credor, este poderá enjeitá-la e exigir perdas e danos'. A mora se converte em inadimplemento absoluto. O credor pode optar entre aceitar o pagamento tardio ou resolver o contrato com perdas e danos."
    },

    # ============================================================
    # 20. PERDAS E DANOS (Arts. 402 - 405)
    # ============================================================
    {
        "subject": "Perdas e danos",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB XXXIX) Em relação às perdas e danos, assinale a alternativa correta.",
        "options": {
            "A": "As perdas e danos abrangem apenas o que a parte efetivamente perdeu (danos emergentes).",
            "B": "As perdas e danos abrangem os danos emergentes e os lucros cessantes, salvo se o devedor provar que não agiu com dolo.",
            "C": "As perdas e danos abrangem o que a parte efetivamente perdeu e o que razoavelmente deixou de lucrar.",
            "D": "Os lucros cessantes presumem-se sempre que há inadimplemento contratual, independentemente de prova."
        },
        "gabarito": "C",
        "article": "Arts. 402 e 403 CC",
        "legal_basis": "Arts. 402, 403, 404 do Código Civil.",
        "explanation": "O art. 402 define as perdas e danos como 'o que a parte efetivamente perdeu (danos emergentes) e o que razoavelmente deixou de lucrar (lucros cessantes)'. O art. 403 estabelece que a indenização se limita ao prejuízo direto e imediato (teoria dos danos diretos e imediatos, ou teoria da causalidade adequada)."
    },
    {
        "subject": "Perdas e danos",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre a indenização por perdas e danos nas obrigações pecuniárias, assinale a alternativa correta.",
        "options": {
            "A": "Nas dívidas em dinheiro, a indenização por perdas e danos inclui juros de mora e correção monetária, independentemente de prova de prejuízo.",
            "B": "Os juros de mora nas dívidas em dinheiro dependem de prova do prejuízo efetivo do credor.",
            "C": "A correção monetária incide apenas se houver cláusula expressa no contrato.",
            "D": "Nas dívidas pecuniárias, as perdas e danos só são devidas se o credor provar que sofreu prejuízo."
        },
        "gabarito": "A",
        "article": "Art. 404 CC",
        "legal_basis": "Art. 404 do Código Civil.",
        "explanation": "O art. 404 dispõe que nas obrigações pecuniárias, as perdas e danos incluem juros de mora e correção monetária, sem necessidade de prova de prejuízo. Os juros de mora são devidos a partir da citação inicial (art. 405). A correção monetária incide independentemente de cláusula contratual."
    },
    {
        "subject": "Perdas e danos",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Assinale a alternativa correta acerca dos lucros cessantes.",
        "options": {
            "A": "Os lucros cessantes devem ser provados de forma concreta e efetiva, não se admitindo presunção ou razoabilidade.",
            "B": "Os lucros cessantes correspondem ao que a parte razoavelmente deixou de lucrar, em decorrência direta e imediata do inadimplemento.",
            "C": "Os lucros cessantes são devidos automaticamente em qualquer caso de inadimplemento contratual.",
            "D": "Os lucros cessantes não podem ultrapassar o valor dos danos emergentes."
        },
        "gabarito": "B",
        "article": "Arts. 402 e 403 CC",
        "legal_basis": "Arts. 402, 403 do Código Civil.",
        "explanation": "O art. 402 estabelece que os lucros cessantes correspondem 'ao que razoavelmente deixou de lucrar', não exigindo prova concreta e efetiva, mas sim razoável probabilidade. O art. 403 limita a indenização aos danos diretos e imediatos. Lucros cessantes podem superar danos emergentes, não há hierarquia entre eles."
    },

    # ============================================================
    # 21. JUROS LEGAIS (Arts. 406 - 407)
    # ============================================================
    {
        "subject": "Juros legais",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre os juros legais, assinale a alternativa correta.",
        "options": {
            "A": "Os juros de mora fluem a partir da citação inicial nas obrigações contratuais.",
            "B": "Os juros de mora são devidos desde o vencimento da obrigação, independentemente de citação.",
            "C": "Os juros de mora não podem ser cumulados com correção monetária.",
            "D": "Os juros legais são fixados em 12% ao ano, salvo disposição em contrário."
        },
        "gabarito": "B",
        "article": "Arts. 406 e 407 CC",
        "legal_basis": "Arts. 406, 407 do Código Civil.",
        "explanation": "O art. 406 estabelece que os juros de mora serão fixados segundo a taxa legal (atualmente a taxa SELIC, para fins tributários, ou 1% ao mês pelo CC). O art. 407 dispõe que os juros de mora fluem desde o vencimento (mora ex re) ou desde a citação (se não houver termo). A cumulação com correção monetária é admitida (Súmula 562 STJ)."
    },
    {
        "subject": "Juros legais",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Em relação aos juros nas obrigações civis, assinale a alternativa correta.",
        "options": {
            "A": "Os juros compensatórios são devidos desde a mora, independentemente de convenção.",
            "B": "Os juros de mora sobre dívidas em dinheiro são devidos independentemente de prova de prejuízo.",
            "C": "A taxa de juros de mora, na omissão contratual, é de 6% ao ano nas obrigações civis.",
            "D": "Os juros compensatórios e moratórios podem ser cumulados, limitados a 12% ao ano."
        },
        "gabarito": "B",
        "article": "Arts. 406 e 407 CC",
        "legal_basis": "Arts. 406, 407 do Código Civil.",
        "explanation": "Os juros de mora nas dívidas em dinheiro são devidos independentemente de prova de prejuízo (arts. 404 e 407). Na omissão, a taxa de juros de mora é de 1% ao mês (art. 406 c/c Código Tributário Nacional). Juros compensatórios dependem de convenção. A cumulação entre moratórios e compensatórios é possível."
    },
    {
        "subject": "Juros legais",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Sobre os juros de mora nas obrigações civis, assinale a alternativa correta.",
        "options": {
            "A": "Os juros de mora correm da citação inicial nas obrigações contratuais com termo certo de vencimento.",
            "B": "Os juros de mora correm do vencimento da obrigação nas obrigações líquidas com prazo estipulado.",
            "C": "Os juros de mora nas obrigações ilíquidas correm da data do evento danoso.",
            "D": "Os juros de mora não incidem sobre valores corrigidos monetariamente."
        },
        "gabarito": "B",
        "article": "Arts. 405, 406, 407 CC",
        "legal_basis": "Arts. 405, 406, 407 do Código Civil.",
        "explanation": "O art. 405 dispõe: 'Contam-se os juros de mora desde a citação inicial'. Entretanto, o art. 407 estabelece que, nas obrigações com termo certo (prazo), os juros fluem do vencimento (derrogação ao art. 405). Nas obrigações ilíquidas, os juros correm da citação. A correção monetária não impede a incidência de juros."
    },

    # ============================================================
    # 22. CLÁUSULA PENAL (Arts. 408 - 416)
    # ============================================================
    {
        "subject": "Cláusula penal",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB XXV) Sobre a cláusula penal moratória, assinale a alternativa correta.",
        "options": {
            "A": "A cláusula penal moratória tem por objetivo prefixar as perdas e danos decorrentes do inadimplemento absoluto da obrigação.",
            "B": "A cláusula penal moratória incide sobre a mora, permitindo ao credor exigi-la juntamente com a prestação principal.",
            "C": "A cláusula penal moratória exclui a possibilidade de o credor cobrar juros de mora e correção monetária.",
            "D": "A cláusula penal moratória pode ser cumulada com a cláusula penal compensatória."
        },
        "gabarito": "B",
        "article": "Arts. 408, 409 e 411 CC",
        "legal_basis": "Arts. 408, 409, 411 do Código Civil.",
        "explanation": "A cláusula penal moratória (art. 408) tem por finalidade punir a mora (retardamento), sendo cumulável com a prestação principal (art. 411). Já a cláusula penal compensatória substitui a prestação principal no caso de inadimplemento absoluto. O credor pode exigir a pena moratória e também cobrar a prestação principal."
    },
    {
        "subject": "Cláusula penal",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB XXII) Sobre a cláusula penal compensatória, assinale a alternativa correta.",
        "options": {
            "A": "A cláusula penal compensatória pode ser exigida juntamente com a prestação principal, em caso de inadimplemento.",
            "B": "A cláusula penal compensatória constitui prévia estimativa das perdas e danos, substituindo a prestação principal.",
            "C": "A cláusula penal compensatória exclui a possibilidade de o credor rescindir o contrato.",
            "D": "A cláusula penal compensatória é sempre reduzida pelo juiz, independentemente de requerimento."
        },
        "gabarito": "B",
        "article": "Arts. 394, 408 e 410 CC",
        "legal_basis": "Arts. 394, 408, 409, 410 do Código Civil.",
        "explanation": "A cláusula penal compensatória (art. 410) substitui a indenização pelas perdas e danos, sendo exigível no caso de inadimplemento absoluto. O credor pode optar entre exigir a prestação principal ou a pena compensatória. Não pode cumulá-las. A redução judicial (art. 413) depende de requerimento e prova de excesso."
    },
    {
        "subject": "Cláusula penal",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB XLIII) Sobre a cláusula penal moratória e sua redução judicial, assinale a alternativa correta.",
        "options": {
            "A": "A cláusula penal, ainda que moratória, não admite redução judicial, pois decorre da autonomia da vontade.",
            "B": "A cláusula penal pode ser reduzida pelo juiz se for manifestamente excessiva, tendo em vista a natureza e a finalidade do negócio.",
            "C": "A redução judicial da cláusula penal depende de prova de dolo ou má-fé do credor.",
            "D": "A cláusula penal moratória não pode ser reduzida, ao contrário da compensatória."
        },
        "gabarito": "B",
        "article": "Arts. 389, 396, 408, 411, 413 CC",
        "legal_basis": "Arts. 389, 408, 411, 413 do Código Civil.",
        "explanation": "O art. 413 autoriza a redução equitativa da cláusula penal pelo juiz se for manifestamente excessiva, considerando a natureza e a finalidade do negócio. Aplica-se tanto à penal moratória quanto à compensatória. A redução independe de dolo ou má-fé - é um controle de equidade e proporcionalidade."
    },
    {
        "subject": "Cláusula penal",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Em relação à cláusula penal, assinale a alternativa correta.",
        "options": {
            "A": "A cláusula penal moratória não é devida se o devedor pagar a prestação principal com juros e correção.",
            "B": "Na cláusula penal compensatória, o credor pode exigir a prestação principal e a pena simultaneamente.",
            "C": "A cláusula penal pode ser estipulada em valor não superior ao da obrigação principal, salvo em contratos aleatórios.",
            "D": "A cláusula penal moratória pode ser cumulada com a prestação principal e com perdas e danos suplementares."
        },
        "gabarito": "C",
        "article": "Arts. 408, 410, 411, 412 CC",
        "legal_basis": "Arts. 408, 410, 411, 412 do Código Civil.",
        "explanation": "O art. 412 limita o valor da cláusula penal ao da obrigação principal. A penal moratória é cumulável com a prestação principal (art. 411). A penal compensatória não é cumulável (art. 410). A penal moratória não exclui perdas e danos suplementares se provado maior prejuízo (art. 416)."
    },

    # ============================================================
    # 23. ARRAS OU SINAL (Arts. 417 - 420)
    # ============================================================
    {
        "subject": "Arras ou sinal",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB XXXIII) Sobre as arras penitenciais, assinale a alternativa correta.",
        "options": {
            "A": "Nas arras penitenciais, a parte que deu o sinal pode arrepender-se, perdendo-o, e a que recebeu pode devolvê-lo em dobro.",
            "B": "Nas arras penitenciais, a parte prejudicada pode exigir a execução forçada do contrato, independentemente de arrependimento.",
            "C": "Nas arras penitenciais, o arrependimento não é admitido, devendo o contrato ser cumprido obrigatoriamente.",
            "D": "Nas arras penitenciais, o valor do sinal é devolvido em dobro independentemente de quem deu causa ao arrependimento."
        },
        "gabarito": "A",
        "article": "Arts. 417, 418, 419, 420 CC",
        "legal_basis": "Arts. 417, 418, 419, 420 do Código Civil.",
        "explanation": "Nas arras penitenciais (art. 420), as partes podem arrepender-se: quem deu o sinal perde-o; quem recebeu, devolve-o em dobro. Diferem das arras confirmatórias (arts. 418-419), onde o arrependimento não é admitido, podendo a parte inocente exigir o cumprimento ou perdas e danos suplementares."
    },
    {
        "subject": "Arras ou sinal",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre as arras confirmatórias, assinale a alternativa correta.",
        "options": {
            "A": "Nas arras confirmatórias, a parte inocente pode exigir o cumprimento do contrato ou a devolução das arras em dobro.",
            "B": "Nas arras confirmatórias, o arrependimento é livre, perdendo o sinal quem o deu ou devolvendo-o em dobro quem o recebeu.",
            "C": "Nas arras confirmatórias, a parte inocente pode exigir perdas e danos suplementares, independentemente de prova de prejuízo maior.",
            "D": "Nas arras confirmatórias, o valor das arras não pode ultrapassar 10% do valor total do contrato."
        },
        "gabarito": "A",
        "article": "Arts. 417, 418, 419 CC",
        "legal_basis": "Arts. 417, 418, 419 do Código Civil.",
        "explanation": "Nas arras confirmatórias (arts. 418-419), não há direito de arrependimento. Se a parte que deu as arras descumprir, a outra pode: I - exigir o cumprimento forçado; II - rescindir o contrato com arras em dobro. Se o prejuízo for maior, pode pedir indenização suplementar (art. 419)."
    },
    {
        "subject": "Arras ou sinal",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Assinale a alternativa corerca acerca do direito de arrependimento nas arras.",
        "options": {
            "A": "Nas arras confirmatórias, o direito de arrependimento é expressamente vedado, salvo cláusula em contrário.",
            "B": "Nas arras penitenciais, o arrependimento é a regra, e a parte que se arrepende perde o sinal ou o devolve em dobro.",
            "C": "Nas arras confirmatórias, o arrependimento é permitido desde que haja indenização integral de perdas e danos.",
            "D": "Nas arras penitenciais, o direito de arrependimento se extingue com o princípio da execução do contrato."
        },
        "gabarito": "B",
        "article": "Arts. 418 e 420 CC",
        "legal_basis": "Arts. 418, 419, 420 do Código Civil.",
        "explanation": "Nas arras penitenciais (art. 420), o arrependimento é a regra: quem deu o sinal perde-o; quem recebeu devolve-o em dobro. Nas arras confirmatórias (arts. 418-419), não há arrependimento, salvo cláusula expressa em contrário (que as converteria em penitenciais)."
    },

    # ============================================================
    # QUESTIONS ADICIONAIS PARA COMPLEMENTAR ASSUNTOS
    # ============================================================
    # Inadimplemento - Disposições gerais (extra)
    {
        "subject": "Inadimplemento - Disposições gerais",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Em relação à exceção do contrato não cumprido (exceptio non adimpleti contractus), assinale a alternativa correta.",
        "options": {
            "A": "A exceptio non adimpleti contractus permite que uma parte se recuse a cumprir sua prestação enquanto a outra não cumprir a sua.",
            "B": "A exceção do contrato não cumprido só se aplica aos contratos unilaterais, não aos bilaterais.",
            "C": "A exceptio non adimpleti contractus extingue a obrigação, liberando ambas as partes.",
            "D": "A exceção do contrato não cumprido depende de interpelação judicial para ser oposta."
        },
        "gabarito": "A",
        "article": "Art. 476 CC",
        "legal_basis": "Art. 476 do Código Civil.",
        "explanation": "O art. 476 consagra a exceptio non adimpleti contractus: 'Nos contratos bilaterais, nenhum dos contratantes, antes de cumprida a sua prestação, pode exigir o implemento da do outro'. Trata-se de exceção substancial que suspende o cumprimento, não extingue a obrigação, e independe de interpelação."
    },
    {
        "subject": "Inadimplemento - Disposições gerais",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre a responsabilidade do devedor nas obrigações contratuais, assinale a alternativa correta.",
        "options": {
            "A": "O devedor responde pelos prejuízos causados por caso fortuito ou força maior, salvo se expressamente excluídos no contrato.",
            "B": "O devedor não responde por caso fortuito e força maior, salvo expressa previsão contratual em contrário.",
            "C": "O caso fortuito exonera o devedor apenas se for absolutamente imprevisível e inevitável.",
            "D": "A força maior difere do caso fortuito por ser sempre decorrente de ato humano."
        },
        "gabarito": "B",
        "article": "Arts. 391 e 393 CC",
        "legal_basis": "Arts. 391 e 393 do Código Civil.",
        "explanation": "O art. 393 estabelece a regra: o devedor não responde pelos prejuízos de caso fortuito ou força maior, salvo se expressamente se responsabilizou. O parágrafo único do art. 393 define caso fortuito (ato humano imprevisível) e força maior (fato natural inevitável). Ambos excluem a responsabilidade."
    },
    # Pagamento - Geral (extra)
    {
        "subject": "Pagamento - Geral",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Quanto à transmissão das obrigações, assinale a alternativa correta.",
        "options": {
            "A": "A cessão de crédito transfere ao cessionário o crédito e todos os seus acessórios e garantias.",
            "B": "A assunção de dívida depende do consentimento do devedor originário, dispensando-se o consentimento do credor.",
            "C": "A cessão de crédito não produz efeitos perante terceiros sem o registro no cartório de títulos e documentos.",
            "D": "A assunção de dívida exonera o devedor originário, que não responde mais pela dívida."
        },
        "gabarito": "A",
        "article": "Arts. 286, 287, 299 CC",
        "legal_basis": "Arts. 286, 287, 299, 300 do Código Civil.",
        "explanation": "O art. 287 determina que a cessão de crédito transfere ao cessionário todos os acessórios e garantias. A assunção de dívida (art. 299) exige consentimento do credor. A cessão produz efeitos perante terceiros com a notificação ao devedor (art. 290)."
    },
    # Mora do devedor (extra)
    {
        "subject": "Mora do devedor",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Assinale a alternativa correta acerca dos efeitos da mora do devedor.",
        "options": {
            "A": "O devedor em mora responde pela impossibilidade da prestação decorrente de caso fortuito ou força maior ocorridos durante o atraso.",
            "B": "O devedor em mora não responde por caso fortuito, pois a mora não altera o regime de responsabilidade objetiva.",
            "C": "O devedor em mora pode purgá-la a qualquer tempo, mesmo depois de constituído em mora e citado judicialmente.",
            "D": "O devedor em mora não é obrigado a pagar juros de mora se provar que o atraso foi mínimo."
        },
        "gabarito": "A",
        "article": "Arts. 399, 401, 407 CC",
        "legal_basis": "Arts. 399, 401, 407 do Código Civil.",
        "explanation": "O art. 399 agrava a responsabilidade do devedor em mora: responde até por caso fortuito e força maior ocorridos durante o atraso. A purgação da mora (art. 401) é possível enquanto não houver prejuízo irreversível. Os juros de mora são devidos independentemente de prova de prejuízo (art. 407)."
    },
    # Mora do credor (extra)
    {
        "subject": "Mora do credor",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Caracterizada a mora do credor, assinale a alternativa correta.",
        "options": {
            "A": "O devedor pode exigir a purgação da mora pelo credor, mediante notificação judicial.",
            "B": "O credor em mora responde pela conservação da coisa, podendo o devedor exigir-lhe o pagamento das despesas de guarda.",
            "C": "O devedor é automaticamente liberado da obrigação se o credor recusar o pagamento.",
            "D": "A mora do credor interrompe a prescrição contra o devedor."
        },
        "gabarito": "B",
        "article": "Art. 400 CC",
        "legal_basis": "Art. 400 do Código Civil.",
        "explanation": "O art. 400 estabelece que, na mora do credor, este responde pela conservação da coisa. O devedor não se libera automaticamente e deve consignar. A mora do credor não interrompe a prescrição. O devedor pode exigir indenização pelas despesas de guarda e conservação."
    },
    # Perdas e danos (extra)
    {
        "subject": "Perdas e danos",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Sobre a indenização suplementar, assinale a alternativa correta.",
        "options": {
            "A": "A indenização suplementar é devida quando o prejuízo excede o valor da cláusula penal, desde que provado o maior prejuízo.",
            "B": "A indenização suplementar é automaticamente devida independentemente de prova de prejuízo adicional.",
            "C": "A indenização suplementar substitui a cláusula penal, que deixa de ser devida.",
            "D": "A indenização suplementar não pode ultrapassar o valor da obrigação principal."
        },
        "gabarito": "A",
        "article": "Art. 416 CC",
        "legal_basis": "Art. 416 do Código Civil.",
        "explanation": "O art. 416 dispõe: 'Para exigir a pena convencional, não é necessário que o credor alegue prejuízo. Se a obrigação for com cláusula penal, poderá o credor exigir a pena, sem prejuízo da indenização suplementar, se provar maior prejuízo'. A indenização suplementar depende de prova."
    },
    # Juros legais (extra)
    {
        "subject": "Juros legais",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Assinale a alternativa correta acerca dos juros nas obrigações civis.",
        "options": {
            "A": "Os juros de mora sobre dívidas em dinheiro são devidos a partir da citação inicial, inclusive nas obrigações contratuais com prazo certo.",
            "B": "A taxa de juros de mora, quando omissa a lei ou o contrato, será de 1% ao mês.",
            "C": "Os juros compensatórios são devidos a partir da mora, independentemente de pactuação.",
            "D": "A correção monetária substitui os juros de mora nas obrigações civis."
        },
        "gabarito": "B",
        "article": "Arts. 406 e 407 CC",
        "legal_basis": "Arts. 406, 407 do Código Civil.",
        "explanation": "Na omissão legal ou contratual, os juros de mora são fixados em 1% ao mês (art. 406 c/c art. 161, parágrafo 1º do CTN). Os juros de mora nas obrigações com prazo fluem do vencimento (art. 407), não da citação. Juros compensatórios dependem de convenção. Correção e juros são cumuláveis."
    },
    # Cláusula penal (extra)
    {
        "subject": "Cláusula penal",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Em relação ao valor da cláusula penal, assinale a alternativa correta.",
        "options": {
            "A": "A cláusula penal não pode exceder o valor da obrigação principal.",
            "B": "A cláusula penal pode ser estipulada em qualquer valor, desde que as partes convencionem livremente.",
            "C": "A cláusula penal pode exceder o valor da obrigação principal se houver expressa previsão contratual.",
            "D": "A cláusula penal tem limite de 10% do valor da obrigação principal."
        },
        "gabarito": "A",
        "article": "Art. 412 CC",
        "legal_basis": "Art. 412 do Código Civil.",
        "explanation": "O art. 412 limita o valor da cláusula penal: 'O valor da cominação imposta na cláusula penal não pode exceder o da obrigação principal'. Esse limite é cogente (ordem pública). A redução judicial (art. 413) pode ainda reduzir a pena mesmo dentro desse limite, se for manifestamente excessiva."
    },
    # Arras ou sinal (extra)
    {
        "subject": "Arras ou sinal",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Sobre a indenização suplementar nas arras confirmatórias, assinale a alternativa correta.",
        "options": {
            "A": "Nas arras confirmatórias, a parte inocente pode exigir indenização suplementar se provar que o prejuízo excede o valor do sinal.",
            "B": "Nas arras confirmatórias, o sinal substitui integralmente as perdas e danos, excluindo a indenização suplementar.",
            "C": "Nas arras confirmatórias, a indenização suplementar é devida automaticamente, independentemente de prova.",
            "D": "Nas arras confirmatórias, a indenização suplementar não pode ultrapassar o valor do sinal."
        },
        "gabarito": "A",
        "article": "Art. 419 CC",
        "legal_basis": "Art. 419 do Código Civil.",
        "explanation": "O art. 419 permite à parte inocente, nas arras confirmatórias, exigir a indenização suplementar se provar que o prejuízo sofrido excede o valor das arras. Não há limite máximo para a indenização suplementar - ela corresponde ao dano efetivo comprovado. Apenas nas arras penitenciais (art. 420) não cabe indenização suplementar."
    },
    # Dação em pagamento (extra)
    {
        "subject": "Dação em pagamento",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Assinale a alternativa correta acerca da dação em pagamento.",
        "options": {
            "A": "A dação em pagamento exige que o valor da coisa seja determinado por avaliação ou acordo entre as partes.",
            "B": "A dação em pagamento independe de qualquer avaliação, bastando a entrega da coisa.",
            "C": "O credor pode rejeitar a dação se o valor da coisa oferecida for inferior ao da dívida.",
            "D": "A dação em pagamento não admite evicção, por ser forma de pagamento definitivo."
        },
        "gabarito": "A",
        "article": "Art. 358 CC",
        "legal_basis": "Arts. 356, 357, 358 do Código Civil.",
        "explanation": "O art. 358 dispõe: 'Sendo determinada a coisa por estimação, valerá pelos preço estimado'. A avaliação é necessária para determinar o valor. Se sofrer evicção, a obrigação primitiva se restaura (art. 359). O credor pode recusar a coisa se não concordar com o valor ou a qualidade."
    },
    # Novação (extra)
    {
        "subject": "Novação",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Assinale a alternativa correta acerca da novação objetiva.",
        "options": {
            "A": "A novação objetiva ocorre quando se modifica o objeto da prestação, mantendo-se os mesmos sujeitos.",
            "B": "A novação objetiva ocorre quando se substitui o devedor, mantendo-se o mesmo objeto.",
            "C": "A novação objetiva ocorre quando se substitui o credor, mantendo-se o objeto.",
            "D": "A novação objetiva ocorre quando se modifica o título da dívida, mantendo-se objeto e sujeitos."
        },
        "gabarito": "A",
        "article": "Art. 360, I CC",
        "legal_basis": "Art. 360, I, e art. 361 do Código Civil.",
        "explanation": "O art. 360, I, define a novação objetiva como aquela em que 'o devedor contrai com o credor nova dívida para substituir e extinguir a anterior'. Mantêm-se os mesmos sujeitos, alterando-se o objeto da prestação. A novação subjetiva ativa (II) substitui o credor, e a passiva (III) substitui o devedor."
    },
    # Compensação (extra)
    {
        "subject": "Compensação",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Sobre a compensação legal, assinale a alternativa correta.",
        "options": {
            "A": "A compensação legal opera de pleno direito, extinguindo as obrigações reciprocamente até o limite do menor valor.",
            "B": "A compensação legal depende de declaração formal de uma das partes para produzir efeitos.",
            "C": "A compensação legal só é admitida entre dívidas de igual valor, não se aplicando a dívidas desiguais.",
            "D": "A compensação legal exige que as dívidas sejam da mesma natureza, não se aplicando a dívidas em dinheiro."
        },
        "gabarito": "A",
        "article": "Arts. 369, 376 CC",
        "legal_basis": "Arts. 369, 376, 377 do Código Civil.",
        "explanation": "A compensação legal opera-se ipso iure (de pleno direito), independentemente de declaração (art. 369). Extingue as obrigações até onde se compensarem (art. 376). Se uma dívida for maior, a compensação se dá até o limite da menor. A diferença subsiste como dívida (art. 377)."
    },
]


def main():
    with open(SEED_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing = data["questions"]
    existing_enunciados = {q["enunciado"] for q in existing}
    existing_ids = {q["id"] for q in existing}
    added = 0
    skipped_existing = 0
    skipped_dup = 0

    for q in OAB_QUESTIONS:
        if q["enunciado"] in existing_enunciados:
            skipped_dup += 1
            continue

        qid = str(uuid.uuid4())
        while qid in existing_ids:
            qid = str(uuid.uuid4())
        q["id"] = qid
        existing.append(q)
        existing_enunciados.add(q["enunciado"])
        existing_ids.add(qid)
        added += 1

    data["questions"] = existing
    with open(SEED_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    from collections import Counter
    subj_count = Counter()
    for q in existing:
        subj_count[q["subject"]] += 1

    print(f"Resumo:")
    print(f"  Questões existentes antes: {len(existing) - added}")
    print(f"  Questões OAB adicionadas: {added}")
    print(f"  Questões puladas (já existem): {skipped_dup}")
    print(f"  Total final: {len(existing)}")
    print()
    print("Distribuição por assunto:")
    for s in sorted(subj_count.keys()):
        print(f"  {s}: {subj_count[s]}")


if __name__ == "__main__":
    main()
