from flask import Flask, jsonify, send_from_directory
from random import randint

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the HTML visualization file
    return send_from_directory('.', 'index.html')

@app.route('/data')
def data():
    # Return random data as JSON
    return jsonify({"value": randint(1, 100)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
