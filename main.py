import os
import subprocess

try:
    import flask
except ModuleNotFoundError:
    subprocess.run(["pip", "install", "flask"])

from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hi'

if __name__ == '__main__':
    port = random.randint(1024, 9999) 
    app.run(host='0.0.0.0', port=port)
