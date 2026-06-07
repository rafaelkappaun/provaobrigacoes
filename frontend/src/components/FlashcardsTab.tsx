import React, { useState, useEffect } from 'react';
import { RefreshCw, Check, AlertCircle, BookOpen, Loader2 } from 'lucide-react';
import { apiFetch } from '../api';

interface Flashcard {
  id: string;
  subject: string;
  front: string;
  back: string;
  box: number;
  interval_days: number;
}

interface FlashcardsTabProps {
  apiBase: string;
}

export const FlashcardsTab: React.FC<FlashcardsTabProps> = ({ apiBase }) => {
  const [selectedSubject, setSelectedSubject] = useState<string>('');
  const [cards, setCards] = useState<Flashcard[]>([]);
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [isFlipped, setIsFlipped] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);
  const [submitting, setSubmitting] = useState<boolean>(false);
  const [dueOnly, setDueOnly] = useState<boolean>(false);
  const [reviewedCount, setReviewedCount] = useState<number>(0);

  // Lista todos os assuntos disponíveis para carregar
  const SUBJECT_LIST = [
    "Todos os Assuntos", "Pagamento - Geral", "Quem deve pagar", "A quem se deve pagar", 
    "Objeto do pagamento e sua prova", "Lugar do pagamento", "Tempo do pagamento", 
    "Consignação em pagamento", "Pagamento com sub-rogação", "Imputação do pagamento", 
    "Dação em pagamento", "Novação", "Compensação", "Confusão", "Remissão das dívidas",
    "Inadimplemento - Disposições gerais", "Mora - Geral", "Mora do devedor", "Mora do credor",
    "Inadimplemento absoluto", "Perdas e danos", "Juros legais", "Cláusula penal", "Arras ou sinal"
  ];

  useEffect(() => {
    fetchCards();
  }, [selectedSubject, dueOnly]);

  const fetchCards = async () => {
    setLoading(true);
    setCurrentIndex(0);
    setIsFlipped(false);
    
    try {
      let path = '/flashcards';
      const params = [];
      
      if (selectedSubject && selectedSubject !== "Todos os Assuntos") {
        params.push(`subject=${encodeURIComponent(selectedSubject)}`);
      }
      if (dueOnly) {
        params.push(`due_only=true`);
      }
      
      if (params.length > 0) {
        path += `?${params.join('&')}`;
      }
      
      const res = await apiFetch(apiBase, path);
      if (res.ok) {
        const data = await res.json();
        setCards(data);
      }
    } catch (e) {
      console.error("Erro ao carregar flashcards:", e);
    } finally {
      setLoading(false);
    }
  };

  const handleReview = async (isEasy: boolean) => {
    if (cards.length === 0 || submitting) return;
    
    const activeCard = cards[currentIndex];
    setSubmitting(true);
    
    try {
      const res = await apiFetch(apiBase, `/flashcards/${activeCard.id}/review`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ is_easy: isEasy })
      });
      
      if (res.ok) {
        setReviewedCount(prev => prev + 1);
        
        // Passa para o próximo card com transição suave
        setIsFlipped(false);
        setTimeout(() => {
          if (currentIndex < cards.length - 1) {
            setCurrentIndex(prev => prev + 1);
          } else {
            // Fim do deck, recarrega para filtrar os revisados
            fetchCards();
          }
          setSubmitting(false);
        }, 300);
      } else {
        setSubmitting(false);
      }
    } catch (e) {
      console.error(e);
      setSubmitting(false);
    }
  };

  const activeCard = cards[currentIndex];

  return (
    <div className="max-w-2xl mx-auto space-y-8 pb-12">
      {/* Filtros e Controles */}
      <div className="p-4 rounded-xl bg-slate-900 border border-slate-800 flex flex-col sm:flex-row justify-between items-stretch sm:items-center gap-4">
        <div className="flex-1">
          <label className="block text-xs font-bold text-slate-500 uppercase tracking-wider mb-1">Filtrar Assunto</label>
          <select
            value={selectedSubject}
            onChange={(e) => setSelectedSubject(e.target.value)}
            className="w-full bg-slate-950 border border-slate-850 rounded-lg px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-indigo-500 font-semibold"
          >
            {SUBJECT_LIST.map(s => (
              <option key={s} value={s}>{s}</option>
            ))}
          </select>
        </div>

        <div className="flex items-center gap-4 self-end sm:self-center">
          <label className="flex items-center gap-2 cursor-pointer select-none">
            <input
              type="checkbox"
              checked={dueOnly}
              onChange={(e) => setDueOnly(e.target.checked)}
              className="rounded bg-slate-950 border-slate-850 text-indigo-600 focus:ring-indigo-500 w-4 h-4"
            />
            <span className="text-xs font-bold text-slate-400">Apenas Agendados</span>
          </label>
          
          <button 
            onClick={fetchCards}
            className="p-2 bg-slate-950 border border-slate-850 hover:bg-slate-800 text-slate-300 rounded-lg transition-all"
            title="Recarregar Deck"
          >
            <RefreshCw size={14} />
          </button>
        </div>
      </div>

      {/* Conteúdo Central do Flashcard */}
      {loading ? (
        <div className="h-80 flex flex-col items-center justify-center space-y-3 p-8 bg-slate-900 border border-slate-800 rounded-2xl">
          <Loader2 className="animate-spin text-indigo-500" size={32} />
          <p className="text-sm font-bold text-slate-400">Embaralhando flashcards...</p>
        </div>
      ) : cards.length === 0 ? (
        <div className="p-10 rounded-2xl bg-slate-900 border border-slate-800 text-center space-y-4">
          <BookOpen className="text-slate-600 mx-auto" size={48} />
          <h4 className="text-lg font-black text-slate-300">Nenhum flashcard pendente!</h4>
          <p className="text-sm text-slate-500 max-w-sm mx-auto">
            {dueOnly 
              ? "Você já revisou todos os cards agendados por hoje. Desmarque 'Apenas Agendados' para praticar livremente!"
              : "Sem cards cadastrados para este assunto no momento."}
          </p>
        </div>
      ) : (
        <div className="space-y-6">
          {/* Header do Deck */}
          <div className="flex justify-between items-center text-xs text-slate-500 font-semibold px-2">
            <span>Tema: <strong className="text-indigo-400">{activeCard.subject}</strong></span>
            <span>Card {currentIndex + 1} de {cards.length}</span>
          </div>

          {/* Card 3D Flip */}
          <div 
            onClick={() => setIsFlipped(!isFlipped)}
            className="h-80 perspective-1000 cursor-pointer w-full select-none"
          >
            <div className={`relative w-full h-full text-center transition-transform duration-500 transform-style-3d ${
              isFlipped ? 'rotate-y-180' : ''
            }`}>
              {/* Frente */}
              <div className="absolute inset-0 w-full h-full bg-slate-900 border-2 border-slate-800 rounded-2xl p-8 flex flex-col justify-between items-center backface-hidden shadow-2xl">
                <span className="text-[10px] font-extrabold text-indigo-400 uppercase tracking-widest bg-indigo-500/10 px-2 py-0.5 rounded border border-indigo-500/20">PERGUNTA</span>
                <p className="text-lg md:text-xl font-bold text-slate-100 leading-relaxed max-w-md">
                  {activeCard.front}
                </p>
                <span className="text-xs font-bold text-slate-500 uppercase tracking-widest">Clique para ver a resposta</span>
              </div>
              
              {/* Verso */}
              <div className="absolute inset-0 w-full h-full bg-indigo-950/80 border-2 border-indigo-500/40 rounded-2xl p-8 flex flex-col justify-between items-center rotate-y-180 backface-hidden shadow-2xl overflow-y-auto">
                <span className="text-[10px] font-extrabold text-emerald-400 uppercase tracking-widest bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">RESPOSTA CC</span>
                <p className="text-base md:text-lg font-bold text-indigo-100 leading-relaxed max-w-md">
                  {activeCard.back}
                </p>
                <span className="text-xs font-bold text-indigo-400 uppercase tracking-widest">Clique para voltar à pergunta</span>
              </div>
            </div>
          </div>

          {/* Botões de Feedback de Repetição Espaçada */}
          <div className="flex justify-center items-center gap-4">
            <button
              disabled={submitting}
              onClick={() => handleReview(false)}
              className="flex-1 max-w-[200px] py-4 rounded-xl border border-red-900/60 bg-red-950/20 hover:bg-red-950/40 text-red-400 font-bold transition-all text-sm flex items-center justify-center gap-2 shadow-lg"
            >
              <AlertCircle size={16} /> Difícil (Rever Hoje)
            </button>
            
            <button
              disabled={submitting}
              onClick={() => handleReview(true)}
              className="flex-1 max-w-[200px] py-4 rounded-xl border border-emerald-900/60 bg-emerald-950/20 hover:bg-emerald-950/40 text-emerald-400 font-bold transition-all text-sm flex items-center justify-center gap-2 shadow-lg"
            >
              <Check size={16} /> Fácil (Avançar)
            </button>
          </div>

          {/* Barra de Progresso inferior */}
          <div className="space-y-2">
            <div className="w-full bg-slate-900 h-2 rounded-full overflow-hidden border border-slate-850">
              <div 
                className="h-full bg-indigo-500 transition-all duration-300"
                style={{ width: `${((currentIndex + 1) / cards.length) * 100}%` }}
              />
            </div>
            <p className="text-[10px] text-center text-slate-500 font-extrabold tracking-wider uppercase">
              Sessão de Estudos • {reviewedCount} cards revisados nesta visita
            </p>
          </div>
        </div>
      )}
    </div>
  );
};
