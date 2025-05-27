import openai
import os

def generate_ai_response(prompt):
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Ты профессиональный AI-ассистент ArtCode Neuro."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']
