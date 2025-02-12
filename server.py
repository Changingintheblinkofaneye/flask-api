from flask import Flask, jsonify, send_file, request
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

# 🆕 New Vision Processing Endpoint
@app.route('/vision', methods=['POST'])
def process_vision():
    data = request.form
    seen_object = data.get("object", "nothing")

    # Simulating a GPT-like response (this can later be replaced with real GPT API calls)
    gpt_response = f"I see a {seen_object}. What should I do?"  

    return jsonify({"response": gpt_response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Use Render's assigned port
    app.run(host="0.0.0.0", port=port)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Use Render's assigned port
    app.run(host="0.0.0.0", port=port)
