from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    user = {}
    return jsonify({'name': 'akram'})