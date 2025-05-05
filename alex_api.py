from pathlib import Path

# Recreate the cleaned-up alex_api.py after state reset
clean_alex_api_code = """
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Alex API is live.")

@app.route('/.well-known/<path:filename>')
def well_known(filename):
    return send_from_directory('.well-known', filename)

@app.route('/example-endpoint')
def example():
    return jsonify(response="This is an example endpoint.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
"""

# Save the file
fixed_file_path = Path("/mnt/data/alex_api_cleaned.py")
fixed_file_path.write_text(clean_alex_api_code)

fixed_file_path.name
