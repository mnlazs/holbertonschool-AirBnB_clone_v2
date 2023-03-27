#!/usr/bin/python3
"""
    Write a script that starts a Flask web application
"""


from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb', methods=['GET'])
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', methods=['GET'])
def c_text(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True, use_reloader=True)
