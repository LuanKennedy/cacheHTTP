# Explorando o cache de HTTP em aplicações REST

## 1º Passo: Configurar o Ambiente

> Passo a Passo Configuração

### 1º Criar um novo repositório no GitHub para o seu projeto;

### 2º Clonar o repositório;

### 3º Instalar as dependências.

> **pip install -r requirements.txt**

OU

> **pip install flask** >**pip install cachetools**

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
     time.sleep(2)
     return [
         {"nome": "Luan Carvalho", "e-mail": "luanc7459@gmail.com"},
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

> 1º Rodar comando `python app.py` no terminal
> 2º Testar o endpoint `/users` com método `GET` para validar o cache.

<br/>

# 1º **Sem Cache**

```json
{
  "data": [
    {
      "e-mail": "luanc7459@gmail.com",
      "nome": "Luan Carvalho"
    }
  ],
  "request_time": 2
}
```

# 2 **Com Cache**

```json
{
  "dados": [
    {
      "e-mail": "luanc7459@gmail.com",
      "nome": "Luan Carvalho"
    }
  ],
  "request_time": 0.0
}
```

# Contribuição

**Luan Carvalho = Realizei todos os processos, desde a documentação até a implementação etc.**
