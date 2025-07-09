from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://Undriling:Undriling34@cluster0.trxckcr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["webhook_db"]
collection = db["github_events"]

@app.route("/webhook", methods=["POST"])
def github_webhook():
    data = request.json
    event_type = request.headers.get("X-GitHub-Event", "ping")

    if event_type == "ping":
        return jsonify({"msg": "pong"}), 200

    if event_type == "push":
        author = data["pusher"]["name"]
        branch = data["ref"].split("/")[-1]
        timestamp = datetime.utcnow().isoformat()
        event_doc = {
            "action": "push",
            "author": author,
            "to_branch": branch,
            "timestamp": timestamp
        }

    elif event_type == "pull_request":
        action = data["action"]
        if action == "opened":
            author = data["pull_request"]["user"]["login"]
            from_branch = data["pull_request"]["head"]["ref"]
            to_branch = data["pull_request"]["base"]["ref"]
            timestamp = datetime.utcnow().isoformat()
            event_doc = {
                "action": "pull_request",
                "author": author,
                "from_branch": from_branch,
                "to_branch": to_branch,
                "timestamp": timestamp
            }
        elif action == "closed" and data["pull_request"]["merged"]:
            author = data["pull_request"]["merged_by"]["login"]
            from_branch = data["pull_request"]["head"]["ref"]
            to_branch = data["pull_request"]["base"]["ref"]
            timestamp = datetime.utcnow().isoformat()
            event_doc = {
                "action": "merge",
                "author": author,
                "from_branch": from_branch,
                "to_branch": to_branch,
                "timestamp": timestamp
            }
        else:
            return jsonify({"msg": "ignored"}), 200

    else:
        return jsonify({"msg": "unhandled event"}), 200

    collection.insert_one(event_doc)
    return jsonify({"msg": "event stored"}), 201

@app.route("/events", methods=["GET"])
def get_events():
    events = list(collection.find().sort("timestamp", -1).limit(10))
    for e in events:
        e["_id"] = str(e["_id"])
    return jsonify(events)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
