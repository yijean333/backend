from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime, timedelta
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
        within = request.args.get("within")  # 取得查詢參數

    filtered = [v for v in violations if v["camera_name"] == camera_name]

    if within == "1d":
        one_day_ago = datetime.now() - timedelta(days=1)
        # 假設你的時間格式是像 "2024-07-11 14:30:00"
        filtered = [
            v for v in filtered
            if datetime.strptime(v["time"], "%Y-%m-%d %H:%M:%S") >= one_day_ago
        ]

if __name__ == "__main__":
    app.run(debug=True)
