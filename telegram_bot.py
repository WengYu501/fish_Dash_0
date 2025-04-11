import requests

BOT_TOKEN = "你的_Telegram_Bot_Token"
CHAT_ID = "你的_Chat_ID"

def send_telegram_alert(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, data=payload)
    return response.status_code