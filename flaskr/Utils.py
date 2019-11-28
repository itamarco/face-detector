import wget
from urllib.parse import urlparse
import uuid

def download_file_url(url):
	try:
		file_path = wget.download(url, f'../imgs/{uuid.uuid1()}')
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

