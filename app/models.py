from passlib.hash import pbkdf2_sha256 as sha256
from datetime import datetime
from app import create_app, db


class User(db.Model):
	""" This class defines the users table. """
	
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(60), nullable = False, unique = True)
	email = db.Column(db.String(120), nullable = False, unique = True)
	password = db.Column(db.String(140), nullable = False)

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	@staticmethod
	def generate_hash(password):
		return sha256.hash(password)

	@staticmethod
	def verify_hash(password, hash):
		return sha256.verify(password, hash)

	@classmethod
	def get_by_id(cls, id):
		""" Find a user by id. """
		return cls.query.filter_by(id = id).first()

	@classmethod
	def get_by_username(cls, username):
		""" Find a user by username. """
		return cls.query.filter_by(username = username).first()

	@classmethod
	def get_by_email(cls, email):
		""" Find a user by email. """
		return cls.query.filter_by(email = email).first()

	@classmethod
	def get_all_users(cls):
		""" Return all users. """
		def to_json(x):
			return {
				'id': x.id,
				'username': x.username,
				'email': x.email,
				'password': x.password
			}
		return {
			'Users': list(map(lambda x: to_json(x), User.query.all()))
		}

	def __repr__(self):
		return '<User {}>'.format(self.username)


class RevokedTokenModel(db.Model):
	""" This class stores a unique jwt token identifier. """

	__tablename__ = 'revoked_tokens'

	id = db.Column(db.Integer, primary_key = True)
	jti = db.Column(db.String(120))

	def add(self):
		""" Add identifier to database. """
		db.session.add(self)
		db.session.commit()

	@classmethod
	def is_jti_blacklisted(cls, jti):
		""" Check if the token is revoked. """
		query = cls.query.filter_by(jti = jti).first()
		return bool(query)


class Menu(db.Model):
	""" This class defines menu tables. """

	__tablename__ = 'menus'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(140), nullable = False)
	description = db.Column(db.String(250))
	created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
	user = db.relationship('User', backref = db.backref(
		'users', lazy = 'dynamic'))

	def add_menu_to_db(self):
		""" Add menu to database. """
		db.session.add(self)
		db.session.commit()

	def delete(self):
		""" Delete menu from database. """
		db.session.delete(self)
		db.session.commit()

	def to_json(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description
		}

	@classmethod
	def get_all_menus(cls):
		""" Return all menus. """
		return {
			'Menus': list(map(lambda x: Menu.to_json(x), Menu.query.all()))
		}

	@staticmethod
	def get_all():
		""" This method gets all the menus for a given user. """
		return Menu.query.filter_by(created_by = user)
