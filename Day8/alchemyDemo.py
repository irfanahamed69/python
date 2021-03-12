from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db=SQLAlchemy(app)

class user(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,unique=True,nullable=False)
    email=db.Column(db.String,unique=True,nullable=False)

    def __repr__(self):
        return '<user %r>' % self.username

db.create_all()
admin = user(username='admin',email='admin@example.com')
guest = user(username='guest',email='guest@example.com')

db.session.add(admin)
db.session.add(guest)
db.session.commit()

print(user.query.all())
print(type(user.query.all()))
print(user.query.filter_by(username='admin').first())