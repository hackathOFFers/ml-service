from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route("/")
def hello_world():
    free_lots = random.randint(30, 50)
    taken_lots = random.randint(20, 40)
    total_lots = free_lots + taken_lots
    return jsonify(
        total=total_lots,
        free=free_lots,
        taken=taken_lots
    )
