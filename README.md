# framework-digital

An API to the challenge of framework


# Using docker

```bash
docker build --tag framework .
docker run -e -d -p 8080:8080 --name framework framework
```

![image](https://user-images.githubusercontent.com/46831966/152361392-b6101da3-7061-4cc4-b6bf-80d55707e4aa.png)


# Without docker

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

## Running

To run the project just type in the folder server

```bash
python __main__.py
```

## Swagger

To access the swagger you can use the URL localhost:8080/v1/ui

# Usage

## /auth

To use this route, you need to use Basic Auth. The credentials are:

Username: ADMIN
Password: SecretPass

## /todos and /todos/{id}

To use this route, you need to pass the x-api-key in header. This token is generated in /auth api.

## Tests

To run tests you need to install the test-requirements

```bash
pip install -r test-requirements.txt
```

Now you can run all the tests using tox:

```bash
tox integration
```
![image](https://user-images.githubusercontent.com/46831966/152357285-a5c9bb8d-3d4a-4a51-9fce-0da5ee5930de.png)

96% COVERAGE.

## Results

# Whats was asked
- [x] Utilizar algum tipo de autorização na sua API (Ex.: Bearer, Basic Auth).
- [x] Sua API deve consultar os dados utilizando a seguinte endpoint - https://jsonplaceholder.typicode.com/todos
- [x] O retorno com sucesso deve ser um JSON no formato: {"id": "", "title": ""}
- [x] O retorno com erro deve ser um JSON no formato: {"error": {"reason": "error description"}}
- [x] Toda e qualquer consulta na sua API deve gerar um log com: timestamp, retorno raw e status code (Decorator)
- [x] Código publicado no github.
- [x] Testes de integração.
  
 # What i did as a plus
- [x] Adição de chamada com possibilidade de passagem parâmetros. Exemplo: /todos?userId=1
- [x] Endpoint de get por ir. Exemplo /todos/{id}
- [x] Utilização do docker.
- [x] Utilização do tox para rodas os testes.
  

