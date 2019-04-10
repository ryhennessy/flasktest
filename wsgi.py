#!/usr/bin/env python

from flask import Flask, jsonify

application = Flask(__name__)

@applicaton.route("/")
def home():
   return jsonify({'a': 1, 'b': 2, 'c': 3}) 

@applicaton.route("/app")
def apphome():
   return jsonify({'a': 4, 'b': 5, 'c': 6}) 


if __name__ == "__main__":
   applicaton.run()

