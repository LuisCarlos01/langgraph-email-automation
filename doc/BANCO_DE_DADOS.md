# 🗃️ BANCO\_DE\_DADOS.md

> Documentação do esquema e uso do banco de dados no projeto iPass - Automação de E-mails com IA

Este documento define as tabelas, relacionamentos e práticas para armazenar e consultar dados no backend (PostgreSQL) do sistema.

---

## 🧩 Banco de Dados Utilizado

* **PostgreSQL** (relacional, robusto e com bom suporte para integração com Python)
* ORM: **SQLAlchemy** com suporte assíncrono via `asyncpg`
* Migrações: **Alembic**

---

## 🧱 Estrutura de Tabelas

### 🔹 `emails`

Armazena os e-mails recebidos pela conta do iPass.

| Campo        | Tipo                | Descrição                                    |
|-------------|---------------------|----------------------------------------------|
| id          | SERIAL              | Chave primária                               |
| subject     | TEXT                | Assunto do e-mail                            |
| sender      | TEXT                | E-mail do remetente                          |
| recipient   | TEXT                | E-mail do destinatário                       |
| content     | TEXT                | Corpo da mensagem                            |
| status      | ENUM                | Status do email (PENDING, PROCESSING, COMPLETED) |
| created_at  | TIMESTAMP           | Data e hora de criação                       |
| updated_at  | TIMESTAMP           | Data e hora da última atualização            |

Índices:
- `ix_emails_id` (não único)

---

### 🔹 `responses`

Histórico das respostas geradas e enviadas pela IA.

| Campo           | Tipo      | Descrição                     |
|----------------|-----------|-------------------------------|
| id             | SERIAL    | Chave primária                |
| email_id       | INTEGER   | Relacionado ao id do `emails` |
| content        | TEXT      | Texto da resposta gerada      |
| generated_by_ai| BOOLEAN   | Se foi IA ou resposta manual  |
| created_at     | TIMESTAMP | Data e hora de criação        |

Índices:
- `ix_responses_id` (não único)

---

### 🔹 `rules`

Regras personalizadas que influenciam o comportamento da IA.

| Campo                | Tipo    | Descrição                               |
|---------------------|---------|------------------------------------------|
| id                  | SERIAL  | Chave primária                           |
| palavra_chave       | TEXT    | Palavra usada como gatilho para a regra  |
| resposta_customizada| TEXT    | Resposta predefinida pela equipe         |
| ativo               | BOOLEAN | Se a regra está habilitada ou não        |

Índices:
- `ix_rules_id` (não único)
- `ix_rules_palavra_chave` (único)

---

## 🔁 Relacionamentos

* `responses.email_id` → 🔗 `emails.id` (com CASCADE DELETE)
* `Email.responses` ← relacionamento bidirecional com `Response`
* Regras são independentes (mas aplicadas no processamento de e-mails)

---

## 📦 Migrações

Usando `alembic` para controle de versão do schema:

```bash
# Criar nova migração
cd backend/app && PYTHONPATH=/path/to/backend alembic revision --autogenerate -m "Descrição"

# Aplicar migrações
cd backend/app && PYTHONPATH=/path/to/backend alembic upgrade head
```

---

## 🔧 Configuração

O banco usa duas configurações de engine:
1. Engine Assíncrono (aplicação):
   - Driver: `asyncpg`
   - Pool de conexões configurável
   - Sessões assíncronas

2. Engine Síncrono (migrações):
   - Driver: `psycopg2`
   - Usado apenas pelo Alembic

---

## 📥 Dados de Teste

Para popular o banco com dados de teste:

```bash
# Executar o comando de seed
python -m app.cli seed
```

O seed inclui:
- Emails de exemplo com diferentes status
- Respostas automáticas e manuais
- Regras comuns de processamento

---

## ✅ Checklist de Implementação

* [x] Criar arquivo `schema.sql` inicial (substituído por migrações Alembic)
* [x] Criar modelos SQLAlchemy para as 3 tabelas
* [x] Configurar conexão no arquivo `database.py`
* [x] Popular banco com dados de teste
* [x] Usar ORM para consultar e inserir e-mails, respostas e regras

---

> Este documento será atualizado com otimizações e novos relacionamentos à medida que o projeto evoluir.
