
import os
from neocitizen import NeocitiesApi

# Your dummy API key from the example script
NEOCITIES_API_KEY = "e629db8800d43833d4724eb190fa8b7e"

# Initialize the Neocities API client with the correct argument
api = NeocitiesApi(api_key=NEOCITIES_API_KEY)

# --- Upload the chatbot file ---
LOCAL_FILE_PATH = "/data/data/com.termux/files/home/deso_chatbot/index.html"
REMOTE_FILE_PATH = "deso_chatbot.html" # The name it will have on Neocities

print(f"--- Uploading {LOCAL_FILE_PATH} to Neocities as {REMOTE_FILE_PATH} ---")
try:
    # Use the correct upload_files method with the correct dictionary format
    # {local_path: remote_path}
    upload_response = api.upload_files({LOCAL_FILE_PATH: REMOTE_FILE_PATH})
    print(f"Upload response: {upload_response}")
    
    # --- Get site information to find the URL ---
    site_info = api.fetch_info()
    if site_info and "info" in site_info:
        site_name = site_info["info"]["sitename"]
        print("\n--- DEPLOYMENT SUCCESSFUL ---")
        print(f"The chatbot is now live at: https://{site_name}.neocities.org/{REMOTE_FILE_PATH}")
    else:
        print("\nCould not retrieve site URL, but upload may have succeeded.")

except Exception as e:
    print(f"\n--- DEPLOYMENT FAILED ---")
    print(f"Error uploading file: {e}")
