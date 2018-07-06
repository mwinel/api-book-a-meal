from flask_restful import Resource
from .. import app

class UserRegistration(Resource):
	# Call the method to create or register a user.
	def post(self):
		return {'message': 'User registration'}

class UserLogin(Resource):
	# Call the method to login a user.
	def post(self):
		return {'message': 'User login'}
		   
class UserLogoutAccess(Resource):
	# Call the method to logout user.
	def post(self):
		return {'message': 'User logout'}
		 
class UserLogoutRefresh(Resource):
	def post(self):
		return {'message': 'User logout'}
		 
class TokenRefresh(Resource):
	def post(self):
		return {'message': 'Token refresh'}
		 
class AllUsers(Resource):
	# Call the method to Get all users.
	def get(self):
		return {'message': 'List of users'}
	  
class SecretResource(Resource):
	# Call the method to get the secret endpoint.
	def get(self):
		return {
			'answer': 200
		}
	  