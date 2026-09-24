import React, { useState } from 'react';
import { User, Users, Smartphone, Laptop, Check, Trash2, Download, Upload, X, ShieldCheck } from 'lucide-react';
import {
  type UserProfile,
  getProfiles,
  getCurrentProfile,
  switchOrCreateProfile,
  deleteProfile,
  getLocalAnswers,
  exportUserData,
  importUserData
} from '../api';

interface UserProfileModalProps {
  isOpen: boolean;
  onClose: () => void;
  onProfileChanged: () => void;
}

export const UserProfileModal: React.FC<UserProfileModalProps> = ({ isOpen, onClose, onProfileChanged }) => {
  const [profiles, setProfiles] = useState<UserProfile[]>(getProfiles());
  const [current, setCurrent] = useState<UserProfile>(getCurrentProfile());
  const [inputName, setInputName] = useState<string>('');
  const [importJson, setImportJson] = useState<string>('');
  const [showImport, setShowImport] = useState<boolean>(false);
  const [feedback, setFeedback] = useState<string>('');

  if (!isOpen) return null;

  const handleSwitch = (nameOrCode: string) => {
    if (!nameOrCode.trim()) return;
    const updated = switchOrCreateProfile(nameOrCode);
    setCurrent(updated);
    setProfiles(getProfiles());
    setInputName('');
    setFeedback(`Perfil ativado: ${updated.name}`);
    setTimeout(() => {
      onProfileChanged();
      onClose();
    }, 800);
  };

  const handleDelete = (id: string, name: string) => {
    if (confirm(`Deseja remover o perfil de "${name}" deste dispositivo?`)) {
      const remaining = deleteProfile(id);
      setProfiles(remaining);
      setCurrent(getCurrentProfile());
      onProfileChanged();
    }
  };

  const handleExport = () => {
    const dataStr = exportUserData(current.id);
    const blob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `backup_jus_${current.code}_${new Date().toISOString().slice(0, 10)}.json`;
    link.click();
    URL.revokeObjectURL(url);
    setFeedback('Backup exportado com sucesso!');
    setTimeout(() => setFeedback(''), 3000);
  };

  const handleImportSubmit = () => {
    if (!importJson.trim()) return;
    const ok = importUserData(importJson);
    if (ok) {
      setProfiles(getProfiles());
      setCurrent(getCurrentProfile());
      setShowImport(false);
      setImportJson('');
      setFeedback('Dados importados com sucesso!');
      setTimeout(() => {
        onProfileChanged();
        onClose();
      }, 1000);
    } else {
      setFeedback('Erro: Formato de JSON inválido.');
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-sm animate-fade-in">
      <div className="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-lg shadow-2xl overflow-hidden flex flex-col max-h-[90vh]">
        {/* Header */}
        <div className="p-5 border-b border-slate-800 flex items-center justify-between bg-slate-850">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-indigo-600/20 text-indigo-400 rounded-xl border border-indigo-500/20">
              <Users size={22} />
            </div>
            <div>
              <h3 className="text-base font-bold text-white leading-tight">Alunos e Sincronização</h3>
              <p className="text-xs text-slate-400">Suas respostas salvas no Celular e Computador</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800 transition-colors"
          >
            <X size={20} />
          </button>
        </div>

        {/* Body */}
        <div className="p-5 overflow-y-auto space-y-6 flex-1 text-sm">
          {feedback && (
            <div className="p-3 bg-indigo-500/10 border border-indigo-500/30 text-indigo-300 rounded-xl text-xs font-semibold flex items-center gap-2">
              <ShieldCheck size={16} />
              <span>{feedback}</span>
            </div>
          )}

          {/* Perfil Atual Ativo */}
          <div className="p-4 bg-indigo-950/30 border border-indigo-500/30 rounded-xl flex items-center justify-between">
            <div>
              <span className="text-[11px] font-bold uppercase tracking-wider text-indigo-400">Perfil Ativo</span>
              <div className="text-lg font-black text-white flex items-center gap-2 mt-0.5">
                <User size={18} className="text-indigo-400" />
                {current.name}
              </div>
              <p className="text-xs text-slate-400 mt-1">
                ID da Sessão: <span className="font-mono text-indigo-300">{current.id}</span>
              </p>
              <p className="text-[11px] text-emerald-400 font-semibold mt-1">
                ✓ {getLocalAnswers(current.id).length} respostas gravadas neste dispositivo
              </p>
            </div>
          </div>

          {/* Dica de Sincronização Celular + Computador */}
          <div className="p-3.5 bg-slate-850 border border-slate-800 rounded-xl text-xs text-slate-300 space-y-2">
            <div className="flex items-center gap-2 font-bold text-white">
              <Laptop size={16} className="text-indigo-400" />
              <span>+</span>
              <Smartphone size={16} className="text-indigo-400" />
              <span>Como sincronizar no Celular e no Computador:</span>
            </div>
            <p className="text-slate-400 leading-relaxed">
              Basta digitar o <strong>mesmo nome ou código</strong> no seu celular e no seu computador. Todas as suas questões, estatísticas e flashcards serão compartilhados entre os seus aparelhos!
            </p>
          </div>

          {/* Alternar / Criar Novo Perfil */}
          <div className="space-y-2">
            <label className="text-xs font-bold text-slate-300 uppercase tracking-wider">
              Entrar com seu Nome ou Código:
            </label>
            <div className="flex gap-2">
              <input
                type="text"
                value={inputName}
                onChange={e => setInputName(e.target.value)}
                onKeyDown={e => e.key === 'Enter' && handleSwitch(inputName)}
                placeholder="Ex: Rafael ou rafael2026"
                className="flex-1 bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 text-sm font-medium"
              />
              <button
                onClick={() => handleSwitch(inputName)}
                disabled={!inputName.trim()}
                className="px-4 py-2.5 bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 text-white rounded-xl font-bold text-xs transition-colors shrink-0 shadow-md shadow-indigo-600/20"
              >
                Ativar Perfil
              </button>
            </div>
          </div>

          {/* Lista de Perfis Salvos neste Navegador */}
          <div className="space-y-2">
            <label className="text-xs font-bold text-slate-400 uppercase tracking-wider">
              Perfis Salvos neste Navegador / Celular:
            </label>
            <div className="space-y-1.5 max-h-40 overflow-y-auto pr-1">
              {profiles.map(p => {
                const isActive = p.id === current.id;
                const ansCount = getLocalAnswers(p.id).length;
                return (
                  <div
                    key={p.id}
                    className={`flex items-center justify-between p-2.5 rounded-xl border transition-colors ${
                      isActive
                        ? 'bg-indigo-600/15 border-indigo-500/40 text-white'
                        : 'bg-slate-950/60 border-slate-800 hover:border-slate-700 text-slate-300'
                    }`}
                  >
                    <div className="flex items-center gap-2.5 min-w-0">
                      <div className={`p-1.5 rounded-lg ${isActive ? 'bg-indigo-600 text-white' : 'bg-slate-800 text-slate-400'}`}>
                        <User size={14} />
                      </div>
                      <div className="truncate">
                        <div className="font-bold text-xs truncate">{p.name}</div>
                        <div className="text-[10px] text-slate-500">{ansCount} respostas salvas localmente</div>
                      </div>
                    </div>

                    <div className="flex items-center gap-1">
                      {!isActive && (
                        <button
                          onClick={() => handleSwitch(p.name)}
                          className="px-2.5 py-1 bg-slate-800 hover:bg-indigo-600 hover:text-white text-slate-300 rounded-lg text-[11px] font-bold transition-colors"
                        >
                          Usar
                        </button>
                      )}
                      {isActive && (
                        <span className="text-xs font-bold text-indigo-400 flex items-center gap-1 px-2">
                          <Check size={14} /> Ativo
                        </span>
                      )}
                      {profiles.length > 1 && (
                        <button
                          onClick={() => handleDelete(p.id, p.name)}
                          className="p-1.5 text-slate-500 hover:text-red-400 transition-colors"
                          title="Remover perfil"
                        >
                          <Trash2 size={13} />
                        </button>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Backup & Migração */}
          <div className="pt-2 border-t border-slate-800 flex flex-wrap gap-2">
            <button
              onClick={handleExport}
              className="flex-1 min-w-[140px] flex items-center justify-center gap-2 py-2 px-3 bg-slate-800 hover:bg-slate-750 text-slate-200 rounded-xl text-xs font-bold transition-colors"
            >
              <Download size={14} /> Exportar Backup (JSON)
            </button>
            <button
              onClick={() => setShowImport(!showImport)}
              className="flex-1 min-w-[140px] flex items-center justify-center gap-2 py-2 px-3 bg-slate-800 hover:bg-slate-750 text-slate-200 rounded-xl text-xs font-bold transition-colors"
            >
              <Upload size={14} /> Importar no Aparelho
            </button>
          </div>

          {/* Importador JSON */}
          {showImport && (
            <div className="p-3 bg-slate-950 border border-slate-800 rounded-xl space-y-2">
              <label className="text-[11px] font-bold text-slate-400">Cole o JSON do seu backup:</label>
              <textarea
                value={importJson}
                onChange={e => setImportJson(e.target.value)}
                placeholder="Cole o conteúdo do arquivo .json de backup aqui..."
                rows={3}
                className="w-full bg-slate-900 border border-slate-800 rounded-lg p-2 text-xs font-mono text-slate-200 placeholder-slate-600 focus:outline-none focus:border-indigo-500"
              />
              <button
                onClick={handleImportSubmit}
                className="w-full py-2 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg text-xs font-bold transition-colors shadow-md"
              >
                Confirmar Importação
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
