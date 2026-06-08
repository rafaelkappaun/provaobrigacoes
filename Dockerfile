# Stage 1: Build do frontend React
FROM node:20-alpine AS frontend-builder
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# Stage 2: Backend Python
FROM python:3.11-slim
WORKDIR /app

# Copia código do backend e dependências
COPY . .
# Sobrescreve frontend/dist/ com o build real (não o cache local)
COPY --from=frontend-builder /app/dist frontend/dist

# Instala dependências do backend
RUN pip install --no-cache-dir -r backend/requirements.txt

EXPOSE 8000

CMD python -m uvicorn backend.main:app --host 0.0.0.0 --port ${PORT:-8000}
