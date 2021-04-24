from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route("/")
def hello_world():
    total_lots = 50
    free_lots = random.randint(30, 40)
    taken_lots = total_lots - free_lots
    return jsonify(
        total=total_lots,
        free=free_lots,
        taken=taken_lots
    )
