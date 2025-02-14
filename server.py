@app.route('/vision', methods=['POST'])
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
