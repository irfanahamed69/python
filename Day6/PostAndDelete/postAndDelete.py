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

@app.route('/groceries', methods=['GET','POST'])
def groceries():
    if request.method == 'GET':
        return render_template('groceries.html',var=data)

    elif request.method == 'POST':
        vegname = request.form['AddVeggie'] # run the groceries.html in browser to get the value
        qty = request.form['AddQuantity']
        # update the value in dictionary present inside list
        exists = next((item for item in data if item['vegetables'] == vegname),'Not Found')
        if exists != 'Not Found':
            oldqty = exists['quantity']
            exists['quantity'] = qty
            return (f'{vegname} is already present. quantity {oldqty} is replaced with {qty}')
        #append value to dict present in list
        else:
             data.append({'vegetables':vegname,'quantity':qty})
             return render_template('groceries.html',var=data)
         

@app.route('/groceries/<string:veg>', methods=['GET','DELETE'])
def user(veg):
    if request.method == 'GET':
        for val in data:
            if val['vegetables'] == veg:
                return render_template('groceries.html',var=[val])
        else:
            return (f'User {veg} is not found'), 404

    elif request.method == 'DELETE':
        exists = next((item for item in data if item['vegetables'] == veg),'Not Found')
        if exists != 'Not Found':
            # remove dict from list
            data.remove(exists) 
            return (f'User {veg} is deleted')

        else:
            return (f'User {veg} is not found'), 404
