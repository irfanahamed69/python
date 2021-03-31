from flask import Flask, render_template, flash, redirect, request, session, logging, url_for, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow
from datetime import datetime
from werkzeug.exceptions import HTTPException
import json
import jsonschema
import logging
from jsonschema import validate
from flask_expects_json import expects_json

app = Flask(__name__)
app.config['SECRET_KEY'] = '!9m@S-dThyIlW[pHQbN^'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
db = SQLAlchemy(app)
ma=Marshmallow(app)

logging.basicConfig(level=logging.ERROR,filename='app.log',format='%(asctime)s- %(levelname)s -  %(module)s -  %(lineno)d - %(message)s')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(15))
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(256), unique=True)
    address = db.Column(db.String(256))
    state = db.Column(db.String(20))
    country = db.Column(db.String(20))
    pan = db.Column(db.String(20), unique=True)
    contactNumber = db.Column(db.String(12), unique=True)
    dob = db.Column(db.String(12))

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    LoanType = db.Column(db.String(20))
    LoanAmount = db.Column(db.Integer)
    Interest = db.Column(db.Integer)
    Date = db.Column(db.String(12))
    Duration = db.Column(db.String(20))

class customerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    name = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
    address = ma.auto_field()
    state = ma.auto_field()
    country = ma.auto_field()
    contactNumber = ma.auto_field()

customer_schema = customerSchema()

class LoanSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Loan

    username = ma.auto_field()
    LoanType = ma.auto_field()
    LoanAmount = ma.auto_field()
    Interest = ma.auto_field()
    Date = ma.auto_field()
    Duration = ma.auto_field()

Loan_Schema = LoanSchema()


@app.route('/cogbank/1.0/login/', methods = ['POST'])
def login():
    try:
        if request.method == 'POST':
            request_data = request.get_json()
            username = request_data['username']
            password = request_data['password']
            if username and password:
                user = User.query.filter_by(username = username).first()
                if user:
                    if check_password_hash(user.password,password):
                        flash('You have successfully logged in.', "success")
                        session['logged_in'] = True
                        session['username'] = user.username
                        data = {'Status' : 'You have logged in successfully'}
                        logging.info(data)
                        return jsonify(data), 200
                    else:
                        flash('Username or Password Incorrect', "Danger")
                        data = {'Status' : 'Username or password is incorrect'}
                        logging.error(data)
                        return jsonify(data), 404
                        #return 'Username or password is incorrect'
                else:
                    data = {'Status' : 'You have not signed up Please sign up to login'}
                    logging.error(data)
                    return jsonify(data), 404
                    #return 'You have not signed up Please sign up to login'
            else:
                data = {'Status' : 'Please enter username and password'}
                logging.error(data)
                return jsonify(data), 404
                #return 'Please enter username and password'
        else:
            data = {'Status' : 'http method is incorrect. Use POST'}
            logging.error(data)
            return jsonify(data), 404
            #return 'http method is incorrect. Use POST'
    except Exception as error:
        logging.error(error, exc_info=True)
        return jsonify({"Error":"There is an internal error Please contact system administrators"}),400
        
@app.route('/cogbank/1.0/register/', methods = ['POST'])
#@expects_json(schema)
def register():
    try:
        if request.method == 'POST':
            
            schema = {  "type" : "object",
                        "properties" : {
                            "name" : {"type" : "string"},
                            "username" : {"type" : "string"},
                            "email" : {"type" : "string","pattern": "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"},
                            "password" : {"type" : "string"},
                            "address" : {"type" : "string"},
                            "state" : {"type" : "string"},
                            "country" : {"type" : "string"},
                            "pan" : {"type" : "string"},
                            "contactNumber" : {"type" : "string", "maxLength":10},
                            "dob" : {"type" : "string"},
                            },
                            "required": ["username", "email","password","pan","contactNumber"]
                    }
            request_data = request.get_json()
            validate(instance=request_data, schema=schema)
            name = request_data['name']
            username = request_data['username']
            email = request_data['email']
            password = request_data['password']
            address = request_data['address'] 
            state = request_data['state'] 
            country = request_data['country'] 
            pan = request_data['pan'] 
            contactNumber = request_data['contactNumber'] 
            dob = request_data['dob'] 
        
            hashed_password = generate_password_hash(password, method='sha256')
            user = User.query.filter_by(username = username).first()
            if user:
                data = {'Status' : 'User already registered Please provide different values '}
                logging.error(data)
                return jsonify(data), 202
                #return 'You have registered successfully'
            else:
                new_user = User(name = name,
                    username = username,
                    email = email, 
                    password = hashed_password,
                    address = address,
                    state = state,
                    country = country,
                    pan = pan, 
                    contactNumber = contactNumber,
                    dob = dob
                    )
                db.session.add(new_user)
                db.session.commit()
                flash('You have successfully registered', 'success')
                data = {'Status' : 'You have registered successfully'}
                return jsonify(data), 200
                #return 'You have registered successfully'
        else:
            data = {'Status' : 'Use http method Post'}
            
            return jsonify(data), 404
            #return 'registration unsuccessful Please contact administrator'
    except jsonschema.ValidationError as e:
        logging.error(error, exc_info=True)
        return jsonify({"Error":str(e.message)}), 400
    except Exception as error:
        logging.error(error, exc_info=True)
        return jsonify({"Error":"There is an internal error Please contact system administrators"}),400

@app.route('/cogbank/1.0/changePassword/',methods = ['POST'])
def changePassword():
    try:
        if request.method == 'POST':
            request_data = request.get_json()
            username = request_data['username']
            password = request_data['password']
            if username and password:
                user = User.query.filter_by(username = username).first()
                if user:
                    hashed_password = generate_password_hash(password, method='sha256')
                    user.password = hashed_password
                    db.session.commit()
                    data = {'Status' : 'Password updated successfully for the user {}'.format(username)}
                    return jsonify(data), 200
                   # return 'Password updated successfully for the user {}'.format(username)
                else:
                    data = {'Status' : 'Invalid username'}
                    logging.error(data)
                    return jsonify(data), 404
                    #return 'Invalid username'
            else:
                data = {'Status' : 'Password not updated pleased try again later'}
                logging.error(data)
                return jsonify(data), 404
                #return 'Password not updated pleased try again later'
        else:
            data = {'Status' : 'Please use http method post'}
            logging.error(data)
            return jsonify(data), 404
            #return 'Please use http method post'
    except Exception as error:
        logging.error(error, exc_info=True)
        return jsonify({"Error":"There is an internal error Please contact system administrators"}),400


@app.route('/cogbank/1.0/checklog/')
def checklog():
    try:
        user = request.args.get('username')

        if 'username' not in session:
            request_data = request.get_json()
            name = request_data['name']
            data = {'Status' : 'user {} logged out'.format(user)}
            return jsonify(data), 200
            #return 'user {} logged out'.format(user)
        else:
            data = {'Status' : 'You have already logged in'}
            return jsonify(data), 200
            #return 'You have already logged in'
    except Exception as error:
        logging.error(error, exc_info=True)
        return jsonify({"Error":"There is an internal error Please contact system administrators"}),400

@app.route('/cogbank/1.0/updateCustomer/', methods = ['POST'])
def updateCustomer():
    try:
        if request.method == 'POST':
            request_data = request.get_json()
            username = request_data['username']
            name = request_data['name']
            address = request_data['address']
            state = request_data['state']
            country = request_data['country']
            pan = request_data['pan']
            contactNumber = request_data['contactNumber']
            dob = request_data['dob']

            if session.get('username') is None:
                data = {'Status' : 'Please log in to update details'}
                logging.error(data)
                return jsonify(data), 404
                #return 'Please log in to update details'
            else:
                user = User.query.filter_by(username = username).first()
                if user:
                    user.name = name
                    user.address = address
                    user.state = state
                    user.country = country
                    user.pan = pan
                    user.contactNumber = contactNumber
                    user.dob = dob
                    db.session.commit()
                    data = {'Status' : 'Details updated successfully'}
                    return jsonify(data), 200
                    #return 'Details updated successfully'
                else:
                    data = {'Status' : 'data is not present for the username {}'.format(username)}
                    logging.error(data)
                    return jsonify(data), 404
                    #return 'data is not present for the username {}'.format(username)
        else:
            data = {'Status' : 'Http Method not allowed. Please use POST'}
            logging.error(data)
            return jsonify(data), 404
            #return 'Http Method not allowed. Please use POST'
    except Exception as error:
        logging.error(error, exc_info=True)
        return jsonify({"Error":"There is an internal error Please contact system administrators"}),400

@app.route('/cogbank/1.0/getCustomer/<string:customer>')
def getCustomer(customer):
    try:
        if session.get('username') is None:
            data = {'Status' : 'Please log in to get customer details'}
            logging.error(data)
            return jsonify(data), 404
            #return 'Please log in to get customer details'
        else:
            if customer:
            #user = User.query.get(customer)
                user = User.query.filter_by(username = customer).first()
                if user:
                    return customer_schema.dump(user), 200
                else:
                    data = {'Status' : 'The user is not registered'}
                    logging.error(data)
                    return jsonify(data), 404
            else:
                data = {'Status' : 'Please pass the customer query parameter'}
                logging.error(data)
                return jsonify(data), 202
    except Exception as error:
        logging.error(error, exc_info=True)
        return jsonify({"Error":"There is an internal error Please contact system administrators"}),400

@app.route('/cogbank/1.0/applyLoan/',methods=['POST'])
def applyLoan():
    try:
        if request.method == 'POST':
            request_data = request.get_json()
            username = request_data['username']
            LoanType = request_data['LoanType']
            LoanAmount = request_data['LoanAmount']
            Interest = request_data['Interest'] 
            Date = request_data['Date'] 
            Duration = request_data['Duration'] 
            if username:
                if session.get('username') is None:
                    data = {'Status' : 'Please log in to get customer details'}
                    logging.error(data)
                    return jsonify(data), 404
                user = User.query.filter_by(username = username).first()
                loan = Loan.query.filter_by(username = username).first()
                if loan:
                    if loan.username == username:
                        data = {'Status' : 'User has already applied loan. Only one loan can be applied'}
                        logging.error(data)
                        return jsonify(data), 202
                if user:
                    loan = Loan(
                    username = username,
                    LoanType = LoanType, 
                    LoanAmount = LoanAmount,
                    Interest = Interest,
                    Date = Date,
                    Duration = Duration
                    )
                    db.session.add(loan)
                    db.session.commit()
                    flash('You have successfully applied loan', 'success')
                    data = {'Status' : 'You have successfully applied loan'}
                    return jsonify(data), 200
                    #return 'You have successfully applied loan'
                else:
                    data = {'Status' : 'User {} is not registered'.format(username)}
                    logging.error(data) 
                    return jsonify(data), 202
                    #return 'User name {} not registered'.format(username)
            else:
                data = {'Status' : 'Please enter username'}
                logging.error(data) 
                return jsonify(data), 202
                #return 'please enter username'
        else:
            data = {'Status' : 'http method not supported. please use POST'}
            logging.error(data) 
            return jsonify(data), 400
            #return 'http method not supported. please use POST'
    except Exception as error:
        logging.error(error, exc_info=True)
        return jsonify({"Error":"There is an internal error Please contact system administrators"}),400

@app.route('/cogbank/1.0/getLoan/<string:customer>')
def getLoan(customer):
    try:
        #if customer in session['username']:
        if session.get('username') is None:
            return 'Please log in to get customer details'
        else:
            #user = User.query.get(customer)
            if customer:
                user = User.query.filter_by(username = customer).first()
                if user:
                    loanDetails = Loan.query.filter_by(username = customer).first()
                    if loanDetails:
                        return Loan_Schema.dump(loanDetails), 200
                    else:
                        logging.error('No Loan details found for user {}'.format(customer))
                        return {'Message': 'No Loan details found for user {}'.format(customer)}, 202
                else:
                    logging.error('User {} not found. Please register'.format(customer))
                    return {'Message':'User {} not found. Please register'.format(customer)}, 202
            else:
                logging.error('Please pass customer parameter')
                return {'Message':'Please pass customer parameter'},202
            logging.error('There is no Loan applied for user {}'.format(customer))
            return {'Messagte':'There is no Loan applied for user {}'.format(customer)}, 202
    except Exception as error:
        logging.error(error, exc_info=True)
        return jsonify({"Error":"There is an internal error Please contact system administrators"}),400

@app.route('/cogbank/1.0/logout/<string:username>')
def logout(username):
    try:
        #if username in session['username']:
        if session.get('username') is None: 
            session.pop('logged_in', None)
            session.pop('username', None)
            return {'Message':'You have logged out'}, 200
        else:
            return {'Message':'You have not logged in'}, 200
    except Exception as error:
        logging.error(error, exc_info=True)
        return jsonify({"Error":"There is an internal error Please contact system administrators"}),400

if __name__ == '__main__':
    db.create_all()
    app.run(debug=False,use_debugger=False)