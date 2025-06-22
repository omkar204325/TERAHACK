from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "TERAHACK backend working ✅"

@app.route('/decode', methods=['POST'])
def decode():
    data = request.get_json()
    link = data.get("link")

    if not link or "terabox" not in link:
        return jsonify({"status": "error", "message": "Invalid link"}), 400

    stream_url = f"https://fake-stream.teraboxcdn.com/decoded/{hash(link)}.mp4"

    return jsonify({
        "status": "success",
        "stream_url": stream_url
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)