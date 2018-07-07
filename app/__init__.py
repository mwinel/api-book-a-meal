from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from config import app_config


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class):
	app = Flask(__name__)
	app.config.from_object(app_config[config_class])
	app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
	app.config['JWT_BLACKLIST_ENABLED'] = True
	app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
	db.init_app(app)
	migrate.init_app(app, db)
	jwt = JWTManager(app)

	@jwt.token_in_blacklist_loader
	def check_if_token_in_blacklist(decrypted_token):
		jti = decrypted_token['jti']
		return models.RevokedTokenModel.is_jti_blacklisted(jti)

	return app

app = create_app("development")
api = Api(app = app, prefix = "/api/v1")