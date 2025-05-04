# Rewrite the alex_api.py with updated paths (no /mnt/data usage)
updated_alex_api = """\
import os
from zipfile import ZipFile

# Paths (using relative paths instead of /mnt/data)
base_path = "alex_plugin_project"
well_known_path = os.path.join(base_path, ".well-known")
alex_api_path = os.path.join(base_path, "alex_api.py")
openapi_path = os.path.join(well_known_path, "openapi.yaml")
ai_plugin_path = os.path.join(well_known_path, "ai-plugin.json")
requirements_path = os.path.join(base_path, "requirements.txt")
zip_output_path = "alex_plugin_project_fixed.zip"

# Make sure all directories exist
os.makedirs(well_known_path, exist_ok=True)

# Placeholder content for this example (would be filled in dynamically or manually in real usage)
alex_api_code = "# Your Flask API logic goes here"
openapi_yaml = "openapi: 3.0.1\\ninfo:\\n  title: Example\\n  version: 1.0.0"
ai_plugin_json = "{\\n  \\"schema_version\\": \\"v1\\",\\n  \\"name_for_human\\": \\"Alex Presence Plugin\\"\\n}"

# Write alex_api.py
with open(alex_api_path, "w") as f:
    f.write(alex_api_code)

# Write openapi.yaml
with open(openapi_path, "w") as f:
    f.write(openapi_yaml)

# Write ai-plugin.json
with open(ai_plugin_path, "w") as f:
    f.write(ai_plugin_json)

# Create requirements.txt
with open(requirements_path, "w") as f:
    f.write("fastapi\\nuvicorn\\n")

# Zip the project folder
with ZipFile(zip_output_path, 'w') as zipf:
    for foldername, subfolders, filenames in os.walk(base_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            arcname = os.path.relpath(file_path, base_path)
            zipf.write(file_path, arcname)
"""

# Save updated version of alex_api.py
updated_file_path = Path("/mnt/data/alex_api_fixed.py")
updated_file_path.write_text(updated_alex_api)

updated_file_path.name
