# 🧠 IA\_PROMPTS.md

> Documentação sobre os prompts utilizados no projeto iPass - Automação de E-mails com IA

Este documento descreve como a IA (baseada em LangChain + LangGraph) gera respostas a partir de e-mails recebidos, utilizando prompts adaptados ao contexto do iPass.

---

## 🎯 Objetivo

* Gerar respostas automáticas, claras e contextualizadas para e-mails recebidos pela equipe do iPass.
* Utilizar regras dinâmicas personalizadas cadastradas via painel para personalizar o comportamento da IA.

---

## 🔧 Estrutura Base do Prompt

Prompt base utilizado no projeto:

```text
Você é um assistente inteligente que trabalha na equipe de atendimento da empresa iPass.

Seu papel é ler a mensagem recebida por e-mail e gerar uma resposta educada, objetiva e útil.

⚠️ Se existir uma regra associada a esse tipo de mensagem (por palavra-chave ou intenção), aplique a resposta personalizada. Caso contrário, gere uma resposta genérica cordial e útil.

Instruções:
- Sempre mantenha o tom profissional e acolhedor
- Nunca forneça informações falsas
- Use linguagem simples e direta
- Se o e-mail for confuso ou incompleto, peça mais informações de forma educada

Mensagem recebida:
"{conteudo_email}"

Resposta:
```

---

## 📌 Exemplos de Aplicação

### 🔹 Caso com Regra Aplicável

**Regra cadastrada:** Palavra-chave "boleto" → Resposta: "Segue o link para emissão da segunda via: ..."

**E-mail recebido:**

```
Bom dia, perdi o boleto de pagamento, como faço pra emitir outro?
```

**Resposta gerada:**

```
Olá! Tudo bem? 💙

Segue o link para emissão da segunda via do seu boleto: [LINK AQUI].

Se precisar de algo mais, é só responder este e-mail!
```

---

### 🔹 Caso sem Regra Aplicável

**E-mail recebido:**

```
Gostaria de saber se vocês têm suporte fora do horário comercial.
```

**Resposta gerada:**

```
Olá! 😊

Agradecemos seu contato. Nosso suporte funciona de segunda a sexta, das 08h às 18h.

Caso tenha urgência, envie sua solicitação e vamos retornar o quanto antes.
```

---

## 🧩 Personalizações Futuras

* [ ] Incluir nome do atendente/assinatura
* [ ] Adicionar histórico de conversas anteriores como contexto
* [ ] Ajustar tom de voz (formal, técnico, casual, etc.)
* [ ] Adicionar "modo treinamento" para IA testar respostas antes de enviar

---

## 📦 Local no projeto (sugestão)

```bash
utils/
├── prompts.py      # Armazena os prompts
├── regra_loader.py # Conecta regras com os prompts dinamicamente
```

---

## ✅ Checklist de Implementação

* [x] Criar prompt base adaptado à linguagem do iPass
* [ ] Criar função que aplica regra se houver
* [ ] Substituir prompt fixo por montagem dinâmica com base nas regras
* [ ] Testar com diferentes tipos de e-mail reais

---

> Este documento deve ser atualizado à medida que novos tipos de resposta e regras forem adicionadas.
