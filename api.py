from datetime import datetime
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open('violations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

violations = data  # 把整包都拿來用

@app.route("/violations/<camera_name>", methods=["GET"])
def get_by_camera(camera_name):
    today_only = request.args.get("today") == "1"

    records = violations.get(camera_name, [])

    if today_only:
        today = datetime.now().date()
        records = [
            v for v in records
            if datetime.strptime(v["time"], "%Y-%m-%d %H:%M:%S").date() == today
        ]

    return jsonify(records)
