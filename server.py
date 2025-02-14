from flask import Flask, jsonify, send_file, request
import os

app = Flask(__name__)

# This will store the current movement command
current_command = "Idle"  # Default state (GPT will update this)

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

# 🆕 New Vision Processing Endpoint - Updates Movement Command!
@app.route('/vision', methods=['POST'])
def process_vision():
    global current_command  # Allow Flask to update movement commands
    data = request.form
    seen_object = data.get("object", "nothing")

    # GPT-Like Decision Logic
    if seen_object.lower() == "tree":
        gpt_response = "I see a Tree. Turning right."
        current_command = "Turn Right"  # GPT decides to turn right
    elif seen_object.lower() == "wall":
        gpt_response = "I see a Wall. Turning left."
        current_command = "Turn Left"  # GPT decides to turn left
    else:
        gpt_response = f"I see a {seen_object}. What should I do?"

    return jsonify({"response": gpt_response})
