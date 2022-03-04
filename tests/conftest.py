from pytest import fixture, fail
from flask import Flask
from dotenv import load_dotenv
from os import getenv, system

load_dotenv(dotenv_path="tests/.env.example")

FILENAME = getenv("DATABASE_FILENAME")


def reset_database():
    with open(FILENAME, "w") as file:
        default_users = [
            "Gol D. Roger:kaizoku123@\n",
            "Kurosaki Ichigo:tensho#2022\n",
            "Minato:flash@folha",
        ]
        file.writelines(default_users)


@fixture
def database_filename():
    return FILENAME


@fixture
def app():
    try:
        return __import__("app").app
    except ModuleNotFoundError:
        fail('Verifique se o arquivo "app.py" existe na raiz do projeto')
    except AttributeError:
        fail('Verifique se a variável "app" existe dentro do arquivo "app.py"')


@fixture
def client(app: Flask):
    with app.test_client() as client:
        reset_database()
        return client


@fixture
def app_post_routes(app: Flask):
    return app.url_map.bind("", default_method="POST")
