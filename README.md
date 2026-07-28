# Deal Tracker Bot

Bot para Telegram que consulta jogos na Steam, registra usuários no banco e organiza a base para acompanhamento de títulos e preços. O projeto já permite iniciar o bot, pesquisar jogos e persistir dados em PostgreSQL, enquanto parte das funcionalidades de monitoramento ainda está em evolução.

## Sobre o projeto

O objetivo do Deal Tracker Bot é centralizar buscas de jogos da Steam dentro do Telegram e preparar uma base para alertas de preço e acompanhamento de promoções.

No estado atual, o projeto:

- inicia um bot Telegram com comandos básicos;
- registra usuários quando recebem o comando `/start`;
- busca jogos na Steam pelo comando `/search`;
- consulta o banco antes de chamar a API pública da Steam;
- mantém modelos e estrutura de persistência para usuários, jogos e relação de acompanhamento.

Algumas partes do domínio já aparecem no código, mas ainda não estão totalmente conectadas ao fluxo principal, como notificações automáticas e o vínculo completo entre usuário e jogos monitorados.

## Tecnologias utilizadas

- Linguagem: Python
- Bot framework: aiogram 3
- Banco de dados: PostgreSQL 17
- ORM e acesso a dados: SQLAlchemy 2
- Cliente HTTP assíncrono: httpx
- Variáveis de ambiente: python-dotenv e dotenv
- Infraestrutura: Docker e Docker Compose
- Biblioteca de PostgreSQL: psycopg2-binary
- Observação de arquivos em desenvolvimento: watchfiles
- Dependências presentes no projeto: APScheduler

## Arquitetura do projeto

O projeto segue uma organização em camadas simples:

- `bot/` concentra o bot e os handlers dos comandos do Telegram;
- `services/` contém a regra de negócio e a orquestração entre fontes de dados;
- `repositories/` acessa o banco via SQLAlchemy;
- `integrations/` concentra integrações externas, como a Steam API;
- `models/` define as entidades persistidas;
- `database/` configura engine, sessão e base declarativa;
- `config/` lê configuração e variáveis de ambiente;
- `utils/` guarda utilitários pequenos, como normalização de texto.

Fluxo geral da aplicação:

1. `main.py` carrega a configuração, cria as tabelas e inicia o bot.
2. O bot registra os routers dos comandos em `bot/handlers/`.
3. Os handlers recebem as mensagens do Telegram e chamam os serviços.
4. Os serviços decidem se a consulta será atendida pelo banco local ou pela Steam API.
5. Os repositórios persistem ou consultam os dados usando SQLAlchemy.

Boas práticas e padrões observados no código:

- separação entre integração externa, regra de negócio e acesso a dados;
- uso de sessão de banco por contexto;
- consultas centralizadas em repositórios;
- normalização simples do termo de busca antes da consulta;
- criação automática das tabelas na inicialização.

## Funcionalidades atuais

- Comando `/start` para apresentar o bot e registrar o usuário no banco.
- Comando `/search <nome do jogo>` para consultar jogos da Steam.
- Prioridade de busca no banco local antes de consultar a API externa.
- Retorno das três primeiras opções encontradas na Steam.
- Estrutura de persistência para usuários, jogos e relacionamento de acompanhamento.
- Inicialização do schema do banco ao subir a aplicação.
- Dockerização do bot e do PostgreSQL para desenvolvimento local.

## Como executar o projeto localmente

### Pré-requisitos

- Docker e Docker Compose.
- Token de bot do Telegram.

### Configuração das variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base em `.env.example`.

Variáveis usadas pelo código atual:

- `TOKEN`: token do bot do Telegram.
- `DB_URL`: string de conexão SQLAlchemy para o banco.
- `DB_NAME`: nome do banco usado pelo container PostgreSQL.
- `DB_USER`: usuário do PostgreSQL.
- `DB_PASSWORD`: senha do PostgreSQL.

Exemplo de estrutura, sem valores reais:

```env
TOKEN=
DB_URL=
DB_NAME=
DB_USER=
DB_PASSWORD=
```

### Executando com Docker

```bash
docker compose up --build
```

Essa é a forma prevista no projeto para subir tanto o bot quanto o PostgreSQL.

No ambiente de desenvolvimento, o override do Compose monta o código-fonte no container e reinicia a aplicação com `watchfiles` quando arquivos Python mudam.

## Configuração de ambiente

O projeto depende de configuração externa para funcionar corretamente:

- `.env`: contém o token do Telegram e a URL de conexão com o banco.
- `compose.yaml`: define os serviços do bot e do PostgreSQL.
- `compose.override.yaml`: ajusta o fluxo de desenvolvimento, expondo a porta do PostgreSQL e ativando reload automático do bot.
- `Dockerfile.dev`: instala as dependências Python e executa `main.py`.

O repositório já inclui `.env.example` para orientar a criação do arquivo local sem expor segredos.

## Exemplos de uso

Após iniciar o bot no Telegram:

```text
/start
```

O bot responde com uma mensagem de apresentação e registra o usuário no banco caso ele ainda não exista.

```text
/search Elden Ring
```

O bot normaliza o termo, consulta o banco e, se não houver resultado local, chama a Steam API para retornar as primeiras opções encontradas.

Observação: os botões inline exibidos no retorno da busca ainda não executam a ação completa no código atual; os callbacks apenas imprimem mensagens no console.

## Roadmap

Melhorias que aparecem como evolução natural do estado atual do projeto:

- finalizar o fluxo de seleção das opções retornadas na busca;
- persistir automaticamente jogos consultados com mais consistência;
- conectar `user_watch_games` ao fluxo principal de monitoramento;
- implementar notificações automáticas de mudança de preço;
- usar o agendador já presente nas dependências para checagens periódicas;
- melhorar mensagens de erro e validação de entrada;
- adicionar testes para serviços, repositórios e handlers.

## Contribuição

Contribuições são bem-vindas. Um fluxo simples para colaborar:

1. Faça um fork ou crie uma branch a partir da principal.
2. Instale as dependências e configure o `.env`.
3. Implemente a melhoria mantendo a separação entre handler, service e repository.
4. Teste localmente antes de abrir o pull request.
5. Explique no PR o comportamento alterado e o impacto esperado.

Ao contribuir, prefira manter o código alinhado com a estrutura atual do projeto e evite misturar regra de negócio com acesso direto ao banco nos handlers.

## Licença

Este projeto está sob licença MIT. Consulte o arquivo [LICENSE](LICENSE) para o texto completo.
