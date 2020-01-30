from model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(username,password):
    """Add a user to the DB."""
    username = User(username=name)
    session.add(User)
    session.commit()



def get_user(username):
	return session.query(User).filter_by(username=username).first()
	

def get_password(username):
	return session.query(User).filter_by(username=name).password()


