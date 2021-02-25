from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

veggie = [{
    'vegetables': 'carrot',
    'quantity': 1
        },
    {
    'vegetables': 'spinach',
    'quantity': 2
}
]


def abort_if_todo_doesnt_exist(vegName):
    index = 0
    for veg in veggie:
        if veg['vegetables'] == vegName:
            return index
        index = index + 1
    else:
        abort(404, message='Veggie {} does not exist'.format(vegName))  # displays message in json


parser = reqparse.RequestParser()
parser.add_argument('veg')
parser.add_argument('qty')

class UpdateVegetables(Resource):
    def get(self, vegName):
        position = abort_if_todo_doesnt_exist(vegName)
        return veggie[position]

    def delete(self, vegName):
        position = abort_if_todo_doesnt_exist(vegName)
        del veggie[position]
        return 'Veggie {} deleted'.format(vegName)

    def put(self, vegName):
        args = parser.parse_args()
        position = abort_if_todo_doesnt_exist(vegName)
        veggie[position]['quantity'] = args['qty']
        return veggie[position]


class Vegetables(Resource):
    def get(self):
        return jsonify(veggie)

    def post(self):
        args = parser.parse_args()
        veggie.append({'vegetables' : args['veg'], 'quantity' : args['qty']})
        return veggie


api.add_resource(Vegetables, '/Vegetables')
api.add_resource(UpdateVegetables, '/Vegetables/<string:vegName>')
