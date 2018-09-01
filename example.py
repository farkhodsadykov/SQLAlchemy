from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import Address, Base, Person
from werkzeug.security import generate_password_hash, check_password_hash

class fscoding():
    def __init__(self, fname, lname, username, password, email, status, role):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = generate_password_hash(password, method='sha256')
        self.email = email
        self.status = status
        self.role = role


    def signup(self):
        self.fname = input("Pleas enter your First name: ")
        self.lname = input("Pleas enter your Last name: ")
        self.username = input("Pleas enter your username: ")
        self.password = input("Pleas enter your password: ")
        self.email = input("Pleas enter your email: ")
        self.status = False
        self.role = 'student'


    def login(self):
        username = input("Pleas enter your username: ")
        password = input("Pleas enter your password: ")
        checked = check_password_hash(password, self.password)
        if username == self.username:
            if checked == True:
                print("You are login")
            else:
                print("Password or username incorect")
        else:
            print("Password or username incorect")
