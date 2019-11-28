from flask import Flask, request
from flaskr import Utils
from flaskr.Utils import DownloadError, FaceDetectionError
from flaskr import FaceService
import logging
import os

# Initialize Flask
app = Flask(__name__)


@app.route("/")
def index():
	print(os.path.dirname(os.path.abspath(__file__)))
	return "Hello from Flask!"


@app.route("/detect-faces", methods=['POST'])
def detect_faces():
	url_input = request.form["url"]
	if not Utils.is_valid_url(url_input):
		return "bad url provided", 400

	try:
		total_faces = FaceService.detect_faces(url_input)
		return f"{total_faces}", 200
	except DownloadError:
		return f"could not download image from {url_input}", 500
	except FaceDetectionError as err:
		logging.exception(err)
		return f"failed to detect faces in {url_input}", 500


if __name__ == "__main__":
	# app.run(host='0.0.0.0', debug=True)
	app.run()