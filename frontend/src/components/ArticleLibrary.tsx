import React, { useState, useEffect, useCallback } from 'react';
import { Search, ChevronDown, ChevronUp, Book, Star, AlertTriangle, Play } from 'lucide-react';
import { apiFetch } from '../api';

interface Article {
  id: string;
  number: number;
  subject: string;
  text: string;
  summary: string;
  tips: string;
  common_errors: string;
}

interface Question {
  bank: string;
  difficulty: string;
  enunciado: string;
  gabarito: string;
  article?: string;
}

interface ArticleLibraryProps {
  apiBase: string;
  onNavigate: (tab: string, extra?: Record<string, unknown>) => void;
}

export const ArticleLibrary: React.FC<ArticleLibraryProps> = ({ apiBase, onNavigate }) => {
  const [articles, setArticles] = useState<Article[]>([]);
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [expandedId, setExpandedId] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [relatedQuestions, setRelatedQuestions] = useState<{[key: string]: Question[]}>({});
  const [questionsLoading, setQuestionsLoading] = useState<{[key: string]: boolean}>({});

  const fetchArticles = useCallback(async () => {
    setLoading(true);
    try {
      const res = await apiFetch(apiBase, `/articles?query=${encodeURIComponent(searchQuery)}`);
      if (res.ok) {
        const data = await res.json();
        setArticles(data);
      }
    } catch (e) {
      console.error("Erro ao obter artigos:", e);
    } finally {
      setLoading(false);
    }
  }, [apiBase, searchQuery]);

  useEffect(() => {
    Promise.resolve().then(() => {
      fetchArticles();
    });
  }, [fetchArticles]);

  const toggleExpand = (id: string) => {
    setExpandedId(prev => (prev === id ? null : id));
  };

  return (
    <div className="max-w-3xl mx-auto space-y-6 pb-12">
      {/* Cabeçalho */}
      <div className="text-left space-y-2">
        <h2 className="text-2xl font-black text-white tracking-tight flex items-center gap-2">
          <Book className="text-indigo-400" size={24} /> Biblioteca Digital de Leis
        </h2>
        <p className="text-xs font-bold text-slate-500 uppercase tracking-widest leading-none">
          Arts. 304 a 420 do Código Civil • Adimplemento e Inadimplemento
        </p>
      </div>

      {/* Caixa de Busca */}
      <div className="relative">
        <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-500">
          <Search size={18} />
        </div>
        <input
          type="search"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          placeholder="Pesquisar por número do artigo, assunto ou palavra-chave (ex: mora, novação, sub-rogação)..."
          autoComplete="off"
          autoCorrect="off"
          autoCapitalize="off"
          spellCheck="false"
          inputMode="search"
          enterKeyHint="search"
          className="w-full bg-slate-900 border border-slate-800 rounded-xl pl-10 pr-4 py-3 text-sm font-semibold text-slate-200 placeholder-slate-500 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 shadow-md"
        />
      </div>

      {/* Listagem de Artigos */}
      {loading && articles.length === 0 ? (
        <div className="p-8 text-center text-slate-400 font-bold">Pesquisando artigos...</div>
      ) : articles.length === 0 ? (
        <div className="p-12 text-center rounded-2xl bg-slate-900 border border-slate-800 text-slate-500 space-y-2">
          <AlertTriangle size={32} className="mx-auto text-slate-600" />
          <h4 className="text-sm font-extrabold text-slate-400">Nenhum artigo encontrado!</h4>
          <p className="text-xs">Tente buscar por termos mais genéricos como 'mora', 'pagar', 'novação' ou o número do artigo.</p>
        </div>
      ) : (
        <div className="space-y-3">
          {articles.map(art => {
            const isExpanded = expandedId === art.id;
            return (
              <div 
                key={art.id}
                className={`rounded-xl border transition-all ${
                  isExpanded 
                    ? 'bg-slate-900 border-indigo-500/40 shadow-lg' 
                    : 'bg-slate-950/40 border-slate-850 hover:bg-slate-900 hover:border-slate-800'
                }`}
              >
                {/* Cabeçalho do Artigo clicável */}
                <button
                  onClick={() => toggleExpand(art.id)}
                  className="w-full p-4 flex justify-between items-center gap-4 text-left select-none focus:outline-none"
                >
                  <div className="flex items-center gap-3">
                    <span className="px-3 py-1 text-xs font-black rounded-lg bg-indigo-600/10 text-indigo-400 border border-indigo-500/20 font-mono">
                      Art. {art.number}
                    </span>
                    <span className="text-sm font-extrabold text-slate-200">{art.subject}</span>
                  </div>
                  <div className="text-slate-400">
                    {isExpanded ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
                  </div>
                </button>

                {/* Conteúdo Detalhado expandido */}
                {isExpanded && (
                  <div className="px-4 pb-5 border-t border-slate-850 pt-4 space-y-4 text-left text-sm leading-relaxed animate-fade-in">
                    {/* Texto Legal */}
                    <div className="space-y-1">
                      <h5 className="text-[10px] font-black tracking-widest text-indigo-400 uppercase">Texto Oficial da Lei</h5>
                      <div className="p-3 bg-slate-950 rounded-lg text-slate-100 font-medium font-serif border border-slate-850">
                        {art.text}
                      </div>
                    </div>

                    {/* Grid com Dicas e Erros */}
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      {/* Resumo Simplificado */}
                      <div className="space-y-1 bg-slate-950/40 p-4 rounded-lg border border-slate-850">
                        <h5 className="text-[10px] font-black tracking-widest text-indigo-400 uppercase flex items-center gap-1.5">
                          <Book size={12} /> Resumo em 30 segundos
                        </h5>
                        <p className="text-xs font-semibold text-slate-300 leading-snug">{art.summary}</p>
                      </div>

                      {/* Dicas de Prova */}
                      <div className="space-y-1 bg-slate-950/40 p-4 rounded-lg border border-slate-850">
                        <h5 className="text-[10px] font-black tracking-widest text-emerald-400 uppercase flex items-center gap-1.5">
                          <Star size={12} /> Dicas de Prova
                        </h5>
                        <p className="text-xs font-semibold text-slate-300 leading-snug">{art.tips}</p>
                      </div>
                    </div>

                    {/* Erros Comuns */}
                    <div className="p-4 bg-red-950/10 border border-red-900/40 rounded-lg space-y-1">
                      <h5 className="text-[10px] font-black tracking-widest text-red-400 uppercase flex items-center gap-1.5">
                        <AlertTriangle size={12} /> Erros Comuns em Provas
                      </h5>
                      <p className="text-xs font-semibold text-red-200/90 leading-snug">{art.common_errors}</p>
                    </div>

                    {/* Questões Relacionadas */}
                    <div className="p-4 bg-indigo-950/10 border border-indigo-900/40 rounded-lg space-y-2">
                      <div className="flex items-center justify-between">
                        <h5 className="text-[10px] font-black tracking-widest text-indigo-400 uppercase flex items-center gap-1.5">
                          <Play size={12} /> Questões Relacionadas
                        </h5>
                        <button
                          onClick={async () => {
                            const artId = art.id.replace('art_', '');
                            setQuestionsLoading(prev => ({ ...prev, [art.id]: true }));
                            try {
                              const res = await apiFetch(apiBase, `/articles?related=${artId}`);
                              if (res.ok) {
                                const data = await res.json();
                                setRelatedQuestions(prev => ({ ...prev, [art.id]: data.questions || [] }));
                              }
                            } catch (e) {
                              console.error(e);
                            } finally {
                              setQuestionsLoading(prev => ({ ...prev, [art.id]: false }));
                            }
                          }}
                          className="px-3 py-1 bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-[10px] rounded-lg transition-all"
                        >
                          {questionsLoading[art.id] ? 'Carregando...' : 'Gerar Questões'}
                        </button>
                      </div>
                      {relatedQuestions[art.id] && relatedQuestions[art.id].length > 0 && (
                        <div className="space-y-2 max-h-60 overflow-y-auto">
                          {relatedQuestions[art.id].map((q, i) => (
                            <div key={i} className="p-2 bg-slate-950 rounded-lg border border-slate-800 text-left">
                              <div className="flex items-center gap-1 mb-1">
                                <span className="px-1.5 py-0.5 text-[8px] font-black bg-indigo-900/50 text-indigo-400 rounded">{q.bank}</span>
                                <span className="text-[8px] text-slate-500">{q.difficulty}</span>
                              </div>
                              <p className="text-[10px] font-semibold text-slate-200 leading-snug line-clamp-2">{q.enunciado}</p>
                              <p className="text-[8px] text-emerald-400 font-bold mt-1">Gabarito: {q.gabarito} • {q.article}</p>
                            </div>
                          ))}
                        </div>
                      )}
                    </div>

                    {/* Botão para Estudar Tema */}
                    <div className="flex justify-end pt-2">
                      <button
                        onClick={() => onNavigate('estudo', { subject: art.subject })}
                        className="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs rounded-lg transition-all flex items-center gap-1.5 shadow-md shadow-indigo-600/10"
                      >
                        <Play size={12} fill="currentColor" /> Praticar Questões do Tema
                      </button>
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
