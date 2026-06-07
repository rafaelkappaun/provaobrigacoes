import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from database.models import Flashcard

# Banco de dados de flashcards offline de alta qualidade para todos os temas
FLASHCARD_BANK: Dict[str, List[Dict[str, str]]] = {
    "Pagamento - Geral": [
        {"front": "Quem é o sujeito ativo e quem é o sujeito passivo no adimplemento?", "back": "O devedor é o sujeito ativo do pagamento (quem realiza a conduta), e o credor é o sujeito passivo (quem recebe)."},
        {"front": "O que acontece se o pagamento for realizado por terceiro com desconhecimento do devedor?", "back": "Extingue a dívida, mas o devedor não é obrigado a reembolsar se demonstrar que tinha meios para ilidir (anular/impedir) a cobrança. Art. 306, CC."},
        {"front": "Qual a consequência de pagar antes de vencida a dívida?", "back": "Se feito por terceiro não interessado, o reembolso só poderá ser exigido no vencimento original da obrigação. Art. 305, parágrafo único, CC."}
    ],
    "Quem deve pagar": [
        {"front": "Qualquer interessado pode pagar a dívida?", "back": "Sim. E caso haja oposição do credor, pode usar os meios de exoneração (ex: consignação). Art. 304, CC."},
        {"front": "Qual a diferença de efeitos entre o terceiro interessado e o não interessado?", "back": "O interessado se sub-roga nos direitos do credor. O não interessado que paga em seu nome tem apenas direito a reembolso, sem sub-rogação. Arts. 304/305, CC."},
        {"front": "O que é um 'terceiro interessado'?", "back": "É aquele que pode sofrer prejuízo patrimonial caso a dívida não seja paga (ex: o fiador, o avalista, o adquirente do imóvel hipotecado)."}
    ],
    "A quem se deve pagar": [
        {"front": "O pagamento feito ao credor putativo de boa-fé é válido?", "back": "Sim, é plenamente válido, mesmo provado depois que ele não era o credor legítimo. Art. 309, CC."},
        {"front": "O que rege o ditado popular 'quem paga mal paga duas vezes' no Código Civil?", "back": "O pagamento feito a quem não é credor (ou representante) só vale se ratificado por este ou se reverter em seu proveito. Art. 308, CC."},
        {"front": "O pagamento ao credor cujo crédito foi penhorado é válido?", "back": "Não. Se o devedor foi notificado da penhora e pagar ao credor, o pagamento não vale contra terceiros penhorantes. Art. 312, CC."}
    ],
    "Objeto do pagamento e sua prova": [
        {"front": "O credor é obrigado a receber prestação diversa se for mais valiosa?", "back": "Não. O credor não pode ser obrigado a receber prestação diversa da que lhe é devida, ainda que mais valiosa. Art. 313, CC."},
        {"front": "O devedor é obrigado a pagar em parcelas se o contrato previu parcela única?", "back": "Não. O credor não pode ser obrigado a receber por partes, nem o devedor a pagar por partes, se não convencionado. Art. 314, CC."},
        {"front": "Qual o principal meio de prova do pagamento?", "back": "A quitação (recibo), que pode ser dada por instrumento particular e conter os requisitos do Art. 320, CC."}
    ],
    "Lugar do pagamento": [
        {"front": "Qual a regra geral para o lugar do pagamento se não convencionado?", "back": "No domicílio do devedor (obrigação querível ou 'quérable'). Art. 327, CC."},
        {"front": "O que caracteriza a obrigação 'portável' (portable)?", "back": "É aquela em que o pagamento deve ser feito no domicílio do credor, por força de lei ou convenção contratual."},
        {"front": "O pagamento reiterado em local diverso do previsto em contrato presume o quê?", "back": "Faz presumir renúncia do credor relativamente ao previsto no instrumento. Art. 330, CC."}
    ],
    "Tempo do pagamento": [
        {"front": "Nas obrigações sem prazo assinalado, quando o credor pode cobrar?", "back": "Imediatamente, salvo disposição especial do Código Civil. Art. 331, CC."},
        {"front": "Em quais casos o credor pode cobrar a dívida antes de vencido o prazo?", "back": "Insolvência/falência do devedor; penhora do bem dado em garantia por outro credor; garantias insuficientes não reforçadas. Art. 333, CC."},
        {"front": "O vencimento antecipado do devedor principal se propaga aos fiadores?", "back": "Não. Nos casos de solidariedade passiva, o vencimento antecipado não se propaga aos codevedores ou fiadores solventes. Art. 333, parágrafo único."}
    ],
    "Consignação em pagamento": [
        {"front": "O que caracteriza a consignação em pagamento?", "back": "O depósito judicial ou em estabelecimento bancário da coisa ou quantia devida, para fins de exoneração da obrigação. Art. 334, CC."},
        {"front": "Quais as principais hipóteses que autorizam a consignação?", "back": "Recusa injusta do credor em receber/dar quitação; credor incapaz, desconhecido ou ausente; dúvida sobre quem é o credor; litígio sobre o crédito. Art. 335, CC."},
        {"front": "Até que momento o devedor pode levantar o depósito consignado?", "back": "Enquanto o credor não declarar que aceita o depósito, ou não o impugnar, o devedor pode levantá-lo, pagando as despesas. Art. 336, CC."}
    ],
    "Pagamento com sub-rogação": [
        {"front": "O que é a sub-rogação legal?", "back": "É a substituição automática do credor operada de pleno direito pela lei (ex: fiador que paga a dívida, adquirente de imóvel hipotecado). Art. 346, CC."},
        {"front": "O que caracteriza a sub-rogação convencional?", "back": "A transferência acordada de direitos, ocorrendo quando o credor recebe o pagamento de terceiro e expressamente lhe transfere os direitos. Art. 347, CC."},
        {"front": "Qual o limite do reembolso na sub-rogação legal?", "back": "O sub-rogado não pode reclamar do devedor mais do que despendeu para desobrigá-lo. Art. 350, CC."}
    ],
    "Imputação do pagamento": [
        {"front": "O que é a imputação do pagamento?", "back": "A indicação de qual dívida está sendo quitada quando o devedor possui dois ou mais débitos da mesma natureza com o mesmo credor. Art. 352, CC."},
        {"front": "Havendo juros e capital vencidos, onde se imputa primeiro o pagamento?", "back": "Primeiro nos juros vencidos e, depois, no capital principal, salvo acordo em contrário. Art. 354, CC."},
        {"front": "Se nem o devedor nem o credor indicarem, onde a lei imputa o pagamento?", "back": "Nas dívidas líquidas e vencidas em primeiro lugar. Sendo todas vencidas ao mesmo tempo, na mais onerosa. Art. 355, CC."}
    ],
    "Dação em pagamento": [
        {"front": "O que é a dação em pagamento?", "back": "Ocorre quando o credor consente em receber prestação diversa da que lhe era devida (ex: receber um carro em vez de dinheiro). Art. 356, CC."},
        {"front": "O que acontece se o credor for evicto (perder judicialmente) do bem recebido em dação?", "back": "Restabelece-se a obrigação original (pecuniária), ficando sem efeito a quitação, ressalvados direitos de terceiros de boa-fé. Art. 359, CC."},
        {"front": "Quais regras se aplicam se as partes fixarem preço para a coisa dada em dação?", "back": "Regula-se pelas normas do contrato de compra e venda. Art. 357, CC."}
    ],
    "Novação": [
        {"front": "O que caracteriza a novação?", "back": "A extinção de uma obrigação anterior mediante a criação de uma nova obrigação substituta. Exige o 'animus novandi'. Art. 360, CC."},
        {"front": "O que é a novação por expromissão?", "back": "Novação subjetiva passiva onde um novo devedor substitui o antigo, independente do consentimento deste último. Art. 362, CC."},
        {"front": "O que ocorre com a fiança se houver novação sem anuência do fiador?", "back": "O fiador fica exonerado da garantia, pois não anuiu com a nova dívida criada. Art. 366, CC."}
    ],
    "Compensação": [
        {"front": "O que é compensação legal?", "back": "Extinção recíproca de obrigações entre duas pessoas que são credoras e devedoras uma da outra. Exige dívidas líquidas, vencidas e de coisas fungíveis da mesma espécie. Arts. 368/369, CC."},
        {"front": "Quais dívidas são excluídas de compensação legal por força do Art. 373?", "back": "As que provierem de esbulho/roubo; comodato ou depósito; e alimentos (verbas alimentares)."},
        {"front": "O fiador pode compensar sua dívida com o débito do credor ao devedor principal?", "back": "Sim, o fiador pode opor a compensação que o devedor principal teria contra o credor. Art. 371, CC."}
    ],
    "Confusão": [
        {"front": "O que é a extinção por confusão?", "back": "Reunião das qualidades de credor e devedor em uma mesma pessoa (ex: filho herda dívida que tinha com o pai falecido). Art. 381, CC."},
        {"front": "O que ocorre se a confusão cessar por causa subsequente?", "back": "Restabelece-se a obrigação anterior com todos os seus acessórios e garantias (ex: anulação do testamento). Art. 384, CC."},
        {"front": "A confusão pode ser parcial?", "back": "Sim, a confusão pode ser total ou apenas parcial, extinguindo apenas parte do débito. Art. 382, CC."}
    ],
    "Remissão das dívidas": [
        {"front": "O que é a remissão?", "back": "O perdão da dívida. É um ato bilateral que exige a aceitação (expressa ou tácita) do devedor para extinguir a obrigação. Art. 385, CC."},
        {"front": "A devolução do objeto empenhado (garantia) significa perdão da dívida?", "back": "Não, prova apenas a renúncia à garantia real (penhor), subsistindo o crédito principal. Art. 387, CC."},
        {"front": "Qual o efeito da remissão dada a um codevedor solidário?", "back": "Extingue a dívida na parte dele. O credor só pode cobrar os demais abatendo a quota perdoada. Art. 388, CC."}
    ],
    "Inadimplemento - Disposições gerais": [
        {"front": "Quem responde pelas perdas e danos no inadimplemento?", "back": "O devedor inadimplente responde por perdas e danos, mais juros, atualização monetária e honorários de advogado. Art. 389, CC."},
        {"front": "O devedor responde por caso fortuito ou força maior?", "back": "Em regra não, exceto se houver se responsabilizado expressamente ou se já estava em mora. Art. 393, CC."},
        {"front": "Nos contratos bilaterais, o inadimplemento permite o quê?", "back": "A parte lesada pode pedir a resolução do contrato ou exigir-lhe o cumprimento, cabendo em qualquer caso indenização."}
    ],
    "Mora - Geral": [
        {"front": "Qual a diferença de mora ex re e mora ex persona?", "back": "A mora ex re decorre do vencimento de obrigação com termo certo. A mora ex persona exige interpelação/notificação judicial ou extrajudicial por falta de termo. Art. 397, CC."},
        {"front": "Quem responde pelos danos em caso de mora do credor?", "back": "O credor responde pela conservação da coisa (salvo dolo do devedor) e deve ressarcir as despesas com a guarda. Art. 400, CC."},
        {"front": "Como se purga a mora do devedor?", "back": "Oferecendo a prestação mais os juros, a atualização monetária e os prejuízos decorrentes do atraso. Art. 401, I, CC."}
    ],
    "Mora do devedor": [
        {"front": "Quais os requisitos para constituição em mora do devedor?", "back": "Existência de obrigação exigível; descumprimento injustificado (atraso culposo); e interpelação (se mora ex persona). Art. 396, CC."},
        {"front": "O devedor responde pelo caso fortuito ocorrido durante sua mora?", "back": "Sim, responde pela impossibilidade da prestação mesmo que decorra de caso fortuito, a menos que prove que ocorreria mesmo se pontual. Art. 399, CC."},
        {"front": "O credor pode rejeitar a prestação se ela se tornar inútil devido à mora?", "back": "Sim. Se a prestação se tornar inútil ao credor devido ao atraso, este pode enjeitá-la e exigir perdas e danos. Art. 395, parágrafo único, CC."}
    ],
    "Mora do credor": [
        {"front": "O que caracteriza a mora do credor (mora accipiendi)?", "back": "A recusa injustificada em aceitar o pagamento no tempo, lugar e forma convencionados. Art. 394, CC."},
        {"front": "Quais os efeitos da mora do credor sobre a responsabilidade do devedor?", "back": "Isenta o devedor (salvo se agir com dolo) da responsabilidade pela conservação da coisa e transfere o risco de oscilação de preço. Art. 400, CC."},
        {"front": "A mora do credor afeta a cobrança de juros?", "back": "Sim, suspende a incidência de juros moratórios contra o devedor durante o período de mora do credor."}
    ],
    "Inadimplemento absoluto": [
        {"front": "Quando a mora se converte em inadimplemento absoluto?", "back": "Quando a prestação se torna inútil para o credor ou impossível de ser cumprida pelo devedor culposamente. Art. 395, parágrafo único."},
        {"front": "Qual a principal consequência do inadimplemento absoluto?", "back": "Conversão da obrigação em indenização equivalente (perdas e danos: danos emergentes + lucros cessantes). Art. 389, CC."},
        {"front": "O devedor responde se a impossibilidade for sem culpa?", "back": "Não. Se a prestação se impossibilitar sem culpa do devedor, a obrigação resolve-se sem perdas e danos para as partes."}
    ],
    "Perdas e danos": [
        {"front": "O que compreende as perdas e danos?", "back": "O dano emergente (o que efetivamente se perdeu) e o lucro cessante (o que razoavelmente se deixou de lucrar). Art. 402, CC."},
        {"front": "Como o Código Civil limita o nexo causal em perdas e danos?", "back": "Só são indenizáveis os prejuízos efetivos que decorram direta e imediatamente do inadimplemento. Art. 403, CC."},
        {"front": "O juiz pode conceder indenização suplementar em obrigações em dinheiro?", "back": "Sim. Se os juros moratórios não cobrirem o prejuízo real e não houver cláusula penal, o juiz pode conceder indenização. Art. 404, parágrafo único."}
    ],
    "Juros legais": [
        {"front": "Qual a taxa de juros de mora legal se não convencionada?", "back": "A taxa vigente para a mora do pagamento de impostos à Fazenda Nacional (atualmente a taxa SELIC). Art. 406, CC."},
        {"front": "Os juros moratórios são devidos apenas se alegado prejuízo?", "back": "Não. Os juros de mora são devidos independentemente da alegação de prejuízo do credor. Art. 407, CC."},
        {"front": "A partir de quando correm os juros de mora?", "back": "Nas obrigações contratuais, a partir da citação (ou vencimento se mora ex re). Nas extracontratuais (delito), desde o evento danoso. Art. 405, CC / Súmula 54 STJ."}
    ],
    "Cláusula penal": [
        {"front": "Qual o limite legal do valor da cláusula penal?", "back": "O valor da cominação imposta na cláusula penal não pode exceder o da obrigação principal. Art. 412, CC."},
        {"front": "Quando o juiz deve reduzir equitativamente a cláusula penal?", "back": "Se a obrigação principal tiver sido cumprida em parte, ou se a penalidade for manifestamente excessiva (deve reduzir de ofício). Art. 413, CC."},
        {"front": "O credor pode cobrar multa compensatória e perdas e danos cumulados?", "back": "Não, salvo se convencionado. E se convencionado, a multa funciona como mínimo, devendo provar o prejuízo excedente. Art. 416, parágrafo único."}
    ],
    "Arras ou sinal": [
        {"front": "Qual a função das arras confirmatórias?", "back": "Sinalizar o fechamento do negócio e servir de taxa mínima de indenização em caso de inadimplemento. Permite indenização suplementar. Arts. 418/419, CC."},
        {"front": "O que caracteriza as arras penitenciais?", "back": "Arras pactuadas quando há direito de arrependimento contratual. Funcionam como indenização máxima, vedando suplementação. Art. 420, CC."},
        {"front": "Se quem recebeu as arras der causa à inexecução, o que deve fazer?", "back": "Deve devolvê-las em dobro a quem as deu, mais equivalente, com atualização, juros e honorários. Art. 418, CC."}
    ]
}

class FlashcardManager:
    @staticmethod
    def create_cards_for_subject(db: Session, subject: str, session_id: str = "default") -> List[Flashcard]:
        """Gera e salva flashcards padrão para o assunto do estudante se não existirem no deck do banco"""
        cards = FLASHCARD_BANK.get(subject, FLASHCARD_BANK["Pagamento - Geral"])
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
                    next_revision_date=datetime.utcnow()
                )
                db.add(fc)
                created_cards.append(fc)
            else:
                created_cards.append(existing)
                
        db.commit()
        return created_cards

    @staticmethod
    def get_due_flashcards(db: Session, session_id: str = "default") -> List[Flashcard]:
        """Obtém flashcards agendados para revisão hoje (exclui dominados)"""
        now = datetime.utcnow()
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
    def mark_as_mastered(db: Session, card_id: str, session_id: str = "default") -> Flashcard:
        """Marca o flashcard como dominado (não aparecerá mais nas revisões agendadas)"""
        card = db.query(Flashcard).filter(
            Flashcard.id == card_id,
            Flashcard.session_id == session_id
        ).first()
        if card:
            card.mastered = True
            card.box = 5
            card.interval_days = 30
            card.next_revision_date = datetime.utcnow() + timedelta(days=30)
            card.last_reviewed = datetime.utcnow()
            db.commit()
        return card

    @classmethod
    def process_review(cls, db: Session, card_id: str, is_easy: bool, session_id: str = "default") -> Flashcard:
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
