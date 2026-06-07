import React, { useState, useEffect, useCallback } from 'react';
import { ShieldAlert, Award, Play, ChevronDown, ChevronUp, Loader2 } from 'lucide-react';
import { apiFetch } from '../api';

interface ErrorLog {
  log_id: string;
  subject: string;
  answered_at: string;
  question: {
    enunciado: string;
    options: { [key: string]: string };
    gabarito: string;
    article?: string;
    legal_basis?: string;
    explanation?: string;
    bank: string;
  };
}

interface ErrorReportProps {
  apiBase: string;
  onNavigate: (tab: string, extra?: Record<string, unknown>) => void;
}

export const ErrorReport: React.FC<ErrorReportProps> = ({ apiBase, onNavigate }) => {
  const [errors, setErrors] = useState<ErrorLog[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [expandedId, setExpandedId] = useState<string | null>(null);

  const fetchErrors = useCallback(async () => {
    setLoading(true);
    try {
      const res = await apiFetch(apiBase, '/errors');
      if (res.ok) {
        const data = await res.json();
        setErrors(data);
      }
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  }, [apiBase]);

  useEffect(() => {
    Promise.resolve().then(() => {
      fetchErrors();
    });
  }, [fetchErrors]);

  const toggleExpand = (id: string) => {
    setExpandedId(prev => (prev === id ? null : id));
  };

  return (
    <div className="max-w-3xl mx-auto space-y-6 pb-12">
      {/* Cabeçalho */}
      <div className="text-left space-y-2">
        <h2 className="text-2xl font-black text-white tracking-tight flex items-center gap-2">
          <ShieldAlert className="text-red-400" size={24} /> Relatório de Erros Recorrentes
        </h2>
        <p className="text-xs font-bold text-slate-500 uppercase tracking-widest leading-none">
          Pratique e supere seus gargalos de aprendizado
        </p>
      </div>

      {loading ? (
        <div className="h-40 flex items-center justify-center">
          <Loader2 className="animate-spin text-indigo-500" size={28} />
        </div>
      ) : errors.length === 0 ? (
        <div className="p-12 rounded-2xl bg-slate-900 border border-slate-800 text-center space-y-4">
          <Award className="text-emerald-500 mx-auto" size={48} />
          <h4 className="text-lg font-black text-slate-350">Nenhum erro cadastrado!</h4>
          <p className="text-sm text-slate-500 max-w-sm mx-auto">
            Excelente trabalho! Você não possui erros pendentes de revisão ou ainda não respondeu a questões.
          </p>
          <button
            onClick={() => onNavigate('estudo')}
            className="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-sm rounded-xl transition-all shadow-md shadow-indigo-600/10"
          >
            Iniciar Estudos Adaptativos
          </button>
        </div>
      ) : (
        <div className="space-y-4">
          {/* Box de Ação Superior */}
          <div className="p-4 rounded-xl bg-red-950/20 border border-red-900/40 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
            <div>
              <h4 className="text-sm font-extrabold text-red-400 uppercase tracking-wider">Modo de Recuperação Ativo</h4>
              <p className="text-xs font-semibold text-slate-400 mt-1">
                Você possui {errors.length} questões na sua fila de erros. Resolva treinos focados para limpar o painel.
              </p>
            </div>
            <button
              onClick={() => onNavigate('estudo', { trainErrors: true })}
              className="w-full md:w-auto px-5 py-3 bg-red-600 hover:bg-red-500 text-white font-bold text-sm rounded-xl transition-all shadow-md hover:shadow-red-650/10 flex items-center justify-center gap-1.5 self-end md:self-auto"
            >
              <Play size={14} fill="currentColor" /> Treinar Apenas Meus Erros
            </button>
          </div>

          {/* Listagem de Questões Erradas */}
          <div className="space-y-3">
            {errors.map(err => {
              const isExpanded = expandedId === err.log_id;
              const answeredDate = new Date(err.answered_at).toLocaleDateString('pt-BR', {
                day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit'
              });

              return (
                <div 
                  key={err.log_id}
                  className={`rounded-xl border transition-all ${
                    isExpanded 
                      ? 'bg-slate-900 border-red-500/40 shadow-lg' 
                      : 'bg-slate-950/40 border-slate-850 hover:bg-slate-900 hover:border-slate-800'
                  }`}
                >
                  <button
                    onClick={() => toggleExpand(err.log_id)}
                    className="w-full p-4 flex justify-between items-center gap-4 text-left select-none"
                  >
                    <div className="flex flex-col gap-1.5 flex-1">
                      <div className="flex items-center gap-2">
                        <span className="px-2 py-0.5 text-[10px] font-black bg-red-950 text-red-400 border border-red-900/60 rounded uppercase">
                          {err.question.bank}
                        </span>
                        <span className="text-xs font-extrabold text-indigo-400 uppercase tracking-wider">{err.subject}</span>
                      </div>
                      <span className="text-xs font-semibold text-slate-500">Respondido em: {answeredDate}</span>
                    </div>
                    <div className="text-slate-400">
                      {isExpanded ? <ChevronDown size={18} /> : <ChevronUp size={18} />}
                    </div>
                  </button>

                  {isExpanded && (
                    <div className="px-4 pb-5 border-t border-slate-850 pt-4 space-y-4 text-left text-sm leading-relaxed animate-fade-in">
                      {/* Caso Concreto */}
                      <div className="space-y-1">
                        <h5 className="text-[10px] font-black tracking-widest text-slate-500 uppercase">Enunciado da Questão</h5>
                        <p className="p-4 bg-slate-950 rounded-lg text-slate-300 font-medium font-serif border border-slate-850">
                          {err.question.enunciado}
                        </p>
                      </div>

                      {/* Gabarito e Raciocínio */}
                      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div className="p-4 bg-slate-950 rounded-lg border border-slate-850 space-y-2">
                          <h5 className="text-[10px] font-black tracking-widest text-emerald-400 uppercase">Gabarito Correto</h5>
                          <div className="flex items-start gap-2 text-xs font-semibold">
                            <span className="w-5 h-5 rounded bg-emerald-600 text-white font-bold flex items-center justify-center shrink-0">
                              {err.question.gabarito}
                            </span>
                            <span className="text-emerald-300 leading-snug">{err.question.options[err.question.gabarito]}</span>
                          </div>
                          {err.question.article && (
                            <p className="text-[11px] text-indigo-400 font-bold block pt-1">
                              Artigo Base: {err.question.article}
                            </p>
                          )}
                        </div>

                        <div className="p-4 bg-slate-950 rounded-lg border border-slate-850 space-y-1">
                          <h5 className="text-[10px] font-black tracking-widest text-indigo-400 uppercase">Justificativa Legal</h5>
                          <p className="text-xs font-semibold text-slate-350 leading-relaxed whitespace-pre-wrap">
                            {err.question.explanation}
                          </p>
                        </div>
                      </div>

                      {/* Botão de Estudo Específico */}
                      <div className="flex justify-end pt-2">
                        <button
                          onClick={() => onNavigate('estudo', { preselectedSubject: err.subject })}
                          className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs rounded-lg transition-all flex items-center gap-1.5"
                        >
                          Treinar Apenas Este Tema
                        </button>
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
};
