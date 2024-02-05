from subprocess import run
from abc import (abstractmethod, ABC)
from os.path import join

import argparse

def _get_cl_parameters() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help=".lnk file with all the links")
    return parser.parse_args()

class Browser(ABC):
	@abstractmethod
	def open_links(self, file_name: str):
		raise NotImplemented


class Brave(Browser):
	def __init__(self, folder: str) -> None:
		super(Browser, self).__init__()
		self._folder = folder

	def open_links(self, file_name: str):
		with open(join(self._folder, file_name), "r") as videos:
			for link in videos.readlines():
				run(f'brave -- {link}', shell=True)

		
if __name__ == "__main__":
	params = _get_cl_parameters()
	brave = Brave("files")
	brave.open_links(params.file_name)
