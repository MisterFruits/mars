#!/usr/bin/env python
from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/api/0.1/genes/<lib>')
def index():
    return "Hello, World!"

@app.route('/api/0.1/exons/<lib>')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
