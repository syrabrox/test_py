from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hi'

if __name__ == '__main__':
    port = random.randint(1024, 9000)
    app.run(host='0.0.0.0', port=port)
