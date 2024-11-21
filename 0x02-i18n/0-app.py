#!/usr/bin/env python3
"""Basic flask server"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    """Returns a hello world page"""
    return render_template('0-index.html')

if __name__ == '__main__':  
   app.run()