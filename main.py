import os.path
import caffe

from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
import random

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MODEL_FILE = BASE_DIR + "/model/snapshot_iter_942.caffemodel"
DEPLOY_FILE = BASE_DIR + "/model/deploy.prototxt"
MEAN_FILE = None
LABELS_FILE = None

UPLOAD_FOLDER = BASE_DIR + "/uploads/"

app = Flask(__name__)

net = caffe.Net(DEPLOY_FILE, MODEL_FILE, caffe.TEST)
caffe.set_mode_cpu()


# def preprocess():
#     size = (28, 28)
#     image =

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


@app.route('/count_lots', methods=['POST'])
def count_lots():
    try:
        file = request.files['file']
        out = net.forward(data=file)
        print(out)

    except Exception as e:
        print(str(e))
