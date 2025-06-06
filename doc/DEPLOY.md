Perfeito, Luiz! Aqui está o conteúdo completo do `DEPLOY.md`, totalmente adaptado ao seu projeto baseado no fork, com foco em deploy local e produção com Docker. Pronto para ser colado no Cursor:

---

```markdown
# 🚀 DEPLOY.md

> Guia completo para preparar, empacotar e publicar o projeto iPass - Automação de E-mails com IA, usando Docker e boas práticas de produção.

---

## 🧱 Estrutura base do projeto

Para o deploy funcionar bem, o projeto deve seguir uma organização clara:

```

langgraph-email-automation/
├── backend/
│   └── app/
│       ├── main.py
│       ├── routes/
│       ├── services/
│       ├── models/
│       └── config.py
├── frontend/
│   └── (painel React + Tailwind)
├── scripts/
│   └── agendador.py
├── db/
│   └── schema.sql
├── docs/
├── .env
├── docker-compose.yml
├── Dockerfile.backend
├── Dockerfile.frontend

````

---

## 🐳 Configurando o Docker

### 🔹 `Dockerfile.backend`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
````

### 🔹 `Dockerfile.frontend` (React com Vite)

```dockerfile
FROM node:20

WORKDIR /app

COPY frontend/package.json frontend/pnpm-lock.yaml ./
RUN npm install -g pnpm && pnpm install

COPY frontend/ ./
RUN pnpm build

CMD ["pnpm", "preview", "--host"]
```

---

## 🧩 `docker-compose.yml`

```yaml
version: "3.9"

services:
  backend:
    build:
      context: .
      dockerfile: Dockerfile.backend
    ports:
      - "8000:8000"
    env_file:
      - .env
    volumes:
      - ./backend:/app

  frontend:
    build:
      context: .
      dockerfile: Dockerfile.frontend
    ports:
      - "5173:4173"
    volumes:
      - ./frontend:/app

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: ipass
      POSTGRES_USER: ipass_user
      POSTGRES_PASSWORD: ipass123
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

---

## ✅ Checklist de Deploy Local com Docker

* [ ] Criar os dois `Dockerfile` (`backend` e `frontend`)
* [ ] Configurar `.env` com variáveis reais
* [ ] Rodar:

  ```bash
  docker-compose up --build
  ```
* [ ] Acessar:

  * Backend: `http://localhost:8000`
  * Frontend: `http://localhost:5173`
* [ ] Validar funcionamento da API, painel e leitura de e-mails

---

## ☁️ Sugestões para Deploy em Produção

* 🔒 Adicionar variáveis seguras com `.env.production`
* ☁️ Usar serviços como:

  * **Render.com**
  * **Railway.app**
  * **Fly.io**
  * **VPS com Docker**
* 🧠 Monitorar com:

  * Logs: Logtail, Loki, Grafana
  * Erros: Sentry
  * E-mails: Logs do Gmail API (se necessário)

---

> Esse documento será atualizado conforme o deploy for testado em ambientes reais.

````



