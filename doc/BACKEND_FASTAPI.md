# 🚀 BACKEND\_FASTAPI.md

> Documentação da estrutura e implementação do backend FastAPI do projeto iPass - Automação de E-mails com IA.

---

## 📁 Estrutura de Pastas (sugerida)

```
backend/
└── app/
    ├── main.py             # Ponto de entrada da aplicação FastAPI
    ├── routes/             # Rotas da API
    │   ├── regras.py
    │   └── respostas.py
    ├── models/             # Modelos Pydantic
    │   ├── regra.py
    │   └── resposta.py
    ├── services/           # Lógica de negócios
    │   ├── regra_service.py
    │   └── ia_service.py
    ├── db/                 # Conexão com o banco de dados
    │   └── database.py
    └── config.py           # Variáveis de ambiente e configurações globais
```

---

## 🌐 Endpoints Planejados

### 🔸 Regras de Resposta

| Método | Rota               | Descrição                 |
| ------ | ------------------ | ------------------------- |
| GET    | `/api/regras`      | Listar todas as regras    |
| POST   | `/api/regras`      | Criar nova regra          |
| PUT    | `/api/regras/{id}` | Atualizar regra existente |
| DELETE | `/api/regras/{id}` | Deletar regra por ID      |

### 🔸 Respostas

| Método | Rota             | Descrição                          |
| ------ | ---------------- | ---------------------------------- |
| GET    | `/api/respostas` | Listar todas as respostas enviadas |
| GET    | `/api/emails`    | Listar e-mails recebidos           |

---

## 🧱 Exemplo de Modelos (Pydantic)

```python
# models/regra.py
from pydantic import BaseModel

class RegraCreate(BaseModel):
    palavra_chave: str
    resposta_customizada: str
    ativo: bool = True

class RegraResponse(RegraCreate):
    id: int
```

---

## 🔧 Configuração Inicial do Projeto

```bash
# Entrar na pasta backend
cd backend

# Criar ambiente virtual (se não estiver usando pyenv)
python -m venv .venv
source .venv/bin/activate

# Instalar FastAPI e Uvicorn
pip install fastapi uvicorn python-dotenv psycopg2-binary

# Rodar a API
uvicorn app.main:app --reload
```

---

## 🔌 Integração com Frontend

* Usar `http://localhost:8000/api/regras` para buscar/cadastrar regras no painel
* CORS será habilitado para permitir chamadas do painel React

---

## ✅ Checklist de Implementação

* [ ] Criar estrutura de pastas do backend
* [ ] Configurar `main.py` com CORS e roteador
* [ ] Criar models Pydantic para `Regra` e `Resposta`
* [ ] Criar rotas CRUD para regras
* [ ] Integrar banco PostgreSQL (via SQLAlchemy ou asyncpg)
* [ ] Adicionar autenticação básica (JWT ou OAuth opcional)

---

> Este documento será atualizado à medida que o desenvolvimento da API avança.
