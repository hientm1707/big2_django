from functools import wraps

from flask import Blueprint, request
from json.decoder import JSONDecodeError

auth = Blueprint('auth', __name__, url_prefix='/auth')

# def validate_json_input(func):
#     @wraps(func)
#     def wrapper(**kwargs):
#         if not request.is_json:
#             raise JSONDecodeError('User input is not valid json')
#         return func(**kwargs)
#     return wrapper()

@auth.route('/login', methods=['GET', 'POST'])
def login():
    json_request = request.get_json()
    return "Login called"
    username = json_request.get('username', None)
    password = json_request.get('password', None)



@auth.route('/signup', methods=['POST'])
def signup():
    pass


@auth.route('/logout', methods=['GET'])
def logout():
    pass
