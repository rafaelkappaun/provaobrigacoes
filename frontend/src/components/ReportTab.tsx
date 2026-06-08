import React, { useState, useEffect } from 'react';
import { Award, FileText, CheckCircle2, TrendingUp, AlertTriangle, Play, RefreshCw, Loader2 } from 'lucide-react';
import { apiFetch } from '../api';

interface CognitiveReport {
  overall_accuracy: number;
  questions_answered: number;
  critical_count: number;
  intermediate_count: number;
  mastered_count: number;
  recommendation: string;
  diagnostic: string;
  weakest_topics: string[];
}

interface ReportTabProps {
  apiBase: string;
  onNavigate: (tab: string, extra?: Record<string, unknown>) => void;
}

export const ReportTab: React.FC<ReportTabProps> = ({ apiBase, onNavigate }) => {
  const [report, setReport] = useState<CognitiveReport | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  const fetchReport = async () => {
    setLoading(true);
    try {
      const res = await apiFetch(apiBase, '/report');
      if (res.ok) {
        const data = await res.json();
        setReport(data);
      }
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    Promise.resolve().then(() => {
      fetchReport();
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="max-w-2xl mx-auto space-y-6 pb-12 text-left">
      {/* Cabeçalho */}
      <div className="flex justify-between items-center">
        <div className="space-y-2">
          <h2 className="text-2xl font-black text-white tracking-tight flex items-center gap-2">
            <FileText className="text-indigo-400" size={24} /> Parecer Pedagógico da IA
          </h2>
          <p className="text-xs font-bold text-slate-500 uppercase tracking-widest leading-none">
            Análise cognitiva individual e recomendações de estudo
          </p>
        </div>
        <button 
          onClick={fetchReport}
          disabled={loading}
          className="p-2 bg-slate-900 border border-slate-850 hover:bg-slate-800 text-slate-400 rounded-lg transition-all"
        >
          <RefreshCw size={14} className={loading ? 'animate-spin' : ''} />
        </button>
      </div>

      {loading ? (
        <div className="h-60 flex items-center justify-center bg-slate-900 border border-slate-800 rounded-2xl">
          <Loader2 className="animate-spin text-indigo-500" size={32} />
        </div>
      ) : report ? (
        <div className="space-y-6">
          {/* Card Resumo do Desempenho */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="p-5 rounded-xl bg-slate-900 border border-slate-800 text-center space-y-2">
              <Award className="text-indigo-400 mx-auto" size={20} />
              <p className="text-xs font-bold text-slate-500 uppercase tracking-wider">Aproveitamento</p>
              <p className="text-2xl font-extrabold text-white">{report.overall_accuracy}%</p>
            </div>
            
            <div className="p-5 rounded-xl bg-slate-900 border border-slate-800 text-center space-y-2">
              <CheckCircle2 className="text-indigo-400 mx-auto" size={20} />
              <p className="text-xs font-bold text-slate-500 uppercase tracking-wider">Total Respondido</p>
              <p className="text-2xl font-extrabold text-white">{report.questions_answered}q</p>
            </div>

            <div className="p-5 rounded-xl bg-slate-900 border border-slate-800 text-center space-y-2">
              <TrendingUp className="text-indigo-400 mx-auto" size={20} />
              <p className="text-xs font-bold text-slate-500 uppercase tracking-wider">Temas Dominados</p>
              <p className="text-2xl font-extrabold text-emerald-400">{report.mastered_count} / 23</p>
            </div>
          </div>

          {/* Recomendação Direta */}
          <div className="p-5 rounded-xl bg-indigo-950/20 border border-indigo-500/30 text-indigo-200 text-sm flex items-start gap-3 shadow-lg">
            <TrendingUp size={20} className="shrink-0 text-indigo-400 mt-0.5" />
            <div className="space-y-2">
              <p className="font-extrabold text-indigo-200">Recomendação Automática de Estudos:</p>
              <p className="text-xs leading-relaxed opacity-90">{report.recommendation}</p>
              
              {report.weakest_topics.length > 0 && (
                <div className="flex flex-wrap gap-2 pt-2">
                  {report.weakest_topics.map(subj => (
                    <button
                      key={subj}
                      onClick={() => onNavigate('estudo', { subject: subj })}
                      className="px-3 py-1 bg-indigo-650 hover:bg-indigo-600 text-white font-bold text-[10px] rounded-lg transition-all flex items-center gap-1 shadow-md"
                    >
                      <Play size={10} fill="currentColor" /> Praticar: {subj}
                    </button>
                  ))}
                </div>
              )}
            </div>
          </div>

          {/* Relatório Escrito do Professor */}
          <div className="p-6 md:p-8 rounded-2xl bg-slate-900 border border-slate-800 shadow-xl space-y-4">
            <h3 className="text-sm font-extrabold text-white uppercase tracking-wider border-b border-slate-850 pb-3">
              Diagnóstico Pedagógico
            </h3>
            <div className="text-sm text-slate-300 leading-relaxed whitespace-pre-wrap font-serif pl-1">
              {report.diagnostic}
            </div>
          </div>

          {/* Cards Auxiliares: Status da Grade */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 p-5 rounded-xl bg-slate-900/60 border border-slate-850">
            <div className="space-y-2 border-r border-slate-850/50 pr-4">
              <h4 className="text-xs font-bold text-red-400 uppercase tracking-wider flex items-center gap-1.5">
                <AlertTriangle size={14} /> Temas com Atenção Crítica ({report.critical_count})
              </h4>
              <p className="text-xs text-slate-500 leading-snug">
                Estes assuntos possuem taxa de aproveitamento insatisfatória ou alto volume de erros consecutivos. Devem ser priorizados.
              </p>
            </div>
            
            <div className="space-y-2 pl-4">
              <h4 className="text-xs font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-1.5">
                <CheckCircle2 size={14} /> Temas com Domínio Consolidado ({report.mastered_count})
              </h4>
              <p className="text-xs text-slate-500 leading-snug">
                Você atingiu a proficiência ideal nestes temas. O sistema adaptativo fará revisões espaçadas programadas de longo prazo.
              </p>
            </div>
          </div>
        </div>
      ) : (
        <div className="p-8 text-center text-slate-500">Nenhum dado de progresso disponível para gerar parecer.</div>
      )}
    </div>
  );
};
