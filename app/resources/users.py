from flask_restful import Resource, reqparse
from app.models import User
from .. import app


# Initialize parser.
parser = reqparse.RequestParser()


class UserRegistration(Resource):
	# Call the method to create or register a user.
	def post(self):
		# Add parsing of incoming data.
		parser.add_argument('username', required = True, 
			help = 'This field cannot be blank')
		parser.add_argument('email', required = True,
			help = 'This field cannot be blank')
		parser.add_argument('password', required = True,
			help = 'This field cannot be blank')
		data = parser.parse_args()
		if User.get_by_username(data['username']):
			return {
			    'message': 'User {} already exists'.format(data['username'])
			}
		new_user = User(
			username = data['username'],
			email = data['email'],
			password = data['password']
		)
		try:
			new_user.save_to_db()
			return {
				'message': 'User {} created successfully'.format(data['username'])
			}
		except:
			return {
				'message': 'Something went wrong.'
			}, 500


class UserLogin(Resource):
	# Call the method to login a user.
	def post(self):
		parser.add_argument('username', required = True, 
			help = 'This field cannot be blank')
		parser.add_argument('password', required = True,
			help = 'This field cannot be blank')
		data = parser.parse_args()
		current_user = User.get_by_username(data['username'])
		if not current_user:
			return {
			    'message': 'User {} doesn\'t exist'.format(data['username'])
			}
		if data['password'] == current_user.password:
			return {
			    'message': 'Logged in as {}'.format(data['username'])
			}
		else:
			return {
			    'message': 'Invalid username or password'
			}

		   
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
		return User.get_all_users()
	  

class SecretResource(Resource):
	# Call the method to get the secret endpoint.
	def get(self):
		return {
			'answer': 200
		}
	  