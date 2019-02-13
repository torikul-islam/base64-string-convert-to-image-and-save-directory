from flask import Flask, request
from datetime import datetime
from flask_cors import CORS
import os
import base64

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
CORS(app)


def base64_to_image(base64_string):
    target_dir = os.path.join(ROOT_DIR, 'images/')
    if not os.path.isdir(target_dir):
        os.mkdir(target_dir)

    data = base64.b64decode(base64_string)
    filename = "frame_" + str(datetime.utcnow()) + ".jpg"
    destination = "/".join([target_dir, filename])
    with open(destination, 'wb') as f:
        f.write(data)


@app.route('/upload/', methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
        file = request.form['images']
        base64_to_image(file)
        return "Successfully uploaded.", 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
