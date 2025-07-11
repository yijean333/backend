from datetime import datetime
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open('violations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

violations = data.get("test_road", [])

@app.route("/violations/<camera_name>", methods=["GET"])
def get_by_camera(camera_name):
    today_only = request.args.get("today") == "1"

    filtered = [v for v in violations if v["camera_name"] == camera_name]

    if today_only:
        today = datetime.now().date()
        filtered = [
            v for v in filtered
            if datetime.strptime(v["time"], "%Y-%m-%d %H:%M:%S").date() == today
        ]

    return jsonify(filtered)
