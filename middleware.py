# Python Decorator functions that act like middleware
from functools import wraps
from flask import request
from rich import print as rprint # https://rich.readthedocs.io/en/stable/introduction.html


def megan(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        rprint(f"[bold blue]Incoming {request.remote_addr} {request.method} request to {request.path}[/bold blue]")
    
        if(request.data):
            try:
                req_body = request.get_json()
                rprint(f"[bold yellow] Incoming JSON: {req_body}")
            except:
                rprint(f"[bold red] Invalid JSON: {request.data}")

        if(request.form):
            rprint(f"[bold yellow] Incoming HTML Form : {request.form}")

        return f(*args, **kwargs)

    return wrapper

