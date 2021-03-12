from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
db=SQLAlchemy(app)
ma=Marshmallow(app)

class user(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,unique=True,nullable=False)
    email=db.Column(db.String,unique=True,nullable=False)

    def __repr__(self):
        return '<user %r>' % self.username

class userSchema(ma.SQLAlchemySchema):
    class Meta:
        model = user

    id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()

db.create_all()
user_schema = userSchema()
admin = user(username='admin',email='admin@example.com')
guest = user(username='guest',email='guest@example.com')

db.session.add(admin)
db.session.add(guest)
db.session.commit()

print(user.all())
print(type(user.query.all()))
print(user.query.filter_by(username='admin').first())
print(user_schema.dump(guest))