from PY200.ll_drivers.linkedlist_2 import *
from abc import abstractmethod
from PY200.ll_drivers.structure_driver import *


class SDBuilder:
	@abstractmethod
	def build(self):
		return None


class JSONFileBuilder(SDBuilder):

	def build(self):
		filename = input('Enter filename (.json): ')
		return JSONFileDriver(filename)


class JSONStrBuilder(SDBuilder):
	def build(self):
		return JSONStringDriver()


class PickleBuilder(SDBuilder):
	def build(self):
		filename = input('Enter filename (.bin): ')
		return PickleDriver(filename)


class SDFabric:
	@staticmethod
	def get_sd_driver(driver_name):
		builders = {'json': JSONFileBuilder, 'json_str': JSONStrBuilder, 'pickle': PickleBuilder}
		try:
			return builders[driver_name]()
		except:
			return SDBuilder()

	def __str__(self):
		return self.get_sd_driver


if __name__ == '__main__':
	driver_name = input('enter driver name: ')
	driver_builder = SDFabric.get_sd_driver(driver_name)

	print(driver_builder)
