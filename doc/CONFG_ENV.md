Configuração de Ambiente
DATABASE_URL

Componentes da URL de conexão com o banco de dados PostgreSQL:

    Usuário e Senha:

        Para instalações locais, utilize o nome de usuário e a senha definidos durante a instalação do PostgreSQL.

        Em serviços na nuvem como AWS RDS ou Heroku, essas informações estão disponíveis no painel de controle do serviço.

    Host e Porta:

        Para bancos locais:

            host: localhost

            porta: 5432 (porta padrão do PostgreSQL)

        Para serviços em nuvem, utilize o host e porta fornecidos.

    Nome do Banco de Dados:
    Defina o nome do banco criado para seu projeto.

Configurações de E-mail para Alertas

    ALERT_EMAIL_FROM: Endereço de e-mail autorizado para envio de alertas.

    ALERT_EMAIL_TO: Endereço(s) de destino dos alertas.

SMTP

Configure os parâmetros de envio de e-mails:
Parâmetro	Descrição
SMTP_HOST	Host SMTP do serviço (ex: smtp.gmail.com)
SMTP_PORT	Porta SMTP (ex: 587 para TLS no Gmail)
SMTP_USER	Seu endereço de e-mail (ex: usuario@gmail.com)
SMTP_PASSWORD	Senha do e-mail ou senha de app (para contas com autenticação em dois fatores)
SMTP_TLS	Usar TLS? Normalmente true para serviços modernos
Configurações de Monitoramento e Alertas

    ENABLE_METRICS: Ativa/desativa a coleta de métricas (true ou false).

    METRICS_PORT: Porta onde as métricas serão expostas (escolha uma porta disponível no sistema).

    LOG_LEVEL: Define o nível de log (ex: INFO, DEBUG, WARNING, ERROR).

    ENABLE_REQUEST_LOGGING: Ativa o log de requisições HTTP.

    ENABLE_PERFORMANCE_METRICS: Ativa métricas de desempenho da aplicação.

Thresholds de Alerta

Configure os limites aceitáveis para geração de alertas com base no comportamento esperado do sistema:

    ALERT_RESPONSE_TIME_THRESHOLD:
    Tempo máximo de resposta esperado (em segundos).
    Ex: Para alertar quando uma resposta ultrapassar 5 segundos, use 5.0.

Outros thresholds podem ser definidos conforme as métricas disponíveis no seu sistema.