
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__="user_details"
    id = db.Column(db.Integer)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80),nullable=False)
    mobile = db.Column(db.String(80),nullable=False)
    dob = db.Column(db.String,nullable=False)
    email = db.Column(db.String(120), primary_key=True, nullable=False)
    gender = db.Column(db.String(8),nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)



def __init__(self,name,password,mobile,dob,email,gender,timestamp):
    self.name = name
    self.password = password
    self.mobile = mobile
    self.dob = dob
    self.email = email
    self.gender = gender
    self.timestamp = timestamp

class Test(db.Model):
    __tablename__="book_details"
    isbn = db.Column(db.String, primary_key=True, nullable=False)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80),unique=False,nullable=False)
    year = db.Column(db.String(80),unique=False,nullable=False)

def __init__(self,isbn,title,author,year):
    self.isbn=isbn
    self.title=title
    self.author=author
    self.year=year

class Review(db.Model):
    __tablename__="review"
    user = db.Column(db.String(80),nullable=False)
    isbn = db.Column(db.String(80), primary_key=True, nullable=False)
    
    rating = db.Column(db.String(80),unique=False,nullable=False)
    review = db.Column(db.String(80),unique=False,nullable=False)

def __init__(self,user,isbn,rating,review):
    self.user = user
    self.isbn=isbn
    self.rating=rating
    self.review=review 
    
class Bookshelf(db.Model):
    __tablename__="book_shelf"
    user = db.Column(db.String(80),primary_key=True,nullable=False)
    book = db.Column(db.String(80) , nullable=False)
    
  

def __init__(self,user,book):
    self.user = user
    self.book=book
    