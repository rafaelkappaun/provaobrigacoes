import React from 'react';
import { Flame, Clock, Award, CheckCircle, BookOpen, AlertTriangle, ArrowRight, Play, Zap, Shield } from 'lucide-react';

export interface Subject {
  subject: string;
  questions_answered: number;
  questions_correct: number;
  success_rate: number;
  status: 'Critico' | 'Intermediario' | 'Dominado';
  consecutive_errors: number;
  consecutive_correct: number;
  mastery_target: string;
  is_intensive: boolean;
}

export interface DashboardData {
  overall_success_rate: number;
  questions_answered: number;
  questions_correct: number;
  total_time_seconds: number;
  streak_days: number;
  meta_achieved: boolean;
  meta_progress: number;
  ranking: string;
  ranking_emoji: string;
  criticos_count: number;
  intermediarios_count: number;
  dominados_count: number;
  intensive_subject: string | null;
  subjects: Subject[];
  next_step: string;
}

interface DashboardProps {
  data: DashboardData;
  onNavigate: (tab: string, extra?: Record<string, unknown>) => void;
}

export const Dashboard: React.FC<DashboardProps> = ({ data, onNavigate }) => {
  const formatTime = (seconds: number) => {
    const hrs = Math.floor(seconds / 3600);
    const mins = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    return `${hrs.toString().padStart(2, '0')}:${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const adimplementoSubjects = data.subjects.filter(s => 
    [
      "Pagamento - Geral", "Quem deve pagar", "A quem se deve pagar", "Objeto do pagamento e sua prova",
      "Lugar do pagamento", "Tempo do pagamento", "Consignação em pagamento", "Pagamento com sub-rogação",
      "Imputação do pagamento", "Dação em pagamento", "Novação", "Compensação", "Confusão", "Remissão das dívidas"
    ].includes(s.subject)
  );

  const inadimplementoSubjects = data.subjects.filter(s => 
    [
      "Inadimplemento - Disposições gerais", "Mora - Geral", "Mora do devedor", "Mora do credor",
      "Inadimplemento absoluto", "Perdas e danos", "Juros legais", "Cláusula penal", "Arras ou sinal"
    ].includes(s.subject)
  );

  const renderStatusTag = (sub: Subject) => {
    if (sub.is_intensive) {
      return (
        <span className="px-2 py-0.5 text-xs font-semibold rounded bg-red-950/60 text-red-400 border border-red-800 animate-pulse flex items-center gap-1">
          <Zap size={10} className="fill-current" /> INTENSIVO
        </span>
      );
    }
    if (sub.status === 'Dominado' || sub.consecutive_correct >= 5) {
      return (
        <div className="flex items-center gap-1">
          <span className="px-2 py-0.5 text-xs font-semibold rounded bg-emerald-950/40 text-emerald-400 border border-emerald-900/60 font-medium">🟢 Dominado</span>
        </div>
      );
    }
    if (sub.questions_answered === 0) {
      return (
        <div className="flex items-center gap-1">
          <span className="px-2 py-0.5 text-xs font-semibold rounded bg-slate-800/60 text-slate-400 border border-slate-700">⬜ Novo</span>
          <span className="text-xs font-bold text-amber-400">0/5</span>
        </div>
      );
    }
    return (
      <div className="flex items-center gap-1">
        <span className={`px-2 py-0.5 text-xs font-semibold rounded ${
          sub.status === 'Critico'
            ? 'bg-red-950/40 text-red-400 border border-red-900/60'
            : 'bg-amber-950/40 text-amber-400 border border-amber-900/60'
        }`}>
          {sub.status === 'Critico' ? '🔴 Crítico' : '🟡 Intermediário'}
        </span>
        <span className={`text-xs font-bold ${sub.consecutive_correct > 0 ? 'text-amber-400' : 'text-slate-500'}`}>
          {sub.consecutive_correct}/{sub.mastery_target || '5'}
        </span>
      </div>
    );
  };

  return (
    <div className="space-y-8 animate-fade-in pb-12">
      {/* Banner Principal */}
      <div className="relative rounded-2xl bg-gradient-to-r from-indigo-900/40 via-indigo-950/50 to-slate-900 border border-indigo-500/20 p-6 md:p-8 overflow-hidden">
        <div className="absolute right-0 bottom-0 top-0 opacity-10 flex items-center pointer-events-none pr-8">
          <Award size={260} className="text-indigo-400 animate-float" />
        </div>
        <div className="max-w-2xl space-y-4">
          <span className="px-3 py-1 text-xs font-semibold rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/30 uppercase tracking-widest">
            Direito Civil adaptativo
          </span>
          <h1 className="text-3xl md:text-4xl font-extrabold text-white tracking-tight">
            Domine Adimplemento e Inadimplemento das Obrigações
          </h1>
          <p className="text-slate-300 leading-relaxed text-sm md:text-base">
            Preparação inteligente baseada nos artigos 304 a 420 do Código Civil. Nosso professor virtual guiará seus estudos até alcançar a meta de 95% de acertos.
          </p>
          
          {data.intensive_subject && (
            <div className="p-4 rounded-xl bg-red-950/30 border border-red-500/30 text-red-200 text-sm flex flex-col md:flex-row items-start md:items-center justify-between gap-3 shadow-lg">
              <div className="flex items-center gap-3">
                <div className="p-2 rounded-lg bg-red-500/20 text-red-400">
                  <Flame className="animate-pulse" size={20} />
                </div>
                <div>
                  <p className="font-bold text-red-300">🔥 Modo Intensivo Ativado!</p>
                  <p className="text-xs text-red-400/90">Tema bloqueado: <strong className="text-white">{data.intensive_subject}</strong> (Obtenha 80% de acertos para desbloquear novos temas).</p>
                </div>
              </div>
              <button 
                onClick={() => onNavigate('estudo')}
                className="px-4 py-2 text-xs font-bold bg-red-600 hover:bg-red-500 text-white rounded-lg transition-all duration-200 shadow-md hover:shadow-red-600/20 flex items-center gap-1.5 self-end md:self-auto"
              >
                Superar Tema <ArrowRight size={14} />
              </button>
            </div>
          )}
        </div>
      </div>

      {/* Grid de Estatísticas Globais */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Taxa de acerto */}
        <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col justify-between space-y-4 glow-card">
          <div className="flex justify-between items-center text-slate-400">
            <span className="text-xs font-semibold tracking-wider uppercase">Taxa de Acertos</span>
            <Award className="text-indigo-400" size={18} />
          </div>
          <div className="space-y-1">
            <div className="flex items-baseline gap-1.5">
              <span className={`text-3xl font-extrabold tracking-tight ${data.overall_success_rate >= 95 ? 'text-emerald-400' : 'text-white'}`}>
                {data.overall_success_rate}%
              </span>
              <span className="text-xs text-slate-500">/ 95% meta</span>
            </div>
            <div className="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden">
              <div 
                className={`h-full rounded-full transition-all duration-500 ${data.overall_success_rate >= 95 ? 'bg-emerald-500' : 'bg-indigo-500'}`}
                style={{ width: `${Math.min(100, data.overall_success_rate)}%` }}
              />
            </div>
          </div>
        </div>

        {/* Questões Respondidas */}
        <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col justify-between space-y-4 glow-card">
          <div className="flex justify-between items-center text-slate-400">
            <span className="text-xs font-semibold tracking-wider uppercase">Questões Respondidas</span>
            <CheckCircle className="text-indigo-400" size={18} />
          </div>
          <div className="space-y-0.5">
            <span className="text-3xl font-extrabold tracking-tight text-white">
              {data.questions_answered}
            </span>
            <p className="text-xs text-slate-500">
              {data.questions_correct} acertos corretos
            </p>
          </div>
        </div>

        {/* Tempo de estudo */}
        <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col justify-between space-y-4 glow-card">
          <div className="flex justify-between items-center text-slate-400">
            <span className="text-xs font-semibold tracking-wider uppercase">Tempo de Estudo</span>
            <Clock className="text-indigo-400" size={18} />
          </div>
          <div className="space-y-0.5">
            <span className="text-3xl font-extrabold tracking-tight text-white">
              {formatTime(data.total_time_seconds)}
            </span>
            <p className="text-xs text-slate-500">Foco e aprendizado ativo</p>
          </div>
        </div>

        {/* Sequência de estudos */}
        <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col justify-between space-y-4 glow-card">
          <div className="flex justify-between items-center text-slate-400">
            <span className="text-xs font-semibold tracking-wider uppercase">Streak (Sequência)</span>
            <Flame className="text-orange-500 fill-orange-500/20" size={18} />
          </div>
          <div className="space-y-0.5">
            <span className="text-3xl font-extrabold tracking-tight text-white flex items-center gap-2">
              {data.streak_days} {data.streak_days === 1 ? 'Dia' : 'Dias'}
            </span>
            <p className="text-xs text-slate-500">Mantenha a chama ativa!</p>
          </div>
        </div>
      </div>

      {/* Ranking Pessoal e Meta 95% */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div className="p-5 rounded-2xl bg-gradient-to-r from-amber-950/20 to-slate-900 border border-amber-500/20 flex items-center gap-4 glow-card">
          <div className="text-3xl">{data.ranking_emoji}</div>
          <div>
            <p className="text-xs font-bold text-amber-400 uppercase tracking-wider">Ranking Pessoal</p>
            <p className="text-lg font-extrabold text-white">{data.ranking}</p>
            <p className="text-[10px] text-slate-500">Responda mais questões para subir de nível</p>
          </div>
        </div>
        <div className="p-5 rounded-2xl bg-gradient-to-r from-indigo-950/20 to-slate-900 border border-indigo-500/20 flex items-center gap-4 glow-card">
          <div className="p-2 rounded-xl bg-indigo-500/10">
            <Award className="text-indigo-400" size={28} />
          </div>
          <div className="flex-1">
            <div className="flex justify-between items-center">
              <p className="text-xs font-bold text-indigo-400 uppercase tracking-wider">Meta 95%</p>
              <span className="text-lg font-extrabold text-white">{data.meta_progress}%</span>
            </div>
            <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden mt-1">
              <div className="h-full rounded-full bg-indigo-500 transition-all duration-500" style={{ width: `${Math.min(100, data.meta_progress)}%` }} />
            </div>
            <p className="text-[10px] text-slate-500 mt-1">{data.meta_achieved ? '🏆 DOMÍNIO ALCANÇADO!' : 'Continue estudando para atingir 95%'}</p>
          </div>
        </div>
      </div>

      {/* Atalhos Rápidos */}
      <div className="space-y-3">
        <h3 className="text-lg font-bold text-white tracking-tight">Atalhos de Estudos</h3>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <button 
            onClick={() => onNavigate('estudo')}
            className="flex items-center justify-between p-4 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold transition-all shadow-lg hover:shadow-indigo-600/20 group text-left"
          >
            <div className="flex items-center gap-3">
              <div className="p-2 rounded-lg bg-white/10">
                <Play size={18} fill="currentColor" />
              </div>
              <div>
                <p className="text-sm font-extrabold">Estudar Agora</p>
                <p className="text-xs text-indigo-200 font-normal">Questões adaptativas</p>
              </div>
            </div>
            <ArrowRight size={18} className="transform group-hover:translate-x-1 transition-transform" />
          </button>

          <button 
            onClick={() => onNavigate('simulado')}
            className="flex items-center justify-between p-4 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-bold transition-all border border-slate-800 group text-left"
          >
            <div className="flex items-center gap-3">
              <div className="p-2 rounded-lg bg-indigo-500/10 text-indigo-400">
                <Shield size={18} />
              </div>
              <div>
                <p className="text-sm font-extrabold">Simulado Rápido</p>
                <p className="text-xs text-slate-400 font-normal">Testar conhecimentos</p>
              </div>
            </div>
            <ArrowRight size={18} className="text-slate-400 transform group-hover:translate-x-1 transition-transform" />
          </button>

          <button 
            onClick={() => onNavigate('simulado', { vespera: true })}
            className="flex items-center justify-between p-4 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-bold transition-all border border-slate-800 group text-left"
          >
            <div className="flex items-center gap-3">
              <div className="p-2 rounded-lg bg-orange-500/10 text-orange-400">
                <Flame size={18} />
              </div>
              <div>
                <p className="text-sm font-extrabold">Revisão de Véspera</p>
                <p className="text-xs text-slate-400 font-normal">50 itens prioritários</p>
              </div>
            </div>
            <ArrowRight size={18} className="text-slate-400 transform group-hover:translate-x-1 transition-transform" />
          </button>

          <button 
            onClick={() => onNavigate('erros')}
            className="flex items-center justify-between p-4 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-bold transition-all border border-slate-800 group text-left"
          >
            <div className="flex items-center gap-3">
              <div className="p-2 rounded-lg bg-red-500/10 text-red-400">
                <AlertTriangle size={18} />
              </div>
              <div>
                <p className="text-sm font-extrabold">Treinar Erros</p>
                <p className="text-xs text-slate-400 font-normal">Foco no que errou</p>
              </div>
            </div>
            <ArrowRight size={18} className="text-slate-400 transform group-hover:translate-x-1 transition-transform" />
          </button>
        </div>
      </div>

      {/* Próximo Passo Inteligente */}
      {data.next_step && (
        <div className="p-4 rounded-xl bg-gradient-to-r from-indigo-950/30 to-slate-900 border border-indigo-500/15 flex items-start gap-3 glow-card">
          <div className="text-lg shrink-0 mt-0.5">💡</div>
          <div>
            <p className="text-xs font-bold text-indigo-400 uppercase tracking-wider mb-0.5">Próximo Passo</p>
            <p className="text-sm text-slate-200 font-semibold">{data.next_step}</p>
          </div>
        </div>
      )}

      {/* Jornada Adaptativa dos Temas */}
      <div className="space-y-6">
        <div className="flex justify-between items-center">
          <h3 className="text-lg font-bold text-white tracking-tight">Grade de Temas do Código Civil</h3>
          <div className="flex items-center gap-4 text-xs text-slate-400">
            <span className="flex items-center gap-1">🔴 Crítico</span>
            <span className="flex items-center gap-1">🟡 Intermediário</span>
            <span className="flex items-center gap-1">🟢 Dominado (5/5 consecutivos)</span>
          </div>
        </div>

        {/* Categoria 1: Adimplemento */}
        <div className="space-y-4 p-6 rounded-2xl bg-slate-900 border border-slate-800">
          <h4 className="text-sm font-extrabold text-indigo-400 uppercase tracking-widest flex items-center gap-2">
            <BookOpen size={16} /> Adimplemento das Obrigações (arts. 304 a 388)
          </h4>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {adimplementoSubjects.map(sub => (
              <div key={sub.subject} className="p-4 rounded-xl bg-slate-950 border border-slate-800/60 hover:border-indigo-500/20 transition-all flex flex-col justify-between gap-3">
                <div className="flex items-start justify-between gap-2">
                  <span className="text-sm font-bold text-slate-200 line-clamp-1">{sub.subject}</span>
                  {renderStatusTag(sub)}
                </div>
                <div className="space-y-1">
                  <div className="flex justify-between text-xs text-slate-500">
                    <span>Respondidas: {sub.questions_answered}</span>
                    <span>Acertos: {sub.success_rate}%</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <div className="flex-1 w-full bg-slate-900 h-1.5 rounded-full overflow-hidden">
                      <div 
                        className={`h-full rounded-full transition-all duration-300 ${
                          sub.is_intensive ? 'bg-red-600 animate-pulse' :
                          sub.status === 'Critico' ? 'bg-red-500' : 
                          sub.status === 'Intermediario' ? 'bg-amber-500' : 'bg-emerald-500'
                        }`}
                        style={{ width: `${sub.questions_answered > 0 ? sub.success_rate : 0}%` }}
                      />
                    </div>
                    <span className="text-xs font-bold text-slate-400 shrink-0">{sub.success_rate}%</span>
                  </div>
                  {/* Barra de progresso: acertos consecutivos para Dominado */}
                  <div className="flex items-center gap-1.5">
                    <span className="text-[10px] text-slate-500">🔥</span>
                    {[1,2,3,4,5].map(step => (
                      <div key={step} className={`w-3.5 h-3.5 rounded-full border flex items-center justify-center ${
                        step <= sub.consecutive_correct
                          ? 'bg-emerald-500/40 border-emerald-500'
                          : 'bg-slate-800 border-slate-700'
                      }`}>
                        {step <= sub.consecutive_correct && (
                          <span className="text-[8px] text-emerald-300 font-bold">✓</span>
                        )}
                      </div>
                    ))}
                    <span className="text-[10px] text-slate-500 ml-1">
                      {sub.consecutive_correct >= 5 ? '✅ Dominado!' : `${sub.consecutive_correct}/5`}
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Categoria 2: Inadimplemento */}
        <div className="space-y-4 p-6 rounded-2xl bg-slate-900 border border-slate-800">
          <h4 className="text-sm font-extrabold text-indigo-400 uppercase tracking-widest flex items-center gap-2">
            <AlertTriangle size={16} /> Inadimplemento das Obrigações (arts. 389 a 420)
          </h4>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {inadimplementoSubjects.map(sub => (
              <div key={sub.subject} className="p-4 rounded-xl bg-slate-950 border border-slate-800/60 hover:border-indigo-500/20 transition-all flex flex-col justify-between gap-3">
                <div className="flex items-start justify-between gap-2">
                  <span className="text-sm font-bold text-slate-200 line-clamp-1">{sub.subject}</span>
                  {renderStatusTag(sub)}
                </div>
                <div className="space-y-1">
                  <div className="flex justify-between text-xs text-slate-500">
                    <span>Respondidas: {sub.questions_answered}</span>
                    <span>Acertos: {sub.success_rate}%</span>
                  </div>
                  <div className="flex items-center gap-2">
                    <div className="flex-1 w-full bg-slate-900 h-1.5 rounded-full overflow-hidden">
                      <div 
                        className={`h-full rounded-full transition-all duration-300 ${
                          sub.is_intensive ? 'bg-red-600 animate-pulse' :
                          sub.status === 'Critico' ? 'bg-red-500' : 
                          sub.status === 'Intermediario' ? 'bg-amber-500' : 'bg-emerald-500'
                        }`}
                        style={{ width: `${sub.questions_answered > 0 ? sub.success_rate : 0}%` }}
                      />
                    </div>
                    <span className="text-xs font-bold text-slate-400 shrink-0">{sub.success_rate}%</span>
                  </div>
                  {/* Barra de progresso: acertos consecutivos para Dominado */}
                  <div className="flex items-center gap-1.5">
                    <span className="text-[10px] text-slate-500">🔥</span>
                    {[1,2,3,4,5].map(step => (
                      <div key={step} className={`w-3.5 h-3.5 rounded-full border flex items-center justify-center ${
                        step <= sub.consecutive_correct
                          ? 'bg-emerald-500/40 border-emerald-500'
                          : 'bg-slate-800 border-slate-700'
                      }`}>
                        {step <= sub.consecutive_correct && (
                          <span className="text-[8px] text-emerald-300 font-bold">✓</span>
                        )}
                      </div>
                    ))}
                    <span className="text-[10px] text-slate-500 ml-1">
                      {sub.consecutive_correct >= 5 ? '✅ Dominado!' : `${sub.consecutive_correct}/5`}
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
