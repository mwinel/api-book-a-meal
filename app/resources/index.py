from flask import jsonify
from flask_restful import Resource
from .. import app

class Index(Resource):
    # Call the method to Get the index response.
    def get(self):
        """ Return a welcome message. """
        return {"message": "Welcome to Book-a-meal."}

