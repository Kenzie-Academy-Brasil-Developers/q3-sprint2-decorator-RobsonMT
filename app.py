from flask import Flask, request

from decorators import verify_credentials, verify_keys

app = Flask(__name__)

# Não altere essa configuração
# Ela desabilita o sort automático dos JSONs por ordem alfabética
app.config['JSON_SORT_KEYS'] = False

# Desenvolva suas rotas abaixo
@app.post("/login")
@verify_keys(["username", "password"])
@verify_credentials()
def login():

    return "success", 200