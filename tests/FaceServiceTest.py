import unittest
from flaskr import FaceService


class MyTestCase(unittest.TestCase):
	def test_faceService(self):
		FaceService.detect_faces("https://peopledotcom.files.wordpress.com/2019/11/obama-family-thanksgiving.jpg")
		self.assertEqual(True, False)


if __name__ == '__main__':
	unittest.main()
