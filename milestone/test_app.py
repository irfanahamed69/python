from app import app as flask_app
from app import db, User, Loan
from flask import session
import pytest
import requests
import json


@pytest.fixture(scope='session')
def app():
    yield flask_app


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()

def test_register(app,client):
    data = {
            "name":"Test6",
            "username":"Test6",
            "email":"Test6@google.com",
            "password":"Test6",
            "address":"Test6 add",
            "state":"Test6 st",
            "country":"Test6 cn",
            "pan":"12345TEST6",
            "contactNumber":"3765532197",
            "dob":"30-Mar-2021"
            }
    response = client.post('/cogbank/1.0/register/',data=json.dumps(data),content_type='application/json')
    print(response.data)
    assert response.status_code == 200

def test_login(app,client):
    data =  {
            "username":"Test6",
            "password":"Test6"
            }
    response = client.post('/cogbank/1.0/login/',data=json.dumps(data),content_type='application/json')
    print(response.data)
    assert response.status_code == 200

#@pytest.mark.skipif(1==1, reason="Will use this test depending upon test case scenarios")
def test_updateCustomer(app,client):
    data = {
            "name":"Test6",
            "username":"Test6",
            "address":"Test6 testing",
            "state":"Test6 state",
            "country":"Test6 country",
            "pan":"12345TEST6",
            "contactNumber":"498376655",
            "dob":"29-Mar-2021"
            }
    response = client.post('/cogbank/1.0/updateCustomer/',data=json.dumps(data),content_type='application/json')
    print(response.data)
    assert response.status_code == 200

def test_getCustomer(app, client):
    res = client.get('/cogbank/1.0/getCustomer/Test6')
    print(res.data)
    assert res.status_code == 200

def test_applyLoan(app,client):
    data = {
            "username":"Test6",
            "address":"Test6 testing",
            "LoanType":"Fixed",
            "LoanAmount":100,
            "Interest":2,
            "Date":"2021-03-19",
            "Duration":"1 month"
            }
    response = client.post('/cogbank/1.0/applyLoan/',data=json.dumps(data),content_type='application/json')
    print(response.data)
    assert response.status_code == 200

def test_getLoan(app, client):
    res = client.get('/cogbank/1.0/getLoan/Test6')
    print(res.data)
    assert res.status_code == 200

#@pytest.mark.skipif(1==1,reason="Will use this test depending upon test case scenarios")
def test_logout(app, client):
    res = client.get('/cogbank/1.0/logout/Test6')
    print(res.data)
    assert res.status_code == 200


    
