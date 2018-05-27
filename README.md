[![Build Status](https://travis-ci.org/mwinel/api-book-a-meal.svg?branch=master)](https://travis-ci.org/mwinel/api-book-a-meal)

# book-a-meal api
Book-A-Meal is an api that allows customers to make food orders and helps the food vendor know what the customers want to eat.

## Stack
- Python
- Flask
- PostgreSQL

## Installation and Set Up

Clone the repo from GitHub:

```
git clone https://github.com/mwinel/api-book-a-meal.git
```

Fetch from the develop branch:

```
git fetch origin develop
```

## Create and activate virtualenv

```
python -m venv venv
venv/Scripts/activate
```

## Set enviroment variables

Update **config** and env variables:

```
set FLASK_APP="run.py"
```

Set a SECRET_KEY. You should set your own secure secret key for security reasons.

```
set SECRET_KEY="you-own-your-own"
```

## Requirements

```
pip install -r requirements
```

## Create DB

Create a psql databases

```
CREATE DATABASE book-a-meal;
CREATE DATABASE book-a-meal_test;
```

Create the tables and run the migrations:

```
flask db init
flask db migrate
flask db upgrade
```

## Run the Application

```
python run.py
```

Access the application at the address **http://localhost:5000/**

## Testing

```
python tests.py 
```

## Methods

The API handles four HTTP requests

- POST – Used to create the menus and meal options
- GET – For retrieving one menus, meal options and orders using their ID's
- PUT – For updating a menus and meal options given its ID
- DELETE – For deleting a menus and meal options given its ID

## API Endpoints

| Resource URL | Methods | Description | Requires Token |
| -------- | ------------- | --------- |--------------- |
| `/api/v1/` | GET  | The index | FALSE |
| `/api/v1/index` | GET  | The index | FALSE |
| `/api/v1/auth/register` | POST  | User registration | FALSE |
| `/api/v1/auth/login` | POST | User login | FALSE |
| `/api/v1/menu` | GET, POST | A user's menu | TRUE |
| `/api/v1/menu/<id>` | GET, PUT, DELETE | A single menu | TRUE |
| `/api/v1/menu/<id>/meals` | GET, POST | meals in a menu | TRUE |
| `/api/v1/menu/<id>/meals/<meal_id>` | GET, PUT, DELETE| A single menu meal | TRUE |

## Sample Requests

To register a new user:
[User Registration](#)

To log the user in:
[User Login](#)

To add a new menu (includes the token in the header):
[Adding menu](#)

## Contribute
Would you like to make **book-a-meal** a better platform?
See [CONTRIBUTING.md](#) for the steps to contribute.

## UI
[Check out the project user interface](https://mwiru.github.io/book-a-meal/ui/index.html)
