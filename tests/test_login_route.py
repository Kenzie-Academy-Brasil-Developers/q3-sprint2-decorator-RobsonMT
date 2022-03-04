from flask.testing import FlaskClient


def test_route_login_success(client: FlaskClient):
    payload = {"username": "Gol D. Roger", "password": "kaizoku123@"}
    response = client.post("/login", json=payload)

    expected = {"msg": f"Bem vindo {payload['username']}"}

    assert (
        response.status_code == 200
    ), "Verifique se está retornando 200 quando bem sucedido na rota /login"

    assert (
        response.get_json() == expected
    ), "Verifique se a mensagem de sucesso de /login está formatada corretamente"


def test_route_login_unauthorized(client: FlaskClient):
    payload = {"username": "Gol D. Rogerr", "password": "kaizoku123@"}
    response = client.post("/login", json=payload)

    expected = {"error": "not authorized"}

    assert (
        response.status_code == 401
    ), "Verifique se está retornando 401 quando não autorizado na rota /login"

    assert (
        response.get_json() == expected
    ), "Verifique se a mensagem 'not authorized' de /login está formatada corretamente"


def test_route_login_wrong_keys(client: FlaskClient):
    payload = {"usernameeeeee": "Gol D. Roger", "password": "kaizoku123@"}
    response = client.post("/login", json=payload)

    expected = {
        "error": "chave(s) incorreta(s)",
        "expected": ["username", "password"],
        "received": ["usernameeeeee", "password"],
    }

    assert (
        response.status_code == 400
    ), "Verifique se está retornando 400 quando as chaves username e password não forem passadas na rota /login"

    assert (
        response.get_json() == expected
    ), "Verifique se a mensagem para wrong keys de /login está formatada corretamente"
