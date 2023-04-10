# whenever the client contact the server either create a new annon session or check the existing one

# currently doing nothing

from flask import request

def clientVerifier (req):
    if(req.session['client'] == request.headers['client']):
        return True
    else:
        return False


