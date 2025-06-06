# 📘 Plano de Desenvolvimento - Projeto iPass: Automação de E-mails com IA

> Baseado no fork do repositório [langgraph-email-automation](https://github.com/kaymen99/langgraph-email-automation), adaptado para a realidade do sistema iPass.

---

## 🧩 1️⃣ Planejamento Inicial

### 🎯 Problema

Automatizar a leitura e resposta de e-mails recebidos pela equipe do iPass, utilizando IA para melhorar o tempo de resposta e padronizar a comunicação.

### 👥 Público-Alvo

Equipe de atendimento interno e usuários com acesso autorizado ao painel de regras e histórico de respostas.

### 📌 Escopo

* Leitura automática da caixa de entrada do Gmail
* Geração de respostas com IA (LLM via LangGraph)
* Cadastro e edição de regras personalizadas de resposta
* Painel visual com histórico e gestão de regras
* Armazenamento de e-mails e respostas em banco de dados

### ✳️ MVP (Minimum Viable Product)

* Backend FastAPI com endpoints de regras e respostas
* Integração com Gmail via OAuth2
* IA respondendo e-mails com base em regras simples
* Frontend React com Tailwind para visualizar e editar regras

### 🛠 Tecnologias

* **Backend:** FastAPI (Python)
* **IA:** LangChain + LangGraph
* **Frontend:** React + Vite + TailwindCSS
* **Banco de Dados:** PostgreSQL
* **Containerização:** Docker + Docker Compose
* **Agendamento:** CronJob ou APScheduler

---

## 📋 2️⃣ Análise de Requisitos

### Funcionais

* [ ] Listar e-mails recebidos
* [ ] Cadastrar/editar/deletar regras de resposta
* [ ] Gerar resposta automática com base na IA
* [ ] Visualizar histórico de respostas

### Não funcionais

* [ ] Segurança de autenticação OAuth com Google
* [ ] Armazenamento seguro de tokens de acesso
* [ ] Sistema modular e testável
* [ ] Logs de execução e resposta

### Endpoints Planejados (FastAPI)

| Método | Rota               | Ação                       |
| ------ | ------------------ | -------------------------- |
| GET    | `/api/emails`      | Listar e-mails lidos       |
| GET    | `/api/respostas`   | Ver histórico de respostas |
| POST   | `/api/regras`      | Criar regra personalizada  |
| GET    | `/api/regras`      | Listar regras cadastradas  |
| PUT    | `/api/regras/{id}` | Editar regra               |
| DELETE | `/api/regras/{id}` | Deletar regra              |

---

## 🧱 3️⃣ Design do Sistema

### Estrutura Modular Sugerida

```
langgraph-email-automation/
├── backend/
│   └── app/
│       ├── main.py
│       ├── models/
│       ├── routes/
│       ├── services/
│       └── config.py
├── frontend/
│   └── (React + Tailwind)
├── db/
│   └── migrations/ ou schema.sql
├── scripts/
│   └── agendador.py
├── docker-compose.yml
├── .env
└── README.md
```

### Banco de Dados (PostgreSQL)

* `emails`: assunto, remetente, corpo, data, respondido
* `respostas`: email\_id, corpo, gerada\_por\_ia, data\_envio
* `regras`: palavra\_chave, resposta\_customizada, ativo

---

## ⚙️ 4️⃣ Configuração do Ambiente

* [x] Fork realizado
* [x] Branch `ipass-integration` criada
* [x] `.env` criado e configurado
* [ ] Instalação das dependências
* [ ] Testes com `main.py`
* [ ] Criação de estrutura FastAPI
* [ ] Inicialização do painel em React

---

## 🧪 Etapas Futuras (Resumo)

1. Criar API em FastAPI com endpoints REST
2. Criar painel visual com React e consumir API
3. Adaptar prompts da IA para regras dinâmicas
4. Integrar banco PostgreSQL para armazenar e-mails e regras
5. Criar agendador para leitura automática da caixa
6. Dockerizar o projeto
7. Realizar deploy em ambiente externo
8. Monitorar com logs e métricas

---

> Este plano será atualizado conforme o desenvolvimento evoluir, mantendo a estrutura do modelo de projeto padrão definido por Luiz Carlos.
