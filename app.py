from flask import Flask
from flask_cors import CORS
from routes.webhook_routes import webhook_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(webhook_bp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
