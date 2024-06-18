from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/ping")
def ping():
    return jsonify({'message': 'pong'})
@app.route("/")
def index():
    return jsonify({'message': 'hello world'})
if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0')
