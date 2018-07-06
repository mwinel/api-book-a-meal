import os 


class Config(object):
	""" Default configurations. """

	DEBUG = False
	TESTING = False
	SECRET_KEY = os.environ.get('SECRET_KEY') or "go-on-until-you-get-it"
	SQLALCHEMY_DATABASE_URI = "postgresql://postgres:myPassword@localhost/bkameal"
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
	""" Development configurations. """

	DEBUG = True
	TESTING = True

class TestingConfig(Config):
	""" Test configurations. """

	DEBUG = True
	TESTING = True
	SQLALCHEMY_DATABASE_URI = "postgresql://postgres:myPassword@localhost/bkameal_test"
	PRESERVE_CONTEXT_ON_EXCEPTION = False

class ProductionConfig(Config):
	""" Production configurations. """

	DEBUG = False
	TESTING = False

app_config = {
	"development": DevelopmentConfig,
	"testing": TestingConfig,
	"production": ProductionConfig
}



