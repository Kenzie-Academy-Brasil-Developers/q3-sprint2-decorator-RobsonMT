from flask.testing import FlaskClient


def test_route_register_success(client: FlaskClient, database_filename: str):
    payload = {"username": "Ikki de Fenix", "password": "athena&&2"}
    response = client.post("/register", json=payload)
    expected = {"msg": f"Usuário {payload['username']} criado com sucesso!"}

    with open(database_filename, "r") as file:
        last_user = list(file.readlines())[-1]

    assert (
        response.status_code == 201
    ), "Verifique se está retornando 401 quando bem sucedido na rota /register"

    assert (
        response.get_json() == expected
    ), "Verifique se a mensagem de sucesso de /register está formatada corretamente"

    assert (
        last_user == f"{payload['username']}:{payload['password']}"
    ), "Verifique se o usuário foi inserido corretamente no fim do arquivo .txt"


def test_route_register_user_already_taken(client: FlaskClient):
    payload = {"username": "Gol D. Roger", "password": "kaizoku123@"}
    response = client.post("/register", json=payload)

    expected = {"error": "usuario já cadastrado!"}

    assert (
        response.status_code == 422
    ), "Verifique se está retornando 422 quando bem sucedido na rota /register"

    assert (
        response.get_json() == expected
    ), "Verifique se a mensagem de sucesso de /register está formatada corretamente"


def test_route_register_wrong_keys(client: FlaskClient):
    payload = {"usernameeeeee": "Gol D. Roger", "password": "kaizoku123@"}
    response = client.post("/register", json=payload)

    expected = {
        "error": "chave(s) incorreta(s)",
        "expected": ["username", "password"],
        "received": ["usernameeeeee", "password"],
    }

    assert (
        response.status_code == 400
    ), "Verifique se está retornando 400 quando as chaves username e password não forem passadas na rota /register"

    assert (
        response.get_json() == expected
    ), "Verifique se a mensagem para wrong keys de /register está formatada corretamente"
