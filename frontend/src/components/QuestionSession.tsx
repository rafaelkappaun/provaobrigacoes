import React, { useState, useEffect, useRef, useCallback } from 'react';
import { ArrowRight, CheckCircle2, XCircle, Clock, Filter, User, Award, BookOpen, AlertCircle } from 'lucide-react';
import { apiFetch, saveLocalAnswer, getCurrentProfile } from '../api';

const CONTRATOS_SUBJECTS = [
  "Todos os Temas (Automático)",
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
  "Exceção do Contrato Não Cumprido e Onerosidade Excessiva"
];

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

interface AnswerResponse {
  is_correct: boolean;
  is_insecure: boolean;
  feedback: ProfessorFeedback;
  topic_status: string;
  topic_success_rate: number;
}

interface QuestionSessionProps {
  apiBase: string;
  subject?: string;
  onSessionFinished?: () => void;
}

export const QuestionSession: React.FC<QuestionSessionProps> = ({ apiBase, subject, onSessionFinished }) => {
  const [currentSubject, setCurrentSubject] = useState<string>(subject || '');
  const [question, setQuestion] = useState<Question | null>(null);
  const [selectedOption, setSelectedOption] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);
  const [checking, setChecking] = useState<boolean>(false);
  const [response, setResponse] = useState<AnswerResponse | null>(null);
  const [errorMessage, setErrorMessage] = useState<string>('');
  
  // Trava anti-duplo envio
  const submittingRef = useRef<boolean>(false);
  const mountedRef = useRef<boolean>(true);
  
  // Cronômetro da questão
  const [seconds, setSeconds] = useState<number>(0);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const startTimeRef = useRef<number>(0);

  const stopTimer = useCallback(() => {
    if (timerRef.current) {
      clearInterval(timerRef.current);
      timerRef.current = null;
    }
  }, []);

  const startTimer = useCallback(() => {
    stopTimer();
    setSeconds(0);
    startTimeRef.current = Date.now();
    timerRef.current = setInterval(() => {
      setSeconds(Math.floor((Date.now() - startTimeRef.current) / 1000));
    }, 1000);
  }, [stopTimer]);

  useEffect(() => {
    mountedRef.current = true;
    return () => {
      mountedRef.current = false;
      stopTimer();
    };
  }, [stopTimer]);

  // Se o prop subject mudar externamente, atualiza o assunto
  useEffect(() => {
    if (subject !== undefined) {
      setCurrentSubject(subject);
    }
  }, [subject]);

  const fetchNextQuestion = useCallback(async (forcedSubject?: string) => {
    stopTimer();
    setLoading(true);
    setErrorMessage('');
    setSelectedOption('');
    setResponse(null);

    const targetSub = forcedSubject !== undefined ? forcedSubject : currentSubject;
    let url = `/question/next`;
    const params = new URLSearchParams();
    if (targetSub && targetSub !== "Todos os Temas (Automático)") {
      params.append('subject', targetSub);
    }
    const queryString = params.toString();
    if (queryString) {
      url += `?${queryString}`;
    }

    try {
      const res = await apiFetch(apiBase, url);
      if (!mountedRef.current) return;
      if (res.ok) {
        const data = await res.json();
        setQuestion(data);
        startTimer();
      } else {
        setErrorMessage(`Não foi possível carregar a questão (${res.status}). Tente novamente.`);
      }
    } catch (e) {
      if (!mountedRef.current) return;
      console.error(e);
      setErrorMessage("Erro de conexão ao carregar questão. Verifique se o servidor está ativo.");
    } finally {
      if (mountedRef.current) {
        setLoading(false);
      }
    }
  }, [apiBase, currentSubject, startTimer, stopTimer]);

  // Carrega primeira questão ao montar ou quando o assunto muda
  useEffect(() => {
    fetchNextQuestion();
  }, [fetchNextQuestion]);

  const handleSelectOption = (key: string) => {
    if (response || checking) return; // Não altera após responder
    setSelectedOption(key);
  };

  const handleSubmitAnswer = async () => {
    if (!selectedOption || !question || checking || response) return;
    if (submittingRef.current) return;
    submittingRef.current = true;

    stopTimer();
    const responseTime = Math.max(1, (Date.now() - startTimeRef.current) / 1000);
    setChecking(true);
    setErrorMessage('');

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

      if (!mountedRef.current) return;

      if (res.ok) {
        const data: AnswerResponse = await res.json();
        setResponse(data);

        // Salva histórico no armazenamento local
        saveLocalAnswer({
          questionId: question.id,
          subject: question.subject,
          bank: question.bank,
          difficulty: question.difficulty,
          selectedOption: selectedOption,
          gabarito: question.gabarito,
          isCorrect: data.is_correct,
          responseTime: responseTime,
          enunciado: question.enunciado?.slice(0, 150)
        });
      } else if (res.status === 409) {
        setErrorMessage('Esta questão já foi respondida anteriormente. Carregando próxima...');
        setTimeout(() => fetchNextQuestion(), 1200);
      } else {
        const errData = await res.json().catch(() => ({ detail: `Erro HTTP ${res.status}` }));
        setErrorMessage(errData.detail || `Erro ${res.status} ao verificar resposta.`);
      }
    } catch (e) {
      if (!mountedRef.current) return;
      console.error("Erro ao verificar resposta:", e);
      setErrorMessage("Erro de conexão ao verificar resposta.");
    } finally {
      if (mountedRef.current) {
        setChecking(false);
        submittingRef.current = false;
      }
    }
  };

  const formatTimer = (totalSecs: number) => {
    const mins = Math.floor(totalSecs / 60);
    const secs = totalSecs % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  return (
    <div className="max-w-3xl mx-auto space-y-6 pb-20 animate-fade-in">
      {/* BARRA SUPERIOR: Voltar, Usuário, Filtro de Tema e Cronômetro */}
      <div className="p-3.5 rounded-2xl bg-slate-900 border border-slate-800 flex flex-wrap items-center justify-between gap-3 shadow-md">
        <div className="flex items-center gap-2">
          {onSessionFinished && (
            <button 
              onClick={onSessionFinished} 
              className="px-3 py-1.5 bg-slate-950 hover:bg-slate-800 border border-slate-800 rounded-lg text-xs font-bold text-slate-300 transition-all flex items-center gap-1"
            >
              ← Painel
            </button>
          )}
          <div className="flex items-center gap-1.5 px-2.5 py-1 bg-slate-950 rounded-lg border border-slate-800 text-[11px] font-bold text-slate-400">
            <User size={13} className="text-indigo-400" />
            <span className="text-white truncate max-w-[120px]">{getCurrentProfile().name}</span>
          </div>
        </div>

        <div className="flex items-center gap-3 flex-1 justify-end">
          {/* Seletor de Conteúdo */}
          <div className="flex items-center gap-1.5 max-w-xs w-full sm:w-auto">
            <Filter size={13} className="text-indigo-400 shrink-0" />
            <select
              value={currentSubject || "Todos os Temas (Automático)"}
              onChange={(e) => {
                const val = e.target.value === "Todos os Temas (Automático)" ? "" : e.target.value;
                setCurrentSubject(val);
                fetchNextQuestion(val);
              }}
              className="bg-slate-950 border border-slate-800 rounded-lg px-2.5 py-1.5 text-xs font-bold text-slate-200 focus:outline-none focus:border-indigo-500 w-full truncate"
            >
              {CONTRATOS_SUBJECTS.map((s) => (
                <option key={s} value={s} className="bg-slate-900 text-slate-200">
                  {s}
                </option>
              ))}
            </select>
          </div>

          {/* Cronômetro */}
          <div className="flex items-center gap-1.5 px-2.5 py-1 bg-slate-950 border border-slate-800 rounded-lg text-xs font-mono font-bold text-slate-300 shrink-0">
            <Clock size={13} className="text-indigo-400" />
            <span>{formatTimer(seconds)}</span>
          </div>
        </div>
      </div>

      {/* MENSAGEM DE ERRO (SE HOUVER) */}
      {errorMessage && (
        <div className="p-3.5 rounded-xl bg-rose-950/40 border border-rose-800 text-rose-300 text-xs font-semibold flex items-center justify-between gap-2">
          <div className="flex items-center gap-2">
            <AlertCircle size={16} className="text-rose-400 shrink-0" />
            <span>{errorMessage}</span>
          </div>
          <button
            onClick={() => fetchNextQuestion()}
            className="px-2.5 py-1 bg-rose-900 hover:bg-rose-800 text-white rounded text-xs font-bold shrink-0"
          >
            Tentar Novamente
          </button>
        </div>
      )}

      {/* ESTADO DE CARREGAMENTO */}
      {loading ? (
        <div className="p-16 rounded-2xl bg-slate-900 border border-slate-800 text-center space-y-4">
          <div className="w-10 h-10 border-4 border-indigo-500 border-t-transparent rounded-full animate-spin mx-auto" />
          <p className="text-xs font-bold text-slate-400 uppercase tracking-widest">Carregando questão...</p>
        </div>
      ) : question ? (
        <div className="space-y-6">
          {/* CARD DA QUESTÃO */}
          <div className="p-6 md:p-8 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-6">
            {/* Cabeçalho da Questão */}
            <div className="flex flex-wrap items-center justify-between gap-2 pb-4 border-b border-slate-800">
              <div className="flex items-center gap-2">
                <span className="px-2.5 py-1 rounded bg-indigo-950 text-indigo-400 border border-indigo-800 text-xs font-black uppercase">
                  {question.bank || 'OAB'}
                </span>
                <span className="text-xs font-extrabold text-slate-300">
                  {question.subject}
                </span>
              </div>
              <span className="text-[11px] font-semibold text-slate-500">
                {question.difficulty || 'Nível Médio'}
              </span>
            </div>

            {/* Enunciado do Caso Concreto */}
            <div className="text-sm md:text-base text-slate-100 font-medium leading-relaxed whitespace-pre-line">
              {question.enunciado}
            </div>

            {/* Alternativas (A, B, C, D) */}
            <div className="space-y-3 pt-2">
              {Object.entries(question.options || {}).map(([key, text]) => {
                const isSelected = selectedOption === key;
                const isUserWrong = response && !response.is_correct && isSelected;
                const isOfficialRight = response && key === question.gabarito;

                let optionStyles = 'bg-slate-950/80 border-slate-800 hover:border-slate-700 text-slate-200';
                
                if (response) {
                  if (isOfficialRight) {
                    optionStyles = 'bg-emerald-950/40 border-emerald-500 text-emerald-200 font-semibold shadow-[0_0_12px_rgba(16,185,129,0.15)]';
                  } else if (isUserWrong) {
                    optionStyles = 'bg-rose-950/40 border-rose-500 text-rose-200 line-through opacity-90';
                  } else {
                    optionStyles = 'bg-slate-950/40 border-slate-850 text-slate-500 opacity-60';
                  }
                } else if (isSelected) {
                  optionStyles = 'bg-indigo-950/60 border-indigo-500 text-white font-semibold ring-1 ring-indigo-500 shadow-md shadow-indigo-600/10';
                }

                return (
                  <button
                    key={key}
                    disabled={!!response || checking}
                    onClick={() => handleSelectOption(key)}
                    className={`w-full text-left p-4 rounded-xl border transition-all flex items-start gap-3.5 ${optionStyles}`}
                  >
                    <span className={`w-7 h-7 rounded-lg flex items-center justify-center text-xs font-black shrink-0 ${
                      response && isOfficialRight
                        ? 'bg-emerald-500 text-slate-950 font-black'
                        : response && isUserWrong
                        ? 'bg-rose-500 text-white font-black'
                        : isSelected
                        ? 'bg-indigo-600 text-white font-black'
                        : 'bg-slate-900 border border-slate-800 text-slate-400'
                    }`}>
                      {key}
                    </span>
                    <span className="text-xs md:text-sm leading-snug pt-0.5 flex-1">{text}</span>
                  </button>
                );
              })}
            </div>

            {/* BOTÃO CONFIRMAR RESPOSTA (ANTES DE RESPONDER) */}
            {!response && (
              <div className="pt-4 flex justify-end">
                <button
                  disabled={!selectedOption || checking}
                  onClick={handleSubmitAnswer}
                  className={`px-8 py-3.5 rounded-xl text-sm font-extrabold shadow-lg transition-all flex items-center gap-2 ${
                    selectedOption && !checking
                      ? 'bg-indigo-600 hover:bg-indigo-500 text-white shadow-indigo-600/30'
                      : 'bg-slate-800 text-slate-500 cursor-not-allowed border border-slate-700/50'
                  }`}
                >
                  {checking ? (
                    <>
                      <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin" />
                      Verificando...
                    </>
                  ) : (
                    <>
                      Confirmar Resposta <ArrowRight size={16} />
                    </>
                  )}
                </button>
              </div>
            )}
          </div>

          {/* FEEDBACK IMEDIATO DA RESPOSTA (APÓS RESPONDER) */}
          {response && (
            <div className="space-y-4 animate-slide-up">
              {/* BANNER DE RESULTADO */}
              <div className={`p-5 rounded-2xl border flex items-center justify-between gap-4 ${
                response.is_correct 
                  ? 'bg-emerald-950/30 border-emerald-500/30 text-emerald-200' 
                  : 'bg-rose-950/30 border-rose-500/30 text-rose-200'
              }`}>
                <div className="flex items-center gap-3">
                  <div className={`p-2.5 rounded-xl ${
                    response.is_correct ? 'bg-emerald-500/20 text-emerald-400' : 'bg-rose-500/20 text-rose-400'
                  }`}>
                    {response.is_correct ? <CheckCircle2 size={24} /> : <XCircle size={24} />}
                  </div>
                  <div>
                    <h3 className="text-base font-extrabold text-white">
                      {response.is_correct ? 'Parabéns! Resposta Correta!' : 'Resposta Incorreta'}
                    </h3>
                    <p className="text-xs opacity-90">
                      {response.is_correct 
                        ? `Você acertou marcando a alternativa ${selectedOption}.` 
                        : `Você marcou ${selectedOption}, mas a resposta certa é a alternativa ${question.gabarito}.`}
                    </p>
                  </div>
                </div>

                <button
                  onClick={() => fetchNextQuestion()}
                  className="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-extrabold rounded-xl transition-all shadow-lg shadow-indigo-600/20 flex items-center gap-2 shrink-0"
                >
                  Próxima Questão <ArrowRight size={14} />
                </button>
              </div>

              {/* CARD DE FUNDAMENTAÇÃO LEGAL E EXPLICAÇÃO */}
              <div className="p-6 rounded-2xl bg-slate-900 border border-slate-800 space-y-4 shadow-lg">
                {/* Artigo da Lei */}
                <div className="flex items-center gap-2 text-xs font-bold text-indigo-400 uppercase tracking-wider">
                  <BookOpen size={16} />
                  <span>Fundamentação Legal: {question.article || 'Código Civil'}</span>
                </div>

                {/* Texto da Lei */}
                {question.legal_basis && (
                  <blockquote className="p-3.5 bg-slate-950/80 border-l-4 border-indigo-500 rounded-r-xl text-xs md:text-sm text-slate-300 italic leading-relaxed">
                    "{question.legal_basis}"
                  </blockquote>
                )}

                {/* Raciocínio Didático / Análise */}
                {question.explanation && (
                  <div className="space-y-1.5 pt-1">
                    <p className="text-xs font-bold text-slate-400 uppercase tracking-wider">
                      Explicação & Análise da Questão:
                    </p>
                    <p className="text-xs md:text-sm text-slate-200 leading-relaxed whitespace-pre-line">
                      {question.explanation}
                    </p>
                  </div>
                )}

                {/* Aproveitamento no Conteúdo e Meta 90% */}
                <div className="pt-3 border-t border-slate-800 flex flex-wrap items-center justify-between gap-3 text-xs">
                  <div className="flex items-center gap-2 text-slate-400">
                    <Award size={15} className="text-amber-400" />
                    <span>Aproveitamento em <strong className="text-white">{question.subject}</strong>:</span>
                    <span className={`font-bold ${response.topic_success_rate >= 90 ? 'text-emerald-400' : 'text-amber-400'}`}>
                      {response.topic_success_rate}%
                    </span>
                    <span className="text-[11px] text-slate-500">(Meta: 90%)</span>
                  </div>

                  <button
                    onClick={() => fetchNextQuestion()}
                    className="text-indigo-400 hover:text-indigo-300 font-bold flex items-center gap-1 transition-all"
                  >
                    Próxima Questão →
                  </button>
                </div>
              </div>
            </div>
          )}
        </div>
      ) : null}
    </div>
  );
};
