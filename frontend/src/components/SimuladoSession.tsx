import React, { useState, useEffect, useRef, useMemo } from 'react';
import { Shield, Play, Clock, ArrowLeft, ArrowRight, CheckCircle2, XCircle, Award, Loader2, AlertTriangle } from 'lucide-react';
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

interface SimuladoSessionProps {
  apiBase: string;
  vesperaMode?: boolean;
}

export const SimuladoSession: React.FC<SimuladoSessionProps> = ({ apiBase, vesperaMode = false }) => {
  const [size, setSize] = useState<number>(vesperaMode ? 50 : 10);
  const [questions, setQuestions] = useState<Question[]>([]);
  const [answers, setAnswers] = useState<{ [index: number]: string }>({});
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [isPlaying, setIsPlaying] = useState<boolean>(false);
  const [isFinished, setIsFinished] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);
  const [submittedIndex, setSubmittedIndex] = useState<number | null>(null);

  // Tempo do Simulado
  const [seconds, setSeconds] = useState<number>(0);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const questionStartTimes = useRef<{ [index: number]: number }>({});

  // Estatísticas em tempo real
  const liveStats = useMemo(() => {
    let correct = 0;
    let incorrect = 0;
    Object.keys(answers).forEach((key) => {
      const idx = parseInt(key);
      const q = questions[idx];
      if (!q) return;
      if (answers[idx] === q.gabarito) correct++;
      else if (answers[idx]) incorrect++;
    });
    const totalAnswered = correct + incorrect;
    const remaining = questions.length - totalAnswered;
    return { correct, incorrect, totalAnswered, remaining };
  }, [answers, questions]);

  const startTimer = () => {
    setSeconds(0);
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

  useEffect(() => {
    return () => stopTimer();
  }, []);

  const startSimulado = async () => {
    setLoading(true);
    setIsFinished(false);
    setAnswers({});
    setCurrentIndex(0);
    setSubmittedIndex(null);
    questionStartTimes.current = {};
    
    try {
      const endpoint = vesperaMode ? 'vespera/start' : `simulado/start?size=${size}`;
      const res = await apiFetch(apiBase, `/${endpoint}`);
      if (res.ok) {
        const data = await res.json();
        setQuestions(data);
        setIsPlaying(true);
        startTimer();
        // Marca o tempo inicial da primeira questão
        questionStartTimes.current[0] = Date.now();
      }
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  const submitAnswer = () => {
    if (submittedIndex === currentIndex) return;
    setSubmittedIndex(currentIndex);
  };

  const nextQuestion = () => {
    if (currentIndex < questions.length - 1) {
      const nextIdx = currentIndex + 1;
      if (!questionStartTimes.current[nextIdx]) {
        questionStartTimes.current[nextIdx] = Date.now();
      }
      setCurrentIndex(nextIdx);
      setSubmittedIndex(null);
    }
  };

  const prevQuestion = () => {
    if (currentIndex > 0) {
      const prevIdx = currentIndex - 1;
      if (!questionStartTimes.current[prevIdx]) {
        questionStartTimes.current[prevIdx] = Date.now();
      }
      setCurrentIndex(prevIdx);
      setSubmittedIndex(null);
    }
  };

  const [submitting, setSubmitting] = useState<boolean>(false);
  const [submitProgress, setSubmitProgress] = useState<number>(0);

  const finishSimulado = async () => {
    stopTimer();
    setSubmitting(true);
    setSubmitProgress(0);
    
    const now = Date.now();
    const batchSize = 5;
    const results = [];
    
    for (let start = 0; start < questions.length; start += batchSize) {
      const batch = questions.slice(start, start + batchSize);
      const batchResults = await Promise.allSettled(
        batch.map(async (q, bi) => {
          const i = start + bi;
          const ans = answers[i] || '';
          const startTime = questionStartTimes.current[i] || now - 30000;
          const elapsed = (now - startTime) / 1000;
          
          const res = await apiFetch(apiBase, '/question/answer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              question: q,
              selected_option: ans,
              response_time: Math.max(1, elapsed)
            })
          });
          setSubmitProgress(prev => prev + 1);
          if (!res.ok) {
            const err = await res.json().catch(() => ({ detail: 'Erro de rede' }));
            console.error(`Erro na questão ${i + 1}:`, err.detail);
          }
          return res;
        })
      );
      results.push(...batchResults);
    }
    
    const failed = results.filter(r => r.status === 'rejected').length;
    if (failed > 0) {
      console.error(`${failed} questão(ões) não foram registradas devido a erro de rede.`);
    }
    
    setSubmitting(false);
    setIsFinished(true);
  };

  const selectOption = (opt: string) => {
    if (submittedIndex === currentIndex) return;
    setAnswers(prev => ({
      ...prev,
      [currentIndex]: opt
    }));
  };

  const formatTime = (totalSecs: number) => {
    const hrs = Math.floor(totalSecs / 3600);
    const mins = Math.floor((totalSecs % 3600) / 60);
    const secs = totalSecs % 60;
    return `${hrs.toString().padStart(2, '0')}:${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  // Cálculos pós-simulado
  const getResults = () => {
    let correct = 0;
    const detailsBySubject: { [subject: string]: { total: number; correct: number } } = {};
    
    questions.forEach((q, idx) => {
      const selected = answers[idx];
      const isCorrect = selected === q.gabarito;
      if (isCorrect) correct++;
      
      if (!detailsBySubject[q.subject]) {
        detailsBySubject[q.subject] = { total: 0, correct: 0 };
      }
      detailsBySubject[q.subject].total++;
      if (isCorrect) detailsBySubject[q.subject].correct++;
    });
    
    return {
      correct,
      total: questions.length,
      percentage: Math.round((correct / questions.length) * 100),
      subjectBreakdown: Object.entries(detailsBySubject)
    };
  };

  const results = isFinished ? getResults() : null;

  return (
    <div className="max-w-3xl mx-auto space-y-6 pb-12">
      {/* 1. TELA DE CONFIGURAÇÃO ANTES DE INICIAR */}
      {!isPlaying && !isFinished && (
        <div className="p-8 rounded-2xl bg-slate-900 border border-slate-800 text-center space-y-6 max-w-xl mx-auto shadow-2xl">
          <div className="p-4 bg-indigo-500/10 text-indigo-400 rounded-full w-fit mx-auto border border-indigo-500/20">
            <Shield size={36} />
          </div>
          
          <div className="space-y-2">
            <h3 className="text-xl font-black text-white tracking-tight">
              {vesperaMode ? '🔥 Simulado Véspera de Prova' : '🛡️ Iniciar Novo Simulado'}
            </h3>
            <p className="text-xs text-slate-400 leading-relaxed max-w-sm mx-auto">
              {vesperaMode 
                ? '50 questões mescladas cobrindo os artigos mais importantes e focadas nos seus piores tópicos de adimplemento e inadimplemento.'
                : 'As questões do simulado serão geradas dinamicamente priorizando seus pontos críticos identificados no histórico.'}
            </p>
          </div>

          {!vesperaMode && (
            <div className="space-y-2 max-w-xs mx-auto text-left">
              <label className="block text-xs font-bold text-slate-500 uppercase tracking-widest text-center">Tamanho do Exame</label>
              <div className="grid grid-cols-5 gap-1.5">
                {[10, 20, 30, 50, 100].map(s => (
                  <button
                    key={s}
                    onClick={() => setSize(s)}
                    className={`py-2 text-xs font-bold rounded-lg transition-all ${
                      size === s 
                        ? 'bg-indigo-600 text-white font-bold' 
                        : 'bg-slate-950 text-slate-400 border border-slate-850 hover:bg-slate-800'
                    }`}
                  >
                    {s}q
                  </button>
                ))}
              </div>
            </div>
          )}

          <div className="pt-2">
            <button
              onClick={startSimulado}
              disabled={loading}
              className="w-full max-w-xs py-3.5 bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm rounded-xl transition-all shadow-lg hover:shadow-indigo-650/15 flex items-center justify-center gap-2"
            >
              {loading ? (
                <>
                  <Loader2 className="animate-spin" size={16} />
                  Criando Prova...
                </>
              ) : (
                <>
                  <Play size={14} fill="currentColor" /> Começar Simulado
                </>
              )}
            </button>
          </div>
        </div>
      )}

      {/* 2. TELA DE EXECUÇÃO DO SIMULADO */}
      {isPlaying && !isFinished && questions.length > 0 && (
        <div className="space-y-4">
          {/* Painel de Estatísticas em Tempo Real */}
          <div className="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl">
            <div className="flex items-center justify-between gap-4 flex-wrap">
              <div className="flex items-center gap-4">
                <span className="text-xs font-bold text-indigo-400 uppercase tracking-wider">
                  {vesperaMode ? '🔥 Véspera' : '🛡️ Simulado'}
                </span>
                <span className="text-sm font-black text-slate-200">
                  {currentIndex + 1}/{questions.length}
                </span>
              </div>
              <div className="flex items-center gap-3 text-xs font-bold">
                <span className="flex items-center gap-1.5 text-emerald-400">
                  <CheckCircle2 size={14} /> {liveStats.correct}
                </span>
                <span className="flex items-center gap-1.5 text-red-400">
                  <XCircle size={14} /> {liveStats.incorrect}
                </span>
                <span className="flex items-center gap-1.5 text-slate-500">
                  <AlertTriangle size={14} /> {liveStats.remaining}
                </span>
                <span className="flex items-center gap-1.5 px-3 py-1 bg-slate-950 border border-slate-850 rounded-lg text-slate-400 font-mono">
                  <Clock size={14} /> {formatTime(seconds)}
                </span>
              </div>
            </div>
            {/* Barra de progresso geral */}
            <div className="mt-3 h-1.5 bg-slate-950 rounded-full overflow-hidden flex">
              <div className="bg-emerald-500 h-full transition-all" style={{ width: `${(liveStats.correct / Math.max(questions.length, 1)) * 100}%` }} />
              <div className="bg-red-500 h-full transition-all" style={{ width: `${(liveStats.incorrect / Math.max(questions.length, 1)) * 100}%` }} />
            </div>
            <div className="flex justify-between mt-1 text-[10px] text-slate-600 font-semibold">
              <span>{Math.round((liveStats.correct / Math.max(questions.length, 1)) * 100)}% acertos</span>
              <span>{liveStats.totalAnswered}/{questions.length} respondidas</span>
            </div>
          </div>

          {/* Card da Questão Atual */}
          <div className="p-6 md:p-8 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-6">
            {/* Enunciado */}
            <div className="space-y-6 text-left">
              <p className="text-xs text-slate-500 font-extrabold tracking-wider uppercase">
                Assunto: {questions[currentIndex].subject} • Estilo: {questions[currentIndex].bank}
              </p>
              <div className="text-slate-100 leading-relaxed font-medium text-base bg-slate-950/40 p-5 rounded-xl border border-slate-850">
                {questions[currentIndex].enunciado}
              </div>

              {/* Alternativas */}
              <div className="space-y-3">
                {Object.entries(questions[currentIndex].options).map(([letter, text]) => {
                  const isSelected = answers[currentIndex] === letter;
                  const isSubmitted = submittedIndex === currentIndex;
                  const gabarito = questions[currentIndex].gabarito;
                  const isWrong = isSubmitted && isSelected && letter !== gabarito;
                  const isGabarito = isSubmitted && letter === gabarito;

                  let optionStyle = "bg-slate-950 border-slate-850 text-slate-300 hover:bg-slate-800";
                  if (isSubmitted) {
                    if (isGabarito) {
                      optionStyle = "bg-emerald-950/40 border-emerald-500 text-emerald-300 shadow-md";
                    } else if (isWrong) {
                      optionStyle = "bg-red-950/40 border-red-500 text-red-300 shadow-md";
                    } else {
                      optionStyle = "opacity-50 border-slate-900 bg-slate-950 text-slate-500 pointer-events-none";
                    }
                  } else if (isSelected) {
                    optionStyle = "bg-indigo-950/40 border-indigo-500 text-indigo-300 shadow-md";
                  }

                  return (
                    <button
                      key={letter}
                      disabled={isSubmitted}
                      onClick={() => selectOption(letter)}
                      className={`w-full p-4 rounded-xl border-2 transition-all text-left flex items-start gap-4 text-sm font-semibold ${optionStyle}`}
                    >
                      <span className={`w-6 h-6 rounded-lg flex items-center justify-center text-xs font-black border transition-all shrink-0 ${
                        isSubmitted && isGabarito
                          ? 'bg-emerald-600 text-white border-emerald-500'
                          : isSubmitted && isWrong
                          ? 'bg-red-600 text-white border-red-500'
                          : isSelected
                          ? 'bg-indigo-600 text-white border-indigo-500'
                          : 'bg-slate-900 border-slate-850 text-slate-400'
                      }`}>
                        {letter}
                      </span>
                      <span className="flex-1 leading-snug">{text}</span>
                      {isSubmitted && isGabarito && <CheckCircle2 size={18} className="text-emerald-400 shrink-0" />}
                      {isSubmitted && isWrong && <XCircle size={18} className="text-red-400 shrink-0" />}
                    </button>
                  );
                })}
              </div>

              {/* Feedback pós-submissão */}
              {submittedIndex === currentIndex && (
                <div className={`p-4 rounded-xl border text-sm font-semibold leading-relaxed ${
                  answers[currentIndex] === questions[currentIndex].gabarito
                    ? 'bg-emerald-950/20 border-emerald-500/30 text-emerald-200'
                    : 'bg-red-950/20 border-red-500/30 text-red-200'
                }`}>
                  {answers[currentIndex] === questions[currentIndex].gabarito ? (
                    <span className="flex items-center gap-2"><CheckCircle2 size={18} /> Correto! {questions[currentIndex].article && `(${questions[currentIndex].article})`}</span>
                  ) : (
                    <div>
                      <span className="flex items-center gap-2 mb-1"><XCircle size={18} /> Incorreto! Gabarito: {questions[currentIndex].gabarito}</span>
                      {questions[currentIndex].legal_basis && (
                        <p className="text-xs opacity-80 mt-2">{questions[currentIndex].legal_basis}</p>
                      )}
                    </div>
                  )}
                </div>
              )}
            </div>

            {/* Navegação */}
            <div className="flex justify-between items-center border-t border-slate-800 pt-6">
              <button
                disabled={currentIndex === 0}
                onClick={prevQuestion}
                className="px-4 py-2.5 bg-slate-950 border border-slate-850 hover:bg-slate-800 disabled:opacity-30 rounded-lg text-xs font-bold text-slate-400 flex items-center gap-1 transition-all"
              >
                <ArrowLeft size={14} /> Anterior
              </button>

              <div className="flex gap-2">
                {submittedIndex !== currentIndex && (
                  <button
                    disabled={!answers[currentIndex]}
                    onClick={submitAnswer}
                    className="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-500 disabled:bg-slate-800 disabled:text-slate-500 text-white rounded-lg text-xs font-bold transition-all"
                  >
                    Responder
                  </button>
                )}
                {currentIndex < questions.length - 1 ? (
                  <button
                    onClick={nextQuestion}
                    className="px-4 py-2.5 bg-slate-800 hover:bg-slate-700 text-white rounded-lg text-xs font-bold flex items-center gap-1 transition-all"
                  >
                    Próxima <ArrowRight size={14} />
                  </button>
                ) : submittedIndex === currentIndex && (
                  <button
                    onClick={finishSimulado}
                    disabled={submitting}
                    className="px-6 py-2.5 bg-emerald-600 hover:bg-emerald-500 disabled:bg-slate-700 disabled:text-slate-500 text-white rounded-lg text-xs font-bold transition-all shadow-md flex items-center gap-2"
                  >
                    {submitting ? (
                      <><Loader2 className="animate-spin" size={14} /> {submitProgress}/{questions.length}</>
                    ) : (
                      'Finalizar Prova'
                    )}
                  </button>
                )}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* 3. TELA DE SCORECARD FINAL / RESULTADOS */}
      {isFinished && results && (
        <div className="space-y-6 max-w-xl mx-auto">
          {/* Card de Desempenho Global */}
          <div className="p-8 rounded-2xl bg-slate-900 border border-slate-800 text-center space-y-5 shadow-2xl">
            <div className="p-3 bg-emerald-500/10 text-emerald-400 rounded-full w-fit mx-auto border border-emerald-500/20">
              <Award size={36} />
            </div>

            <div className="space-y-1">
              <h3 className="text-xl font-black text-white tracking-tight">Simulado Finalizado!</h3>
              <p className="text-xs text-slate-500 font-semibold">Tempo de Prova: {formatTime(seconds)}</p>
            </div>

            <div className="flex justify-center items-baseline gap-2">
              <span className={`text-4xl font-extrabold tracking-tight ${results.percentage >= 95 ? 'text-emerald-400' : 'text-white'}`}>
                {results.percentage}%
              </span>
              <span className="text-sm text-slate-500 font-bold">de acertos</span>
            </div>

            <p className="text-xs font-semibold text-slate-400">
              Você acertou <strong className="text-slate-200">{results.correct}</strong> de <strong className="text-slate-200">{results.total}</strong> questões propostas.
            </p>

            <div className="pt-2">
              <button
                onClick={() => {
                  setIsPlaying(false);
                  setIsFinished(false);
                }}
                className="w-full max-w-xs py-3 bg-indigo-650 hover:bg-indigo-600 text-white font-bold text-xs rounded-xl transition-all shadow-md"
              >
                Novo Simulado
              </button>
            </div>
          </div>

          {/* Desempenho Detalhado por Assunto */}
          <div className="p-6 rounded-2xl bg-slate-900 border border-slate-800 space-y-4 shadow-xl text-left">
            <h4 className="text-sm font-extrabold text-white uppercase tracking-wider">Desempenho por Assunto</h4>
            <div className="divide-y divide-slate-850">
              {results.subjectBreakdown.map(([subj, data]) => {
                const subRate = Math.round((data.correct / data.total) * 100);
                return (
                  <div key={subj} className="py-3 first:pt-0 last:pb-0 flex items-center justify-between gap-4">
                    <div>
                      <p className="text-xs font-bold text-slate-200">{subj}</p>
                      <p className="text-[10px] text-slate-500 font-semibold">{data.correct} acertos de {data.total} questões</p>
                    </div>
                    <div className="flex items-center gap-2 shrink-0">
                      <span className={`text-xs font-bold ${subRate >= 80 ? 'text-emerald-400' : subRate >= 60 ? 'text-amber-400' : 'text-red-400'}`}>
                        {subRate}%
                      </span>
                      {subRate >= 80 ? (
                        <CheckCircle2 size={16} className="text-emerald-500" />
                      ) : (
                        <XCircle size={16} className="text-red-500" />
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
