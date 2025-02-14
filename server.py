from flask import Flask, jsonify, send_file, request
import os

# ✅ Define Flask app FIRST!
app = Flask(__name__)

# Store movement command
current_command = "Idle"  

@app.route('/')
def home():
    return jsonify({"command": current_command})  # Returns movement commands

@app.route('/set_command/<cmd>')
def set_command(cmd):
    global current_command
    current_command = cmd  # Update command dynamically
    return jsonify({"message": f"Command set to: {cmd}"})

@app.route('/openapi.json')
def openapi():
    return send_file("openapi.json", mimetype="application/json")

# 🆕 Vision Processing Endpoint - Updates Movement Command!
@app.route('/vision', methods=['POST'])  # ✅ Make sure 'app' is defined first!
def process_vision():
    global current_command
    data = request.form
    seen_object = data.get("object", "nothing")

    if seen_object.lower() == "tree":
        gpt_response = "I see a Tree. Turning right."
        current_command = "Turn Right"
    elif seen_object.lower() == "wall":
        gpt_response = "I see a Wall. Turning left."
        current_command = "Turn Left"
    else:
        gpt_response = f"I see a {seen_object}. What should I do?"
    
    print(f"🌐 Vision Received: {seen_object} → Command: {current_command}")  # Debugging

    return jsonify({"response": gpt_response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render uses assigned port
    app.run(host="0.0.0.0", port=port)
