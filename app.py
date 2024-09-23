from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/getcode')
def getcode():
    return "Hello!"

@app.route('/plus/<int:a>/<int:b>')
def get_code(a, b):
    c = a + b
    return str(c)
