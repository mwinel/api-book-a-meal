from flask_restful import Resource, reqparse
from app.models import Menu
from .. import app


class MenusAPI(Resource):
	# Call a method to create a new menu.
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name', required = True, 
			help = 'This can not be blank')
		parser.add_argument('description', type = str, 
			default = "")
		data = parser.parse_args()
		new_menu = Menu(
			name = data['name'],
			description = data['description']
		)
		try:
			new_menu.add_menu_to_db()
			return {
			    'message': 'Menu {} created successfully'.format(data['name'])
			}, 201
		except:
			return {
			    'message': 'Something went wrong.'
			}, 500

	# Return all menus.
	def get(self):
		return Menu.get_all_menus()


class MenuAPI(Resource):
	# Update a single menu.
	def put(self, id):
		menu = Menu.query.filter_by(id = id).first()
		parser = reqparse.RequestParser()
		parser.add_argument('name', required = True, 
			help = 'This can not be blank')
		parser.add_argument('description', type = str, 
			default = "")
		data = parser.parse_args()
		name, description = data['name'], data['description']
		menu.name = name
		menu.description = description
		try:
			menu.add_menu_to_db()
			return {
			    'message': 'Menu updated successfully to {}.'.format(data['name'])
			}, 201
		except:
			return {
			    'message': 'Something went wrong.'
			}, 500

	# Return a single menu.
	def get(self, id):
		menu = Menu.query.filter_by(id = id).first()
		if not menu:
			return {'message': 'Menu not found'}
		return {
		    'Menu': Menu.to_json(menu)
		}

	# Delete a menu.
	def delete(self, id):
		menu = Menu.query.filter_by(id = id).first()
		if not menu:
			return {'message': 'Menu not found'}
		menu.delete()
		return {'message': 'Menu successfully deleted'}
