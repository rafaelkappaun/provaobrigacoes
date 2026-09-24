import React, { useState } from 'react';
import { 
  Award, 
  CheckCircle, 
  XCircle, 
  BookOpen, 
  ArrowRight, 
  Play, 
  Target, 
  Sparkles, 
  Search,
  Check,
  ChevronRight
} from 'lucide-react';

export interface SubjectDetail {
  subject: string;
  questions_answered: number;
  questions_correct: number;
  questions_incorrect: number;
  success_rate: number;
  status: 'Dominado' | 'Intermediario' | 'Critico' | 'NaoIniciado';
  consecutive_errors: number;
  consecutive_correct: number;
  is_goal_achieved: boolean;
  needed_for_90: number;
  articles?: string;
  key_concept?: string;
  trap?: string;
}

export interface DashboardData {
  overall_success_rate: number;
  questions_answered: number;
  questions_correct: number;
  questions_incorrect?: number;
  total_time_seconds: number;
  streak_days: number;
  meta_target?: number;
  meta_achieved: boolean;
  meta_progress: number;
  ranking: string;
  ranking_emoji: string;
  dominados_count: number;
  intermediarios_count: number;
  criticos_count: number;
  nao_iniciados_count?: number;
  subjects: SubjectDetail[];
  study_recommendations?: SubjectDetail[];
  next_step: string;
}

interface DashboardProps {
  data: DashboardData;
  module?: string;
  onNavigate: (tab: string, extra?: Record<string, unknown>) => void;
}

export const Dashboard: React.FC<DashboardProps> = ({ data, module = 'contratos', onNavigate }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [filterStatus, setFilterStatus] = useState<'all' | 'need_study' | 'mastered'>('all');

  // Recomendações: assuntos abaixo de 90%
  const recommendations = data.study_recommendations || data.subjects.filter(s => !s.is_goal_achieved);

  // Filtragem da lista geral de assuntos
  const filteredSubjects = data.subjects.filter(s => {
    const matchesSearch = s.subject.toLowerCase().includes(searchTerm.toLowerCase()) ||
                          (s.articles && s.articles.toLowerCase().includes(searchTerm.toLowerCase()));
    if (!matchesSearch) return false;
    if (filterStatus === 'need_study') return !s.is_goal_achieved;
    if (filterStatus === 'mastered') return s.is_goal_achieved;
    return true;
  });

  return (
    <div className="max-w-5xl mx-auto space-y-8 animate-fade-in pb-16">
      {/* BANNER PRINCIPAL: META 90% */}
      <div className="relative rounded-2xl bg-gradient-to-br from-indigo-950/80 via-slate-900 to-slate-950 border border-indigo-500/30 p-6 md:p-8 shadow-xl overflow-hidden">
        <div className="absolute -right-8 -top-8 w-64 h-64 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none" />
        
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-6 relative z-10">
          <div className="space-y-3 max-w-2xl">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/30 text-indigo-300 text-xs font-bold tracking-wider uppercase">
              <Target size={14} className="text-indigo-400" />
              Meta de Aprovação: 90% de Acertos
            </div>
            
            <h1 className="text-2xl md:text-3xl font-black text-white tracking-tight">
              Desempenho & Onde Estudar
            </h1>
            
            <p className="text-slate-300 text-sm leading-relaxed">
              {data.next_step}
            </p>
            
            {/* Barra de Progresso Rumo aos 90% */}
            <div className="pt-2 space-y-1.5">
              <div className="flex justify-between text-xs font-bold">
                <span className="text-slate-400">Progresso Geral:</span>
                <span className={`text-sm ${data.overall_success_rate >= 90 ? 'text-emerald-400 font-extrabold' : 'text-indigo-300'}`}>
                  {data.overall_success_rate}% de acertos {data.overall_success_rate >= 90 && '🎉'}
                </span>
              </div>
              
              <div className="relative w-full h-3 bg-slate-800/80 rounded-full overflow-hidden border border-slate-700/50">
                {/* Linha indicadora dos 90% */}
                <div 
                  className="absolute top-0 bottom-0 w-0.5 bg-amber-400 z-10 shadow-[0_0_8px_rgba(251,191,36,0.8)]"
                  style={{ left: '90%' }}
                  title="Meta de 90%"
                />
                {/* Barra preenchida */}
                <div 
                  className={`h-full rounded-full transition-all duration-700 ${
                    data.overall_success_rate >= 90 
                      ? 'bg-gradient-to-r from-emerald-500 to-teal-400' 
                      : 'bg-gradient-to-r from-indigo-500 to-indigo-400'
                  }`}
                  style={{ width: `${Math.min(100, data.overall_success_rate)}%` }}
                />
              </div>
              <div className="flex justify-between text-[11px] text-slate-500">
                <span>0%</span>
                <span className="text-amber-400 font-bold ml-auto pr-8">Meta: 90%</span>
                <span>100%</span>
              </div>
            </div>
          </div>

          {/* Botão de ação rápida */}
          <div className="w-full md:w-auto shrink-0 flex flex-col sm:flex-row md:flex-col gap-3">
            <button
              onClick={() => onNavigate('estudo')}
              className="px-6 py-3.5 bg-indigo-600 hover:bg-indigo-500 text-white font-extrabold rounded-xl text-sm shadow-lg shadow-indigo-600/30 transition-all flex items-center justify-center gap-2"
            >
              <Play size={16} fill="currentColor" />
              Praticar Questões Agora
            </button>
          </div>
        </div>
      </div>

      {/* CARDS DE ESTATÍSTICAS RÁPIDAS */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Total Respondidas */}
        <div className="p-4 rounded-xl bg-slate-900/90 border border-slate-800 space-y-1">
          <div className="flex items-center justify-between text-slate-400 text-xs font-bold uppercase tracking-wider">
            <span>Respondidas</span>
            <BookOpen size={16} className="text-indigo-400" />
          </div>
          <p className="text-2xl font-black text-white">{data.questions_answered}</p>
          <p className="text-[11px] text-slate-500">Total de questões feitas</p>
        </div>

        {/* Quantidade de Acertos */}
        <div className="p-4 rounded-xl bg-slate-900/90 border border-slate-800 space-y-1">
          <div className="flex items-center justify-between text-emerald-400 text-xs font-bold uppercase tracking-wider">
            <span>Acertos</span>
            <CheckCircle size={16} />
          </div>
          <p className="text-2xl font-black text-emerald-400">{data.questions_correct}</p>
          <p className="text-[11px] text-slate-500">
            {data.questions_answered > 0 ? `${data.overall_success_rate}% de aproveitamento` : 'Ainda não iniciado'}
          </p>
        </div>

        {/* Quantidade de Erros */}
        <div className="p-4 rounded-xl bg-slate-900/90 border border-slate-800 space-y-1">
          <div className="flex items-center justify-between text-rose-400 text-xs font-bold uppercase tracking-wider">
            <span>Erros</span>
            <XCircle size={16} />
          </div>
          <p className="text-2xl font-black text-rose-400">
            {data.questions_answered - data.questions_correct}
          </p>
          <p className="text-[11px] text-slate-500">Oportunidades de revisão</p>
        </div>

        {/* Conteúdos em 90%+ */}
        <div className="p-4 rounded-xl bg-slate-900/90 border border-slate-800 space-y-1">
          <div className="flex items-center justify-between text-amber-400 text-xs font-bold uppercase tracking-wider">
            <span>Meta 90%</span>
            <Award size={16} />
          </div>
          <p className="text-2xl font-black text-amber-400">
            {data.dominados_count} <span className="text-xs text-slate-500 font-semibold">/ {data.subjects.length} temas</span>
          </p>
          <p className="text-[11px] text-slate-500">
            {data.dominados_count === data.subjects.length ? 'Todos dominados!' : `Faltam ${data.subjects.length - data.dominados_count} para os 90%`}
          </p>
        </div>
      </div>

      {/* SEÇÃO PRINCIPAL: ONDE ESTUDAR MAIS ATÉ 90% */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div className="space-y-0.5">
            <h2 className="text-lg font-black text-white flex items-center gap-2">
              <Sparkles size={18} className="text-amber-400" />
              Onde Estudar Mais (Rumo aos 90%)
            </h2>
            <p className="text-xs text-slate-400">
              {module === 'multiportas'
                ? 'Conteúdos prioritários que ainda não atingiram 90% de acertos, com fundamentos normativos (CPC/15, Lei 9.099/95, Lei 13.140/15) e conceitos-chave.'
                : 'Conteúdos prioritários que ainda não atingiram 90% de acertos, com artigos do Código Civil e dicas para memorizar.'}
            </p>
          </div>
          <span className="text-xs font-bold px-2.5 py-1 bg-amber-500/10 text-amber-400 border border-amber-500/20 rounded-lg">
            {recommendations.length} {recommendations.length === 1 ? 'conteúdo pendente' : 'conteúdos pendentes'}
          </span>
        </div>

        {recommendations.length === 0 ? (
          <div className="p-8 rounded-2xl bg-emerald-950/20 border border-emerald-500/30 text-center space-y-3">
            <div className="w-12 h-12 mx-auto rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center">
              <Award size={28} />
            </div>
            <h3 className="text-lg font-bold text-white">Parabéns! Meta de 90% atingida em todos os temas!</h3>
            <p className="text-xs text-slate-300 max-w-md mx-auto">
              Você alcançou pelo menos 90% de acertos em cada um dos {data.subjects.length} conteúdos {module === 'multiportas' ? 'do Modelo Multiportas' : 'da matéria'}. Continue praticando para manter o conhecimento fresco.
            </p>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {recommendations.slice(0, 6).map((item) => (
              <div 
                key={item.subject}
                className="p-5 rounded-2xl bg-slate-900 border border-slate-800 hover:border-slate-700 transition-all flex flex-col justify-between space-y-4 shadow-md"
              >
                <div className="space-y-2.5">
                  <div className="flex items-start justify-between gap-2">
                    <span className="text-xs font-black text-indigo-400 bg-indigo-950/50 border border-indigo-800/50 px-2 py-0.5 rounded">
                      {item.articles || 'Código Civil'}
                    </span>
                    <span className={`text-[11px] font-bold px-2 py-0.5 rounded ${
                      item.questions_answered === 0 
                        ? 'bg-slate-800 text-slate-400' 
                        : item.success_rate < 60 
                        ? 'bg-rose-950/50 text-rose-400 border border-rose-800/40' 
                        : 'bg-amber-950/50 text-amber-400 border border-amber-800/40'
                    }`}>
                      {item.questions_answered === 0 ? 'Não Iniciado' : `${item.success_rate}% de acertos`}
                    </span>
                  </div>

                  <h3 className="text-sm font-bold text-white leading-snug">
                    {item.subject}
                  </h3>

                  {/* Resumo do que estudar */}
                  {item.key_concept && (
                    <p className="text-xs text-slate-300 leading-relaxed bg-slate-950/60 p-2.5 rounded-lg border border-slate-850">
                      📖 <strong className="text-white">O que estudar:</strong> {item.key_concept}
                    </p>
                  )}

                  {/* Pegadinha de prova */}
                  {item.trap && (
                    <p className="text-[11px] text-amber-300/90 leading-relaxed bg-amber-950/20 p-2 rounded border border-amber-900/30">
                      ⚡ <strong className="text-amber-200">Atenção em prova:</strong> {item.trap}
                    </p>
                  )}
                </div>

                <div className="pt-2 border-t border-slate-850 flex items-center justify-between gap-3">
                  <div className="text-[11px] text-slate-400">
                    {item.questions_answered === 0 ? (
                      <span className="text-slate-400">Faça ao menos 3 questões</span>
                    ) : (
                      <span>
                        Faltam <strong className="text-amber-400">~{item.needed_for_90} acertos</strong> para os 90%
                      </span>
                    )}
                  </div>

                  <button
                    onClick={() => onNavigate('estudo', { subject: item.subject })}
                    className="px-3.5 py-1.5 bg-indigo-650 hover:bg-indigo-500 text-white text-xs font-bold rounded-lg transition-all flex items-center gap-1.5 shadow"
                  >
                    Praticar <ChevronRight size={14} />
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* SEÇÃO: QUANTIDADE DE ACERTOS DE CADA CONTEÚDO (TODOS OS 22 TEMAS) */}
      <div className="space-y-4 pt-4 border-t border-slate-800/60">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
          <div className="space-y-0.5">
            <h2 className="text-lg font-black text-white flex items-center gap-2">
              <CheckCircle size={18} className="text-emerald-400" />
              Acertos por Conteúdo ({data.subjects.length} Temas)
            </h2>
            <p className="text-xs text-slate-400">
              Acompanhe a quantidade exata de acertos e o percentual em cada conteúdo.
            </p>
          </div>

          {/* Filtros e Busca */}
          <div className="flex flex-wrap items-center gap-2 w-full sm:w-auto">
            <div className="relative flex-1 sm:w-48">
              <Search size={14} className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-500" />
              <input
                type="text"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                placeholder="Buscar tema ou artigo..."
                className="w-full pl-8 pr-3 py-1.5 bg-slate-900 border border-slate-800 rounded-lg text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-indigo-500"
              />
            </div>

            <div className="flex bg-slate-900 border border-slate-800 rounded-lg p-0.5 text-xs font-bold">
              <button
                onClick={() => setFilterStatus('all')}
                className={`px-2.5 py-1 rounded ${filterStatus === 'all' ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-white'}`}
              >
                Todos ({data.subjects.length})
              </button>
              <button
                onClick={() => setFilterStatus('need_study')}
                className={`px-2.5 py-1 rounded ${filterStatus === 'need_study' ? 'bg-amber-600 text-white' : 'text-slate-400 hover:text-white'}`}
              >
                Abaixo de 90% ({recommendations.length})
              </button>
              <button
                onClick={() => setFilterStatus('mastered')}
                className={`px-2.5 py-1 rounded ${filterStatus === 'mastered' ? 'bg-emerald-600 text-white' : 'text-slate-400 hover:text-white'}`}
              >
                ≥ 90% ({data.dominados_count})
              </button>
            </div>
          </div>
        </div>

        {/* LISTAGEM DOS CONTEÚDOS */}
        <div className="space-y-2.5">
          {filteredSubjects.map((sub) => {
            const is90 = sub.is_goal_achieved;
            return (
              <div 
                key={sub.subject}
                className={`p-4 rounded-xl border transition-all ${
                  is90 
                    ? 'bg-slate-900/60 border-emerald-500/20 hover:border-emerald-500/40' 
                    : sub.questions_answered === 0
                    ? 'bg-slate-900/40 border-slate-800 hover:border-slate-700'
                    : 'bg-slate-900 border-slate-800 hover:border-indigo-500/30'
                } flex flex-col md:flex-row items-start md:items-center justify-between gap-3`}
              >
                <div className="space-y-1 flex-1">
                  <div className="flex flex-wrap items-center gap-2">
                    <h4 className="text-sm font-bold text-white">
                      {sub.subject}
                    </h4>
                    {sub.articles && (
                      <span className="text-[10px] font-semibold text-slate-400 bg-slate-800/80 px-2 py-0.5 rounded">
                        {sub.articles}
                      </span>
                    )}
                  </div>

                  {/* Barra de Progresso do Conteúdo */}
                  <div className="flex items-center gap-3 pt-1 max-w-md">
                    <div className="relative flex-1 h-2 bg-slate-800 rounded-full overflow-hidden">
                      <div 
                        className="absolute top-0 bottom-0 w-0.5 bg-amber-400 z-10"
                        style={{ left: '90%' }}
                        title="Meta 90%"
                      />
                      <div 
                        className={`h-full rounded-full transition-all duration-500 ${
                          is90 
                            ? 'bg-emerald-500' 
                            : sub.success_rate >= 70 
                            ? 'bg-indigo-500' 
                            : 'bg-amber-500'
                        }`}
                        style={{ width: `${Math.min(100, sub.success_rate)}%` }}
                      />
                    </div>
                    <span className="text-xs font-bold text-slate-400 w-12 text-right">
                      {sub.questions_answered === 0 ? '0%' : `${sub.success_rate}%`}
                    </span>
                  </div>
                </div>

                {/* Acertos e Status */}
                <div className="flex items-center gap-4 self-end md:self-auto shrink-0">
                  <div className="text-right">
                    <p className="text-xs font-black text-white">
                      {sub.questions_correct} <span className="text-slate-500 font-normal">/ {sub.questions_answered} acertos</span>
                    </p>
                    <p className="text-[10px]">
                      {is90 ? (
                        <span className="text-emerald-400 font-bold flex items-center gap-1 justify-end">
                          <Check size={12} /> Meta 90% Atingida
                        </span>
                      ) : sub.questions_answered === 0 ? (
                        <span className="text-slate-500">Não iniciado</span>
                      ) : (
                        <span className="text-amber-400 font-medium">
                          Faltam ~{sub.needed_for_90} acertos
                        </span>
                      )}
                    </p>
                  </div>

                  <button
                    onClick={() => onNavigate('estudo', { subject: sub.subject })}
                    className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1 ${
                      is90
                        ? 'bg-slate-800 text-slate-300 hover:bg-slate-700'
                        : 'bg-indigo-650 text-white hover:bg-indigo-500 shadow-md shadow-indigo-600/20'
                    }`}
                  >
                    Treinar <ArrowRight size={13} />
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
