// Gerenciador de Sessão, Multi-Usuários e Armazenamento Local Persistente

export interface UserProfile {
  id: string;        // ID enviado no X-Session-Id (ex: 'user_rafael')
  name: string;      // Nome visível (ex: 'Rafael')
  code: string;      // Código ou nome de sincronização
  createdAt: number;
  lastActive: number;
}

export interface LocalAnswerRecord {
  id: string;
  questionId: string;
  subject: string;
  bank?: string;
  difficulty?: string;
  selectedOption: string;
  gabarito: string;
  isCorrect: boolean;
  responseTime: number;
  timestamp: number;
  enunciado?: string;
}

const STORAGE_PROFILES_KEY = 'jus_profiles_list';
const STORAGE_ACTIVE_PROFILE_KEY = 'jus_active_profile_id';
const LEGACY_SESSION_KEY = 'jus_session_id';

function sanitizeSlug(input: string): string {
  const clean = input
    .trim()
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "") // remove acentos
    .replace(/[^a-z0-9_-]/g, "_")    // apenas letras, numeros e _
    .replace(/_+/g, "_")
    .slice(0, 32);
  return clean || 'aluno';
}

function generateShortId(): string {
  return Math.random().toString(36).substring(2, 9);
}

// Inicializa ou recupera os perfis disponíveis neste navegador/celular
export function getProfiles(): UserProfile[] {
  try {
    const raw = localStorage.getItem(STORAGE_PROFILES_KEY);
    if (raw) {
      const list = JSON.parse(raw);
      if (Array.isArray(list) && list.length > 0) return list;
    }
  } catch (e) {
    console.warn("Erro ao ler perfis do localStorage:", e);
  }

  // Se não existir, migra da sessão legada ou cria padrão
  let defaultId = 'user_estudante';
  try {
    const legacy = localStorage.getItem(LEGACY_SESSION_KEY);
    if (legacy && legacy.length > 5) {
      defaultId = legacy.startsWith('user_') ? legacy : `user_${sanitizeSlug(legacy)}`;
    }
  } catch {
    // fallback
  }

  const initialProfile: UserProfile = {
    id: defaultId.slice(0, 45),
    name: 'Estudante 1',
    code: 'estudante1',
    createdAt: Date.now(),
    lastActive: Date.now(),
  };

  saveProfiles([initialProfile]);
  setActiveProfileId(initialProfile.id);
  return [initialProfile];
}

export function saveProfiles(profiles: UserProfile[]): void {
  try {
    localStorage.setItem(STORAGE_PROFILES_KEY, JSON.stringify(profiles));
  } catch (e) {
    console.warn("Não foi possível salvar perfis no localStorage:", e);
  }
}

export function getCurrentProfile(): UserProfile {
  const profiles = getProfiles();
  let activeId: string | null = null;
  try {
    activeId = localStorage.getItem(STORAGE_ACTIVE_PROFILE_KEY);
  } catch {
    // fallback
  }

  const found = profiles.find(p => p.id === activeId);
  if (found) {
    found.lastActive = Date.now();
    return found;
  }
  return profiles[0];
}

export function setActiveProfileId(id: string): void {
  try {
    localStorage.setItem(STORAGE_ACTIVE_PROFILE_KEY, id);
    localStorage.setItem(LEGACY_SESSION_KEY, id);
  } catch {
    // fallback
  }
  // Notifica o React para recarregar dados do perfil
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new CustomEvent('jus_profile_changed', { detail: { profileId: id } }));
  }
}

// Cria ou seleciona um perfil por Nome/Código (ex: 'Rafael', 'Mariana')
export function switchOrCreateProfile(nameOrCode: string): UserProfile {
  const trimmed = nameOrCode.trim();
  if (!trimmed) return getCurrentProfile();

  const slug = sanitizeSlug(trimmed);
  const targetId = `user_${slug}`.slice(0, 45);

  const profiles = getProfiles();
  const existing = profiles.find(p => p.id === targetId || p.name.toLowerCase() === trimmed.toLowerCase() || p.code.toLowerCase() === slug);

  if (existing) {
    existing.lastActive = Date.now();
    saveProfiles(profiles);
    setActiveProfileId(existing.id);
    return existing;
  }

  // Novo perfil
  const newProfile: UserProfile = {
    id: targetId,
    name: trimmed,
    code: slug,
    createdAt: Date.now(),
    lastActive: Date.now(),
  };

  profiles.push(newProfile);
  saveProfiles(profiles);
  setActiveProfileId(newProfile.id);
  return newProfile;
}

export function deleteProfile(profileId: string): UserProfile[] {
  let profiles = getProfiles();
  if (profiles.length <= 1) {
    return profiles; // não deleta o último
  }
  profiles = profiles.filter(p => p.id !== profileId);
  saveProfiles(profiles);
  const current = getCurrentProfile();
  if (current.id === profileId) {
    setActiveProfileId(profiles[0].id);
  }
  return profiles;
}

// Session ID usado no header X-Session-Id
export function getSessionId(): string {
  return getCurrentProfile().id;
}

// --- PERSISTÊNCIA LOCAL DE RESPOSTAS (OFFLINE + BROWSER/MOBILE BACKUP) ---
export function saveLocalAnswer(record: Omit<LocalAnswerRecord, 'id' | 'timestamp'>): void {
  const profile = getCurrentProfile();
  const key = `jus_answers_${profile.id}`;
  try {
    const listRaw = localStorage.getItem(key);
    const list: LocalAnswerRecord[] = listRaw ? JSON.parse(listRaw) : [];
    
    // Evita duplicata imediata
    const exists = list.some(item => item.questionId === record.questionId);
    if (!exists) {
      list.push({
        ...record,
        id: `ans_${generateShortId()}_${Date.now()}`,
        timestamp: Date.now()
      });
      // Mantém últimas 1000 respostas para não estourar storage
      if (list.length > 1000) list.shift();
      localStorage.setItem(key, JSON.stringify(list));
    }
  } catch (e) {
    console.warn("Erro ao salvar resposta no armazenamento local:", e);
  }
}

export function getLocalAnswers(profileId?: string): LocalAnswerRecord[] {
  const pId = profileId || getCurrentProfile().id;
  try {
    const listRaw = localStorage.getItem(`jus_answers_${pId}`);
    return listRaw ? JSON.parse(listRaw) : [];
  } catch {
    return [];
  }
}

// Exporta todos os dados do aluno atual como JSON para backup ou migração
export function exportUserData(profileId?: string): string {
  const pId = profileId || getCurrentProfile().id;
  const profile = getProfiles().find(p => p.id === pId) || getCurrentProfile();
  const answers = getLocalAnswers(pId);
  
  const payload = {
    version: '1.0',
    exportDate: new Date().toISOString(),
    profile,
    answers,
  };
  return JSON.stringify(payload, null, 2);
}

// Importa backup de outro celular ou navegador
export function importUserData(jsonStr: string): boolean {
  try {
    const data = JSON.parse(jsonStr);
    if (!data.profile || !data.profile.name) return false;

    const importedProfile = switchOrCreateProfile(data.profile.name);
    if (Array.isArray(data.answers)) {
      const key = `jus_answers_${importedProfile.id}`;
      localStorage.setItem(key, JSON.stringify(data.answers));
    }
    return true;
  } catch (e) {
    console.error("Falha ao importar dados do usuário:", e);
    return false;
  }
}

// --- CHAMADAS API COM TIMEOUT E SESSÃO ---
const FETCH_TIMEOUT = 30_000;

export function apiFetch(apiBase: string, url: string, options?: RequestInit): Promise<Response> {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), FETCH_TIMEOUT);

  const headers: Record<string, string> = {
    'X-Session-Id': getSessionId(),
  };
  if (options?.headers) {
    const existing = options.headers as Record<string, string>;
    Object.assign(headers, existing);
  }

  const signal = options?.signal ? anySignal(options.signal, controller.signal) : controller.signal;

  return fetch(`${apiBase}${url}`, { ...options, headers, signal })
    .finally(() => clearTimeout(timeoutId));
}

function anySignal(...signals: AbortSignal[]): AbortSignal {
  const controller = new AbortController();
  for (const s of signals) {
    if (s.aborted) { controller.abort(s.reason); return controller.signal; }
    s.addEventListener('abort', () => controller.abort(s.reason), { once: true });
  }
  return controller.signal;
}
