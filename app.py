import os
import json
from flask import Flask, request, jsonify
from amo import get_access_token, add_note_to_lead
from openai_utils import generate_ai_response
from logging_utils import log_event

app = Flask(__name__)

@app.route('/oauth', methods=['GET'])
def oauth_callback():
    # Получаем code и state из параметров запроса
    code = request.args.get('code')
    state = request.args.get('state')

    # Здесь будет логика обмена code на access_token через API amoCRM
    # Пока можно просто для теста:
    print(f"Authorization code: {code}, state: {state}")
    return "Авторизация прошла успешно. Код авторизации получен."

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    log_event('Received webhook', data)

    # Извлечение нужных данных из webhook amoCRM
    lead_id = extract_lead_id(data)  # реализовать по вашей структуре webhook
    fields = extract_fields(data)    # реализовать по вашей структуре webhook

    # Формируем промт для AI
    ai_prompt = make_prompt(fields)
    ai_response = generate_ai_response(ai_prompt)

    # Добавляем комментарий в сделку amoCRM
    access_token = get_access_token()
    add_note_to_lead(lead_id, ai_response, access_token)

    return jsonify({'status': 'ok'})

