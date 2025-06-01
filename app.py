from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form.get('message', '')
    image = request.files.get('image')

    # Trenutno ignorišemo sliku, može se proširiti kasnije
    prompt = f"Korinsik kaže: {message}"

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    reply = response.choices[0].message.content
    return jsonify({"reply": reply})
