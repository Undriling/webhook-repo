from datetime import datetime

def parse_event(event_type, data):
    timestamp = datetime.utcnow().isoformat()

    if event_type == "push":
        return {
            "action": "push",
            "author": data["pusher"]["name"],
            "to_branch": data["ref"].split("/")[-1],
            "timestamp": timestamp,
        }

    elif event_type == "pull_request":
        action = data["action"]
        if action == "opened":
            return {
                "action": "pull_request",
                "author": data["pull_request"]["user"]["login"],
                "from_branch": data["pull_request"]["head"]["ref"],
                "to_branch": data["pull_request"]["base"]["ref"],
                "timestamp": timestamp,
            }
        elif action == "closed" and data["pull_request"]["merged"]:
            return {
                "action": "merge",
                "author": data["pull_request"]["merged_by"]["login"],
                "from_branch": data["pull_request"]["head"]["ref"],
                "to_branch": data["pull_request"]["base"]["ref"],
                "timestamp": timestamp,
            }

    return None
