from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow cross-origin requests

@app.route('/decode', methods=['POST'])
def decode():
    data = request.get_json()
    link = data.get("link")

    # Placeholder decoding logic
    if not link or "terabox" not in link:
        return jsonify({"status": "error", "message": "Invalid link"}), 400

    # Simulated decoded stream link (replace with real logic)
    stream_url = f"https://fake-stream.teraboxcdn.com/decoded/{hash(link)}.mp4"

    return jsonify({
        "status": "success",
        "stream_url": stream_url
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)