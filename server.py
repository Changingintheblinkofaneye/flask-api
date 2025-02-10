from flask import Flask, jsonify, send_file

app = Flask(__name__)

@app.route('/')
def home():
    response = jsonify({"message": "Hello! Your API is running."})
    response.headers["bypass-tunnel-reminder"] = "true"  # Add this header to bypass LocalTunnel warning
    return response

@app.route('/openapi.json')
def openapi():
    return send_file("openapi.json", mimetype="application/json")

if __name__ == '__main__':
    app.run(port=5000)
