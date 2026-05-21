from flask import Flask, request
import requests

app = Flask(__fakhirbot__)

BOT_TOKEN = "8686975477:AAGrmKRCBhgBRyzw9Ux44pdfDqv4Ba7yTJc"
CHANNEL_ID = "-1003620161496"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHANNEL_ID,
        "text": text
    }

    requests.post(url, json=payload)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    message = f"""
Signal Alert

Symbol: {data.get('ticker')}
Price: {data.get('price')}
Action: {data.get('action')}
"""

    send_message(message)

    return "OK"

@app.route('/')
def home():
    return "Bot Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
