import os
import requests
import time

def get_access_token():
    # Если есть валидный токен — вернуть его
    # Если нет — обновить через refresh_token
    # Здесь можно реализовать логику хранения/обновления токена
    # Пока просто из переменных окружения (для MVP)
    return os.environ.get("AMO_ACCESS_TOKEN")

def add_note_to_lead(lead_id, text, access_token):
    domain = os.environ.get("AMO_DOMAIN")
    url = f"https://{domain}/api/v4/leads/{lead_id}/notes"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    note = {
        "note_type": "common",
        "params": {
            "text": text
        }
    }
    response = requests.post(url, headers=headers, json=[note])
    return response.json()
