from app.models import User
from app.extensions import db

def get_all_users():
    return User.query.all()

def create_user(name, email):
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()

def update_user(user, name, email):
    user.name = name
    user.email = email
    db.session.commit()

def delete_user(user):
    db.session.delete(user)
    db.session.commit()
