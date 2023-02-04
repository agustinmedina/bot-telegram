import requests
import os

bot_token = "5757222060:"
chat_id = "-84"
message = "Message for Python"

url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"

response = requests.get(url)

print(response.content)
