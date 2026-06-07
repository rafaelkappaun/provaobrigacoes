FROM python:3.11-slim

WORKDIR /app

# Instala Node.js para build do frontend
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Copia tudo primeiro
COPY . .

# Instala dependências do backend
RUN pip install --no-cache-dir -r backend/requirements.txt

# Instala dependências do frontend e faz o build
RUN cd frontend && npm install && npm run build

# Remove node_modules (desnecessário em produção)
RUN rm -rf frontend/node_modules

EXPOSE 8000

CMD python -m uvicorn backend.main:app --host 0.0.0.0 --port ${PORT:-8000}
