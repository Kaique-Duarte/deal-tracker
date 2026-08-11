# Deal Tracker Bot

O Deal Tracker Bot é um bot para Telegram desenvolvido em Python para acompanhar promoções de jogos da Steam. A proposta é simples: o usuário busca jogos, escolhe os que deseja acompanhar e recebe uma notificação quando houver desconto.

## O que a V1 faz

Nesta primeira versão, o fluxo principal já está presente:

- cadastro de usuário ao iniciar o bot;
- busca de jogos na Steam por comando de texto;
- exibição dos resultados para o usuário;
- seleção de jogos para acompanhamento via botão inline;
- monitoramento periódico dos jogos acompanhados;
- envio de notificação quando uma promoção é identificada.

## Fluxo principal

```text
/start
↓
/search <jogo>
↓
Usuário seleciona o jogo
↓
Usuário ↔ Jogo
↓
APScheduler (a cada 1 hora)
↓
Steam API
↓
Promoção encontrada?
↓
Telegram → Notificação
```

## Relacionamento usuário ↔ jogo

O acompanhamento é individual por usuário. A relação entre usuários e jogos é feita por uma tabela de associação, ou seja, um mesmo jogo pode ser acompanhado por vários usuários, e cada usuário recebe suas próprias notificações.

## Monitoramento e promoções

O monitoramento é executado pelo APScheduler a cada 1 hora. A tarefa verifica os jogos acompanhados, consulta os preços atuais na Steam e envia uma notificação ao usuário quando identifica uma promoção.

## Stack utilizada

- Python 3.14
- aiogram 3 para o bot do Telegram
- SQLAlchemy 2 para persistência e ORM
- PostgreSQL como banco de dados
- httpx para consumo da API da Steam
- APScheduler para execução de tarefas agendadas
- Docker e Docker Compose para execução em container

## Estrutura do projeto

```text
deal-tracker/
├── bot/
│   └── handlers/
├── config/
├── database/
├── exceptions/
├── integrations/
├── models/
├── repositories/
├── scheduler/
├── services/
├── utils/
├── main.py
├── requirements.txt
├── compose.yaml
├── Dockerfile.dev
└── .env.example
```

## Comandos do bot

- /start: apresenta o bot e registra o usuário.
- /search <nome do jogo>: busca jogos na Steam com base no termo informado.

Ao receber os resultados, o bot exibe botões inline para o usuário selecionar um jogo e adicioná-lo ao acompanhamento.

## Como executar

### Pré-requisitos

- Docker e Docker Compose, se for usar containers
- Python 3.14 e PostgreSQL, se for rodar localmente
- Token de um bot do Telegram

Para criar o token, abra o BotFather no Telegram, envie o comando /newbot, siga as instruções e copie o token gerado. Esse valor deve ser colocado na variável TOKEN do arquivo .env.

Para instalar o Docker, consulte a documentação oficial: https://docs.docker.com/

### Configurando o ambiente

Crie um arquivo .env na raiz do projeto com base no arquivo .env.example:

```env
TOKEN=seu_token_do_telegram
DB_URL=postgresql+psycopg2://usuario:senha@host:5432/banco
DB_NAME=nome_do_banco
DB_USER=usuario
DB_PASSWORD=senha
```

### Executando com Docker

No diretório do projeto, rode:

```bash
docker compose up --build
```

Esse comando sobe o bot e o banco PostgreSQL.

### Executando localmente

No Linux ou macOS:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

No Windows, em PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

No Windows, em CMD:

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
python main.py
```

Certifique-se de que o PostgreSQL esteja acessível pela configuração informada em DB_URL.

## Observação importante

Esta é a V1 do projeto. O fluxo principal já está funcional: usuário → busca → acompanhamento → scheduler → consulta de preço → notificação.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
