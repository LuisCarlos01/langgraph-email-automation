# Estrutura do Projeto

## 📁 Visão Geral

O iPassResponder é organizado em módulos bem definidos, seguindo princípios de Clean Architecture e separação de responsabilidades. Abaixo está a estrutura detalhada do projeto:

```
iPassResponder/
├── agents/                 # Agentes de IA
│   ├── __init__.py
│   ├── read_email.py      # Leitura de emails
│   ├── analyze_email.py   # Análise de conteúdo
│   ├── generate_response.py # Geração de respostas
│   └── send_email.py      # Envio de emails
│
├── api/                    # API REST
│   ├── __init__.py
│   ├── routes.py          # Rotas da API
│   ├── schemas.py         # Schemas Pydantic
│   └── auth_google.py     # Autenticação Google
│
├── db/                     # Camada de Dados
│   ├── __init__.py
│   ├── models.py          # Modelos SQLAlchemy
│   ├── crud.py           # Operações CRUD
│   └── database.py       # Configuração do DB
│
├── src/                    # Código Principal
│   ├── __init__.py
│   ├── prompts.py        # Templates de prompts
│   └── structure_outputs.py # Estruturas de saída
│
├── tests/                  # Testes
│   ├── __init__.py
│   ├── test_agents/      # Testes dos agentes
│   ├── test_api/        # Testes da API
│   └── test_db/         # Testes do banco
│
├── frontend/              # Interface React
│   ├── src/             # Código fonte React
│   ├── public/          # Assets públicos
│   └── package.json     # Dependências
│
├── docs/                  # Documentação
│   ├── api/             # Documentação da API
│   ├── architecture/    # Diagramas e docs
│   └── guides/          # Guias de uso
│
└── scripts/              # Scripts úteis
    ├── setup.sh         # Script de setup
    └── deploy.sh        # Script de deploy
```

## 🔍 Detalhamento dos Módulos

### 1. Agents
Contém os agentes de IA responsáveis pelo processamento de emails:
- `read_email.py`: Lê e processa emails recebidos
- `analyze_email.py`: Analisa conteúdo e categoriza emails
- `generate_response.py`: Gera respostas usando IA
- `send_email.py`: Gerencia envio de respostas

### 2. API
Interface REST para o sistema:
- `routes.py`: Define endpoints da API
- `schemas.py`: Validação de dados com Pydantic
- `auth_google.py`: Integração com Gmail API

### 3. Database
Camada de persistência:
- `models.py`: Modelos do banco de dados
- `crud.py`: Operações de banco de dados
- `database.py`: Configuração e conexão

### 4. Source
Código core do sistema:
- `prompts.py`: Templates para IA
- `structure_outputs.py`: Estruturas de dados

### 5. Tests
Testes automatizados:
- Testes unitários
- Testes de integração
- Fixtures e mocks

### 6. Frontend
Interface do usuário em React:
- Components
- Services
- State management

## 🔧 Configuração do Ambiente

### Requisitos
- Python 3.8+
- Node.js 14+
- SQLite3

### Variáveis de Ambiente
```env
MY_EMAIL=seu_email@gmail.com
GROQ_API_KEY=sua_chave_groq
GOOGLE_API_KEY=sua_chave_google
```

## 📚 Convenções de Código

### Python
- PEP 8 para estilo
- Type hints
- Docstrings Google style
- Máximo 88 caracteres/linha

### JavaScript/TypeScript
- ESLint
- Prettier
- TypeScript strict mode

## 🚀 Fluxo de Desenvolvimento

1. **Setup**
   ```bash
   # Backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

   # Frontend
   cd frontend
   npm install
   ```

2. **Desenvolvimento**
   ```bash
   # Backend
   python run_api.py

   # Frontend
   cd frontend
   npm run dev
   ```

3. **Testes**
   ```bash
   pytest
   npm test
   ```

## 📈 Monitoramento

- Logs: `logs/`
- Métricas: Prometheus/Grafana
- Tracing: OpenTelemetry

## 🔐 Segurança

- Rate limiting
- Input validation
- JWT authentication
- CORS configuration 