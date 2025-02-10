from flask import Flask, jsonify, send_file
import os

app = Flask(__name__)

@app.route('/')
def home():
    response = jsonify({"message": "Hello! Your API is running."})
    response.headers["bypass-tunnel-reminder"] = "true"  # Bypass LocalTunnel warning
    return response

@app.route('/openapi.json')
def openapi():
    return send_file("openapi.json", mimetype="application/json")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Use Render's assigned port
    app.run(host="0.0.0.0", port=port)

