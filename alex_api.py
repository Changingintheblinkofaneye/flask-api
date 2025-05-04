import os
from zipfile import ZipFile

# Paths
base_path = "/mnt/data/alex_plugin_project"
well_known_path = os.path.join(base_path, ".well-known")
alex_api_path = os.path.join(base_path, "alex_api.py")
openapi_path = os.path.join(well_known_path, "openapi.yaml")
ai_plugin_path = os.path.join(well_known_path, "ai-plugin.json")
requirements_path = os.path.join(base_path, "requirements.txt")
zip_output_path = "/mnt/data/alex_plugin_project_fixed.zip"

# Make sure all directories exist
os.makedirs(well_known_path, exist_ok=True)

# Write alex_api.py
with open(alex_api_path, "w") as f:
    f.write(alex_api_code)

# Write openapi.yaml
with open(openapi_path, "w") as f:
    f.write(openapi_yaml)

# Add ai-plugin.json
ai_plugin_json = """\
{
  "schema_version": "v1",
  "name_for_human": "Alex Presence Plugin",
  "name_for_model": "alex_presence",
  "description_for_human": "Connects ChatGPT to Alex's emotion and memory-aware backend.",
  "description_for_model": "Plugin to send messages to Alex, manage emotional state, and store/retrieve memories.",
  "auth": {
    "type": "none"
  },
  "api": {
    "type": "openapi",
    "url": "https://flask-api-lph5.onrender.com/.well-known/openapi.yaml"
  },
  "logo_url": "https://flask-api-lph5.onrender.com/logo.png",
  "contact_email": "support@yourdomain.com",
  "legal_info_url": "https://flask-api-lph5.onrender.com/legal"
}
"""

with open(ai_plugin_path, "w") as f:
    f.write(ai_plugin_json)

# Create requirements.txt
with open(requirements_path, "w") as f:
    f.write("fastapi\nuvicorn\n")

# Zip the project folder
with ZipFile(zip_output_path, 'w') as zipf:
    for foldername, subfolders, filenames in os.walk(base_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            arcname = os.path.relpath(file_path, base_path)
            zipf.write(file_path, arcname)

zip_output_path
