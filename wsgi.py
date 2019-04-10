#!/usr/bin/env python

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
   return jsonify({'a': 1, 'b': 2, 'c': 3}) 

@app.route("/app")
def apphome():
   return jsonify({'a': 4, 'b': 5, 'c': 6}) 


if __name__ == "__main__":
   app.run()

