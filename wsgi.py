#!/usr/bin/env python

from flask import Flask, jsonify

application = Flask(__name__)

@application.route("/")
def home():
   return jsonify({'a': 1, 'b': 3, 'c': 3}) 

@application.route("/app")
def apphome():
   return jsonify({'a': 4, 'b': 5, 'c': 6}) 


if __name__ == "__main__":
   application.run()

