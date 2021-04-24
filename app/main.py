from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
import random

app = Flask(__name__)


@app.route("/")
def mock():
    total_lots = 50
    free_lots = random.randint(30, 40)
    taken_lots = total_lots - free_lots
    return jsonify(
        total=total_lots,
        free=free_lots,
        taken=taken_lots
    )


@app.route('/mask_image', methods=['POST'])
def mask_image():
    try:
        file = request.files['file']
        return secure_filename(file.filename)
    except Exception as e:
        print(str(e))
