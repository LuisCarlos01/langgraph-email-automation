Perfeito, Luiz! Aqui está o conteúdo completo e formatado do arquivo `docs/INTEGRACAO_GMAIL.md`, pronto para você **copiar e colar no Cursor**:

---

````markdown
# 📬 INTEGRACAO_GMAIL.md

> Documentação para integrar o projeto do iPass com a conta do Gmail via API e autenticação OAuth2.

---

## 🔐 Por que usar o Gmail API com OAuth2?

Porque é a forma segura e oficial de acessar os e-mails da conta da empresa, garantindo que a IA possa:

- Ler mensagens da caixa de entrada
- Identificar palavras-chave
- Enviar respostas automaticamente

---

## 🛠️ Etapas para configurar no Google Cloud

### 1️⃣ Criar um projeto

1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Clique em **"Criar Projeto"**
3. Dê um nome como `ipass-automacao-email`
4. Clique em **Criar**

---

### 2️⃣ Ativar a API do Gmail

1. No menu lateral, clique em **"APIs e serviços" > "Biblioteca"**
2. Procure por **"Gmail API"**
3. Clique nela e depois em **"Ativar"**

---

### 3️⃣ Criar a tela de consentimento OAuth

1. Vá em **"APIs e serviços" > "Tela de consentimento OAuth"**
2. Tipo de usuário: **Externo**
3. Nome do app: `iPass Automação`
4. Email de suporte: seu@email.com
5. Escopos autorizados:
   - `https://www.googleapis.com/auth/gmail.readonly`
   - `https://www.googleapis.com/auth/gmail.send`
6. Usuários de teste: adicione o e-mail do iPass

---

### 4️⃣ Criar as credenciais OAuth

1. Vá em **"APIs e serviços" > "Credenciais"**
2. Clique em **"Criar credencial" > "ID do Cliente OAuth"**
3. Tipo de aplicativo: **Aplicativo para computador**
4. Nome: `ipass-gmail-integration`
5. Após salvar, copie:
   - **Client ID**
   - **Client Secret**

---

## 🔐 Configurar variáveis no `.env`

No arquivo `.env`, adicione:

```env
GMAIL_CLIENT_ID=seu_client_id_aqui
GMAIL_CLIENT_SECRET=seu_client_secret_aqui
EMAIL_USER=suporte@ipass.com.br
EMAIL_NAME=iPass Automático
````

> Essas variáveis serão usadas para autenticar e permitir que o sistema leia e envie e-mails com segurança.

---

## 🔄 Como funciona o fluxo OAuth2

1. Ao rodar o sistema pela primeira vez, ele abre um link de autenticação no navegador
2. Você autoriza o acesso à conta Gmail
3. Um **token de acesso** é gerado e salvo em disco (ex: `token.json`)
4. O sistema usa esse token para acessar os e-mails

---

## ✅ Checklist final

* [ ] Projeto criado no Google Cloud
* [ ] API do Gmail ativada
* [ ] Tela de consentimento configurada
* [ ] Credenciais copiadas para o `.env`
* [ ] Testou rodar o sistema com `python main.py` e autorizou o acesso
* [ ] Token gerado com sucesso (ver arquivo `token.json` ou pasta `data/`)

---

> Essa documentação será atualizada conforme novas credenciais, escopos ou requisitos forem exigidos pela Google.

````

