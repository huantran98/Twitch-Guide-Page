import pytest
# from app import models, forms
from app.models import User, Post
from app.forms import LoginForm
#from app import routes


def test_login(client):
    response = client.get('/login')
    assert response.status_code == 200
    
    
def test_add_user_to_db(db):
    test_user = User(email='test_user@gmail.com',username = 'user', password_hash='1234')
    db.session.add(test_user)
    db.session.commit()
    assert len(User.query.all()) == 1    
    
def test_verify_user_exists(db):
    user = User.query.get(1)
    assert user.is_authenticated == True 
    
def test_valid_register(client, db):
    response = client.post('/login',
                           data=dict(username='user', email='testing@testing.com',
                                     password='testing', confirm='testing'),
                           follow_redirects=True)
    assert response.status_code == 200  

    