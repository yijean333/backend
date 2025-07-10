from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
# 讀入 JSON 資料
with open('violations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

violations = data.get("test_road", [])

@app.route("/violations", methods=["GET"])
def get_all_violations():
    return jsonify(violations)

@app.route("/violations/latest", methods=["GET"])
def get_latest_violation():
    if violations:
        return jsonify(violations[-1])
    return jsonify({"error": "No data found"}), 404

@app.route("/violations/<camera_name>", methods=["GET"])
def get_by_camera(camera_name):
    filtered = [v for v in violations if v["camera_name"] == camera_name]
    return jsonify(filtered)

if __name__ == "__main__":
    app.run(debug=True)
