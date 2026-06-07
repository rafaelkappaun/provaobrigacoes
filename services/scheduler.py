from datetime import datetime, timedelta, timezone
from database.models import TopicMastery, Flashcard

# Sequência padrão de revisão espaçada em dias: 1, 3, 7, 15, 30
REVISION_INTERVALS = [1, 3, 7, 15, 30]

class SpacedRepetitionScheduler:
    @staticmethod
    def schedule_next_revision(mastery: TopicMastery, is_correct: bool, is_insecure: bool):
        """Atualiza a data da próxima revisão do assunto com base no desempenho"""
        now = datetime.now(timezone.utc).replace(tzinfo=None)

        if not is_correct:
            # Erro: reseta o intervalo para o passo inicial (1 dia)
            mastery.interval_days = 1
        else:
            # Acerto
            current_int = mastery.interval_days
            
            if is_insecure:
                # Acerto inseguro: não avança o intervalo ou reduz se possível, mantendo o reforço frequente
                if current_int in REVISION_INTERVALS:
                    idx = REVISION_INTERVALS.index(current_int)
                    # Mantém o mesmo ou reduz para o anterior
                    mastery.interval_days = REVISION_INTERVALS[max(0, idx - 1)]
                else:
                    mastery.interval_days = 1
            else:
                # Acerto seguro: avança na sequência
                if current_int == 0:
                    mastery.interval_days = 1
                elif current_int in REVISION_INTERVALS:
                    idx = REVISION_INTERVALS.index(current_int)
                    if idx < len(REVISION_INTERVALS) - 1:
                        mastery.interval_days = REVISION_INTERVALS[idx + 1]
                    else:
                        mastery.interval_days = 30 # Máximo de 30 dias
                else:
                    mastery.interval_days = 1
                    
        # Calcula a nova data de revisão
        mastery.next_revision_date = now + timedelta(days=mastery.interval_days)

    @staticmethod
    def update_flashcard_repetition(flashcard: Flashcard, is_easy: bool):
        """Atualiza o agendamento de repetição espaçada de um flashcard individual (Leitner Simplificado)"""
        now = datetime.now(timezone.utc).replace(tzinfo=None)

        if is_easy:
            # Avança na caixa (max caixa 5)
            flashcard.box = min(5, flashcard.box + 1)
            # Define o intervalo baseado na caixa
            # Caixa 1: 1 dia, Caixa 2: 3 dias, Caixa 3: 7 dias, Caixa 4: 15 dias, Caixa 5: 30 dias
            box_intervals = {1: 1, 2: 3, 3: 7, 4: 15, 5: 30}
            flashcard.interval_days = box_intervals.get(flashcard.box, 1)
        else:
            # Reseta para a caixa 1 (revisão em 1 dia)
            flashcard.box = 1
            flashcard.interval_days = 1
            
        flashcard.last_reviewed = now
        flashcard.next_revision_date = now + timedelta(days=flashcard.interval_days)
