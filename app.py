# main

from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from db.database import init_db, db_session
from db.userModel import User
from userRoutes import UserRegister

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


@app.route('/api/users', methods=['GET'])
def get_user():
    if(request.method == 'GET'):
        users = User.query.all()
        return [user.to_json() for user in users]

@app.route('/api/user', methods=['POST'])
def create_user():
    if(request.method == 'POST'):
        data = request.json
        user = User(name=data['name'], password=data['password'], email=data['email'])
        db_session.add(user)
        db_session.commit()
        return user.__repr__()


api.add_resource(UserRegister, '/api/user/<string:id>')

if __name__ == "__main__":
    app.run(debug=True, port=5000)