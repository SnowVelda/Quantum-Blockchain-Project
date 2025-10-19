
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Flask server is running on the phone!"

@app.route('/api/test')
def api_test():
    return jsonify({'message': 'Hello from your phone!'})

if __name__ == '__main__':
    # Running on port 8001 to avoid conflicts with other servers
    app.run(host='0.0.0.0', port=8001)
