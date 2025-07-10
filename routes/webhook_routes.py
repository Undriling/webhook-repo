from flask import Blueprint, request, jsonify
from models.db import insert_event, get_recent_events
from utils.event_parser import parse_event

webhook_bp = Blueprint("webhook", __name__)

@webhook_bp.route("/webhook", methods=["POST"])
def github_webhook():
    data = request.json
    event_type = request.headers.get("X-GitHub-Event", "ping")

    if event_type == "ping":
        return jsonify({"msg": "pong"}), 200

    event_doc = parse_event(event_type, data)

    if event_doc is None:
        if event_type == "pull_request":
            return jsonify({"msg": "ignored"}), 200
        return jsonify({"msg": "unhandled event"}), 200

    insert_event(event_doc)
    return jsonify({"msg": "event stored"}), 201

@webhook_bp.route("/events", methods=["GET"])
def get_events():
    events = get_recent_events()
    return jsonify(events)
