from passlib.hash import pbkdf2_sha256 as sha256
from datetime import datetime
from app import create_app, db


class User(db.Model):
	""" This class defines the users table. """

	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(60), nullable = False, 
		unique = True)
	email = db.Column(db.String(120), nullable = False, 
		unique = True)
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
		""" Find a user by username. """
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
			'users': list(map(lambda x: to_json(x), User.query.all()))
		}

	@classmethod
	def delete_users(cls):
		""" Delete all users. """
		try:
			num_rows_deleted = db.session.query(cls).delete()
			db.session.commit()
			return {
				'message': '{} row(s) deleted'.format(num_rows_deleted)
			}
		except:
			return {
				'message': 'Something went wrong'
			}

	def __repr__(self):
		return '<User {}>'.format(self.username)


class RevokedTokenModel(db.Model):
	""" This class stores a unique token identifier. """

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
	""" This class defines the Menus table. """

	__tablename__ = 'menus'

	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(80), nullable = False)
	desc = db.Column(db.Text)
	created_on = db.Column(db.DateTime, default = datetime.now)
	modified_on = db.Column(db.DateTime, onupdate = datetime.now)
	created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
	meals = db.relationship('Meal', backref = db.backref('menu'))


	def add_menu(self):
		""" Add menu to database. """
		db.session.add(self)
		db.session.commit()

	def delete_menu(self):
		""" Delete menu from database. """
		db.session.delete(self)
		db.session.commit()

	@classmethod
	def get_menu_by_id(cls, id):
		""" Find a menu by id. """
		return cls.query.filter_by(id = id).first()

	@classmethod
	def get_menu_by_title(cls, title):
		""" Find a menu by title. """
		return cls.query.filter_by(title = title).first()


class Meal(db.Model):
	""" This class defines the Meals table. """

	__tablename__ = 'meals'

	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(80), nullable = False)
	description = db.Column(db.Text)
	created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
	user = db.relationship('User', backref = db.backref('users', 
		lazy = 'dynamic'))
	menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'))


	def add_meal(self):
		""" Add meal to database. """
		db.session.add(self)
		db.session.commit()
		

