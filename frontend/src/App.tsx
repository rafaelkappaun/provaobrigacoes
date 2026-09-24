import { useState, useEffect, useCallback, useRef } from 'react';
import { LayoutDashboard, PlayCircle, BookOpen, Menu, X, Flame, Loader2, User, Users, Scale, FileText, ShieldAlert } from 'lucide-react';
import { Dashboard, type DashboardData } from './components/Dashboard';
import { QuestionSession } from './components/QuestionSession';
import { ArticleLibrary } from './components/ArticleLibrary';
import { UserProfileModal } from './components/UserProfileModal';
import { apiFetch, getCurrentProfile } from './api';

const API_BASE = import.meta.env.VITE_API_BASE || "/api";

export type CourseModule = 'multiportas' | 'contratos' | 'processo_penal';

interface ModuleConfig {
  id: CourseModule;
  title: string;
  shortTitle: string;
  badge: string;
  countLabel: string;
  icon: typeof Scale;
  isAvailable: boolean;
}

const MODULES: ModuleConfig[] = [
  {
    id: 'multiportas',
    title: 'Modelo Multiportas & Conflitos',
    shortTitle: 'Multiportas',
    badge: '14 Temas',
    countLabel: '14 temas (Prova 01)',
    icon: Scale,
    isAvailable: true,
  },
  {
    id: 'contratos',
    title: 'Direito dos Contratos',
    shortTitle: 'Contratos',
    badge: '22 Temas',
    countLabel: '22 temas do Código Civil',
    icon: FileText,
    isAvailable: true,
  },
  {
    id: 'processo_penal',
    title: 'Processo Penal',
    shortTitle: 'Proc. Penal',
    badge: 'Em Breve',
    countLabel: 'Em desenvolvimento',
    icon: ShieldAlert,
    isAvailable: false,
  }
];

export default function App() {
  const [activeModule, setActiveModule] = useState<CourseModule>(() => {
    const saved = localStorage.getItem('jus_active_module') as CourseModule;
    return (saved === 'contratos' || saved === 'multiportas' || saved === 'processo_penal') ? saved : 'multiportas';
  });

  const [activeTab, setActiveTab] = useState<string>('estudo');
  const [dashboardData, setDashboardData] = useState<DashboardData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [mobileMenuOpen, setMobileMenuOpen] = useState<boolean>(false);
  const [extraProps, setExtraProps] = useState<Record<string, unknown>>({});
  const [profileModalOpen, setProfileModalOpen] = useState<boolean>(false);
  const [profileName, setProfileName] = useState<string>(getCurrentProfile().name);

  const fetchDashboardData = useCallback(async (moduleName: string): Promise<DashboardData> => {
    const res = await apiFetch(API_BASE, `/dashboard?module=${encodeURIComponent(moduleName)}`);
    if (res.ok) {
      return await res.json();
    }
    throw new Error(`Erro do servidor (${res.status})`);
  }, []);

  const isLoadingRef = useRef(false);

  const loadDashboard = useCallback((moduleName: string) => {
    if (isLoadingRef.current) return;
    isLoadingRef.current = true;
    setLoading(true);
    setError(null);
    fetchDashboardData(moduleName)
      .then(data => { setDashboardData(data); })
      .catch(e => {
        console.error("Erro de conexão com o servidor:", e);
        setError("Não foi possível conectar ao servidor. Verifique se o backend está em execução.");
      })
      .finally(() => { setLoading(false); isLoadingRef.current = false; });
  }, [fetchDashboardData]);

  useEffect(() => {
    if (activeModule !== 'processo_penal') {
      loadDashboard(activeModule);
    } else {
      setLoading(false);
      setDashboardData(null);
    }
  }, [activeModule, loadDashboard]);

  const handleSelectModule = (modId: CourseModule) => {
    setActiveModule(modId);
    localStorage.setItem('jus_active_module', modId);
    setExtraProps({});
    setMobileMenuOpen(false);
  };

  const handleRetry = useCallback(() => {
    if (activeModule !== 'processo_penal') {
      loadDashboard(activeModule);
    }
  }, [activeModule, loadDashboard]);

  const handleNavigate = (tab: string, extra: Record<string, unknown> = {}) => {
    setExtraProps(extra);
    setActiveTab(tab);
    setMobileMenuOpen(false);
    if (tab === 'dashboard' && activeModule !== 'processo_penal') {
      loadDashboard(activeModule);
    }
  };

  const handleProfileChanged = () => {
    setProfileName(getCurrentProfile().name);
    if (activeModule !== 'processo_penal') {
      loadDashboard(activeModule);
    }
  };

  const currentModuleConfig = MODULES.find(m => m.id === activeModule) || MODULES[0];

  const renderActiveTab = () => {
    if (activeModule === 'processo_penal') {
      return (
        <div className="max-w-2xl mx-auto my-12 p-8 rounded-3xl bg-slate-900 border border-slate-800 text-center space-y-6 shadow-2xl animate-fade-in">
          <div className="w-16 h-16 mx-auto rounded-2xl bg-amber-500/10 border border-amber-500/30 text-amber-400 flex items-center justify-center text-3xl">
            🏛️
          </div>
          <div className="space-y-2">
            <span className="px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider bg-amber-500/10 text-amber-300 border border-amber-500/20">
              Módulo em Fase de Desenvolvimento
            </span>
            <h2 className="text-2xl font-black text-white">Processo Penal</h2>
            <p className="text-slate-400 text-sm max-w-md mx-auto leading-relaxed">
              Este módulo está reservado para a 3ª matéria do semestre. O questionário de revisão oficial do professor ainda será inserido.
            </p>
          </div>
          <div className="p-5 rounded-2xl bg-slate-950/70 border border-slate-850 text-xs text-slate-300 text-left space-y-3">
            <p className="font-bold text-white flex items-center gap-2">
              <span>📋</span> O que terá neste módulo quando liberado:
            </p>
            <ul className="list-disc pl-5 space-y-1.5 text-slate-400">
              <li>Banco completo de questões objetivas baseadas no questionário de Processo Penal;</li>
              <li>Módulo 100% isolado (suas estatísticas e erros desta matéria não se misturam com as demais);</li>
              <li>Acompanhamento de acertos por tema até atingir no mínimo 90%;</li>
              <li>Guia de onde estudar mais com dispositivos do CPP e jurisprudência.</li>
            </ul>
          </div>
          <div className="pt-2 flex flex-col sm:flex-row items-center justify-center gap-3">
            <button
              onClick={() => handleSelectModule('multiportas')}
              className="w-full sm:w-auto px-5 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded-xl text-xs font-bold transition-all shadow-lg shadow-indigo-600/20"
            >
              Estudar Modelo Multiportas (14 Temas) →
            </button>
            <button
              onClick={() => handleSelectModule('contratos')}
              className="w-full sm:w-auto px-5 py-2.5 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-xs font-bold transition-all"
            >
              Estudar Direito dos Contratos (22 Temas)
            </button>
          </div>
        </div>
      );
    }

    switch (activeTab) {
      case 'estudo':
        return (
          <QuestionSession 
            key={`${activeModule}-session`}
            apiBase={API_BASE} 
            module={activeModule}
            subject={extraProps.subject as string | undefined}
            onSessionFinished={() => handleNavigate('dashboard')} 
          />
        );
      case 'dashboard':
        return dashboardData && (
          <Dashboard 
            key={`${activeModule}-dashboard`}
            data={dashboardData} 
            module={activeModule}
            onNavigate={handleNavigate} 
          />
        );
      case 'artigos':
        return <ArticleLibrary apiBase={API_BASE} onNavigate={handleNavigate} />;
      default:
        return (
          <QuestionSession 
            key={`${activeModule}-default`}
            apiBase={API_BASE} 
            module={activeModule}
            onSessionFinished={() => handleNavigate('dashboard')} 
          />
        );
    }
  };

  const menuItems = [
    { id: 'estudo', label: 'Praticar Questões', icon: PlayCircle },
    { id: 'dashboard', label: 'Desempenho & Onde Estudar', icon: LayoutDashboard },
    ...(activeModule === 'contratos' ? [{ id: 'artigos', label: 'Artigos do Código Civil', icon: BookOpen }] : []),
  ];

  return (
    <div className="flex h-screen bg-slate-950 text-slate-100 overflow-hidden font-sans">
      {/* SIDEBAR PARA DESKTOP */}
      <aside className="hidden lg:flex lg:flex-col lg:w-72 bg-slate-900 border-r border-slate-800 shrink-0">
        {/* Header Logo */}
        <div className="p-5 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="p-2 bg-gradient-to-br from-indigo-500 to-indigo-700 text-white rounded-xl shadow-md shadow-indigo-600/30">
              <Scale size={20} />
            </div>
            <div>
              <h1 className="text-sm font-black tracking-tight text-white leading-none">JUS PROVAS</h1>
              <span className="text-[10px] font-extrabold text-indigo-400 tracking-wider uppercase">3 MATÉRIAS DO SEMESTRE</span>
            </div>
          </div>
          {dashboardData && dashboardData.streak_days > 0 && (
            <div className="flex items-center gap-1 text-orange-500 font-extrabold text-xs" title="Sequência de dias">
              <Flame size={16} fill="currentColor" /> {dashboardData.streak_days}
            </div>
          )}
        </div>

        {/* SELETOR DE MÓDULOS ISOLADOS */}
        <div className="p-4 border-b border-slate-800/80 space-y-2">
          <span className="text-[10px] font-extrabold text-slate-400 uppercase tracking-wider block px-1">
            Módulos Isolados:
          </span>
          <div className="space-y-1.5">
            {MODULES.map(mod => {
              const isSelected = activeModule === mod.id;
              const Icon = mod.icon;
              return (
                <button
                  key={mod.id}
                  onClick={() => handleSelectModule(mod.id)}
                  className={`w-full flex items-center justify-between p-2.5 rounded-xl border text-left transition-all ${
                    isSelected
                      ? 'bg-indigo-600/15 border-indigo-500 text-white shadow-sm ring-1 ring-indigo-500/40'
                      : 'bg-slate-950/60 border-slate-850 text-slate-400 hover:border-slate-700 hover:text-slate-200'
                  }`}
                >
                  <div className="flex items-center gap-2.5 min-w-0">
                    <div className={`p-1.5 rounded-lg shrink-0 ${isSelected ? 'bg-indigo-600 text-white' : 'bg-slate-900 text-slate-500'}`}>
                      <Icon size={15} />
                    </div>
                    <div className="truncate">
                      <p className="text-xs font-bold truncate leading-tight text-white">{mod.title}</p>
                      <p className="text-[10px] text-slate-500 leading-tight">{mod.countLabel}</p>
                    </div>
                  </div>
                  <span className={`text-[10px] font-extrabold px-1.5 py-0.5 rounded shrink-0 ${
                    mod.id === 'processo_penal'
                      ? 'bg-amber-950/50 text-amber-400 border border-amber-900/50'
                      : isSelected
                      ? 'bg-indigo-500/20 text-indigo-300'
                      : 'bg-slate-800 text-slate-400'
                  }`}>
                    {mod.badge}
                  </span>
                </button>
              );
            })}
          </div>
        </div>

        {/* Links do Menu do Módulo Ativo */}
        <nav className="flex-1 p-4 space-y-1.5 overflow-y-auto">
          <div className="px-1 pb-1">
            <span className="text-[10px] font-extrabold text-slate-400 uppercase tracking-wider">
              {currentModuleConfig.shortTitle}:
            </span>
          </div>
          {menuItems.map(item => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => handleNavigate(item.id)}
                className={`w-full flex items-center gap-3.5 px-4 py-3 rounded-xl text-xs font-bold transition-all duration-200 ${
                  isActive 
                    ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/20' 
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/80'
                }`}
              >
                <Icon size={17} />
                <span>{item.label}</span>
              </button>
            );
          })}
        </nav>

        {/* Perfil Ativo / Amigos */}
        <div className="p-4 border-t border-slate-800 space-y-2">
          <button
            onClick={() => setProfileModalOpen(true)}
            className="w-full flex items-center justify-between p-2.5 rounded-xl bg-slate-950/70 border border-slate-800 hover:border-indigo-500/50 transition-all text-left"
          >
            <div className="flex items-center gap-2 truncate">
              <div className="w-7 h-7 rounded-lg bg-indigo-950 text-indigo-400 flex items-center justify-center font-bold text-xs shrink-0">
                <User size={14} />
              </div>
              <div className="truncate">
                <p className="text-xs font-bold text-white truncate">{profileName}</p>
                <p className="text-[10px] text-slate-500">Alternar Aluno</p>
              </div>
            </div>
            <Users size={14} className="text-slate-500 shrink-0" />
          </button>
          <p className="text-center text-[10px] text-slate-500 font-semibold">100% Offline • Sem Cota de IA</p>
        </div>
      </aside>

      {/* CONTEÚDO PRINCIPAL COM TOP BAR RESPONSIVA */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* TOP BAR MOBILE */}
        <header className="lg:hidden flex items-center justify-between p-3.5 bg-slate-900 border-b border-slate-800 safe-top">
          <div className="flex items-center gap-2">
            <div className="p-1.5 bg-indigo-600 text-white rounded-lg">
              <Scale size={16} />
            </div>
            <div>
              <span className="text-xs font-black tracking-tight text-white block leading-tight">JUS PROVAS</span>
              <span className="text-[9px] font-bold text-indigo-400 uppercase leading-none block">{currentModuleConfig.shortTitle}</span>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={() => setProfileModalOpen(true)}
              className="px-2 py-1 bg-slate-950 border border-slate-800 rounded-lg text-xs font-bold text-indigo-300 flex items-center gap-1.5"
            >
              <User size={12} />
              <span className="truncate max-w-[70px]">{profileName}</span>
            </button>
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="p-1.5 text-slate-400 hover:text-slate-200 focus:outline-none"
            >
              {mobileMenuOpen ? <X size={20} /> : <Menu size={20} />}
            </button>
          </div>
        </header>

        {/* MENU MOBILE EXPANDIDO */}
        {mobileMenuOpen && (
          <div className="lg:hidden fixed inset-0 top-14 bg-slate-950 z-50 flex flex-col p-4 space-y-4 overflow-y-auto animate-fade-in border-t border-slate-900 safe-bottom">
            {/* Seletor Mobile de Matérias */}
            <div className="space-y-2">
              <span className="text-[10px] font-extrabold text-slate-400 uppercase tracking-wider px-1">
                Escolha a Matéria do Semestre:
              </span>
              <div className="grid grid-cols-1 gap-1.5">
                {MODULES.map(mod => {
                  const isSelected = activeModule === mod.id;
                  const Icon = mod.icon;
                  return (
                    <button
                      key={mod.id}
                      onClick={() => handleSelectModule(mod.id)}
                      className={`w-full flex items-center justify-between p-3 rounded-xl border text-left transition-all ${
                        isSelected
                          ? 'bg-indigo-600/20 border-indigo-500 text-white'
                          : 'bg-slate-900 border-slate-800 text-slate-400'
                      }`}
                    >
                      <div className="flex items-center gap-2.5">
                        <Icon size={16} className={isSelected ? 'text-indigo-400' : 'text-slate-500'} />
                        <div>
                          <p className="text-xs font-bold text-white">{mod.title}</p>
                          <p className="text-[10px] text-slate-500">{mod.countLabel}</p>
                        </div>
                      </div>
                      <span className="text-[10px] font-bold px-2 py-0.5 bg-slate-950 rounded border border-slate-800">
                        {mod.badge}
                      </span>
                    </button>
                  );
                })}
              </div>
            </div>

            {/* Menu de Navegação */}
            <div className="space-y-1.5 pt-2 border-t border-slate-850">
              <span className="text-[10px] font-extrabold text-slate-400 uppercase tracking-wider px-1">
                Navegação:
              </span>
              {menuItems.map(item => {
                const Icon = item.icon;
                const isActive = activeTab === item.id;
                return (
                  <button
                    key={item.id}
                    onClick={() => handleNavigate(item.id)}
                    className={`w-full flex items-center gap-4 px-4 py-3 rounded-xl text-xs font-bold transition-all ${
                      isActive 
                        ? 'bg-indigo-600 text-white' 
                        : 'text-slate-400 hover:bg-slate-900'
                    }`}
                  >
                    <Icon size={17} />
                    <span>{item.label}</span>
                  </button>
                );
              })}
            </div>
          </div>
        )}

        {/* CONTAINER DE EXIBIÇÃO DA PÁGINA */}
        <main className="flex-1 overflow-y-auto p-4 md:p-8">
          {loading && !dashboardData && activeTab === 'dashboard' && activeModule !== 'processo_penal' ? (
            <div className="h-full flex flex-col items-center justify-center space-y-3">
              <Loader2 className="animate-spin text-indigo-500" size={32} />
              <p className="text-xs font-bold text-slate-500 uppercase tracking-widest">Carregando dados da matéria...</p>
            </div>
          ) : error && activeTab === 'dashboard' && activeModule !== 'processo_penal' ? (
            <div className="h-full flex flex-col items-center justify-center space-y-4 max-w-md mx-auto text-center px-4">
              <h2 className="text-lg font-bold text-white">Falha ao carregar</h2>
              <p className="text-sm text-slate-400">{error}</p>
              <button 
                onClick={handleRetry}
                className="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded-xl text-sm font-bold shadow-lg shadow-indigo-600/20 transition-all"
              >
                Tentar Novamente
              </button>
            </div>
          ) : (
            renderActiveTab()
          )}
        </main>
      </div>

      {/* Modal de Troca de Perfil de Usuário */}
      <UserProfileModal 
        isOpen={profileModalOpen} 
        onClose={() => setProfileModalOpen(false)} 
        onProfileChanged={handleProfileChanged} 
      />
    </div>
  );
}
