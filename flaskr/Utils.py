import wget
import uuid
import os
from urllib.parse import urlparse

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def download_file_url(url):
	img_name = uuid.uuid1()
	path = os.path.join(APP_ROOT, f'imgs/{img_name}')
	try:
		file_path = wget.download(url, path)
		return file_path
	except:
		raise DownloadError()


def is_valid_url(url):
	if not url or "\n" in url or '\r' in url:
		return False
	try:
		result = urlparse(url)
		return all([result.scheme, result.netloc, result.path])
	except:
		return False


class DownloadError(BaseException):
	pass


class FaceDetectionError(BaseException):
	pass

