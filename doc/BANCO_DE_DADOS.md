# 🗃️ BANCO\_DE\_DADOS.md

> Documentação do esquema e uso do banco de dados no projeto iPass - Automação de E-mails com IA

Este documento define as tabelas, relacionamentos e práticas para armazenar e consultar dados no backend (PostgreSQL) do sistema.

---

## 🧩 Banco de Dados Utilizado

* **PostgreSQL** (relacional, robusto e com bom suporte para integração com Python)
* ORM sugerido: **SQLAlchemy** (pode usar async com `asyncpg` se necessário)

---

## 🧱 Estrutura de Tabelas

### 🔹 `emails`

Armazena os e-mails recebidos pela conta do iPass.

| Campo             | Tipo      | Descrição                         |
| ----------------- | --------- | --------------------------------- |
| id                | SERIAL    | Chave primária                    |
| remetente         | TEXT      | E-mail do remetente               |
| assunto           | TEXT      | Assunto do e-mail                 |
| corpo             | TEXT      | Corpo da mensagem                 |
| data\_recebimento | TIMESTAMP | Data e hora em que foi recebido   |
| respondido        | BOOLEAN   | Indica se o e-mail foi respondido |

---

### 🔹 `respostas`

Histórico das respostas geradas e enviadas pela IA.

| Campo           | Tipo      | Descrição                     |
| --------------- | --------- | ----------------------------- |
| id              | SERIAL    | Chave primária                |
| email\_id       | INTEGER   | Relacionado ao id do `emails` |
| corpo\_resposta | TEXT      | Texto da resposta gerada      |
| gerada\_por\_ia | BOOLEAN   | Se foi IA ou resposta manual  |
| data\_envio     | TIMESTAMP | Data e hora do envio          |

---

### 🔹 `regras`

Regras personalizadas que influenciam o comportamento da IA.

| Campo                 | Tipo    | Descrição                               |
| --------------------- | ------- | --------------------------------------- |
| id                    | SERIAL  | Chave primária                          |
| palavra\_chave        | TEXT    | Palavra usada como gatilho para a regra |
| resposta\_customizada | TEXT    | Resposta predefinida pela equipe        |
| ativo                 | BOOLEAN | Se a regra está habilitada ou não       |

---

## 🔁 Relacionamentos

* `respostas.email_id` → 🔗 `emails.id`
* Regras são independentes (mas aplicadas no processamento de e-mails)

---

## 📦 Migrações

Sugestão: usar `alembic` para controle de versão do schema

```bash
pip install alembic
alembic init migrations
```

Ou criar script inicial:

```sql
CREATE TABLE emails (
  id SERIAL PRIMARY KEY,
  remetente TEXT,
  assunto TEXT,
  corpo TEXT,
  data_recebimento TIMESTAMP,
  respondido BOOLEAN
);

CREATE TABLE respostas (
  id SERIAL PRIMARY KEY,
  email_id INTEGER REFERENCES emails(id),
  corpo_resposta TEXT,
  gerada_por_ia BOOLEAN,
  data_envio TIMESTAMP
);

CREATE TABLE regras (
  id SERIAL PRIMARY KEY,
  palavra_chave TEXT,
  resposta_customizada TEXT,
  ativo BOOLEAN
);
```

---

## ✅ Checklist de Implementação

* [ ] Criar arquivo `schema.sql` inicial
* [ ] Criar modelos SQLAlchemy para as 3 tabelas
* [ ] Configurar conexão no arquivo `database.py`
* [ ] Popular banco com dados de teste
* [ ] Usar ORM para consultar e inserir e-mails, respostas e regras

---

> Este documento será atualizado com índices, otimizações e novos relacionamentos à medida que o projeto evoluir.
