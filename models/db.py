from config import collection

def insert_event(event_doc):
    collection.insert_one(event_doc)

def get_recent_events(limit=10):
    events = list(collection.find().sort("timestamp", -1).limit(limit))
    for e in events:
        e["_id"] = str(e["_id"])
    return events
