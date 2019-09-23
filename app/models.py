from . import db,login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Author(UserMixin, db.Model):
    __tablename__="authors"
    # Password is a string nullable = required username should be unique unique
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),nullable=False, unique=True)
    email = db.Column(db.String(255),nullable=False, unique=True)
    password = db.Column(db.String(255),nullable=False)
    posts = db.relationship('Blog', backref='author', lazy="dynamic")
    comments = db.relationship('Blogcomment', backref='author', lazy="dynamic")

    def save_author(self):
        db.session.add(self)
        db.session.commit()

    def delete_author(self):
        db.session.delete(self)
        db.session.commit()

    def set_password(self, password):
        # We intend to get the password as a hash from the text they get
        password_hash=generate_password_hash(password)
        # save the password hash
        self.password=password_hash

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "Author: %s"%str(self.username)

@login_manager.user_loader
def user_loader(user_id):
    return Author.query.get(user_id)

class Blog(db.Model):
    __tablename__="blogs"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    blogcomment = db.relationship('Blogcomment', backref='post_blog', lazy="dynamic")
    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Blog('{self.title}','{self.date_posted}')"

class Blogcomment(db.Model):
    __tablename__ = "blogcomments"
    id = db.Column(db.Integer,primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)

    # Our function for deleting  
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Blog('{self.date_posted}')"

class Quotes:
  def __init__ (self,author,quote,permalink):
    self.author = author
    self.quote = quote
    self.permalink = permalink