from flask_restful import Resource, reqparse
from db.database import User, db_session

# /users/<username>
class UsersRegister(Resource):
    # get one by username
    def get(self, username):
        user = db_session.query(User).filter_by(username=username).first()
        if user:
            return user.json()
        return {'message': 'User not found'}, 404
    

class UserRegister(Resource):
    # create new user
    def post(self):
        # parse request
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='This field cannot be left blank')
        parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')
        parser.add_argument('email', type=str, required=True, help='This field cannot be left blank')
        data = parser.parse_args()
        # check if user exists
        if db_session.query(User).filter_by(username=data['username']).first():
            return {'message': 'User already exists'}, 400
        # create new user
        new_user = User(username=data['username'], password=data['password'], email=data['email'])
        db_session.add(new_user)
        db_session.commit()
