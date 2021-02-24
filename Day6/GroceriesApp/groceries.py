from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

data = [{
    'vegetables' : 'carrot',
     'quantity' : 5
},
{
    'vegetables' : 'Potato',
     'quantity' : 4
}]

@app.route('/groceries')
def groceries():
    return render_template('groceries.html',var=data)

@app.route('/groceries/<string:veg>', methods=['GET'])
def user(veg):
    for val in data:
        if val['vegetables'] == veg:
            return render_template('groceries.html',var=[val])
    else:
        return (f'User {veg} is not found'), 404
