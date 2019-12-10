# import pytest
# from app import routes
# from app.models import User, Post
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import current_user, login_user, logout_user

# @pytest.fixture(scope = 'module')
# def new_user():
#   user = User(email = 'yennhilam@ymail.com' , username = 'username', password_hash = '1234')
#   return user

# @pytest.fixture(scope = 'module') # not sure it is correct, need to edit
# def new_task():
#   Post = Post(nameTitle = 'Test', id = 234, complete = False)
#   return post

# # Pytest 1
# # testing validating new user yennhilam@ymail.com <---  maybe need to change
# def test_new_user(new_user):
#   assert new_user.email == 'yennhilam@ymail.com'
#   assert new_user.password_hash != '1234'
  
# # Pytest 2
# # verifying the new user is yennhilam@ymail.com
# def test_login(new_user):
#   assert new_user.is_authenticated == True
  
# # Pytest 3
# # Testing email is incorrect, but password is correct
# def test_new_user(new_user):
#   assert new_user.email != 'yennhilam@ymail.com'
#   assert new_user.password_hash == '1234'
  
# # Pytest 4 not sure it is correct, need to edit 
# def test_new_task(new_task):
#   assert new_task.id == 234
#   assert new_task.nameTitle == 'Test'
#   assert new_task.complete == False
  

# # Pytest 5
# # testing content is not empty
# def test_content(new_task):
#     assert new_task.content != None
      


