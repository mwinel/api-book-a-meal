from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token, 
	jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from app.models import User, RevokedTokenModel
from .. import app


class UserRegistration(Resource):
	# Call the method to create or register a user.
	def post(self):
		parser = reqparse.RequestParser()
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
			password = User.generate_hash(data['password'])
		)
		try:
			new_user.save_to_db()
			access_token = create_access_token(identity = data['username'])
			refresh_token = create_refresh_token(identity = data['username'])
			return {
				'message': 'User {} created successfully'.format(data['username']),
				'access token': access_token,
				'refresh token': refresh_token
			}, 201
		except:
			return {
				'message': 'Something went wrong.'
			}, 500


class UserLogin(Resource):
	# Call the method to login a user.
	def post(self):
		parser = reqparse.RequestParser()
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
		if User.verify_hash(data['password'], current_user.password):
			access_token = create_access_token(identity = data['username'])
			refresh_token = create_refresh_token(identity = data['username'])
			return {
				'message': 'Logged in as {}'.format(data['username']),
				'access token': access_token,
				'refresh token': refresh_token
			}
		else:
			return {
				'message': 'Invalid username or password'
			}

		   
class UserLogoutAccess(Resource):
	# Call the method to access token logout.
	@jwt_required
	def post(self):
		jti = get_raw_jwt()['jti']
		try:
			revoked_token = RevokedTokenModel(jti = jti)
			revoked_token.add()
			return {
				'message': 'Access token has been revoked'
			}
		except:
			return {
				'message': 'Something went wrong.'
			}, 500

		 
class UserLogoutRefresh(Resource):
	# Call the method to refresh token logout.
	@jwt_refresh_token_required
	def post(self):
		jti = get_raw_jwt()['jti']
		try:
			revoked_token = RevokedTokenModel(jti = jti)
			revoked_token.add()
			return {
				'message': 'Refresh token has been revoked'
			}
		except:
			return {
				'message': 'Something went wrong.'
			}, 500

		 
class TokenRefresh(Resource):
	# Reissue access token with refresh token
	@jwt_refresh_token_required
	def post(self):
		current_user = get_jwt_identity()
		access_token = create_access_token(identity = current_user)
		return {
			'access token': access_token
		}
		 

class AllUsers(Resource):
	# Call the method to Get all users.
	def get(self):
		return User.get_all_users()
	  

class SecretResource(Resource):
	# Call the method to get the secret endpoint.
	@jwt_required
	def get(self):
		return {
			'answer': 200
		}
	  