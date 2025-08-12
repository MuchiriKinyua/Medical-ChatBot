from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def serve_index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # Placeholder response
    bot_reply = f"Generating: "

    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
