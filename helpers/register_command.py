import requests
import os


url = f"https://discord.com/api/v10/applications/{os.getenv('APP_ID')}/commands"

# This is an example CHAT_INPUT or Slash Command, with a type of 1
zen_json = {
    "name": "zen",
    "type": 1,
    "description": "Make zen"
}

log_a_match_json = {
    "name":         "log_a_match",
    "type":         1,
    "description":  "After you play a tag match, use this command to log the results."
}

headers = {
    "Authorization": f"Bot {os.getenv('BOT_TOKEN')}",
    "Content-Type": "application/json"
}

r = requests.post(url, headers=headers, json=log_a_match_json)
print(r.status_code)
print(r.text)
