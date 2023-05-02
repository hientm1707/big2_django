# from ... import db
# from flask_login import UserMixin
#
#
# class Account(UserMixin, db.Model):
#     __tablename__ = 'account'
#
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False, default=username)
#     password = db.Column(db.String(300), nullable=False, unique=True)
#
#     def __repr__(self):
#         return f'<User {self.username}>'
#
#
#
