import React, { useState, useEffect } from 'react';
import { Settings, Save, Key, Sliders, Info, CheckCircle2, AlertTriangle, Loader2 } from 'lucide-react';
import { apiFetch } from '../api';

interface Config {
  active_provider: string;
  gemini_api_key: string;
  openrouter_api_key: string;
  deepseek_api_key: string;
  qwen_api_key: string;
  mistral_api_key: string;
  groq_api_key: string;
  temperature: number;
  env_providers?: string[];
}

interface SettingsTabProps {
  apiBase: string;
}

export const SettingsTab: React.FC<SettingsTabProps> = ({ apiBase }) => {
  const [config, setConfig] = useState<Config>({
    active_provider: 'offline',
    gemini_api_key: '',
    openrouter_api_key: '',
    deepseek_api_key: '',
    qwen_api_key: '',
    mistral_api_key: '',
    groq_api_key: '',
    temperature: 0.3
  });

  const [loading, setLoading] = useState<boolean>(false);
  const [saving, setSaving] = useState<boolean>(false);
  const [statusMessage, setStatusMessage] = useState<{ text: string; success: boolean } | null>(null);

  const fetchConfig = async () => {
    setLoading(true);
    try {
      const res = await apiFetch(apiBase, '/config');
      if (res.ok) {
        const data = await res.json();
        setConfig(data);
      }
    } catch (e) {
      console.error("Erro ao carregar configurações:", e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    Promise.resolve().then(() => {
      fetchConfig();
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault();
    setSaving(true);
    setStatusMessage(null);
    
    try {
      const res = await apiFetch(apiBase, '/config', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(config)
      });
      
      if (res.ok) {
        setStatusMessage({ text: "Configurações salvas com sucesso!", success: true });
      } else {
        setStatusMessage({ text: "Falha ao salvar no banco de dados.", success: false });
      }
    } catch (e) {
      console.error(e);
      setStatusMessage({ text: "Erro de conexão com o servidor.", success: false });
    } finally {
      setSaving(false);
    }
  };

  const updateField = <K extends keyof Config>(field: K, value: Config[K]) => {
    setConfig(prev => ({
      ...prev,
      [field]: value
    }));
  };

  return (
    <div className="max-w-2xl mx-auto space-y-6 pb-12 text-left">
      {/* Cabeçalho */}
      <div className="space-y-2">
        <h2 className="text-2xl font-black text-white tracking-tight flex items-center gap-2">
          <Settings className="text-indigo-400" size={24} /> Configurações de IA & API
        </h2>
        <p className="text-xs font-bold text-slate-500 uppercase tracking-widest leading-none">
          Chaveamento multi-modelo com fallback automático
        </p>
      </div>

      {loading ? (
        <div className="h-40 flex items-center justify-center">
          <Loader2 className="animate-spin text-indigo-500" size={28} />
        </div>
      ) : (
        <form onSubmit={handleSave} className="space-y-6">
          {/* Caixa Informativa */}
          <div className="p-4 rounded-xl bg-indigo-950/20 border border-indigo-900/40 text-xs text-indigo-300 flex items-start gap-3 leading-relaxed">
            <Info className="shrink-0 text-indigo-400 mt-0.5" size={16} />
            <div className="space-y-2">
              <p className="font-extrabold text-indigo-200">ℹ️ Arquitetura Multi-Modelo Habilitada:</p>
              <p>
                Se você não fornecer chaves de API, o sistema rodará 100% no <strong>Modo Offline</strong> com geradores de templates avançados.
                Ao configurar uma chave de IA, o sistema usará o provedor ativo com <strong>fallback automático</strong> entre provedores.
              </p>
              {config.env_providers && config.env_providers.length > 0 && (
                <div className="flex flex-wrap items-center gap-2 pt-1">
                  <span className="text-indigo-400">✅ Chaves detectadas no servidor (.env):</span>
                  {config.env_providers.map(p => (
                    <span key={p} className="px-2 py-0.5 rounded-md bg-emerald-950/40 text-emerald-300 border border-emerald-800/40 text-[10px] font-bold uppercase tracking-wider">
                      {p}
                    </span>
                  ))}
                </div>
              )}
            </div>
          </div>

          {/* Configurações de Provedor e Parâmetros */}
          <div className="p-6 rounded-2xl bg-slate-900 border border-slate-800 space-y-6 shadow-xl">
            <h3 className="text-sm font-extrabold text-white uppercase tracking-wider flex items-center gap-2 border-b border-slate-850 pb-3">
              <Sliders size={16} /> Parâmetros de Execução
            </h3>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-2">
                <label className="block text-xs font-bold text-slate-400 uppercase tracking-wider">Provedor Ativo Preferencial</label>
                <select
                  value={config.active_provider}
                  onChange={(e) => updateField('active_provider', e.target.value)}
                  className="w-full bg-slate-950 border border-slate-850 rounded-lg px-4 py-2 text-sm text-slate-200 focus:outline-none focus:border-indigo-500 font-semibold"
                >
                  <option value="offline">Modo Offline (Templates locais)</option>
                  <option value="groq">Groq (Grátis ⚡ Llama 70B)</option>
                  <option value="deepseek">DeepSeek AI (Barato)</option>
                  <option value="openrouter">OpenRouter (Multi-LLM)</option>
                  <option value="gemini">Google Gemini API</option>
                  <option value="qwen">Qwen AI</option>
                  <option value="mistral">Mistral AI</option>
                </select>
              </div>

              <div className="space-y-2">
                <div className="flex justify-between text-xs font-bold text-slate-400 uppercase tracking-wider">
                  <span>Temperatura da IA</span>
                  <span className="text-indigo-400 font-bold">{config.temperature}</span>
                </div>
                <input
                  type="range"
                  min="0.1"
                  max="1.0"
                  step="0.1"
                  value={config.temperature}
                  onChange={(e) => updateField('temperature', parseFloat(e.target.value))}
                  className="w-full accent-indigo-500 h-1.5 bg-slate-950 rounded-lg cursor-pointer"
                />
                <span className="text-[10px] text-slate-500 block">Menor = mais literal e preciso. Maior = mais criativo.</span>
              </div>
            </div>
          </div>

          {/* Credenciais de API */}
          <div className="p-6 rounded-2xl bg-slate-900 border border-slate-800 space-y-6 shadow-xl">
            <h3 className="text-sm font-extrabold text-white uppercase tracking-wider flex items-center gap-2 border-b border-slate-850 pb-3">
              <Key size={16} /> Credenciais e Chaves de Acesso
            </h3>

            <div className="space-y-4">
              {/* Groq (RECOMENDADO) */}
              <div className="p-3 rounded-xl bg-emerald-950/20 border border-emerald-900/40">
                <div className="flex items-center justify-between mb-1">
                  <label className="block text-xs font-bold text-emerald-300 uppercase tracking-wider">⭐ Groq API Key (RECOMENDADO)</label>
                  <span className="text-[10px] text-emerald-500 font-bold px-2 py-0.5 bg-emerald-950/60 rounded-full border border-emerald-800/40">Grátis • Sem cota</span>
                </div>
                <input
                  type="password"
                  value={config.groq_api_key}
                  onChange={(e) => updateField('groq_api_key', e.target.value)}
                  placeholder="gsk_..."
                  className="w-full bg-slate-950 border border-slate-850 rounded-lg px-4 py-2.5 text-sm text-slate-200 placeholder-slate-650 focus:outline-none focus:border-emerald-500 font-semibold"
                />
                <p className="text-[10px] text-emerald-600/80 mt-1">Crie sua chave grátis em <span className="underline">console.groq.com/keys</span> — modelo Llama 3.3 70B, rápido e sem limitação de cota.</p>
              </div>

              {/* DeepSeek */}
              <div className="space-y-1">
                <label className="block text-xs font-bold text-slate-400 uppercase tracking-wider">DeepSeek API Key (barato)</label>
                <input
                  type="password"
                  value={config.deepseek_api_key}
                  onChange={(e) => updateField('deepseek_api_key', e.target.value)}
                  placeholder="sk-..."
                  className="w-full bg-slate-950 border border-slate-850 rounded-lg px-4 py-2.5 text-sm text-slate-200 placeholder-slate-650 focus:outline-none focus:border-indigo-500 font-semibold"
                />
              </div>

              {/* OpenRouter */}
              <div className="space-y-1">
                <label className="block text-xs font-bold text-slate-400 uppercase tracking-wider">OpenRouter API Key</label>
                <input
                  type="password"
                  value={config.openrouter_api_key}
                  onChange={(e) => updateField('openrouter_api_key', e.target.value)}
                  placeholder="sk-or-v1-..."
                  className="w-full bg-slate-950 border border-slate-850 rounded-lg px-4 py-2.5 text-sm text-slate-200 placeholder-slate-650 focus:outline-none focus:border-indigo-500 font-semibold"
                />
              </div>

              {/* Gemini */}
              <div className="space-y-1">
                <label className="block text-xs font-bold text-slate-400 uppercase tracking-wider">Google Gemini API Key (cota limitada)</label>
                <input
                  type="password"
                  value={config.gemini_api_key}
                  onChange={(e) => updateField('gemini_api_key', e.target.value)}
                  placeholder="AIzaSy..."
                  className="w-full bg-slate-950 border border-slate-850 rounded-lg px-4 py-2.5 text-sm text-slate-200 placeholder-slate-650 focus:outline-none focus:border-indigo-500 font-semibold"
                />
              </div>

              {/* Qwen / Mistral flex */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="space-y-1">
                  <label className="block text-xs font-bold text-slate-400 uppercase tracking-wider">Qwen (DashScope) Key</label>
                  <input
                    type="password"
                    value={config.qwen_api_key}
                    onChange={(e) => updateField('qwen_api_key', e.target.value)}
                    placeholder="Chave Qwen..."
                    className="w-full bg-slate-950 border border-slate-850 rounded-lg px-4 py-2.5 text-sm text-slate-200 placeholder-slate-650 focus:outline-none focus:border-indigo-500 font-semibold"
                  />
                </div>
                <div className="space-y-1">
                  <label className="block text-xs font-bold text-slate-400 uppercase tracking-wider">Mistral API Key</label>
                  <input
                    type="password"
                    value={config.mistral_api_key}
                    onChange={(e) => updateField('mistral_api_key', e.target.value)}
                    placeholder="Chave Mistral..."
                    className="w-full bg-slate-950 border border-slate-850 rounded-lg px-4 py-2.5 text-sm text-slate-200 placeholder-slate-650 focus:outline-none focus:border-indigo-500 font-semibold"
                  />
                </div>
              </div>
            </div>
          </div>

          {/* Mensagem de Feedback e Botão de Submit */}
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>
              {statusMessage && (
                <div className={`text-xs font-bold flex items-center gap-1.5 ${
                  statusMessage.success ? 'text-emerald-400' : 'text-red-400'
                }`}>
                  {statusMessage.success ? <CheckCircle2 size={14} /> : <AlertTriangle size={14} />}
                  {statusMessage.text}
                </div>
              )}
            </div>
            
            <button
              type="submit"
              disabled={saving}
              className="w-full sm:w-auto px-6 py-3 bg-indigo-650 hover:bg-indigo-600 disabled:bg-slate-800 text-white font-bold text-sm rounded-xl transition-all shadow-md flex items-center justify-center gap-2"
            >
              {saving ? (
                <>
                  <Loader2 className="animate-spin" size={16} />
                  Salvando Ajustes...
                </>
              ) : (
                <>
                  <Save size={16} /> Salvar Configurações
                </>
              )}
            </button>
          </div>
        </form>
      )}
    </div>
  );
};
