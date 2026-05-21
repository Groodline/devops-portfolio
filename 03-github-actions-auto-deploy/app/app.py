from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.route("/")
def home():
    return jsonify({
        "message": "Auto deploy with GitHub Actions works!",
        "version": APP_VERSION
    })


@app.route("/health")
def health():
    return jsonify({"status": "ok"})
