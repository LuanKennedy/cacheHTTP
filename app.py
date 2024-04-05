from cachetools import TTLCache
from flask import Flask, jsonify
import time

cache = TTLCache(maxsize=100, ttl=30)
app = Flask(__name__)

def database_mock():
    "Simula uma requisição demorada ao banco de dados."
    time.sleep(5)
    return [
        {"nome": "Luan Carvalho", "email": "luanc7459@gmail.com"},
        {"nome":"teste", "email": "teste@gmail.com" }
    ]

@app.route("/users")
def get_users_route():
    start_request = time.time()
    data = cache.get("users")

    if data is None:
        data =database_mock()
        cache["users"] = data

    response_time = time.time() - start_request
    return jsonify({"dados": data, "tempo_de_resposta": response_time})

if __name__ == "__main__":
    app.run(debug=True)
