import { useState, useEffect, useCallback, useRef } from 'react';
import { LayoutDashboard, PlayCircle, BookOpen, Menu, X, Flame, Loader2, User, Users } from 'lucide-react';
import { Dashboard, type DashboardData } from './components/Dashboard';
import { QuestionSession } from './components/QuestionSession';
import { ArticleLibrary } from './components/ArticleLibrary';
import { UserProfileModal } from './components/UserProfileModal';
import { apiFetch, getCurrentProfile } from './api';

const API_BASE = import.meta.env.VITE_API_BASE || "/api";

export default function App() {
  const [activeTab, setActiveTab] = useState<string>('estudo');
  const [dashboardData, setDashboardData] = useState<DashboardData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [mobileMenuOpen, setMobileMenuOpen] = useState<boolean>(false);
  const [extraProps, setExtraProps] = useState<Record<string, unknown>>({});
  const [profileModalOpen, setProfileModalOpen] = useState<boolean>(false);
  const [profileName, setProfileName] = useState<string>(getCurrentProfile().name);

  const fetchDashboardData = useCallback(async (): Promise<DashboardData> => {
    const res = await apiFetch(API_BASE, '/dashboard');
    if (res.ok) {
      return await res.json();
    }
    throw new Error(`Erro do servidor (${res.status})`);
  }, []);

  const isLoadingRef = useRef(false);

  const loadDashboard = useCallback(() => {
    if (isLoadingRef.current) return;
    isLoadingRef.current = true;
    setLoading(true);
    setError(null);
    fetchDashboardData()
      .then(data => { setDashboardData(data); })
      .catch(e => {
        console.error("Erro de conexão com o servidor:", e);
        setError("Não foi possível conectar ao servidor. Verifique se o backend está em execução.");
      })
      .finally(() => { setLoading(false); isLoadingRef.current = false; });
  }, [fetchDashboardData]);

  useEffect(() => {
    loadDashboard();
  }, [loadDashboard]);

  const handleRetry = useCallback(() => {
    loadDashboard();
  }, [loadDashboard]);

  const handleNavigate = (tab: string, extra: Record<string, unknown> = {}) => {
    setExtraProps(extra);
    setActiveTab(tab);
    setMobileMenuOpen(false);
    if (tab === 'dashboard') {
      loadDashboard();
    }
  };

  const handleProfileChanged = () => {
    setProfileName(getCurrentProfile().name);
    loadDashboard();
  };

  const renderActiveTab = () => {
    switch (activeTab) {
      case 'estudo':
        return (
          <QuestionSession 
            apiBase={API_BASE} 
            subject={extraProps.subject as string | undefined}
            onSessionFinished={() => handleNavigate('dashboard')} 
          />
        );
      case 'dashboard':
        return dashboardData && <Dashboard data={dashboardData} onNavigate={handleNavigate} />;
      case 'artigos':
        return <ArticleLibrary apiBase={API_BASE} onNavigate={handleNavigate} />;
      default:
        return (
          <QuestionSession 
            apiBase={API_BASE} 
            onSessionFinished={() => handleNavigate('dashboard')} 
          />
        );
    }
  };

  const menuItems = [
    { id: 'estudo', label: 'Praticar Questões', icon: PlayCircle },
    { id: 'dashboard', label: 'Desempenho & Onde Estudar', icon: LayoutDashboard },
    { id: 'artigos', label: 'Artigos do Código Civil', icon: BookOpen },
  ];

  return (
    <div className="flex h-screen bg-slate-950 text-slate-100 overflow-hidden font-sans">
      {/* SIDEBAR PARA DESKTOP */}
      <aside className="hidden lg:flex lg:flex-col lg:w-64 bg-slate-900 border-r border-slate-800 shrink-0">
        {/* Header Logo */}
        <div className="p-6 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="p-2 bg-indigo-600 text-white rounded-xl shadow-md shadow-indigo-600/20">
              <PlayCircle size={20} />
            </div>
            <div>
              <h1 className="text-sm font-black tracking-tight text-white leading-none">JUS CONTRATOS</h1>
              <span className="text-[10px] font-extrabold text-indigo-400 tracking-wider">QUESTÕES & METAS</span>
            </div>
          </div>
          {dashboardData && dashboardData.streak_days > 0 && (
            <div className="flex items-center gap-1 text-orange-500 font-extrabold text-xs" title="Sequência de dias">
              <Flame size={16} fill="currentColor" /> {dashboardData.streak_days}
            </div>
          )}
        </div>

        {/* Links do Menu */}
        <nav className="flex-1 p-4 space-y-2 overflow-y-auto">
          {menuItems.map(item => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => handleNavigate(item.id)}
                className={`w-full flex items-center gap-3.5 px-4 py-3.5 rounded-xl text-sm font-bold transition-all duration-200 ${
                  isActive 
                    ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/20' 
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/80'
                }`}
              >
                <Icon size={18} />
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
          <p className="text-center text-[10px] text-slate-600 font-semibold">100% Offline • Sem Cota de IA</p>
        </div>
      </aside>

      {/* CONTEÚDO PRINCIPAL COM TOP BAR RESPONSIVA */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* TOP BAR MOBILE */}
        <header className="lg:hidden flex items-center justify-between p-4 min-h-14 bg-slate-900 border-b border-slate-800 safe-top">
          <div className="flex items-center gap-2.5">
            <div className="p-1.5 bg-indigo-600 text-white rounded-lg">
              <PlayCircle size={16} />
            </div>
            <span className="text-xs font-black tracking-tight text-white">JUS CONTRATOS</span>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={() => setProfileModalOpen(true)}
              className="px-2.5 py-1 bg-slate-950 border border-slate-800 rounded-lg text-xs font-bold text-indigo-300 flex items-center gap-1.5"
            >
              <User size={13} />
              <span className="truncate max-w-[80px]">{profileName}</span>
            </button>
            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="p-2 text-slate-400 hover:text-slate-200 focus:outline-none"
            >
              {mobileMenuOpen ? <X size={20} /> : <Menu size={20} />}
            </button>
          </div>
        </header>

        {/* MENU MOBILE EXPANDIDO */}
        {mobileMenuOpen && (
          <div className="lg:hidden fixed inset-0 top-14 bg-slate-950 z-50 flex flex-col p-4 space-y-2 overflow-y-auto animate-fade-in border-t border-slate-900 safe-bottom">
            {menuItems.map(item => {
              const Icon = item.icon;
              const isActive = activeTab === item.id;
              return (
                <button
                  key={item.id}
                  onClick={() => handleNavigate(item.id)}
                  className={`w-full flex items-center gap-4 px-4 py-3.5 rounded-xl text-sm font-bold transition-all ${
                    isActive 
                      ? 'bg-indigo-600 text-white' 
                      : 'text-slate-400 hover:bg-slate-900'
                  }`}
                >
                  <Icon size={18} />
                  <span>{item.label}</span>
                </button>
              );
            })}
          </div>
        )}

        {/* CONTAINER DE EXIBIÇÃO DA PÁGINA */}
        <main className="flex-1 overflow-y-auto p-4 md:p-8">
          {loading && !dashboardData && activeTab === 'dashboard' ? (
            <div className="h-full flex flex-col items-center justify-center space-y-3">
              <Loader2 className="animate-spin text-indigo-500" size={32} />
              <p className="text-xs font-bold text-slate-500 uppercase tracking-widest">Carregando painel...</p>
            </div>
          ) : error && activeTab === 'dashboard' ? (
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
