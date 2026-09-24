import uuid
import logging
from datetime import datetime, timedelta, timezone
from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session
from database.models import Flashcard

logger = logging.getLogger("FlashcardManager")

# Banco de dados de flashcards cobrindo minuciosamente os 22 temas do Questionário da Prova de Contratos
FLASHCARD_BANK: Dict[str, List[Dict[str, str]]] = {
    "Planos do Negócio Jurídico (Escada Ponteana)": [
        {
            "front": "Quais são os três planos da Escada Ponteana no negócio jurídico e o que cada um analisa?",
            "back": "1) Plano da Existência (substantivos: manifestação de vontade, partes, objeto e forma);\n2) Plano da Validade (adjetivos: vontade livre, agente capaz, objeto lícito/possível/determinado e forma prescrita em lei - art. 104, CC);\n3) Plano da Eficácia (elementos acidentais: condição, termo e encargo; produção de efeitos)."
        },
        {
            "front": "Qual a diferença prática entre um negócio inexistente e um negócio nulo (inválido)?",
            "back": "O negócio inexistente não preencheu os pressupostos materiais mínimos e sequer adentrou o ordenamento jurídico (não se convalesce nem gera efeitos típicos). O negócio nulo existe no mundo fático, mas padece de nulidade absoluta (art. 166, CC) por vício no plano da validade, necessitando de declaração judicial."
        },
        {
            "front": "Em qual degrau da Escada Ponteana se situam a condição, o termo e o encargo?",
            "back": "No Plano da Eficácia. São elementos acidentais que interferem na exigibilidade ou resolução dos efeitos do negócio jurídico, não afetando sua existência nem sua validade."
        }
    ],
    "Princípios do Direito Contratual": [
        {
            "front": "Quais são os principais princípios fundamentais do Direito Contratual brasileiro?",
            "back": "1) Autonomia Privada;\n2) Força Obrigatória (Pacta Sunt Servanda);\n3) Relatividade dos Efeitos dos Contratos;\n4) Consensualismo;\n5) Boa-fé Objetiva (art. 422, CC);\n6) Função Social do Contrato (art. 421, CC);\n7) Equilíbrio e Justiça Contratual."
        },
        {
            "front": "Como a Lei da Liberdade Econômica regulamentou a função social e a intervenção judicial (arts. 421 e 421-A)?",
            "back": "Consagrou a intervenção mínima do Estado, a excepcionalidade da revisão contratual, a presunção de paridade e simetria dos contratos civis e empresariais, e o dever do juiz de respeitar a alocação de riscos convencionada pelas partes."
        },
        {
            "front": "O que significa a eficácia externa da função social do contrato?",
            "back": "Significa que o contrato não pode causar prejuízos a terceiros nem à coletividade, bem como terceiros não podem interferir ilicitamente na relação contratual alheia (tutela externa do crédito)."
        }
    ],
    "Boa-fé Objetiva e Figuras Parcelares": [
        {
            "front": "O que significa 'Venire Contra Factum Proprium'? Cite um exemplo prático.",
            "back": "É a proibição do comportamento contraditório decorrente da boa-fé objetiva (art. 422, CC). Impede que alguém exerça posição jurídica em contradição com conduta anterior sua que gerou legítima confiança na outra parte. Exemplo: locador que aceita sem oposição o aluguel no dia 20 e, de repente, cobra multa porque o contrato previa dia 10."
        },
        {
            "front": "Qual a diferença exata entre Supressio (Verwirkung) e Surrectio (Erwirkung)?",
            "back": "Supressio é a perda/supressão de um direito ou prerrogativa contratual decorrente do seu não exercício continuado e prolongado no tempo. Surrectio é o reflexo positivo correlato: o surgimento/nascimento de um novo direito para a contraparte com base nessa prática reiterada."
        },
        {
            "front": "O que significa o dever anexo de proteção e informação na boa-fé objetiva?",
            "back": "São deveres implícitos de conduta ética que obrigam as partes a agir com lealdade, transparência, cooperação mútua, informação clara e guarda de sigilo antes, durante e após a execução do contrato."
        }
    ],
    "Interpretação dos Contratos no Direito Brasileiro": [
        {
            "front": "Como o Código Civil harmoniza a intenção das partes e a literalidade do contrato (art. 112)?",
            "back": "Art. 112, CC: 'Nas declarações de vontade se atenderá mais à intenção nelas consubstanciada do que ao sentido literal da linguagem'. Prevalece a vontade real e o propósito prático comum sobre a frieza gramatical das palavras."
        },
        {
            "front": "Como devem ser interpretados os negócios jurídicos benéficos e a renúncia (art. 114, CC)?",
            "back": "Interpretam-se ESTRITAMENTE (de forma restritiva). Como o disponente transfere patrimônio sem contraprestação ou abre mão de direito, não se admite interpretação extensiva que amplie a liberalidade."
        },
        {
            "front": "Como a redação de cláusulas ambíguas é interpretada nos contratos de adesão (art. 423, CC)?",
            "back": "Interpreta-se contra o estipulante (contra stipulatorem), isto é, adota-se a interpretação mais favorável ao aderente, que não teve oportunidade de negociar o conteúdo das cláusulas."
        }
    ],
    "Classificação dos Contratos": [
        {
            "front": "Qual a diferença entre contratos unilaterais, bilaterais e plurilaterais?",
            "back": "Unilaterais: geram obrigações para apenas um dos lados (ex: doação pura, mútuo). Bilaterais (sinalagmáticos): geram obrigações recíprocas e interdependentes para ambos os contratantes (ex: compra e venda, locação). Plurilaterais: envolvem múltiplos polos com finalidade comum (ex: sociedade, consórcio)."
        },
        {
            "front": "Qual a distinção entre contratos comutativos e contratos aleatórios?",
            "back": "Comutativos: as prestações são certas, conhecidas e estimadas pelas partes desde a celebração do contrato. Aleatórios: a prestação de uma das partes depende de um evento futuro e incerto (álea), gerando risco de ganho ou perda patrimonial."
        },
        {
            "front": "O que são contratos reais e contratos consensuais?",
            "back": "Consensuais: aperfeiçoam-se pelo mero acordo de vontades (consenso), que é a regra geral. Reais: só se aperfeiçoam com a efetiva entrega (tradição) da coisa (ex: comodato, mútuo, depósito, penhor)."
        }
    ],
    "Etapas de Formação do Contrato": [
        {
            "front": "Quais são as três etapas sucessivas de formação do contrato civil?",
            "back": "1) Punctuação (negociações preliminares / tratativas); \n2) Proposta ou Policitação (declaração receptícia e vinculante de contratar);\n3) Aceitação ou Oblação (aquiescência do oblato que sela o contrato)."
        },
        {
            "front": "As negociações preliminares (fase de punctuação) vinculam a celebração do contrato?",
            "back": "Não vinculam a obrigação de contratar, mas geram responsabilidade civil pré-contratual (dever de indenizar despesas e danos) se uma das partes romper abrupta e deslealmente as tratativas, violando a boa-fé objetiva."
        },
        {
            "front": "Quando o contrato entre pessoas ausentes é considerado concluído pelo Código Civil?",
            "back": "Pela Teoria da Agnição na subespécie da Expedição (art. 434, CC): considera-se concluído no momento em que a aceitação é expedida/enviada, salvo hipóteses de retratação tempestiva anterior ou simultânea."
        }
    ],
    "Estipulação em Favor de Terceiro": [
        {
            "front": "Quem são as partes e quem tem o direito de exigir na Estipulação em Favor de Terceiro?",
            "back": "Partes: Estipulante e Promitente; o Terceiro é o Beneficiário. Tanto o estipulante quanto o terceiro beneficiário possuem legitimidade para exigir o cumprimento da prestação do promitente (art. 436, CC)."
        },
        {
            "front": "O estipulante pode revogar a indicação e substituir o terceiro beneficiário?",
            "back": "Sim! O estipulante pode reservar-se o direito de substituir o terceiro designado no contrato, independentemente da anuência deste e do promitente, por ato entre vivos ou por testamento (art. 438, CC)."
        },
        {
            "front": "Cite um exemplo prático de Estipulação em Favor de Terceiro diverso de seguro de vida.",
            "back": "Exemplo: Um acordo de separação judicial no qual o pai estipula que a empresa locatária do seu imóvel deposite os aluguéis mensais diretamente na conta dos filhos menores para custeio de seus estudos."
        }
    ],
    "Promessa de Fato de Terceiro": [
        {
            "front": "O que ocorre se quem prometeu fato de terceiro não obtiver o cumprimento por este?",
            "back": "Aquele que prometeu fato de terceiro responderá por perdas e danos perante o credor (art. 439, CC). O terceiro não responde porque não manifestou vontade nem celebrou o contrato."
        },
        {
            "front": "Em quais casos o promitente fica exonerado de indenizar na promessa de fato de terceiro?",
            "back": "1) Quando o terceiro assumir expressamente a obrigação perante o credor (art. 440, CC);\n2) Quando o terceiro for cônjuge do promitente, dependendo de sua outorga o ato, e o regime de bens afetar seu patrimônio (art. 439, parágrafo único)."
        },
        {
            "front": "Cite um exemplo de Promessa de Fato de Terceiro.",
            "back": "Exemplo: Um produtor de eventos que contrata com uma casa de shows garantindo que uma banda famosa irá se apresentar no dia da festa; se a banda se recusar, o produtor responde integralmente por perdas e danos."
        }
    ],
    "Contratos Aleatórios - Conceito e Espécies": [
        {
            "front": "Qual a diferença entre contrato aleatório por natureza e acidentalmente aleatório?",
            "back": "Aleatório por natureza: o risco é da essência ontológica do contrato (ex: seguro, jogo e aposta). Acidentalmente aleatório: contrato originariamente comutativo (como compra e venda) cujas partes pactuam que o objeto fica sujeito a uma álea (arts. 458 a 461, CC)."
        },
        {
            "front": "Quais são as três espécies de contratos acidentalmente aleatórios no Código Civil?",
            "back": "1) Emptio Spei (venda da esperança - risco da existência);\n2) Emptio Rei Speratae (venda da coisa esperada - risco da quantidade);\n3) Risco sobre coisas existentes expostas a perigo (arts. 460 e 461)."
        }
    ],
    "Contrato Aleatório: Emptio Spei": [
        {
            "front": "O que é o contrato de 'Emptio Spei' (art. 458 do CC) e cite um exemplo?",
            "back": "É a venda da esperança. O risco assumido pelo comprador concerne à própria EXISTÊNCIA da coisa futura. O comprador deve pagar 100% do preço ainda que NADA venha a existir, salvo se houver dolo ou culpa do alienante. Exemplo: compra antecipada pelo valor fixo de R$ 1.000 de tudo o que for capturado em um único lance de rede de pesca."
        },
        {
            "front": "Na emptio spei, em que hipótese o comprador não é obrigado a pagar o preço?",
            "back": "Se o alienante agir com dolo ou culpa para a não ocorrência da coisa (ex: o pescador sequer foi ao mar lançar a rede ou sabotou a pesca)."
        }
    ],
    "Contrato Aleatório: Emptio Rei Speratae": [
        {
            "front": "O que é o contrato de 'Emptio Rei Speratae' (art. 459 do CC) e cite um exemplo?",
            "back": "É a venda da coisa esperada. O risco assumido pelo comprador recai sobre a QUANTIDADE, mas não sobre a existência. Se vier qualquer quantidade (mesmo mínima), o preço integral é devido. Mas se NADA vier a existir, o contrato é ineficaz e o alienante restitui o preço recebido. Exemplo: compra da safra futura de laranjas de um pomar."
        },
        {
            "front": "Qual a diferença fulcral entre Emptio Spei e Emptio Rei Speratae?",
            "back": "Na Emptio Spei o risco é da EXISTÊNCIA (se colher zero peixes, paga tudo). Na Emptio Rei Speratae o risco é apenas da QUANTIDADE (se colher zero laranjas, o alienante devolve o dinheiro; se colher 1 laranja, o comprador paga tudo)."
        }
    ],
    "Contrato Aleatório: Coisas Existentes Expostas a Risco": [
        {
            "front": "Como funciona o contrato sobre coisas existentes mas expostas a risco (art. 460 do CC)?",
            "back": "O adquirente assume o risco da perda ou deterioração da coisa que já esteja exposta a perigo ou transporte arriscado. O alienante tem direito ao preço mesmo que a coisa já não existisse no dia do contrato, desde que estivesse de boa-fé."
        },
        {
            "front": "Quando a venda aleatória de coisa exposta a risco pode ser anulada (art. 461 do CC)?",
            "back": "Pode ser anulada como dolosa pelo prejudicado se provar que o outro contratante não ignorava a consumação do risco (já sabia que a carga havia naufragado ou sido destruída antes do contrato)."
        }
    ],
    "Contrato Preliminar / Promessa de Contratar": [
        {
            "front": "Quais os requisitos de validade do Contrato Preliminar segundo o art. 462 do CC?",
            "back": "O contrato preliminar, exceto quanto à FORMA, deve conter todos os requisitos essenciais ao contrato a ser celebrado (capacidade, objeto lícito, preço e consentimento). Pode ser celebrado por instrumento particular mesmo que o definitivo exija escritura pública."
        },
        {
            "front": "O que pode fazer o promitente comprador se o vendedor se recusar a outorgar a escritura definitiva?",
            "back": "Esgotado o prazo e sem cláusula de arrependimento, o credor pode mover ação de adjudicação compulsória para obter suprimento judicial da vontade (art. 464, CC), valendo a sentença como título translativo, ou resolver em perdas e danos (art. 465)."
        }
    ],
    "Contrato com Pessoa a Declarar": [
        {
            "front": "O que é o Contrato com Pessoa a Declarar e qual o prazo legal para a indicação (electio amici)?",
            "back": "É o contrato em que uma das partes se reserva o direito de nomear terceiro que assumirá sua posição jurídica com efeito retroativo (ex tunc). O prazo legal supletivo para indicar o terceiro é de 5 DIAS após a conclusão do contrato (art. 468, CC), salvo convenção em contrário."
        },
        {
            "front": "Cite um exemplo prático de Contrato com Pessoa a Declarar.",
            "back": "Exemplo: Um corretor adquire um galpão em leilão constando a cláusula 'pro amico' (com pessoa a declarar), para posteriormente nomear a empresa investidora que realmente explorará a atividade, evitando especulação imobiliária."
        },
        {
            "front": "Se a pessoa nomeada for insolvente e o estipulante ignorava, quem responde pelo contrato?",
            "back": "O contrato produzirá seus efeitos unicamente entre os contratantes originários (o próprio estipulante continua obrigado), se a pessoa nomeada era incapaz ou insolvente no momento da nomeação (art. 470, II, CC)."
        }
    ],
    "Contrato com Pessoa a Declarar vs. Outros Contratos": [
        {
            "front": "Qual a diferença entre o Contrato com Pessoa a Declarar e a Representação/Mandato?",
            "back": "No Mandato, o mandatário age em nome e por conta do mandante desde o início. No Contrato com Pessoa a Declarar, a parte contrata em seu próprio nome e só depois nomeia o terceiro; caso este recuse, o contratante originário permanece pessoalmente obrigado."
        },
        {
            "front": "Qual a diferença entre o Contrato com Pessoa a Declarar e a Estipulação em Favor de Terceiro?",
            "back": "Na Estipulação em Favor de Terceiro, o terceiro é apenas beneficiário de uma vantagem econômica (não assume deveres contratuais). No Contrato com Pessoa a Declarar, o terceiro assume a posição contratual inteira (direitos e obrigações)."
        }
    ],
    "Vícios Redibitórios - Conceito e Requisitos": [
        {
            "front": "O que são Vícios Redibitórios e quais são seus requisitos legais cumulativos (art. 441 do CC)?",
            "back": "São defeitos ocultos na coisa recebida em contrato comutativo ou doação onerosa que a tornam imprópria ao uso ou lhe diminuem o valor. Requisitos: 1) Contrato oneroso/comutativo ou doação modal; 2) Defeito oculto (não aparente); 3) Gravidade do vício; 4) Preexistência à tradição; 5) Ignorância do vício pelo adquirente."
        },
        {
            "front": "O doador de uma doação pura e simples responde por vícios redibitórios?",
            "back": "NÃO! A responsabilidade por vícios redibitórios aplica-se somente a contratos comutativos onerosos e a doações ONEROSAS/MÓDAIS (com encargo), conforme art. 441, parágrafo único, do CC."
        }
    ],
    "Efeitos da Boa-fé e Má-fé do Alienante no Vício": [
        {
            "front": "A ciência do defeito pelo alienante gera efeitos diferentes? O que prevê o art. 443 do CC?",
            "back": "SIM! Se o alienante SABIA do vício (má-fé), restituirá o que recebeu mais PERDAS E DANOS. Se o alienante NÃO SABIA do vício (boa-fé), apenas restituirá o valor recebido mais as despesas do contrato, ficando ISENTO de perdas e danos."
        },
        {
            "front": "A boa-fé subjetiva (ignorância do vício) exonera o alienante de devolver o valor da coisa?",
            "back": "NÃO! A responsabilidade pelo vício redibitório é de garantia objetiva: ele responde pelo desfazimento do contrato ou pelo abatimento no preço mesmo que estivesse de boa-fé; sua boa-fé apenas o livra de pagar perdas e danos adicionais."
        }
    ],
    "Ações Edilícias (Redibitória e Estimatória/Quanti Minoris)": [
        {
            "front": "Quais são as duas Ações Edilícias e qual a característica preponderante de cada uma delas?",
            "back": "1) Ação Redibitória: visa a RESOLUÇÃO do contrato com devolução da coisa defeituosa e restituição do preço pago;\n2) Ação Estimatória (ou Quanti Minoris): visa a CONSERVAÇÃO do contrato mediante abatimento proporcional do preço pago em virtude da desvalorização sofrida."
        },
        {
            "front": "O comprador pode ajuizar conjuntamente a Ação Redibitória e a Estimatória para o mesmo bem?",
            "back": "NÃO. São ações de escolha disjuntiva/alternativa. O adquirente tem o direito potestativo de eleger uma delas; escolhendo uma, preclui a faculdade de pleitear a outra."
        }
    ],
    "Vício Redibitório vs. Entrega de Coisa Diversa (Aliud Pro Alio)": [
        {
            "front": "A entrega de coisa diversa da contratada (aliud pro alio) constitui vício redibitório?",
            "back": "NÃO! Constitui INADIMPLEMENTO ABSOLUTO da obrigação de dar/entregar (arts. 389 e 475, CC), sujeita aos prazos prescricionais gerais de responsabilidade civil contratual (art. 205, 10 anos). No vício redibitório, a coisa entregue é a contratada, porém com defeito oculto."
        },
        {
            "front": "Cite um exemplo que diferencia vício redibitório de erro essencial ou 'aliud pro alio'.",
            "back": "Comprar um touro reprodutor e receber o touro contratado, mas que é estéril = vício redibitório (coisa certa, vício oculto). Comprar um cavalo de corrida e o vendedor entregar uma égua de tração = aliud pro alio (inadimplemento da obrigação de entrega)."
        }
    ],
    "Prazos Decadenciais dos Vícios Redibitórios": [
        {
            "front": "Quais são os prazos decadenciais gerais para reclamar vícios redibitórios no Código Civil (art. 445)?",
            "back": "Contados da entrega efetiva (tradição): 30 DIAS para bens móveis; 1 ANO para bens imóveis. Se o adquirente já estava na posse da coisa, o prazo conta da alienação e cai pela metade (15 dias para móveis, 6 meses para imóveis)."
        },
        {
            "front": "Como funciona o prazo quando o vício redibitório só puder ser conhecido mais tarde?",
            "back": "O prazo de 30 dias (móvel) ou 1 ano (imóvel) conta-se a partir do momento em que o adquirente tiver CIÊNCIA do vício, desde que essa ciência ocorra no prazo máximo de 180 DIAS para bens móveis e de 1 ANO para bens imóveis (art. 445, § 1º, CC)."
        }
    ],
    "Extinção dos Contratos - Resolução e Cláusula Resolutiva": [
        {
            "front": "Qual a diferença entre resolução, resilição e rescisão contratual?",
            "back": "Resolução: extinção por inadimplemento culposo ou fortuito (arts. 474 e 475, CC). Resilição: extinção pela vontade das partes, podendo ser bilateral (distrato) ou unilateral (denúncia/aviso prévio - arts. 472 e 473). Rescisão: termo genérico ou extinção por vício congênito contemporâneo à formação (lesão, estado de perigo)."
        },
        {
            "front": "Qual a diferença de eficácia entre a cláusula resolutiva expressa e a tácita (art. 474 do CC)?",
            "back": "A cláusula resolutiva expressa opera de pleno direito (automaticamente pelo inadimplemento). A cláusula resolutiva tácita depende de interpelação judicial para constituir a parte em mora e rescindir o vínculo."
        }
    ],
    "Exceção do Contrato Não Cumprido e Onerosidade Excessiva": [
        {
            "front": "O que é a 'Exceptio Non Adimpleti Contractus' (art. 476 do CC) e quais seus pressupostos?",
            "back": "É a exceção do contrato não cumprido. Nos contratos bilaterais e sinalagmáticos, nenhum dos contratantes, antes de cumprida a sua própria obrigação, pode exigir o implemento da obrigação do outro. É uma defesa de direito material."
        },
        {
            "front": "Quais os requisitos para pleitear a resolução do contrato por onerosidade excessiva (art. 478 do CC)?",
            "back": "1) Contrato de execução continuada ou diferida; 2) Prestação excessivamente onerosa para uma das partes com extrema vantagem para a outra; 3) Acontecimento extraordinário e imprevisível (Teoria da Imprevisão)."
        }
    ]
}

class FlashcardManager:
    @staticmethod
    def create_cards_for_subject(db: Session, subject: str, session_id: str = "default") -> List[Flashcard]:
        """Gera e salva flashcards padrão para o assunto do estudante se não existirem no deck do banco"""
        cards = FLASHCARD_BANK.get(subject)
        if cards is None:
            logger.warning("Nenhum flashcard cadastrado para '%s' — pulando", subject)
            return []
        created_cards = []
        
        for idx, card_data in enumerate(cards):
            card_id = f"fc_{session_id}_{subject.replace(' ', '_')}_{idx}"
            
            # Verifica se já existe para esta sessão
            existing = db.query(Flashcard).filter(Flashcard.id == card_id).first()
            if not existing:
                fc = Flashcard(
                    id=card_id,
                    session_id=session_id,
                    subject=subject,
                    front=card_data["front"],
                    back=card_data["back"],
                    box=1,
                    interval_days=1,
                    next_revision_date=datetime.now(timezone.utc).replace(tzinfo=None)
                )
                db.add(fc)
                created_cards.append(fc)
            else:
                created_cards.append(existing)
                
        db.commit()
        return created_cards

    @staticmethod
    def create_card_from_error(db: Session, question: Dict[str, Any], session_id: str = "default") -> Optional[Flashcard]:
        """Cria instantaneamente um flashcard focado quando o aluno erra uma questão"""
        q_id = str(question.get("id") or uuid.uuid4().hex[:8])[:30]
        card_id = f"fc_err_{session_id}_{q_id}"
        
        existing = db.query(Flashcard).filter(Flashcard.id == card_id).first()
        if existing:
            # Reseta intervalo para forçar revisão imediata
            existing.box = 1
            existing.interval_days = 1
            existing.mastered = False
            existing.next_revision_date = datetime.now(timezone.utc).replace(tzinfo=None)
            db.commit()
            return existing
            
        subject = question.get("subject", "Contratos")
        bank = question.get("bank", "Questão")
        enunciado = question.get("enunciado", "")
        gabarito = question.get("gabarito", "")
        options = question.get("options", {})
        texto_correto = options.get(gabarito, "") if isinstance(options, dict) else ""
        expl = question.get("explanation", "")
        art = question.get("article", "")
        basis = question.get("legal_basis", "")
        
        front = f"⚠️ [REVISÃO DE ERRO - {bank} | {subject}]\n\n{enunciado}"
        back = (
            f"✅ GABARITO CORRETO: ({gabarito})\n"
            f"{texto_correto}\n\n"
            f"📖 FUNDAMENTAÇÃO LEGAL: {art}\n"
            f"{basis}\n\n"
            f"💡 EXPLICAÇÃO DIDÁTICA:\n{expl}"
        )
        
        fc = Flashcard(
            id=card_id,
            session_id=session_id,
            subject=subject,
            front=front,
            back=back,
            box=1,
            interval_days=1,
            next_revision_date=datetime.now(timezone.utc).replace(tzinfo=None)
        )
        db.add(fc)
        db.commit()
        return fc

    @staticmethod
    def get_due_flashcards(db: Session, session_id: str = "default") -> List[Flashcard]:
        """Obtém flashcards agendados para revisão hoje (exclui dominados)"""
        now = datetime.now(timezone.utc).replace(tzinfo=None)
        return db.query(Flashcard).filter(
            Flashcard.next_revision_date <= now,
            Flashcard.session_id == session_id,
            Flashcard.mastered == False
        ).all()

    @staticmethod
    def get_all_flashcards(db: Session, subject: str = None, session_id: str = "default", include_mastered: bool = False) -> List[Flashcard]:
        """Obtém todos os flashcards do banco, opcionalmente filtrados por assunto"""
        query = db.query(Flashcard).filter(Flashcard.session_id == session_id)
        if subject:
            query = query.filter(Flashcard.subject == subject)
        if not include_mastered:
            query = query.filter(Flashcard.mastered == False)
        return query.all()

    @staticmethod
    def mark_as_mastered(db: Session, card_id: str, session_id: str = "default") -> Optional[Flashcard]:
        """Marca o flashcard como dominado (não aparecerá mais nas revisões agendadas)"""
        card = db.query(Flashcard).filter(
            Flashcard.id == card_id,
            Flashcard.session_id == session_id
        ).first()
        if card:
            card.mastered = True
            card.box = 5
            card.interval_days = 30
            card.next_revision_date = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(days=30)
            card.last_reviewed = datetime.now(timezone.utc).replace(tzinfo=None)
            db.commit()
        return card

    @classmethod
    def process_review(cls, db: Session, card_id: str, is_easy: bool, session_id: str = "default") -> Optional[Flashcard]:
        """Processa a auto-avaliação do flashcard e atualiza sua data de repetição espaçada"""
        card = db.query(Flashcard).filter(
            Flashcard.id == card_id,
            Flashcard.session_id == session_id
        ).first()
        if card:
            from services.scheduler import SpacedRepetitionScheduler
            SpacedRepetitionScheduler.update_flashcard_repetition(card, is_easy)
            db.commit()
        return card
