import { useState, useEffect, useCallback } from 'react';
import { LayoutDashboard, PlayCircle, Layers, BookOpen, ShieldAlert, Award, FileText, Settings, Menu, X, Flame, Loader2 } from 'lucide-react';
import { Dashboard, type DashboardData } from './components/Dashboard';
import { QuestionSession } from './components/QuestionSession';
import { FlashcardsTab } from './components/FlashcardsTab';
import { ArticleLibrary } from './components/ArticleLibrary';
import { ErrorReport } from './components/ErrorReport';
import { SimuladoSession } from './components/SimuladoSession';
import { ReportTab } from './components/ReportTab';
import { SettingsTab } from './components/SettingsTab';
import { apiFetch } from './api';

const API_BASE = import.meta.env.VITE_API_BASE || "http://127.0.0.1:8000/api";

export default function App() {
  const [activeTab, setActiveTab] = useState<string>('dashboard');
  const [dashboardData, setDashboardData] = useState<DashboardData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [mobileMenuOpen, setMobileMenuOpen] = useState<boolean>(false);
  const [extraProps, setExtraProps] = useState<Record<string, unknown>>({});

  const loadDashboard = useCallback(async () => {
    try {
      const res = await apiFetch(API_BASE, '/dashboard');
      if (res.ok) {
        const data = await res.json();
        setDashboardData(data);
      }
    } catch (e) {
      console.error("Erro de conexão com o servidor:", e);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    Promise.resolve().then(() => {
      loadDashboard();
    });
  }, [activeTab, loadDashboard]);

  const handleNavigate = (tab: string, extra: Record<string, unknown> = {}) => {
    setExtraProps(extra);
    setActiveTab(tab);
    setMobileMenuOpen(false);
  };

  const renderActiveTab = () => {
    switch (activeTab) {
      case 'dashboard':
        return dashboardData && <Dashboard data={dashboardData} onNavigate={handleNavigate} />;
      case 'estudo':
        return (
          <QuestionSession 
            apiBase={API_BASE} 
            onSessionFinished={() => handleNavigate('dashboard')} 
          />
        );
      case 'flashcards':
        return <FlashcardsTab apiBase={API_BASE} />;
      case 'artigos':
        return <ArticleLibrary apiBase={API_BASE} onNavigate={handleNavigate} />;
      case 'simulado':
        return <SimuladoSession apiBase={API_BASE} vesperaMode={!!extraProps.vespera} />;
      case 'erros':
        return <ErrorReport apiBase={API_BASE} onNavigate={handleNavigate} />;
      case 'report':
        return <ReportTab apiBase={API_BASE} onNavigate={handleNavigate} />;
      case 'settings':
        return <SettingsTab apiBase={API_BASE} />;
      default:
        return <div>Tab não encontrada</div>;
    }
  };

  const menuItems = [
    { id: 'dashboard', label: 'Painel Geral', icon: LayoutDashboard },
    { id: 'estudo', label: 'Estudo Dinâmico', icon: PlayCircle },
    { id: 'flashcards', label: 'Flashcards', icon: Layers },
    { id: 'artigos', label: 'Biblioteca de Leis', icon: BookOpen },
    { id: 'simulado', label: 'Simulados', icon: Award },
    { id: 'erros', label: 'Meus Erros', icon: ShieldAlert },
    { id: 'report', label: 'Parecer da IA', icon: FileText },
    { id: 'settings', label: 'Configurações', icon: Settings },
  ];

  return (
    <div className="flex h-screen bg-slate-950 text-slate-100 overflow-hidden font-sans">
      {/* SIDEBAR PARA DESKTOP */}
      <aside className="hidden lg:flex lg:flex-col lg:w-64 bg-slate-900 border-r border-slate-800 shrink-0">
        {/* Header Logo */}
        <div className="p-6 border-b border-slate-850 flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="p-2 bg-indigo-650 text-white rounded-xl shadow-md shadow-indigo-600/10">
              <Award size={20} />
            </div>
            <div>
              <h1 className="text-sm font-black tracking-tight text-white leading-none">JUS OBRIGAÇÕES</h1>
              <span className="text-[10px] font-extrabold text-indigo-400 tracking-wider">MASTER V1.0</span>
            </div>
          </div>
          {dashboardData && dashboardData.streak_days > 0 && (
            <div className="flex items-center gap-1 text-orange-500 font-extrabold text-xs" title="Sequência de dias estudados">
              <Flame size={16} fill="currentColor" /> {dashboardData.streak_days}
            </div>
          )}
        </div>

        {/* Links do Menu */}
        <nav className="flex-1 p-4 space-y-1.5 overflow-y-auto">
          {menuItems.map(item => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => handleNavigate(item.id)}
                className={`w-full flex items-center gap-3.5 px-4 py-3 rounded-xl text-sm font-bold transition-all duration-200 ${
                  isActive 
                    ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/15' 
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
                }`}
              >
                <Icon size={18} />
                <span>{item.label}</span>
              </button>
            );
          })}
        </nav>

        {/* Footer Sidebar */}
        <div className="p-4 border-t border-slate-850 text-center text-[10px] font-extrabold text-slate-500 tracking-wider">
          CÓDIGO CIVIL CC/02
        </div>
      </aside>

      {/* CONTEÚDO PRINCIPAL COM TOP BAR RESPONSIVA */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* TOP BAR MOBILE */}
        <header className="lg:hidden flex items-center justify-between p-4 bg-slate-900 border-b border-slate-800">
          <div className="flex items-center gap-2.5">
            <div className="p-1.5 bg-indigo-650 text-white rounded-lg">
              <Award size={16} />
            </div>
            <span className="text-xs font-black tracking-tight text-white">JUS OBRIGAÇÕES</span>
          </div>

          <div className="flex items-center gap-3">
            {dashboardData && dashboardData.streak_days > 0 && (
              <div className="flex items-center gap-1 text-orange-500 font-extrabold text-xs">
                <Flame size={14} fill="currentColor" /> {dashboardData.streak_days}
              </div>
            )}
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
          <div className="lg:hidden fixed inset-0 top-14 bg-slate-950 z-50 flex flex-col p-4 space-y-2 animate-fade-in border-t border-slate-900">
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
          {loading ? (
            <div className="h-full flex flex-col items-center justify-center space-y-3">
              <Loader2 className="animate-spin text-indigo-500" size={32} />
              <p className="text-xs font-bold text-slate-500 uppercase tracking-widest">Sincronizando estatísticas...</p>
            </div>
          ) : (
            renderActiveTab()
          )}
        </main>
      </div>
    </div>
  );
}
