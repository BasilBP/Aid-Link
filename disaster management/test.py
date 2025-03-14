import requests

# Replace with your Telegram bot token
BOT_TOKEN = "7510873387:AAE3nAGacP37Xiz7xGwGEyNDxToeRMd3SjE"

# List of chat IDs (Users or Groups)
CHAT_IDS = ["gauthamfr"]  # Add more as needed

# Your message
MESSAGE = "🚀 Broadcast Message: Stay Safe & Alert!"

def send_telegram_message(chat_id, message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {

        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    return response.json()

# Broadcast message to all chat IDs
for chat_id in CHAT_IDS:
    response = send_telegram_message(chat_id, MESSAGE)
    print(f"Message sent to {chat_id}: {response}")
