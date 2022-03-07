# Desenvolva sua funções auxiliares para processamento de arquivo txt aqui
from os import getenv

FILENAME = getenv("DATABASE_FILENAME")

def register_user(username: str, password: str):
    new_user = f"{username}:{password}"

    with open(FILENAME, "a", newline="") as f:
        f.write("\n")
        f.write(new_user)

    return {"msg": f"Usuário {username} criado com sucesso!"}, 201