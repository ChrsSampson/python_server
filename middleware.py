# Python Decorator functions that act like middleware
from functools import wraps
from flask import request
from rich import print as rprint # https://rich.readthedocs.io/en/stable/introduction.html
from db.userModel import User

def megan(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        rprint(f"[bold blue]Incoming {request.remote_addr} {request.method} request to {request.path}[/bold blue]")
    
        if(request.headers.get('session')):
            rprint(f"[bold yellow] Incoming Session: {request.headers.get('session')}")

        if(request.data):
            try:
                req_body = request.get_json()
                rprint(f"[bold yellow] Incoming JSON: {req_body}")
            except:
                rprint(f"[bold red] Invalid JSON Detected: {request.data}")

        if(request.form):
            rprint(f"[bold yellow] Incoming HTML Form : {request.form}")

        return f(*args, **kwargs)

    return wrapper

def require_login(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        currentSession = request.headers.get('session')
        if(currentSession):
            user = User.query.filter_by(session=currentSession).one_or_none()
            if(user):
                return f(*args, **kwargs)
            else:
                #set status code to 401
                return {"error": "Invalid Session"}, 401
        else:
            return {"error": "No Session"}, 401

    return wrapper