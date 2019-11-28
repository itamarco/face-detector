import unittest
import os

from flaskr import Utils


class MyTestCase(unittest.TestCase):
	def test_downloadImage(self):
		Utils.download_file_url("https://media.wired.com/photos/5b8999943667562d3024c321/master/w_2560%2Cc_limit/trash2-01.jpg")
		self.assertTrue(os.path.exists("./pic.jpg"))


class UrlValidation(unittest.TestCase):
	def test_validUrl(self):
		res = Utils.is_valid_url("http://host.com/pics/img.jpg")
		self.assertTrue(res)

	def test_invalidUrl(self):
		res = Utils.is_valid_url("""https://via.placeholder.com/150

C/O https://placeholder.com/
			""""")
		self.assertFalse(res)


if __name__ == '__main__':
	unittest.main()
