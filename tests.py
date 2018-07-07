import json
import unittest
from flask_testing import TestCase
from app import create_app, db
from run import app
from config import app_config

app.config.from_object(app_config["testing"])

class TestBase(TestCase):
	""" Base configurations for the tests. """

	def create_app(self):
		""" Returns app. """
		return app

	def setUp(self):
		""" Create test database and set up test client. """
		self.app = app.test_client()
		db.create_all()
		db.session.commit()

	def tearDown(self):
		""" Destroy test database. """
		db.session.remove()
		db.drop_all()

	def test_index(self):
		""" Test response to the index endpoint. """
		response = self.app.get('/api/v1/')
		self.assertEqual(response.status_code, 200)
		output = json.loads(response.data)
		self.assertEqual(output, {'message': 'Welcome to Book-a-meal.'})

	def test_user_registration(self):
		""" Test user registration. """
		self.user = {
			"username": "sally1",
			"email": "sally1@example.com",
			"password": "123456"
		}
		response = self.app.post("/api/v1/registration", data = self.user)
		self.assertEqual(response.status_code, 201)
		output = json.loads(response.data)
		self.assertIn(self.user["username"], str(response.data))

	def test_registered_user(self):
		""" Test registered user can't register again. """
		self.user = {
			"username": "sally1",
			"email": "sally1@example.com",
			"password": "123456"
		}
		response = self.app.post("/api/v1/registration", data = self.user)
		self.assertEqual(response.status_code, 201)
		result = self.app.post("/api/v1/registration", data = self.user)
		self.assertEqual(response.status_code, 201)
		result = json.loads(response.data)
		self.assertTrue(result, {'message': 'User {} already exists'.format('username')})
	
	def test_user_login(self):
		""" Test user can login. """
		self.user = {
			"username": "sally1",
			"email": "sally1@example.com",
			"password": "123456"
		}
		response = self.app.post("/api/v1/registration", data = self.user)
		self.assertEqual(response.status_code, 201)
		response = self.app.post("/api/v1/login", data = self.user)
		self.assertEqual(response.status_code, 200)
		output = json.loads(response.data)
		self.assertTrue(output, {'message': 'Logged in as {}'.format('username')})

	def test_non_registered_user_login(self):
		""" Test non registered user can not login. """
		self.user = {
			"username": "sally1",
			"email": "sally1@example.com",
			"password": "123456"
		}
		response = self.app.post("/api/v1/registration", data = self.user)
		self.assertEqual(response.status_code, 201)
		self.unrgistered_user = {
			"username": "sally",
			"email": "sally@example.com",
			"password": "123456"
		}
		response = self.app.post("/api/v1/login", data = self.user)
		self.assertEqual(response.status_code, 200)
		output = json.loads(response.data)
		self.assertTrue(output, {'message': 'User {} doesn\'t exist'.format('username')})

	def test_create_menu(self):
		""" Test a menu can be created. """
		self.menu = {
			"name": "KFC Special",
			"description": "Finger lickin chicken"
		}
		response = self.app.post("/api/v1/menus", data = self.menu)
		self.assertEqual(response.status_code, 201)
		output = json.loads(response.data)
		self.assertIn(self.menu["name"], str(response.data))

	def test_get_all_menus(self):
		""" Test API can get all menus."""
		self.menu = {
			"name": "KFC Special",
			"description": "Finger lickin chicken"
		}
		response = self.app.post("/api/v1/menus", data = self.menu)
		self.assertEqual(response.status_code, 201)
		response = self.app.get("/api/v1/menus")
		self.assertEqual(response.status_code, 200)
		self.assertIn(self.menu["name"], str(response.data))
		self.assertIn('Finger lickin', str(response.data))

if __name__ == "__main__":
	unittest.main()
