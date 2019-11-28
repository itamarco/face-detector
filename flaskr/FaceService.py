from flaskr import Utils
from flaskr.Utils import FaceDetectionError
from flaskr.face_detect.face_detect_cv3 import count_faces

def detect_faces(img_url):
		img_path = Utils.download_file_url(img_url)
		try:
			return count_faces(img_path)
		except:
			raise FaceDetectionError