# main

from flask import Flask, request, send_from_directory
from flask_restful import Api, Resource, reqparse
from db.database import init_db, db_session
from db.userModel import User
from userRoutes import UserRegister
from middleware import megan
from flask.cli import AppGroup
import click

# set statuc folder for public assets
app = Flask(__name__, static_folder='client/dist', static_url_path='/')
# restful api
api = Api(app)

user_cli_utils = AppGroup('user')

@user_cli_utils.command('create_admin')
@click.argument('email')
@click.argument('password')
def create_admin(email, password):
    try:
        init_db()
        user = User(name="Site Administrator", email=email, password=password)
        user.create_admin_account( email, password)
        db_session.add(user)
        db_session.commit()
        click.echo("Admin account created")
        db_session.remove()
    except Exception as e:
        click.echo(e)

app.cli.add_command(user_cli_utils)

# init db
@app.before_first_request
def init():
    init_db()

# unmount db
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
@megan
def index():
    # serve the client
    return send_from_directory('client/dist', 'index.html')


@app.route('/api/users', methods=['GET'])
@megan
def get_user():
    if(request.method == 'GET'):
        users = User.query.all()
        return [user.to_json() for user in users]


@app.route('/api/user', methods=['POST'])
@megan
def create_user():
    if(request.method == 'POST'):
        data = request.json
        user = User(name=data['name'], password=data['password'], email=data['email'])
        db_session.add(user)
        db_session.commit()
        return user.__repr__()


@app.route('/api/auth/login', methods=['POST'])
@megan
def login_handler():
    if(request.method == 'POST'):
        data = request.json
        user = User.query()
        if(user):
            if(User.check_password(user, data['password'])):
                User.create_session()
                return user.to_json()
            else:
                return {"error": "Invalid Password"}

@app.route('/api/auth/logout/:id', methods=['POST'])
@megan
def logout_handler():
    if(request.method == 'POST'):
        
        user = User.query('id', data['id'])

api.add_resource(UserRegister, '/api/user/<string:id>')

if __name__ == "__main__":
    app.run(port=3000, debug=True)