from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "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" 
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.json.get("message")

    payload = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [
            {"role": "system", "content": "Be concise. Only answer the question directly, no extras."},
            {"role": "user", "content": user_msg}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        data = response.json()
        reply = data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        reply = f"Error: {e}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
