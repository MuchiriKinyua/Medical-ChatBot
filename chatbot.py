from flask import Flask, render_template, request, jsonify
from app import final_result

app = Flask(__name__)

@app.route('/')
def serve_index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        bot_reply = final_result(user_message)
        # Since final_result returns a dict with 'result', get that:
        if isinstance(bot_reply, dict) and 'result' in bot_reply:
            bot_reply = bot_reply['result']
    except Exception as e:
        bot_reply = f"⚠️ Error: {str(e)}"

    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
