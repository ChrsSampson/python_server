from flask_restful import Resource, reqparse
from flask import jsonify
from db.database import db_session
from db.userModel import User
from flask import request
import datetime

class UserRegister(Resource):
    # get one by id
    def get(self, id):
        try:
            user = db_session.query(User).filter(id == id).one()
            print(user.to_json() )
            return user.to_json()
            
        except Exception as err:
            print(err)

    # create new user
    def post(self):
        data = request.json
        user = User(name=data['name'], password=data['password'], email=data['email'])
        db_session.add(user)
        db_session.commit()
        return user.__repr__()
    
    # update user
    def put(self, id):
        data = request.json
        user = db_session.query(User).filter(id == id).one()

        # surely there is a better way to do this
        attrs = ['name', 'email', 'password']
        for attr in attrs:
            if attr in data:
                setattr(user, attr, data[attr])
            

        user.modified_at = datetime.datetime.now()

        db_session.commit()
        # returns the altered user
        return user.to_json()
    
    # delete user
    def delete(self, id):
        user = db_session.query(User).filter(id == id).one()
        db_session.delete(user)
        db_session.commit()
        return f"Removed {user['name']}"

    
