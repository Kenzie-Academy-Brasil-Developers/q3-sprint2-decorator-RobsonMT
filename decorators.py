from helpers import register_user
from functools import wraps
from typing import Callable
from flask import request
from os import getenv

FILENAME = getenv("DATABASE_FILENAME")
    
def verify_keys(trusted_keys: list[str]):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper():
            body_keys = request.get_json().keys()
            invalid_keys = set(trusted_keys) - body_keys

            try:
                if invalid_keys:
                    raise KeyError({
                            "error": "chave(s) incorreta(s)",
                            "expected": list(trusted_keys),
                            "received": list(body_keys),
                        })
                return func()
            except KeyError as e:
                return e.args[0], 400
                
        return wrapper   
    return decorator



def verify_credentials():
    def decorator(func: Callable):
        @wraps(func)
        def wrapper():
            req = request.get_json()
            log_username = req.get("username")
            log_password = req.get("password")

            with open(FILENAME, "r") as f:
                lines = f.readlines()
                for line in lines:
                    new_line = line.strip("\n").split(":")
                    username = new_line[0]
                    password = new_line[1]

                    if username == log_username and password == log_password:
                        return {"msg": f"Bem vindo {username}"}, 200
  
            return {"error": "not authorized"}, 401
        return wrapper   
    return decorator



def verify_username():
    def decorator(func: Callable):
        @wraps(func)
        def wrapper():
            req = request.get_json()
            log_username = req.get("username")
            log_password = req.get("password")
            
            with open(FILENAME, "r") as f:
                lines = f.readlines()
                for line in lines:
                    username = line.strip("\n").split(":")[0]
          
                    try:
                        if username == log_username:
                            raise NameError
                    except NameError:
                        return {"error": "usuario já cadastrado!"}, 422
                    
            return register_user(log_username, log_password)
        return wrapper   
    return decorator

