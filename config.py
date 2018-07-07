import os 


class Config(object):
	""" Default configurations. """

	DEBUG = False
	TESTING = False
	SQLALCHEMY_DATABASE_URI = "postgresql://postgres:myPassword@localhost/api_bk"
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
	""" Development configurations. """

	DEBUG = True
	TESTING = True

class TestingConfig(Config):
	""" Test configurations. """

	DEBUG = True
	TESTING = True
	SQLALCHEMY_DATABASE_URI = "postgresql://postgres:myPassword@localhost/api_bktest"
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



