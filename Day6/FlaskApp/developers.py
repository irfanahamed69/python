from flask import Flask, jsonify, render_template

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
