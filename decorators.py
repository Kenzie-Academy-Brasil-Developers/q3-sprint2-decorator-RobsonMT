from functools import wraps
from http import HTTPStatus
from os import getenv
from typing import Callable
from flask import request

FILENAME = getenv("DATABASE_FILENAME")
    
def verify_keys(trusted_keys: list[str]):
    def function(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            body_keys = request.get_json().keys()
            invalid_keys = set(trusted_keys).difference(body_keys)

            try:
                if invalid_keys:
                    raise KeyError(
                        {
                            "error": "invalid_keys",
                            "expected": list(trusted_keys),
                            "received": list(body_keys),
                        }
                    )
            except KeyError as e:
                return e.args[0], HTTPStatus.BAD_REQUEST

            return func()
        return wrapper   
    return function


def verify_credentials():
    def function(func: Callable):
        @wraps(func)
        def wrapper():
            req = request.get_json()
            with open(f"./{FILENAME}", "r") as f:
                reader = f.read()
            return func()
        return wrapper   
    return function

