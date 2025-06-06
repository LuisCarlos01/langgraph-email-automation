# 🗂️ ESTRUTURA_DE_PROJETO.md

> Estrutura de diretórios do projeto `iPass Email Automation`, baseada no fork original [`langgraph-email-automation`](https://github.com/LuisCarlos01/langgraph-email-automation/tree/ipass-integration) e adaptada para modularidade, escalabilidade e integração frontend + backend + IA.

---

## 🎯 Visão Geral

A estrutura atual foi pensada para preservar o núcleo da automação com IA da fork original, mas reorganizada para manter o código dividido por responsabilidade (backend, frontend, integração, documentação, deploy). Isso facilita a manutenção e o crescimento futuro do projeto.

---

## 📁 Estrutura do Projeto

```
ipass-email-automation/
├── src/                            # Base herdada da fork original
│   ├── agents.py                   # Agentes da IA
│   ├── graph.py                    # Lógica de fluxo LangGraph
│   ├── nodes.py                    # Componentes da execução dos agentes
│   ├── prompts.py                  # Prompts padrão da IA
│   ├── state.py                    # Armazena estado da conversa
│   ├── structure_output.py         # Funções auxiliares de formatação
│   ├── tools/
│   │   └── GmailTools.py           # Classe de leitura de e-mails via Gmail API
│   └── __init__.py
├── main.py                         # Script principal para execução
├── deploy_api.py                   # API básica para servir como endpoint
├── create_index.py                 # Utilitário para geração de índices
├── requirements.txt
├── .env                            # Variáveis de ambiente
│
├── backend/                        # Backend adicional com FastAPI (expansão)
│   └── app/
│       ├── api/
│       │   └── endpoints/
│       │       ├── emails.py
│       │       ├── regras.py
│       │       └── respostas.py
│       ├── core/                   # Configuração de app, ambiente, segurança
│       ├── db/
│       │   ├── models/
│       │   ├── migrations/
│       │   └── database.py
│       ├── schemas/                # Validações Pydantic
│       ├── services/               # Integrações com IA, Gmail, etc.
│       └── main.py                 # Inicializador da FastAPI
│
├── frontend/                       # Painel visual em React + Tailwind
│   └── src/
│       ├── assets/
│       ├── components/
│       ├── pages/
│       ├── routes/
│       ├── context/
│       ├── services/
│       ├── App.jsx
│       └── main.jsx
│   ├── tailwind.config.js
│   ├── vite.config.js
│   └── index.html
│
├── docker/                         # Docker e automações de deploy
│   ├── backend.dockerfile
│   ├── frontend.dockerfile
│   └── docker-compose.yml
│
├── docs/                           # Documentações modulares
│   ├── BANCO_DE_DADOS.md
│   ├── FRONTEND_PAINEL.md
│   ├── IA_PROMPTS.md
│   ├── INTEGRACAO_GMAIL.md
│   ├── DEPLOY.md
│   ├── DOCKER.md
│   └── ESTRUTURA_DE_PROJETO.md
│
├── .gitignore
├── README.md
└── LICENSE
```

---

## ✅ Justificativas da Estrutura

| Diretório      | Origem        | Finalidade                                               |
|----------------|---------------|-----------------------------------------------------------|
| `src/`         | Fork original | Contém núcleo de agentes, IA, GmailTools e fluxo LangGraph |
| `backend/`     | Novo          | Isolar nova API REST com FastAPI                         |
| `frontend/`    | Novo          | Painel visual em React para uso interno                  |
| `docker/`      | Novo          | Ambientes isolados e deploy local/prod                   |
| `docs/`        | Novo          | Toda a documentação modular do projeto                   |

---

## 🚀 Observações Finais

- A estrutura respeita o que já existe no repositório do autor, mas modulariza para permitir crescimento limpo.
- Os scripts do LangGraph continuam funcionando normalmente dentro de `src/`.
- As novas camadas (`frontend`, `backend`, `docker`) tornam o projeto escalável, testável e integrado.

> Essa estrutura poderá ser atualizada à medida que novos módulos forem adicionados (auth, cache, testes E2E, CI/CD).