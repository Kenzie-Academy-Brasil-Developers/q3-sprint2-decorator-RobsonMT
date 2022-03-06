from decorators import verify_credentials, verify_keys, verify_username
from http import HTTPStatus
from flask import Flask

app = Flask(__name__)

# Não altere essa configuração
# Ela desabilita o sort automático dos JSONs por ordem alfabética
app.config['JSON_SORT_KEYS'] = False

# Desenvolva suas rotas abaixo
@app.post("/login")
@verify_keys(["username", "password"])
@verify_credentials()
def login():
    return HTTPStatus.OK

@app.post("/register")
@verify_keys(["username", "password"])
@verify_username()
def register():
    return HTTPStatus.CREATED