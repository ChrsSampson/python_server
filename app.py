# main

from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import sqlite3

#from routes import UserRoutes

db = sqlite3.connect('db/data.db')

app = Flask(__name__)
# restful api
api = Api(app)


#api.add_resource(UserRoutes, '/user/<string:username>') 

@app.route('/')
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True, port=5000)