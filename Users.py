from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import Address, Base, Person

# Connecting to the DataBase
engine = create_engine('sqlite:///DataBase/example.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Insert a new user to the table users
new_user = User(username='farkhodsadykov', name='Farkhod', fullname='Farkhod Sadykov', password='PASSWORD')
session.add(new_user)
session.commit()
