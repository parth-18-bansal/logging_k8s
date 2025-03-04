from flask import Flask, jsonify
import logging
import random
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

#configuring logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

#Define prometheus metrics
REQUEST_COUNT = Counter("http_requests_total", "Total number of HTTP requests", ["endpoint"])

@app.route("/")
def home():
    REQUEST_COUNT.labels(endpoint="/").inc()
    logger.info("Home endpoint accessed")
    return jsonify({"message": "Hello, World!"})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain"}

@app.route("/error")
def error():
    REQUEST_COUNT.labels(endpoint="/error").inc()
    if random.choice([True, False]):
        logger.error("Simulated error occurred")
        return jsonify({"error": "Something went wrong"}), 500
    return jsonify({"message": "No error"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)