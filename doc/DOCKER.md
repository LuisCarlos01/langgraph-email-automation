Perfeito! Aqui está a documentação completa e detalhada para o uso do **Docker no seu projeto**, formatada como `docs/DOCKER.md`, seguindo o mesmo padrão das demais documentações e adaptada à estrutura do seu fork com backend + frontend + agendador + banco de dados.

---

```markdown
# 🐳 DOCKER.md

> Guia técnico para configurar, construir e executar o projeto iPass com Docker, usando containers para backend, frontend e banco de dados.

---

## 🎯 Objetivo

Empacotar toda a aplicação em containers com Docker, facilitando o desenvolvimento local e o deploy em produção, com consistência e isolamento de ambiente.

---

## 📦 Estrutura esperada do projeto

```
langgraph-email-automation/
├── backend/
│   └── app/
│       └── main.py, routes/, models/, services/, config.py
├── frontend/
│   └── painel em React + Tailwind
├── scripts/
│   └── agendador.py
├── db/
├── docs/
├── .env
├── docker-compose.yml
├── Dockerfile.backend
├── Dockerfile.frontend
```

---

## 🛠️ Dockerfile - Backend

Crie o arquivo `Dockerfile.backend` na raiz:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 🛠️ Dockerfile - Frontend (React + Vite)

Crie o arquivo `Dockerfile.frontend` na raiz:

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

## 🧩 docker-compose.yml

Crie o arquivo `docker-compose.yml` na raiz:

```yaml
version: "3.9"

services:
  backend:
    build:
      context: .
      dockerfile: Dockerfile.backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
    env_file:
      - .env

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

## 🧪 Rodando o projeto

No terminal, execute:

```bash
docker-compose up --build
```

Acesse:
- Backend FastAPI: http://localhost:8000/docs
- Frontend React: http://localhost:5173
- PostgreSQL: porta `5432` (via PGAdmin ou Beekeeper)

---

## 🧹 Comandos úteis

| Ação                        | Comando                         |
|-----------------------------|----------------------------------|
| Parar todos os serviços     | `docker-compose down`           |
| Forçar rebuild              | `docker-compose up --build`     |
| Acessar container backend   | `docker exec -it <id> bash`     |
| Limpar tudo                 | `docker system prune -a`        |

---

## ✅ Checklist de configuração

- [ ] Criou os arquivos `Dockerfile.backend` e `Dockerfile.frontend`
- [ ] Criou `docker-compose.yml`
- [ ] Adicionou variáveis no `.env`
- [ ] Testou local com `docker-compose up`
- [ ] Backend e frontend acessíveis via navegador
- [ ] Banco de dados persistente e funcional

---

> Esta documentação será atualizada caso o projeto use Celery, Redis, ou qualquer outro serviço no futuro.
```
