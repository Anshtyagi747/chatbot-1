from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get('msg')
    return f"You said: {user_input}"  # Temporary response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
