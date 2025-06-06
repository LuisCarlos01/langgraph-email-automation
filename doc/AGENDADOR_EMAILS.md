Perfeito! Aqui está o conteúdo completo do `AGENDADOR_EMAILS.md`, salvo na lousa para você copiar e colar direto no Cursor:

---

```markdown
# ⏰ AGENDADOR_EMAILS.md

> Documentação do agendador responsável por verificar novos e-mails automaticamente e gerar respostas com IA no sistema iPass.

---

## 🎯 Objetivo

Automatizar a leitura de novos e-mails recebidos, processar com IA, aplicar regras e, se necessário, enviar respostas — tudo de forma recorrente, sem precisar rodar manualmente.

---

## 🔁 Como funciona o agendador?

1. A cada intervalo (ex: a cada 5 minutos):
   - A API do Gmail é consultada
   - Novos e-mails são buscados
   - Verifica se já foram respondidos
   - Se não foram:
     - Verifica se alguma **regra se aplica**
     - Gera uma **resposta com IA**
     - Envia o e-mail
     - Salva a resposta no banco (`respostas`)

---

## 🧱 Estrutura sugerida

Crie o arquivo:

```

scripts/agendador.py

````

---

### 🧪 Exemplo básico com `schedule`

```python
import schedule
import time
from app.services.ia_service import processar_emails

# Define a tarefa para rodar a cada X minutos
schedule.every(5).minutes.do(processar_emails)

while True:
    schedule.run_pending()
    time.sleep(1)
````

> Pode-se também usar Celery, APScheduler, cronjob ou FastAPI BackgroundTasks para produção.

---

## ⚙️ Função `processar_emails`

Essa função deve:

* Obter e-mails da conta do Gmail (via API)
* Verificar se já foram respondidos
* Verificar se alguma regra personalizada se aplica
* Gerar resposta com IA (via LangGraph)
* Enviar resposta usando Gmail API
* Salvar dados no banco

---

## 📦 Salvando respostas

Use o modelo da tabela `respostas`:

```python
resposta = Resposta(
    email_id=email.id,
    corpo_resposta=texto_gerado,
    gerada_por_ia=True,
    data_envio=datetime.now()
)
db.add(resposta)
```

---

## 🧪 Teste local

1. Crie um e-mail novo na caixa de entrada
2. Rode o script:

```bash
python scripts/agendador.py
```

3. Verifique se o sistema:

   * Identificou o e-mail
   * Aplicou alguma regra
   * Gerou resposta
   * Enviou e salvou no banco

---

## ✅ Checklist de Implementação

* [ ] Criar o arquivo `scripts/agendador.py`
* [ ] Criar função `processar_emails` no serviço de IA
* [ ] Configurar verificação recorrente com `schedule` ou equivalente
* [ ] Testar integração com o banco e Gmail API
* [ ] Documentar logs e erros futuros (extra)

---

> Esta automação é o coração do sistema — ela garante que os e-mails sejam tratados com inteligência, rapidez e sem intervenção manual.


