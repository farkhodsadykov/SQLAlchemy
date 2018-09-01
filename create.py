from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

# Creating table for our Databse
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fname = Column(String(22))
    lname = Column(String(22))
    username = Column(String(22), unique=True)
    password = Column(String(50))
    email = Column(String(22))
    status = Column(String(10))
    role = Column(String(10))



# When user run the script  it will go to Database and create everything
if __name__ == '__main__':
    db = create_engine('sqlite:///DataBase/example.db')
    # db = create_engine('mysql://flaskuser:flask**@ipdatabase/zabbix')
    Base.metadata.create_all(bind=db)
