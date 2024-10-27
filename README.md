# API de Versionamento de Sistema

Esta API fornece um sistema simples para gerenciar o versionamento de um sistema, permitindo incrementar a versão e registrar o usuário que solicitou a mudança, assim como a data dessa solicitação. 

## Descrição

A API expõe dois endpoints:

* **GET /version:** Retorna a versão atual do sistema. Caso não tenha nenhuma versão salva no banco de dados, retorna "0.0.0".
* **POST /version:** Incrementa a versão do sistema e registra o email do usuário que solicitou a alteração.

A versão é armazenada no banco de dados e incrementada seguindo o padrão Major.Minor.Patch (ex: 0.0.1, 0.1.0, 1.0.0).

## Informações Técnicas

* **Linguagem:** Python 3.11 
* **Framework:** FastAPI
* **Banco de Dados:** PostgreSQL 16
* **Bibliotecas:**
    - FastAPI: `pip install fastapi==0.115.2` 
    - Uvicorn: `pip install uvicorn==0.32.0` 
    - SQLAlchemy: `pip install sqlalchemy==2.0.36` 
    - Psycopg2: `pip install psycopg2-binary==2.9.10` 
    - Pydantic: `pip install pydantic==2.9.2`

## Pré-requisitos

Antes de começar, certifique-se de que você tem os seguintes pré-requisitos instalados e configurados:

* **Python 3.11:**
   - A API é desenvolvida em Python, então você precisa ter a versão 3.11 ou superior instalada. Você pode baixar o Python no site oficial: [python.org](https://www.python.org/downloads/).

* **PostgreSQL:**
   - Um banco de dados PostgreSQL deve estar instalado e rodando. Você pode baixar e instalar o PostgreSQL em: [postgresql.org](https://www.postgresql.org/download/).
   - Após a instalação, crie um banco de dados chamado `system_info` que será utilizado pela API.
 
## Instalação

1. **Clone o repositório:**
   ```bash
   git clone <https://github.com/gabrieellyf/desafio-endpoints.git>

### Instale as dependências:

```pip install -r requirements.txt```

### Crie o arquivo requirements.txt na raiz do projeto listando as dependências e suas versões. Exemplo:

fastapi
uvicorn
sqlalchemy
psycopg2-binary
pydantic

### Configure o banco de dados:

Crie um banco de dados PostgreSQL com o nome `system_info`.
Configure as credenciais de acesso ao banco de dados no arquivo database.py.

* Execução
  - Navegue até o diretório src: ```cd src```

* Execute o servidor: ```uvicorn main:app --reload```
  - A API estará disponível em http://127.0.0.1:8000. A documentação interativa estará acessível em http://127.0.0.1:8000/docs.

## Uso com Postman

Para interagir com a API, utilize o Postman ou uma ferramenta similar.

### Obter a versão atual:

* Abra o Postman.
* Selecione o método GET.
* Insira a URL http://127.0.0.1:8000/version.
* Clique em "Send".

### Incrementar a versão:

* Abra o Postman.
* Selecione o método POST.
* Insira a URL http://127.0.0.1:8000/version.
* Na aba "Body", selecione "raw" e "JSON".
* Insira o seguinte JSON:
```json
{
  "user_email": "seu_email@example.com"
}
```
* Clique em "Send".

Alternativamente, você pode usar a documentação interativa da API em http://127.0.0.1:8000/docs para testar os endpoints.
