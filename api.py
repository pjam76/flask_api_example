#!/usr/bin/env python

from application import generate_passwords
from flask import Flask, jsonify
from flask_restplus import Resource, Api
app = Flask(__name__)
api = Api(app)

# Create a REST resource
@api.route('/password', '/password/<int:words>/<int:amount>')
class Password(Resource):
    def get(self, words=4, amount=10):
        return jsonify({"passwords": generate_passwords(words,amount)})

if __name__ == '__main__':
    app.run(debug=True)
