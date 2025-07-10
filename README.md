# GitHub Webhook Event Processor

A **Flask-based backend** that listens for GitHub webhook events (push, pull requests, merges), saves them to MongoDB Atlas, and exposes an API to retrieve them for display in a frontend dashboard.

---

## 🚀 Features

✅ **Webhook Receiver**  
Receives GitHub webhook POST requests with event payloads.

✅ **Event Parsing**  
Intelligently parses different event types:
- Push
- Pull Request (opened)
- Merge (closed & merged)
- Other events are ignored or marked as unhandled.

✅ **MongoDB Storage**  
Stores event metadata (author, action, branches, timestamp) in MongoDB Atlas.

✅ **API Endpoint**  
Provides a REST endpoint to retrieve the latest events .

---

## 🛠️ Tech Stack

- Python 3
- Flask (web server)
- Flask-CORS (CORS support)
- PyMongo (MongoDB driver)
- MongoDB Atlas (cloud database)

---


## ⚙️ Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/Undriling/webhook-repo.git
cd webhook-techstax
pip install -r requirements.txt
```
---

## Start the Flask Server

```bash
python app.py
```

## Use ngrok to expose localhost server 

- About ngrok -
    ngrok creates a secure tunnel from a public URL to your local machine.
    This is essential for receiving webhooks from GitHub because your local server is normally not accessible from the internet.
    (For proper use please follow documentation)

    Run ngrok to expose the URL
    ```bash
    ngrok http 5000
    ```
