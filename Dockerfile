FROM python:3.11-slim

WORKDIR /app

# Instala Node.js para build do frontend
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Instala dependências do backend
COPY backend/requirements.txt backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Instala dependências do frontend e faz o build
COPY frontend/package.json frontend/package-lock.json frontend/
RUN cd frontend && npm install
COPY frontend/ frontend/
RUN cd frontend && npm run build

# Copia o resto do backend
COPY . .

# Remove node_modules (desnecessário em produção)
RUN rm -rf frontend/node_modules

EXPOSE 8000

CMD python -m uvicorn backend.main:app --host 0.0.0.0 --port ${PORT:-8000}
