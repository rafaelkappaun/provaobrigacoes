import React, { useState, useEffect, useRef, useCallback } from 'react';
import { ArrowRight, HelpCircle, AlertTriangle, CheckCircle, Flame, Send, Loader2 } from 'lucide-react';
import { apiFetch } from '../api';

interface Question {
  id: string;
  subject: string;
  bank: string;
  difficulty: string;
  enunciado: string;
  options: { [key: string]: string };
  gabarito: string;
  article?: string;
  legal_basis?: string;
  explanation?: string;
}

interface ProfessorFeedback {
  title: string;
  intro: string;
  body: string;
  article: string;
  legal_basis: string;
}

interface FlashcardReinforce {
  front: string;
  back: string;
}

interface Reinforcement {
  type: 'reforco_normal' | 'modo_intensivo';
  summary_30s?: string;
  summary_2min?: string;
  summary_5min?: string;
  summary?: string;
  jurisprudence?: string;
  flashcards: FlashcardReinforce[];
  mind_map?: string;
  intensive_questions?: Question[];
  message?: string;
}

interface AnswerResponse {
  is_correct: boolean;
  is_insecure: boolean;
  feedback: ProfessorFeedback;
  new_intensive_triggered: boolean;
  reinforcement: Reinforcement | null;
  topic_status: string;
  topic_success_rate: number;
}

interface QuestionSessionProps {
  apiBase: string;
  onSessionFinished?: () => void;
}

const BANKS = ["FGV", "OAB", "CESPE", "FCC", "VUNESP", "AOCP", "FMP", "Consulplan"];
const pickRandomBank = () => BANKS[Math.floor(Math.random() * BANKS.length)];

export const QuestionSession: React.FC<QuestionSessionProps> = ({ apiBase, onSessionFinished }) => {
  const [question, setQuestion] = useState<Question | null>(null);
  const [selectedOption, setSelectedOption] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);
  const [checking, setChecking] = useState<boolean>(false);
  
  // Resposta e Feedbacks
  const [response, setResponse] = useState<AnswerResponse | null>(null);
  const [activeReinforceTab, setActiveReinforceTab] = useState<'summary' | 'summary_2min' | 'summary_5min' | 'flashcards' | 'mindmap' | 'questions'>('summary');
  const [flippedCards, setFlippedCards] = useState<{ [key: number]: boolean }>({});
  
  const [errorMessage, setErrorMessage] = useState<string>('');

  // Chat com Professor
  const [professorQuery, setProfessorQuery] = useState<string>('');
  const [professorResponse, setProfessorResponse] = useState<string>('');
  const [professorLoading, setProfessorLoading] = useState<boolean>(false);
  
  // Trava anti-duplo clique
  const submittingRef = useRef<boolean>(false);
  
  // Cronômetro e métricas
  const [seconds, setSeconds] = useState<number>(0);
  const timerRef = useRef<any>(null);
  const startTimeRef = useRef<number>(0);

  const startTimer = () => {
    stopTimer();
    setSeconds(0);
    startTimeRef.current = Date.now();
    timerRef.current = setInterval(() => {
      setSeconds(prev => prev + 1);
    }, 1000);
  };

  const stopTimer = () => {
    if (timerRef.current) {
      clearInterval(timerRef.current);
      timerRef.current = null;
    }
  };

  const fetchNextQuestion = useCallback(async () => {
    setLoading(true);
    setResponse(null);
    setSelectedOption('');
    setProfessorResponse('');
    setProfessorQuery('');
    setFlippedCards({});
    setActiveReinforceTab('summary');
    setErrorMessage('');
    
    const randomBank = pickRandomBank();
    try {
      const res = await apiFetch(apiBase, `/question/next?bank=${randomBank}`);
      if (res.ok) {
        const data = await res.json();
        setQuestion(data);
        startTimer();
      } else {
        const errData = await res.json().catch(() => ({ detail: `Erro HTTP ${res.status}` }));
        setErrorMessage(errData.detail || `Erro ${res.status} ao carregar questão`);
      }
    } catch (e) {
      console.error("Erro ao carregar questão:", e);
      setErrorMessage("Erro de conexão ao carregar questão. Verifique o servidor.");
    } finally {
      setLoading(false);
    }
  }, [apiBase]);

  // Carrega questão ao iniciar
  useEffect(() => {
    fetchNextQuestion();
    return () => stopTimer();
  }, [fetchNextQuestion]);

  const handleSubmit = async () => {
    if (!question || !selectedOption || checking || submittingRef.current) return;
    submittingRef.current = true;
    
    setChecking(true);
    stopTimer();
    const responseTime = (Date.now() - startTimeRef.current) / 1000;
    
    try {
      const res = await apiFetch(apiBase, '/question/answer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          question: question,
          selected_option: selectedOption,
          response_time: responseTime
        })
      });
      
      if (res.ok) {
        const data = await res.json();
        setResponse(data);
        setErrorMessage('');
      } else {
        const errData = await res.json().catch(() => ({ detail: `Erro HTTP ${res.status}` }));
        setErrorMessage(errData.detail || `Erro ${res.status} ao verificar resposta`);
      }
    } catch (e) {
      console.error("Erro ao verificar resposta:", e);
      setErrorMessage("Erro de conexão ao verificar resposta. Verifique o servidor.");
    } finally {
      setChecking(false);
      submittingRef.current = false;
    }
  };

  const handleAskProfessor = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!professorQuery.trim() || !question || professorLoading) return;
    
    setProfessorLoading(true);
    setProfessorResponse('');
    
    try {
      const res = await apiFetch(apiBase, '/ai/professor/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          context: question,
          query: professorQuery
        })
      });
      
      if (res.ok) {
        const data = await res.json();
        setProfessorResponse(data.response);
      } else {
        setProfessorResponse("Desculpe, ocorreu um erro ao contatar o professor virtual.");
      }
    } catch (e) {
      console.error(e);
      setProfessorResponse("Desculpe, ocorreu um erro de conexão com o professor virtual.");
    } finally {
      setProfessorLoading(false);
    }
  };

  const toggleCard = (index: number) => {
    setFlippedCards(prev => ({
      ...prev,
      [index]: !prev[index]
    }));
  };

  return (
    <div className="max-w-3xl mx-auto space-y-6 pb-24">
      {/* Barra superior com botão de voltar */}
      {onSessionFinished && (
        <div className="p-4 rounded-xl bg-slate-900 border border-slate-800">
          <button 
            onClick={onSessionFinished} 
            className="px-3 py-1 bg-slate-950 hover:bg-slate-800 border border-slate-850 rounded-lg text-xs font-bold text-slate-400 hover:text-slate-200 transition-all"
          >
            ← Painel
          </button>
        </div>
      )}

      {/* Box de Estudo Principal */}
      <div className="p-6 md:p-8 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl relative min-h-[300px] flex flex-col justify-between">
        {loading ? (
          <div className="absolute inset-0 flex flex-col items-center justify-center bg-slate-900/60 rounded-2xl z-10 space-y-3">
            <Loader2 className="animate-spin text-indigo-500" size={40} />
            <p className="text-sm font-medium text-slate-400">O Professor está preparando seu caso concreto...</p>
          </div>
        ) : null}

        {question && (
          <div className="space-y-6 w-full">
            {/* Meta do Caso */}
            <div className="flex justify-between items-center text-xs border-b border-slate-800 pb-4">
              <div className="space-y-1">
                <p className="font-extrabold text-indigo-400 tracking-wider uppercase">{question.subject}</p>
                <p className="text-slate-500 font-medium">{question.bank} • Dificuldade {question.difficulty}</p>
              </div>
              <div className="px-3 py-1 rounded-full bg-slate-950 border border-slate-800 font-mono text-slate-300 font-bold">
                ⏱️ {Math.floor(seconds / 60)}:{(seconds % 60).toString().padStart(2, '0')}
              </div>
            </div>

            {/* Enunciado do Caso Concreto */}
            <div className="text-slate-100 leading-relaxed font-medium text-base md:text-lg bg-slate-950/40 p-5 rounded-xl border border-slate-800/40 text-left">
              {question.enunciado}
            </div>

            {/* Alternativas de Resposta */}
            <div className="space-y-3 text-left">
              {Object.entries(question.options).map(([letter, text]) => {
                const isSelected = selectedOption === letter;
                const isCorrect = response?.is_correct;
                const showResults = response !== null;
                const isThisGabarito = question.gabarito === letter;
                
                let optionStyle = "bg-slate-950 hover:bg-slate-800 border-slate-800 text-slate-300 hover:border-slate-700";
                
                if (isSelected) {
                  optionStyle = "bg-indigo-950/40 border-indigo-500 text-indigo-300 shadow-md shadow-indigo-500/5";
                }
                
                if (showResults) {
                  if (isThisGabarito) {
                    optionStyle = "bg-emerald-950/40 border-emerald-500 text-emerald-300 shadow-md shadow-emerald-500/5";
                  } else if (isSelected && !isCorrect) {
                    optionStyle = "bg-red-950/40 border-red-500 text-red-300 shadow-md shadow-red-500/5";
                  } else {
                    optionStyle = "opacity-50 border-slate-900 bg-slate-950 text-slate-500 pointer-events-none";
                  }
                }

                return (
                  <button
                    key={letter}
                    disabled={showResults || checking}
                    onClick={() => setSelectedOption(letter)}
                    className={`w-full p-4 rounded-xl border-2 transition-all duration-200 flex items-start gap-4 font-semibold text-sm ${optionStyle}`}
                  >
                    <span className={`w-6 h-6 rounded-lg flex items-center justify-center text-xs font-black border transition-all ${
                      isSelected 
                        ? 'bg-indigo-600 text-white border-indigo-500' 
                        : showResults && isThisGabarito
                        ? 'bg-emerald-600 text-white border-emerald-500'
                        : showResults && isSelected && !isCorrect
                        ? 'bg-red-600 text-white border-red-500'
                        : 'bg-slate-900 border-slate-800 text-slate-400'
                    }`}>
                      {letter}
                    </span>
                    <span className="flex-1 leading-snug">{text}</span>
                  </button>
                );
              })}
            </div>
          </div>
        )}

        {/* Barra de ação inferior */}
        <div className="border-t border-slate-800 pt-6 mt-6 flex justify-between items-center gap-4">
          <div className="text-xs text-slate-500 font-semibold">
            {question && `Caso Código Civil: ${question.article || 'Vários artigos'}`}
          </div>
          
          {!response ? (
            <button
              disabled={!selectedOption || checking || loading}
              onClick={handleSubmit}
              className={`px-6 py-3 rounded-xl font-bold flex items-center gap-2 transition-all duration-300 shadow-md ${
                selectedOption && !checking
                  ? 'bg-indigo-600 hover:bg-indigo-500 text-white shadow-indigo-600/15'
                  : 'bg-slate-800 text-slate-500 border border-slate-800/80 cursor-not-allowed'
              }`}
            >
              {checking ? (
                <>
                  <Loader2 className="animate-spin" size={18} />
                  Corrigindo...
                </>
              ) : (
                <>
                  Verificar <ArrowRight size={16} />
                </>
              )}
            </button>
          ) : (
            <button
              onClick={fetchNextQuestion}
              className="px-6 py-3 rounded-xl font-bold bg-indigo-600 hover:bg-indigo-500 text-white shadow-md shadow-indigo-600/15 flex items-center gap-2 transition-all duration-300"
            >
              Continuar <ArrowRight size={16} />
            </button>
          )}
        </div>
      </div>

      {/* Mensagem de Erro */}
      {errorMessage && (
        <div className="p-4 rounded-xl bg-red-950/30 border border-red-500/40 text-red-300 text-sm font-semibold flex items-start gap-3">
          <AlertTriangle size={18} className="shrink-0 mt-0.5" />
          <span>{errorMessage}</span>
        </div>
      )}

      {/* Painel de Correção Deslizante / Relatório de Professor */}
      {response && (
        <div className={`p-6 rounded-2xl border transition-all duration-300 animate-slide-up space-y-6 ${
          response.is_correct 
            ? response.is_insecure 
              ? 'bg-amber-950/20 border-amber-500/30 text-amber-200 glow-warning' 
              : 'bg-emerald-950/20 border-emerald-500/30 text-emerald-200 glow-success'
            : 'bg-red-950/20 border-red-500/30 text-red-200 glow-danger'
        }`}>
          {/* Título de Correção */}
          <div className="flex items-center gap-3">
            {response.is_correct ? (
              response.is_insecure ? (
                <AlertTriangle className="text-amber-400" size={24} />
              ) : (
                <CheckCircle className="text-emerald-400" size={24} />
              )
            ) : (
              <AlertTriangle className="text-red-400" size={24} />
            )}
            <h4 className="text-lg font-black tracking-tight">{response.feedback.title}</h4>
          </div>

          <p className="text-sm font-semibold opacity-90 leading-snug">{response.feedback.intro}</p>

          {/* Raciocínio Didático */}
          <div className="p-5 rounded-xl bg-slate-950/60 border border-slate-800 text-slate-300 space-y-4 text-left">
            <h5 className="text-xs font-extrabold tracking-widest text-indigo-400 uppercase">Explicação do Professor Virtual</h5>
            <div className="text-sm leading-relaxed whitespace-pre-wrap">
              {response.feedback.body}
            </div>
          </div>

          {/* Seção de Pergunta Direta ao Professor */}
          <div className="p-5 rounded-xl bg-slate-950/60 border border-slate-800 space-y-4 text-left">
            <h5 className="text-xs font-extrabold tracking-widest text-indigo-400 uppercase flex items-center gap-2">
              <HelpCircle size={14} /> Dúvida Adicional sobre este Caso?
            </h5>
            <form onSubmit={handleAskProfessor} className="flex gap-2">
              <input
                type="text"
                value={professorQuery}
                onChange={(e) => setProfessorQuery(e.target.value)}
                placeholder="Ex: Por que não aplicamos a novação subjetiva aqui?"
                className="flex-1 bg-slate-900 border border-slate-800 rounded-lg px-4 py-2 text-sm text-slate-200 focus:outline-none focus:border-indigo-500 font-semibold"
              />
              <button
                type="submit"
                disabled={!professorQuery.trim() || professorLoading}
                className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 disabled:bg-slate-800 text-white font-bold text-xs rounded-lg transition-all flex items-center gap-1.5"
              >
                {professorLoading ? <Loader2 className="animate-spin" size={14} /> : <Send size={14} />} Enviar
              </button>
            </form>

            {professorResponse && (
              <div className="p-4 rounded-lg bg-slate-900 border border-slate-800/80 text-sm text-slate-300 leading-relaxed whitespace-pre-wrap">
                <strong className="text-indigo-400 block mb-1">Resposta do Professor:</strong>
                {professorResponse}
              </div>
            )}
          </div>

          {/* Bloco de REFORÇO AUTOMÁTICO em caso de erro */}
          {response.reinforcement && (
            <div className="p-6 rounded-xl bg-slate-950/40 border border-indigo-500/20 text-left space-y-5">
              <div className="flex items-center gap-2 border-b border-slate-800 pb-3">
                <Flame className="text-orange-500" size={20} />
                <h5 className="text-sm font-extrabold text-white uppercase tracking-wider">
                  {response.reinforcement.type === 'modo_intensivo' ? '🔥 Pacote de Modo Intensivo' : '📚 Reforço Pedagógico Automático'}
                </h5>
              </div>

              {/* Tabs de Reforço */}
              <div className="flex border-b border-slate-800 flex-wrap">
                <button
                  onClick={() => setActiveReinforceTab('summary')}
                  className={`px-4 py-2 text-xs font-bold -mb-px transition-all ${
                    activeReinforceTab === 'summary' 
                      ? 'border-b-2 border-indigo-500 text-indigo-400' 
                      : 'text-slate-500 hover:text-slate-300'
                  }`}
                >
                  Resumo 30s
                </button>
                {response.reinforcement.summary_2min && (
                  <button
                    onClick={() => setActiveReinforceTab('summary_2min')}
                    className={`px-4 py-2 text-xs font-bold -mb-px transition-all ${
                      activeReinforceTab === 'summary_2min' 
                        ? 'border-b-2 border-indigo-500 text-indigo-400' 
                        : 'text-slate-500 hover:text-slate-300'
                    }`}
                  >
                    Resumo 2min
                  </button>
                )}
                {response.reinforcement.summary_5min && (
                  <button
                    onClick={() => setActiveReinforceTab('summary_5min')}
                    className={`px-4 py-2 text-xs font-bold -mb-px transition-all ${
                      activeReinforceTab === 'summary_5min' 
                        ? 'border-b-2 border-indigo-500 text-indigo-400' 
                        : 'text-slate-500 hover:text-slate-300'
                    }`}
                  >
                    Resumo 5min
                  </button>
                )}
                <button
                  onClick={() => setActiveReinforceTab('flashcards')}
                  className={`px-4 py-2 text-xs font-bold -mb-px transition-all ${
                    activeReinforceTab === 'flashcards' 
                      ? 'border-b-2 border-indigo-500 text-indigo-400' 
                      : 'text-slate-500 hover:text-slate-300'
                  }`}
                >
                  Flashcards ({response.reinforcement.flashcards.length})
                </button>
                {response.reinforcement.mind_map && (
                  <button
                    onClick={() => setActiveReinforceTab('mindmap')}
                    className={`px-4 py-2 text-xs font-bold -mb-px transition-all ${
                      activeReinforceTab === 'mindmap' 
                        ? 'border-b-2 border-indigo-500 text-indigo-400' 
                        : 'text-slate-500 hover:text-slate-300'
                    }`}
                  >
                    Mapa Mental
                  </button>
                )}
                {response.reinforcement.intensive_questions && (
                  <button
                    onClick={() => setActiveReinforceTab('questions')}
                    className={`px-4 py-2 text-xs font-bold -mb-px transition-all ${
                      activeReinforceTab === 'questions' 
                        ? 'border-b-2 border-indigo-500 text-indigo-400' 
                        : 'text-slate-500 hover:text-slate-300'
                    }`}
                  >
                    10 Questões 🎯
                  </button>
                )}
              </div>

              {/* Conteúdo da Tab de Reforço */}
              <div className="py-2">
                {activeReinforceTab === 'summary' && (
                  <div className="space-y-4">
                    <div className="text-sm text-slate-300 whitespace-pre-wrap leading-relaxed">
                      {response.reinforcement.summary_30s || response.reinforcement.summary}
                    </div>
                    {response.reinforcement.jurisprudence && (
                      <div className="p-3 bg-indigo-950/20 border border-indigo-900/60 rounded-lg text-xs italic text-indigo-300">
                        {response.reinforcement.jurisprudence}
                      </div>
                    )}
                  </div>
                )}

                {activeReinforceTab === 'summary_2min' && response.reinforcement.summary_2min && (
                  <div className="text-sm text-slate-300 whitespace-pre-wrap leading-relaxed">
                    {response.reinforcement.summary_2min}
                  </div>
                )}

                {activeReinforceTab === 'summary_5min' && response.reinforcement.summary_5min && (
                  <div className="text-sm text-slate-300 whitespace-pre-wrap leading-relaxed">
                    {response.reinforcement.summary_5min}
                  </div>
                )}

                {activeReinforceTab === 'flashcards' && (
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    {response.reinforcement.flashcards.map((fc, i) => {
                      const isFlipped = flippedCards[i] || false;
                      return (
                        <div 
                          key={i} 
                          onClick={() => toggleCard(i)}
                          className="h-36 perspective-1000 cursor-pointer"
                        >
                          <div className={`relative w-full h-full text-center transition-transform duration-500 transform-style-3d ${
                            isFlipped ? 'rotate-y-180' : ''
                          }`}>
                            <div className="absolute inset-0 w-full h-full bg-slate-900 border border-slate-800 rounded-xl p-4 flex flex-col justify-center items-center text-xs font-bold text-slate-200 backface-hidden shadow-md">
                              <p className="line-clamp-4">{fc.front}</p>
                              <span className="absolute bottom-2 text-[10px] text-slate-500 font-semibold tracking-widest uppercase">Girar Card</span>
                            </div>
                            <div className="absolute inset-0 w-full h-full bg-indigo-950 border border-indigo-900 rounded-xl p-4 flex flex-col justify-center items-center text-xs font-semibold text-indigo-200 rotate-y-180 backface-hidden shadow-md overflow-y-auto">
                              <p className="leading-snug">{fc.back}</p>
                              <span className="absolute bottom-2 text-[10px] text-indigo-400 font-semibold tracking-widest uppercase">Frente</span>
                            </div>
                          </div>
                        </div>
                      );
                    })}
                  </div>
                )}

                {activeReinforceTab === 'mindmap' && response.reinforcement.mind_map && (
                  <pre className="p-4 rounded-xl bg-slate-900 border border-slate-850 font-mono text-xs text-indigo-300 overflow-x-auto whitespace-pre leading-relaxed">
                    {response.reinforcement.mind_map}
                  </pre>
                )}

                {activeReinforceTab === 'questions' && response.reinforcement.intensive_questions && (
                  <div className="space-y-4">
                    <p className="text-xs font-bold text-indigo-400 uppercase tracking-wider">10 Questões Inéditas para Praticar</p>
                    <div className="space-y-3 max-h-96 overflow-y-auto">
                      {response.reinforcement.intensive_questions.map((q, i) => (
                        <div key={i} className="p-4 rounded-xl bg-slate-950 border border-slate-800 text-left">
                          <div className="flex items-center gap-2 mb-2">
                            <span className="px-2 py-0.5 text-[10px] font-black bg-indigo-900/50 text-indigo-400 rounded">{q.bank}</span>
                            <span className="text-[10px] text-slate-500 font-semibold">Q{i + 1}</span>
                          </div>
                          <p className="text-xs font-semibold text-slate-200 leading-relaxed mb-3">{q.enunciado}</p>
                          <div className="space-y-1">
                            {Object.entries(q.options || {}).map(([key, val]) => (
                              <div key={key} className={`flex items-start gap-2 text-xs p-2 rounded ${key === q.gabarito ? 'bg-emerald-950/30 text-emerald-300' : 'text-slate-400'}`}>
                                <span className="w-4 h-4 rounded flex items-center justify-center text-[10px] font-black bg-slate-950 border border-slate-800 shrink-0">{key}</span>
                                <span>{val as string}</span>
                              </div>
                            ))}
                          </div>
                          <p className="text-[10px] text-indigo-400 font-bold mt-2">{q.article}</p>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};
