#!/usr/bin/env python

from application import generate_passwords
from flask import Flask, jsonify
from flask_restplus import Resource, Api, Namespace
app = Flask(__name__)
api = Api(app)

pw_api = Namespace('passwords', description='XKCD style passwords')
api.add_namespace(pw_api)

# Create a REST resource
@pw_api.route('/', '/words/<int:words>/amount/<int:amount>')
class Password(Resource):
    def get(self, words=4, amount=10):
        return jsonify({"passwords": generate_passwords(words,amount)})

if __name__ == '__main__':
    app.run(debug=True)
