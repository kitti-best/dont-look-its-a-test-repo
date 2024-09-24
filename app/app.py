from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/getcode')
def getcode():
    return "Hello!"

@app.route('/plus/<a>/<b>')
def plus(a, b):
    try:
        c = float(a) + float(b)
    except ValueError:
        c = f"Error can not perform PLUS operation between {a} and {b}"
    return {"result":c}
