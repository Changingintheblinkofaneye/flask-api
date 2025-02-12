from flask import Flask, jsonify, send_file
import os

app = Flask(__name__)

# This will store the current movement command
current_command = "Idle"  # Default state (can be changed dynamically)

@app.route('/')
def home():
    response = jsonify({"command": current_command})  # Now returns movement commands
    response.headers["bypass-tunnel-reminder"] = "true"  # Bypass LocalTunnel warning
    return response

@app.route('/set_command/<cmd>')
def set_command(cmd):
    global current_command
    current_command = cmd  # Update command dynamically
    return jsonify({"message": f"Command set to: {cmd}"})

@app.route('/openapi.json')
def openapi():
    return send_file("openapi.json", mimetype="application/json")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Use Render's assigned port
    app.run(host="0.0.0.0", port=port)
