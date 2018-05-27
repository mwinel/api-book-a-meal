from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from config import app_config


db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class):
	app = Flask(__name__)
	app.config.from_object(app_config[config_class])
	db.init_app(app)
	migrate.init_app(app, db)

	return app

app = create_app("development")
api = Api(app=app, prefix="/api/v1")