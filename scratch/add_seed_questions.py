import json
from pathlib import Path
import uuid

seed_file = Path(__file__).resolve().parent.parent / "database" / "seed_questions.json"

# Load existing database
with open(seed_file, "r", encoding="utf-8") as f:
    db = json.load(f)

new_questions = [
    {
        "id": str(uuid.uuid4()),
        "subject": "Pagamento - Geral",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) João contraiu a obrigação de realizar a entrega de um trator seminovo a Marcos. Diante do vencimento da obrigação, João efetua a entrega voluntária do bem de acordo com as especificações pactuadas. À luz do Direito Civil, a extinção voluntária da obrigação por meio da execução espontânea da prestação devida caracteriza o(a):",
        "options": {
            "A": "Novação, haja vista que a entrega do trator substitui a obrigação originária pecuniária de forma imediata.",
            "B": "Adimplemento (ou pagamento), que é a execução voluntária da prestação devida pelo sujeito passivo ao sujeito ativo, extinguindo a relação jurídica obrigacional.",
            "C": "Remissão de dívidas, haja vista o desprendimento patrimonial voluntário em benefício do credor.",
            "D": "Dação em pagamento tácita, uma vez que a obrigação envolveu a entrega de coisa móvel infungível.",
            "E": "Imputação do pagamento unilateral, por iniciativa exclusiva do devedor do débito."
        },
        "gabarito": "B",
        "article": "Art. 304 do Código Civil",
        "legal_basis": "Art. 304 do Código Civil.",
        "explanation": "O pagamento (ou adimplemento) é o principal meio de extinção das obrigações, consistindo no cumprimento voluntário e espontâneo da prestação pactuada (seja de dar, fazer ou não fazer) pelo devedor em favor do credor."
    },
    {
        "id": str(uuid.uuid4()),
        "subject": "Quem deve pagar",
        "bank": "FGV",
        "difficulty": "Difícil",
        "enunciado": "(FGV) Lucas, irmão de Rodrigo (devedor de uma obrigação pecuniária de R$ 5.000,00 perante Camila), resolve realizar o pagamento da dívida sem o conhecimento de Rodrigo, pois este se encontra viajando. Lucas efetua o pagamento em seu próprio nome. Sabendo que Rodrigo possuía meios legais e eficientes para ilidir (anular) a cobrança de Camila por já ter compensado o valor anteriormente, assinale a opção correta à luz das regras sobre adimplemento por terceiros:",
        "options": {
            "A": "Lucas terá direito de exigir o reembolso integral do valor pago a Rodrigo, pois o pagamento de boa-fé sempre gera direito a reembolso.",
            "B": "Lucas se sub-roga automaticamente em todos os direitos e garantias que Camila possuía contra Rodrigo.",
            "C": "O pagamento feito por Lucas é nulo de pleno direito por ter ocorrido sem a prévia anuência ou procuração de Rodrigo.",
            "D": "O pagamento por terceiro não interessado, feito com desconhecimento ou oposição do devedor, não obriga a reembolso se este tinha meios para ilidir a ação.",
            "E": "Camila responderá criminalmente por enriquecimento sem causa, devendo restituir o valor pago em dobro a Rodrigo."
        },
        "gabarito": "D",
        "article": "Art. 306 do Código Civil",
        "legal_basis": "Art. 305 e Art. 306 do Código Civil.",
        "explanation": "De acordo com o art. 306 do CC, o pagamento feito por terceiro, com desconhecimento ou oposição do devedor, não obriga a reembolso se o devedor tinha meios para ilidir a ação. Como Rodrigo tinha meios para ilidir (compensação), Lucas não terá direito ao reembolso."
    },
    {
        "id": str(uuid.uuid4()),
        "subject": "Quem deve pagar",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) Rogério, devedor de uma obrigação de dar coisa certa, efetua o pagamento a Cláudio mediante a entrega de um veículo que pertence a seu pai, do qual Rogério não tinha autorização para dispor ou alienar. Sobre a validade desse pagamento envolvendo a transmissão de propriedade, de acordo com as normas do Código Civil, assinale a opção correta:",
        "options": {
            "A": "O pagamento é plenamente válido, cabendo ao verdadeiro proprietário (pai de Rogério) apenas pleitear indenização por perdas e danos contra o credor Cláudio.",
            "B": "Só vale o pagamento que importe transmissão da propriedade, quando feito por quem possa alienar a coisa; contudo, se for coisa fungível consumida de boa-fé, o pagamento será eficaz.",
            "C": "O pagamento por terceiro não proprietário é anulável no prazo decadencial de 4 anos a contar da data da tradição do bem móvel.",
            "D": "A validade da transmissão de propriedade de coisas móveis no adimplemento independe da titularidade do devedor, operando-se com a simples tradição.",
            "E": "O credor Cláudio responderá solidariamente com Rogério pelo crime de receptação culposa, independentemente de sua boa-fé."
        },
        "gabarito": "B",
        "article": "Art. 307 do Código Civil",
        "legal_basis": "Art. 307 do Código Civil.",
        "explanation": "Pelo caput do art. 307, só vale o pagamento que importe transmissão da propriedade quando feito por quem possa alienar a coisa. O parágrafo único, contudo, traz a exceção: se se der em pagamento coisa fungível, e o credor a receber de boa-fé, e a consumir, não se poderá mais reclamar do credor, resolvendo-se a relação em perdas e danos contra o pagador."
    },
    {
        "id": str(uuid.uuid4()),
        "subject": "A quem se deve pagar",
        "bank": "CESPE",
        "difficulty": "Médio",
        "enunciado": "(CESPE) O devedor Bruno realiza o pagamento diretamente a Tiago, credor relativamente incapaz, sem a presença de seu assistente legal. Posteriormente, o responsável legal de Tiago cobra Bruno pelo adimplemento da obrigação. Bruno alega que o pagamento foi voluntário e de boa-fé. Nessa situação, de acordo com o Código Civil, o pagamento efetuado por Bruno ao incapaz:",
        "options": {
            "A": "É nulo de pleno direito, devendo o devedor Bruno realizar novo pagamento sob a supervisão do assistente legal do incapaz.",
            "B": "É considerado válido se Bruno comprovar que o pagamento reverteu em proveito do credor incapaz.",
            "C": "Gera a extinção imediata da obrigação devido à aplicação da teoria do credor putativo.",
            "D": "É ineficaz, e Tiago fica obrigado a devolver o valor em dobro por cobrança indevida.",
            "E": "É plenamente válido e inquestionável, pois a incapacidade relativa do credor não obsta o recebimento de valores pecuniários."
        },
        "gabarito": "B",
        "article": "Art. 310 do Código Civil",
        "legal_basis": "Art. 310 do Código Civil.",
        "explanation": "O art. 310 do CC dispõe que 'Não vale o pagamento feito a quem se mostrava incapaz de quitá-lo, se o devedor não provar que reverteu em proveito do credor'. Ou seja, o pagamento ao incapaz em regra não vale, salvo se provado que o valor de fato beneficiou e reverteu em proveito do incapaz."
    },
    {
        "id": str(uuid.uuid4()),
        "subject": "A quem se deve pagar",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Júlio comparece ao estabelecimento de Flávio para adimplir uma obrigação contratual. No caixa do estabelecimento, encontra-se Roberto, funcionário que habitualmente atende no local e porta o respectivo bloco de recibos com a logomarca da empresa. Júlio paga a Roberto e recebe a respectiva quitação. Mais tarde, Flávio afirma que Roberto havia sido demitido no dia anterior e não tinha poderes para receber. À luz do Código Civil, o pagamento efetuado por Júlio:",
        "options": {
            "A": "É ineficaz por ter sido feito a terceiro sem poderes de representação vigentes.",
            "B": "É válido, pois considera-se autorizado a receber o pagamento o portador da quitação, salvo se as circunstâncias contrariarem a presunção resultante desse título.",
            "C": "É nulo por envolver credor putativo de má-fé, devendo Júlio pagar novamente a Flávio.",
            "D": "Gera solidariedade ativa automática entre Roberto e Flávio em relação ao valor recebido.",
            "E": "É anulável por erro substancial sobre a pessoa do credor."
        },
        "gabarito": "B",
        "article": "Art. 311 do Código Civil",
        "legal_basis": "Art. 311 do Código Civil.",
        "explanation": "De acordo com o art. 311 do CC, considera-se autorizado a receber o pagamento o portador da quitação, exceto se as circunstâncias contrariarem a presunção resultante desse título. Como Roberto portava o recibo e as circunstâncias eram normais, o pagamento é perfeitamente válido."
    },
    {
        "id": str(uuid.uuid4()),
        "subject": "Objeto do pagamento e sua prova",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Marcelo contraiu obrigação pecuniária de R$ 20.000,00 com vencimento em 30 dias perante Fábio. No vencimento, em razão de crise inflacionária severa e desequilíbrio imprevisível no contrato, Fábio exige a atualização do valor com base em moeda estrangeira ou ouro. Marcelo recusa-se e oferece o valor nominal em Real. Considerando as regras sobre prestação em dinheiro e teoria da imprevisão, assinale a opção correta:",
        "options": {
            "A": "Fábio está correto, pois o credor pode exigir a correção da moeda estrangeira em qualquer hipótese de desvalorização.",
            "B": "O pagamento em dinheiro deve ser feito em moeda corrente nacional, pelo valor nominal, sendo nulas as convenções de pagamento em ouro ou moeda estrangeira, ressalvados os casos previstos em lei especial.",
            "C": "A teoria da imprevisão autoriza a alteração unilateral do objeto pelo credor sempre que ocorrer inflação acima de dois dígitos.",
            "D": "As obrigações em dinheiro devem ser pagas na cotação oficial do dólar americano do dia do vencimento.",
            "E": "O juiz pode corrigir o valor nominal apenas se houver cláusula de escala móvel, sendo vedada a revisão em contratos sem tal cláusula."
        },
        "gabarito": "B",
        "article": "Art. 315 e Art. 318 do Código Civil",
        "legal_basis": "Arts. 315, 317 e 318 do Código Civil.",
        "explanation": "O art. 315 consagra o princípio do nominalismo (moeda nacional pelo valor nominal). O art. 318 estatui a nulidade de convenções de pagamento em ouro, moeda estrangeira ou de compensação de diferença cambial. A teoria da imprevisão (art. 317) permite revisão pelo juiz, a requerimento da parte, mas não alteração unilateral."
    },
    {
        "id": str(uuid.uuid4()),
        "subject": "Objeto do pagamento e sua prova",
        "bank": "FGV",
        "difficulty": "Difícil",
        "enunciado": "(FGV) Patrícia adquire um terreno com pagamento dividido em 24 prestações periódicas e consecutivas representada por notas promissórias. Ao pagar a 24ª prestação, o credor entrega o recibo sem fazer qualquer ressalva sobre as parcelas anteriores. Meses depois, o credor ingressa com ação de cobrança alegando que as parcelas 3 e 4 não foram adimplidas. Considerando as regras do Código Civil sobre quotas periódicas e devolução de título, assinale a opção correta:",
        "options": {
            "A": "A quitação da última parcela não gera qualquer presunção de pagamento das anteriores, devendo Patrícia apresentar o recibo de todas as 24 parcelas.",
            "B": "Sendo a dívida pagável em quotas periódicas, a quitação da última faz presumir, até prova em contrário, solvidas as anteriores. Ademais, a entrega do título faz presumir o pagamento.",
            "C": "O credor tem direito de exigir a prova do pagamento das parcelas anteriores de forma absoluta, sendo nula qualquer presunção de adimplemento sem o respectivo comprovante escrito.",
            "D": "A quitação da última cota presume extintos os juros e o capital de forma irretratável, vedada qualquer prova em contrário pelo credor.",
            "E": "A devolução das notas promissórias extingue a dívida por novação presumida e impede a cobrança judicial mesmo que comprovada fraude do devedor."
        },
        "gabarito": "B",
        "article": "Art. 322 e Art. 324 do Código Civil",
        "legal_basis": "Arts. 322, 323 e 324 do Código Civil.",
        "explanation": "O art. 322 estabelece que a quitação da última quota periódica faz presumir, até prova em contrário, solvidas as anteriores (presunção iuris tantum). O art. 324 estatui que a entrega do título ao devedor faz presumir o pagamento. Portanto, Patrícia goza de presunção legal, cabendo ao credor provar o inadimplemento."
    },
    {
        "id": str(uuid.uuid4()),
        "subject": "Tempo do pagamento",
        "bank": "OAB",
        "difficulty": "Difícil",
        "enunciado": "(OAB) André contraiu uma obrigação perante Renato com vencimento em 10 de dezembro. O contrato contava com fiança de Eduardo. Em 15 de outubro, André teve sua falência decretada judicialmente por insolvência. Renato cobra a dívida imediatamente de André e de seu fiador Eduardo em 20 de outubro. Eduardo recusa-se a pagar, alegando que o prazo do contrato não venceu. Sobre o tempo do pagamento e cobrança antecipada, assinale a opção correta:",
        "options": {
            "A": "Renato pode cobrar antecipadamente André e o fiador Eduardo de forma solidária e imediata devido à quebra de André.",
            "B": "A cobrança antecipada por insolvência do devedor principal é ineficaz contra o fiador ou codevedores solventes, que continuam vinculados apenas ao termo original do contrato.",
            "C": "O fiador Eduardo está obrigado ao pagamento imediato, pois a insolvência do devedor extingue o benefício de ordem e propaga os efeitos do vencimento antecipado a todos os garantidores.",
            "D": "A falência do devedor não autoriza o vencimento antecipado das obrigações civis, aplicando-se apenas às obrigações estritamente empresariais.",
            "E": "Eduardo está desonerado da fiança, pois a falência do devedor principal extingue as garantias acessórias automaticamente."
        },
        "gabarito": "B",
        "article": "Art. 333 do Código Civil",
        "legal_basis": "Art. 333, parágrafo único do Código Civil.",
        "explanation": "O art. 333 do CC autoriza o vencimento antecipado em caso de insolvência ou falência do devedor (inciso I). No entanto, o parágrafo único determina expressamente que nos casos de solidariedade passiva (ou fiança), o vencimento antecipado não se propaga aos codevedores ou fiadores solventes."
    },
    {
        "id": str(uuid.uuid4()),
        "subject": "Inadimplemento - Disposições gerais",
        "bank": "FGV",
        "difficulty": "Médio",
        "enunciado": "(FGV) Bernardo assume a obrigação de não construir edificação que ultrapasse a altura do muro divisório da propriedade de Arthur. Bernardo descumpre a obrigação e constrói um anexo de dois andares. Arthur exige a demolição e perdas e danos. Bernardo alega que Arthur deveria tê-lo interpelado judicialmente para constituí-lo em mora antes de exigir indenização. À luz do Código Civil, Bernardo:",
        "options": {
            "A": "Tem razão, pois as obrigações de não fazer exigem notificação prévia de 15 dias antes de configurado o inadimplemento.",
            "B": "É considerado inadimplente desde o dia em que realizou o ato que se havia obrigado a abster-se, independentemente de interpelação.",
            "C": "Só responde pelo valor do custo da demolição, sendo indevida qualquer verba a título de perdas e danos devido à natureza da obrigação.",
            "D": "Não responde pelo inadimplemento se demonstrar que a construção valorizou o imóvel vizinho de Arthur.",
            "E": "Pode purgar a mora a qualquer tempo oferecendo desfazer a obra em 90 dias sem arcar com indenização."
        },
        "gabarito": "B",
        "article": "Art. 390 do Código Civil",
        "legal_basis": "Art. 390 do Código Civil.",
        "explanation": "Nas obrigações de não fazer, o devedor é considerado inadimplente desde o dia em que executa o ato de que se devia abster (mora presumida, de pleno direito). Não há necessidade de interpelação ou notificação prévia."
    },
    {
        "id": str(uuid.uuid4()),
        "subject": "Inadimplemento - Disposições gerais",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Em razão do descumprimento culposo de um contrato de prestação de serviços por parte de Ricardo, o credor Felipe ingressa com ação de execução. Ricardo alega que não possui bens suficientes para honrar o débito e que sua responsabilidade deve se limitar aos bens dados em garantia contratual específica. Sobre a responsabilidade patrimonial no inadimplemento, de acordo com o Código Civil, assinale a opção correta:",
        "options": {
            "A": "Ricardo responde exclusivamente com os bens que estavam indicados como garantia no instrumento contratual original.",
            "B": "Pelo inadimplemento das obrigações respondem todos os bens do devedor, ressalvadas as restrições e impenhorabilidades previstas em lei.",
            "C": "A responsabilidade patrimonial civil limita-se a 30% dos bens líquidos do devedor para evitar superendividamento.",
            "D": "O credor só pode executar os bens do devedor após comprovar que a dívida não decorreu de caso fortuito ou força maior de natureza econômica.",
            "E": "O inadimplemento gera a prisão civil por dívida do devedor inadimplente caso este oculte bens da execução."
        },
        "gabarito": "B",
        "article": "Art. 391 do Código Civil",
        "legal_basis": "Art. 391 do Código Civil.",
        "explanation": "O art. 391 do Código Civil estabelece a regra da responsabilidade patrimonial genérica: 'Pelo inadimplemento das obrigações respondem todos os bens do devedor'. Obviamente, excetuam-se os bens impenhoráveis na forma da lei especial (Lei 8.009/90 e CPC)."
    },
    {
        "id": str(uuid.uuid4()),
        "subject": "Mora - Geral",
        "bank": "CESPE",
        "difficulty": "Difícil",
        "enunciado": "(CESPE) No que tange à purgação da mora e mora do credor, julgue a opção que reflete a disciplina do Código Civil brasileiro:",
        "options": {
            "A": "A mora do credor isenta o devedor, em qualquer hipótese, da responsabilidade pela conservação da coisa, mesmo que o devedor aja com dolo.",
            "B": "A purgação da mora pelo credor consiste em oferecer-se a receber o pagamento e sujeitar-se aos efeitos da sua mora até a mesma data.",
            "C": "O devedor em mora responde pela impossibilidade da prestação, exceto se provar que a impossibilidade ocorreria mesmo se a obrigação tivesse sido adimplida no prazo.",
            "D": "A mora do credor obriga-o a ressarcir as despesas com a conservação da coisa, mas não suspende a fluência dos juros de mora contra o devedor.",
            "E": "A purgação da mora pelo devedor extingue retroativamente todos os efeitos dos juros já acumulados, desobrigando-o do pagamento das custas."
        },
        "gabarito": "B",
        "article": "Art. 401 do Código Civil",
        "legal_basis": "Art. 399, Art. 400 e Art. 401 do Código Civil.",
        "explanation": "O art. 401, II, do CC determina que se purga a mora 'por parte do credor, oferecendo-se a receber o pagamento e sujeitando-se aos efeitos da sua mora até a mesma data'. A alternativa C erra porque omitiu a parte final do art. 399 ('se provar que o dano sobreviria, ainda que a obrigação fosse oportunamente desempenhada'). A alternativa A erra porque o art. 400 ressalva o dolo do devedor."
    },
    {
        "id": str(uuid.uuid4()),
        "subject": "Perdas e danos",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Diante do inadimplemento culposo de uma obrigação contratual por parte do devedor, o credor pleiteia indenização abrangendo danos emergentes, lucros cessantes e prejuízos remotos sofridos em sua atividade econômica de forma reflexa. Com relação ao nexo de causalidade das perdas e danos no Código Civil, assinale a opção correta:",
        "options": {
            "A": "O devedor responde por todos os prejuízos diretos, indiretos e reflexos sofridos pelo credor, bastando haver liame histórico entre os fatos.",
            "B": "Salvo as exceções previstas em lei, as perdas e danos devidas ao credor abrangem apenas o que ele efetivamente perdeu (danos emergentes), vedada a indenização por lucros cessantes.",
            "C": "Ainda que o inadimplemento resulte de dolo do devedor, as perdas e danos só incluem os prejuízos efetivos e os lucros cessantes que decorram direta e imediatamente do inadimplemento.",
            "D": "O nexo de causalidade no direito obrigacional adota a teoria do escopo da norma, que veda a indenização por lucros cessantes decorrentes de mora contratual simples.",
            "E": "O valor das perdas e danos deve ser fixado equitativamente pelo juiz, sendo nula qualquer cláusula de prefixação das perdas e danos pelas partes."
        },
        "gabarito": "C",
        "article": "Art. 403 do Código Civil",
        "legal_basis": "Art. 402 e Art. 403 do Código Civil.",
        "explanation": "Pelo art. 403 do CC, as perdas e danos só incluem os prejuízos efetivos e lucros cessantes decorrentes direta e imediatamente do inadimplemento. A teoria adotada é a do dano direto e imediato (teoria da interrupção do nexo causal), mesmo em caso de dolo do devedor."
    },
    {
        "id": str(uuid.uuid4()),
        "subject": "Juros legais",
        "bank": "FGV",
        "difficulty": "Médio",
        "enunciado": "(FGV) Douglas ingressou com ação de cobrança de dívida contratual não adimplida. As partes não estipularam no contrato a taxa de juros de mora a ser aplicada em caso de inadimplemento. De acordo com as disposições do Código Civil e a jurisprudência dominante, como devem ser calculados os juros moratórios legais?",
        "options": {
            "A": "Os juros de mora são limitados a 1% ao ano, aplicando-se subsidiariamente as regras do Código Tributário Nacional.",
            "B": "Quando não convencionados, os juros moratórios serão fixados segundo a taxa que estiver em vigor para a mora do pagamento de impostos devidos à Fazenda Nacional (taxa referencial Selic).",
            "C": "Na omissão das partes, aplica-se a taxa de 12% ao ano com capitalização diária, vedada a incidência de qualquer correção monetária concomitante.",
            "D": "Os juros moratórios dependem de alegação de prejuízo do credor e só podem ser cobrados se demonstrada a culpa grave do devedor.",
            "E": "A taxa aplicável é a taxa média de mercado de empréstimos pessoais divulgada mensalmente pelo Banco Central do Brasil."
        },
        "gabarito": "B",
        "article": "Art. 406 do Código Civil",
        "legal_basis": "Art. 406 e Art. 407 do Código Civil.",
        "explanation": "O art. 406 do CC dispõe que, quando não convencionados, os juros moratórios são calculados segundo a taxa vigente para a mora do pagamento de impostos devidos à Fazenda Nacional (taxa Selic, conforme tese fixada pelo STJ). O art. 407 complementa que são devidos independentemente de alegação de prejuízo."
    },
    {
        "id": str(uuid.uuid4()),
        "subject": "Cláusula penal",
        "bank": "OAB",
        "difficulty": "Médio",
        "enunciado": "(OAB) Um contrato de empreitada firmado entre duas empresas contém cláusula estipulando multa de 100% sobre o valor total do contrato caso o devedor atrase em um único dia a entrega da obra. O devedor concluiu 95% da obra no prazo contratado e atrasou o restante. O credor exige o pagamento integral da multa. Considerando as regras sobre cláusula penal, assinale a opção correta:",
        "options": {
            "A": "A multa contratual deve ser paga integralmente, vigendo de forma absoluta o princípio da autonomia da vontade e pacta sunt servanda.",
            "B": "A penalidade deve ser reduzida equitativamente pelo juiz se a obrigação principal tiver sido cumprida em parte, ou se o montante da penalidade for manifestamente excessivo, tendo em vista a natureza e a finalidade do negócio.",
            "C": "O valor da cláusula penal compensatória pode exceder o valor da obrigação principal se houver pactuação expressa sobre o prejuízo excedente.",
            "D": "A redução da cláusula penal é faculdade exclusiva das partes, sendo vedada a intervenção judicial de ofício sob pena de ativismo judicial.",
            "E": "O cumprimento parcial da obrigação não autoriza redução proporcional se a prestação remanescente se tornou inútil ao credor."
        },
        "gabarito": "B",
        "article": "Art. 413 do Código Civil",
        "legal_basis": "Art. 412 e Art. 413 do Código Civil.",
        "explanation": "O art. 413 do Código Civil estabelece o dever-poder de o juiz reduzir equitativamente a cláusula penal se a obrigação principal tiver sido cumprida em parte ou se for manifestamente excessiva. Trata-se de norma de ordem pública, permitindo redução judicial de ofício."
    },
    {
        "id": str(uuid.uuid4()),
        "subject": "Arras ou sinal",
        "bank": "FGV",
        "difficulty": "Difícil",
        "enunciado": "(FGV) Patrícia e Rodrigo firmaram compromisso de compra e venda de imóvel com entrega de arras confirmatórias de R$ 50.000,00 por Patrícia. O contrato não previu direito de arrependimento. Rodrigo deu causa ao inadimplemento definitivo da obrigação por desistência culposa. Patrícia comprova que o prejuízo real superou o valor do sinal recebido. À luz do Código Civil, Patrícia pode:",
        "options": {
            "A": "Apenas reaver os R$ 50.000,00 originais, sendo vedada qualquer indenização suplementar em arras confirmatórias.",
            "B": "Exigir a devolução do sinal mais o equivalente (sinal em dobro), com atualização monetária, juros e honorários de advogado. E, se provar maior prejuízo, pleitear indenização suplementar.",
            "C": "Pedir a conversão automática das arras confirmatórias em cláusula penal compensatória reduzida judicialmente.",
            "D": "Reter o sinal original de forma perpétua, extinguindo a obrigação sem possibilidade de indenização complementar.",
            "E": "Pedir apenas a devolução simples do sinal sob pena de enriquecimento sem causa."
        },
        "gabarito": "B",
        "article": "Art. 418 e Art. 419 do Código Civil",
        "legal_basis": "Arts. 418, 419 e 420 do Código Civil.",
        "explanation": "Nas arras confirmatórias (sem direito de arrependimento), a parte inocente pode exigir a devolução das arras mais o equivalente (ou seja, arras em dobro) se a outra parte der causa à inexecução. Se provar que os prejuízos reais superaram o sinal, pode pedir indenização suplementar (art. 419). Nas arras penitenciais (com direito de arrependimento), não há direito a indenização suplementar (art. 420)."
    }
]

# Append the new questions
db["questions"].extend(new_questions)

# Write back
with open(seed_file, "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print(f"Sucesso! {len(new_questions)} novas questões detalhadas adicionadas ao banco de sementes.")
