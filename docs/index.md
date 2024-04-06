# Explorando o cache de HTTP em aplicações REST

## 1º Passo: Configurar o Ambiente

**Passo a Passo: Configuração**

- 1º Criar um novo repositório no GitHub para o seu projeto;

- 2º Clonar o repositório;

- 3º Instalar as dependências.

> **pip install -r requirements.txt**

OU

> **pip install flask** <br/>

> **pip install cachetools**

## 2º Codificação

1. **Criar arquivo `app.py`**

```python
 from cachetools import TTLCache
 from flask import Flask, jsonify
 import time

 cache = TTLCache(maxsize=100, ttl=30)
 app = Flask(__name__)


 def database_mock():
     "Simula uma requisição demorada ao banco de dados."
     time.sleep(3)
     return [
         {"nome": "Luan Carvalho", "email": "luanc7459@gmail.com"},
         {"nome":"teste", "email": "teste@gmail.com" }
     ]


 @app.route("/users")
 def get_users_route():
     start_request = time.time()
     data = cache.get("users")

     if data is None:
         data = database_mock()
         cache["users"] = data

     response_time = time.time() - start_request
     return jsonify({"dados": data, "tempo_de_resposta": response_time})


 if __name__ == "__main__":
     app.run(debug=True)


```

# **3ºExecutar aplicação**

> 1º Rodar comando `python app.py` no terminal;
> <br/>

> 2º Testar o endpoint `/users` com método `GET` para validar o cache.

<br/>

# 1º **Sem Cache**

```json
{
  "data": [
    {
      "email": "luanc7459@gmail.com",
      "nome": "Luan Carvalho"
    },
    {
      "email": "teste@gmail.com",
      "nome": "teste"
    }
  ],
  "request_time": 3
}
```

# 2º **Com Cache**

```json
{
  "dados": [
    {
      "email": "luanc7459@gmail.com",
      "nome": "Luan Carvalho"
    },
    {
      "email": "teste@gmail.com",
      "nome": "Joaquim Gomes"
    }
  ],
  "request_time": 0.0
}
```

> Nota-se que com cache a requisição fica mais rápida, pois é utilizada uma resposta associada a uma solicitação e reutiliza a resposta armazenada para solicitações subsequentes.

# Contribuição

**Luan Carvalho = Realizei todos os processos, desde a documentação até a implementação etc.**
