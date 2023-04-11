# main

from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from db.database import init_db, db_session
from db.userModel import User

app = Flask(__name__)
# restful api
api = Api(app)

# init db
@app.before_first_request
def init():
    init_db()

# unmount db 
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/users', methods=['GET'])
def get_user():
    if(request.method == 'GET'):
        users = User.query.all()
        return users

@app.route('/user', methods=['POST'])
def create_user():
    if(request.method == 'POST'):
        data = request.get_json()
        print(data[0])
        return 'hi'

if __name__ == "__main__":
    app.run(debug=True, port=5000)