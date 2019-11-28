import unittest
from flaskr.face_detect.face_detect_cv3 import count_faces
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

class MyTestCase(unittest.TestCase):
	def test_something(self):
		img_path = os.path.join(APP_ROOT, "abba.png")
		total_faces = count_faces(img_path)
		self.assertEqual(total_faces, 4)


if __name__ == '__main__':
	unittest.main()
