from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Set your OpenRouter API Key here
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")  # set this on Render.com

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_message = request.args.get('msg')
    if not user_message:
        return "Please type something!"

    # Send request to OpenRouter API
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openrouter/openai/gpt-3.5-turbo",
        "messages": [{"role": "user", "content": user_message}],
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
