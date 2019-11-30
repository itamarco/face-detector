import unittest
import os

from flaskr import Utils
from flaskr.Utils import DownloadError


class DownloadFile(unittest.TestCase):
	def test_downloadImage(self):
		img_path = Utils.download_file_url("https://media.wired.com/photos/5b8999943667562d3024c321/master/w_2560%2Cc_limit/trash2-01.jpg")
		print(img_path)
		self.assertTrue(os.path.exists(img_path))

	def test_inavlidUrl(self):
		with self.assertRaises(DownloadError):
			Utils.download_file_url("http://www.not-exist-img.com/lie.jpg")

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
