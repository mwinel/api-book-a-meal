from flask import jsonify
from flask_restful import Resource
from .. import app


class Index(Resource):
    """
    Manage responses to the index route.
    URL: /api/v1/ or /api/v1/index
    Request method: GET
    """
    def get(self):
        """ Return a welcome message. """
        return {"message": "Welcome to Book-a-meal."}

