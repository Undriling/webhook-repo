from pymongo import MongoClient

MONGO_URI = (
    "mongodb+srv://Undriling:Undriling34@cluster0.trxckcr.mongodb.net/"
    "?retryWrites=true&w=majority&appName=Cluster0"
)

client = MongoClient(MONGO_URI)
db = client["webhook_db"]
collection = db["github_events"]
