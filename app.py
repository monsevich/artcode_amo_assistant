import os
import json
from flask import Flask, request, jsonify
from amo import get_access_token, add_note_to_lead
from openai_utils import generate_ai_response
from logging_utils import log_event

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
