## 1. Criando  uma Virtual Environment
1.1. Instale o Interpretador Python 3.12
- Link para 64 Bits: https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe
- Link para 32 Bits: https://www.python.org/ftp/python/3.12.0/python-3.12.0.exe

1.2. Crie uma Virtual environment:
```sh
python -m venv venv
```
-------------------------
## 2. Ativando a Virtual environment

2.1. Para ativação da Virtual environment, digite:
- Linux
```sh
source venv/bin/activate
```
- Windows
```sh
\venv\Script\activate
```
----------------------------

## 3. Subindo o container do Docker
3.1. Baixe o WSL(se não estiver instalado)
````sh
wsl --install
````
3.2. Comando para subir o container no Docker
- Container postgres
````sh
docker-compose -f docker-compose.yml up -d
````
- Caso seja necessario derrubar o container trocar "up" por "down" no comando
----------------------------
## 4. Instalando as dependências 
4.1. Para instalação das dependências, digite:
```sh
pip install -r requirements.txt
```
------------------------
## 5 Configuração banco de dados
5.1 Execute o comando a seguir no terminal para execução das migrations no seu banco de dados:
```sh
py manage.py migrate
```
------------------------
## 6 Inicie o Servidor de Desenvolvimento
6.1 Execute o comando a seguir no terminal para execução das migrations no seu banco de dados:
```sh
python manage.py runserver
```
- A API estará disponível em http://127.0.0.1:8000/
------------------------
## 7 Utilizando a API
- Obter Token de Autenticação: Faça uma requisição POST para http://127.0.0.1:8000/api/token/ com o username e password do usuário criado.
- Endpoints: Utilize uma ferramenta como o Insomnia ou Postman para testar os endpoints disponíveis (ex: GET /api/patients/, POST /api/patients/). Lembre-se de incluir o token de acesso no cabeçalho Authorization: Bearer <seu_token>.