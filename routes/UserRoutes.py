from flask_restful import Resource, reqparse


# user Rest API
class UserRoutes(Resource):
    def __init__ (self):
        self.parser = reqparse.RequestParser()

    # get one user by id
    def get(self, id):
        pass

    # create a new user
    def post(self, id):
        
        return f"id:{id}"
        

    # update a user
    def put(self, id):
        pass

    # delete a user
    def delete(self, id):
        pass


# get a list of all users in the user table
# /users 
class UserList(Resource):
    def __init__ (self):
        pass

    # get all users
    def get(self):
        pass

        