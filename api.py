from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)

# 允許指定前端網域跨域
CORS(app, origins=["https://yijean333.github.io"])

with open('violations.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

violations = data  # 把整包都拿來用

@app.route("/", methods=["GET"])
def health_check():
    return "OK", 200

@app.route("/violations/<camera_name>", methods=["GET"])
def get_by_camera(camera_name):
    today_only = request.args.get("today") == "1"

    records = violations.get(camera_name, [])

    if today_only:
        today = (datetime.utcnow() + timedelta(hours=8)).date()
        records = [
            v for v in records
            if datetime.strptime(v["time"], "%Y-%m-%d %H:%M:%S").date() == today
        ]

    return jsonify(records)
