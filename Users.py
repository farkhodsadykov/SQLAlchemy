from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from create import User

engine = create_engine('mysql://flaskuser:flask**@159.89.180.31/zabbix')
Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


new_user = User(username='ahmedali', fname='Ahmed', lname='Ali', password='PASSWORD', email='ahmedali@gmail.com',status='True', role='student')
session.add(new_user)
session.commit()
