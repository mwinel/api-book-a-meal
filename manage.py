import os
import unittest
import coverage
from flask_script import Manager
from app import create_app


# Initialize app with its configurations
app = create_app("development")
manager = Manager(app)

# define testing command "test"
# Usage: python manage.py test
@manager.command
def cov_test():
	""" Runs the unit tests without test coverage. """
	tests = unittest.TestLoader().discover('./tests', pattern='test*.py')
	result = unittest.TextTestRunner(verbosity=2).run(tests)
	if result.wasSuccessful():
		return 0
	return 1

@manager.command
def cover():
	""" Runs the unit tests with coverage. """
	os.system('coverage run manage.py test')
	os.system('coverage report')
	os.system('coverage html')


if __name__ == "__main__":
	manager.run

