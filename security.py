# from werkzeug.security import safe_str_cmp
# from models.user import User



# def authenticate(username, password):
  #   user = User.find_by_username(username=username)
    # if user and safe_str_cmp(user.password, password):
      #   return 'User e Password corretti'
    # else:
      #   return 'User o password errati'


# def identity(payload):
  #   user_id = payload['identity']
    # return User.find_by_id(user_id)
