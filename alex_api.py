from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ The endpoint that will receive prompts and respond
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")

    # You can change this later to something more advanced (like Mistral or GPT-4o)
    response_text = f"You said: {prompt}"

    return jsonify({ "response": response_text })


# 🔹 Optional: Still keep the example one if you want to test in browser
@app.route("/example-endpoint", methods=["GET"])
def example():
    return jsonify({ "response": "This is an example endpoint." })


# ✅ Launch the server (local only – not needed if you're using Render to deploy)
if __name__ == "__main__":
    app.run(debug=True)
