from flask import Flask, request
from flask_cors import CORS
import os
import base64

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

CORS(app)


@app.route('/upload/', methods=['GET', 'POST'])
def upload_image():
    target_dir = os.path.join(ROOT_DIR, 'images/')
    if not os.path.isdir(target_dir):
        os.mkdir(target_dir)

    if request.method == "POST":
        file = request.form['images']
        data = base64.b64decode(file)
        filenamed = 'some_image1.jpg'
        with open(filenamed, 'wb') as f:
            f.write(data)
        return "done", 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
