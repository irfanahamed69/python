from flask import Flask, jsonify, render_template, Request

app = Flask(__name__)

data = [{
    'name' : 'abc',
     'lang' : 'python'
},
{
    'name' : 'def',
     'lang' : 'java'
}]

@app.route('/developers')
def developer():
    return render_template('developers.html',var=data)

@app.route('/developers/<string:user>', methods=['GET'])
def user(user):
    for val in data:
        if val['name'] == user:
            return render_template('developers.html',var=[val])
    else:
        return (f'User {user} is not found'), 404
