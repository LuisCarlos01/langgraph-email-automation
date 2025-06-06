# 🎨 FRONTEND\_PAINEL.md

> Documentação da interface visual (painel) para o projeto iPass - Automação de E-mails com IA

Baseada na estrutura do fork `langgraph-email-automation`, adaptada para um sistema visual com React, TailwindCSS e integração direta com o backend FastAPI.

---

## 🧭 Objetivo do Painel

Criar uma interface amigável para:

* Visualizar e-mails recebidos
* Ver e editar respostas geradas pela IA
* Cadastrar e gerenciar regras personalizadas de resposta
* Acompanhar histórico e status das automações

---

## ⚙️ Tecnologias Sugeridas

* **React + Vite** (estrutura leve e moderna)
* **TailwindCSS** (estilização rápida e responsiva)
* **Axios** (para comunicação com API)
* **React Hook Form** ou **Formik** (para formulários de regras)
* **React Router DOM** (para navegação entre páginas)
* **Framer Motion** (animações suaves)

---

## 📁 Estrutura de Pastas

```
frontend/
├── src/
│   ├── components/
│   │   ├── EmailCard.jsx
│   │   ├── RegraForm.jsx
│   │   └── RespostaItem.jsx
│   ├── pages/
│   │   ├── Inbox.jsx
│   │   ├── Regras.jsx
│   │   ├── Historico.jsx
│   │   └── Dashboard.jsx
│   ├── services/
│   │   └── api.js
│   ├── App.jsx
│   └── main.jsx
├── tailwind.config.js
├── vite.config.js
└── index.html
```

---

## 📌 Telas e Funcionalidades

### 🔹 `Inbox`

* Listagem de e-mails recebidos via API `/api/emails`
* Mostrar status (respondido ou não)
* Exibir botão para visualizar resposta gerada pela IA

### 🔹 `Regras`

* Listar regras cadastradas (`GET /api/regras`)
* Criar nova regra (`POST /api/regras`)
* Editar e deletar regras (`PUT/DELETE /api/regras/{id}`)

### 🔹 `Histórico`

* Exibir todas as respostas enviadas (`GET /api/respostas`)
* Mostrar qual regra foi usada e o conteúdo da resposta

### 🔹 `Dashboard`

* Cards com estatísticas (respostas hoje, regras ativas, e-mails não lidos)
* Atalhos para ações rápidas

---

## 🔌 Integração com a API

Exemplo de uso de `axios` com base no `.env`:

```javascript
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api',
});

export default api;
```

---

## 📝 Formulário de Regra (exemplo de estrutura)

```jsx
// RegraForm.jsx
import { useForm } from 'react-hook-form';

function RegraForm({ onSubmit, defaultValues }) {
  const { register, handleSubmit } = useForm({ defaultValues });

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register('palavra_chave')} placeholder="Palavra-chave" />
      <textarea {...register('resposta_customizada')} />
      <button type="submit">Salvar</button>
    </form>
  );
}
```

---

## ✅ Checklist de Implementação

* [ ] Criar projeto React com Vite
* [ ] Configurar TailwindCSS
* [ ] Criar estrutura de páginas e componentes
* [ ] Implementar chamadas à API (axios)
* [ ] Criar formulários para regras
* [ ] Mostrar e-mails recebidos e respostas
* [ ] Estilizar com responsividade e acessibilidade

---

> Este painel será o principal ponto de interação humana do sistema. Documentação será atualizada conforme evoluir.
