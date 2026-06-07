const SESSION_KEY = 'jus_session_id';

function generateId(): string {
  if (typeof crypto !== 'undefined' && crypto.randomUUID) {
    return crypto.randomUUID();
  }
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => {
    const r = Math.random() * 16 | 0;
    return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
  });
}

export function getSessionId(): string {
  let id = localStorage.getItem(SESSION_KEY);
  if (!id) {
    id = generateId();
    localStorage.setItem(SESSION_KEY, id);
  }
  return id;
}

export function apiFetch(apiBase: string, url: string, options?: RequestInit): Promise<Response> {
  const headers: Record<string, string> = {
    'X-Session-Id': getSessionId(),
  };
  if (options?.headers) {
    const existing = options.headers as Record<string, string>;
    Object.assign(headers, existing);
  }
  return fetch(`${apiBase}${url}`, { ...options, headers });
}
