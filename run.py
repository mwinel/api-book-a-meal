from app import app, api
from app.resources.index import Index
from app.resources.users import UserRegistration, UserLogin, \
        UserLogoutAccess, UserLogoutRefresh, TokenRefresh, \
        AllUsers, SecretResource
from app.resources.menu import MenusAPI, MenuAPI

""" Define API endpoints. """
api.add_resource(Index, "/", "/index")
api.add_resource(UserRegistration, '/registration')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogoutAccess, '/logout/access')
api.add_resource(UserLogoutRefresh, '/logout/refresh')
api.add_resource(TokenRefresh, '/token/refresh')
api.add_resource(AllUsers, '/users')
api.add_resource(SecretResource, '/secret')
api.add_resource(MenusAPI, '/menus')
api.add_resource(MenuAPI, '/menus/<id>')

if __name__ == '__main__':
    app.run(debug = True)
