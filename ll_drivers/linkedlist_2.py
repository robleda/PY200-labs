from weakref import ref
from PY200.ll_drivers.builders import *


class LinkedList:
	class Node:
		"""
		Модуль связанного списка. Внутри списка лежат ноды с данными.
		У нодов есть сильные ссылки на следующие элементы и слабые ссылки на предыдущие
		"""

		def __init__(self, prev_node=None, next_node=None, data=None):

			if prev_node is not None and not isinstance(prev_node, type(self)):
				raise TypeError('prev_node must be Node or None')

			if next_node is not None and not isinstance(next_node, type(self)):
				raise TypeError('next_node must be Node or None')

			self.prev_node_ = ref(prev_node) if prev_node is not None else None
			self.next_node_ = next_node
			self.data = data

		@property
		def prev_node(self):
			return self.prev_node_() if self.prev_node_ is not None else None

		@prev_node.setter
		def prev_node(self, value):
			if value is not None and not isinstance(value, type(self)):
				raise TypeError('Value must be Node or None')
			self.prev_node_ = ref(value) if value is not None else None

		@property
		def next_node(self):
			return self.next_node_

		@next_node.setter
		def next_node(self, value):
			if value is not None and not isinstance(value, type(self)):
				raise TypeError('Value must be Node or None')
			self.next_node_ = value

		def __str__(self):
			return f'{self.data}'

		def __repr__(self):
			return f'LinkedList.Node({self.prev_node}, {self.next_node}, {self.data})'

	def __init__(self):
		self.size = 0
		self.head = self.Node()
		self.tail = self.Node(self.head)
		self.head.next_node = self.tail
		self.__structure_driver = None

	def _insert_next_node(self, current_node, data):
		"""
		Внутренний метод вставки ноды.
		Используется в insert_node и append
		:param current_node: нода, после которой будет вставлена новая нода
		:param data: данные новой ноды
		"""
		new_node = self.Node(current_node, current_node.next_node, data)
		current_node.next_node.prev_node = new_node
		current_node.next_node = new_node
		self.size += 1

	def insert_node(self, index, data):
		"""
		Вставка ноды с неким индексом в список
		node - нода
		index - индекс ноды
		"""
		if not isinstance(index, int):
			raise TypeError('index must be int')

		if index >= 0:
			if not 0 <= index <= self.size:
				raise ValueError('Invalid index')
			current_node = self.head
			for i in range(self.size + 1):
				if i == index:
					self._insert_next_node(current_node, data)
				else:
					current_node = current_node.next_node
					continue
		if index < 0:
			if not self.size * (-1) <= index < 0:
				raise ValueError('Invalid index')
			current_node = self.tail.prev_node
			for i in range(-1, self.size * (-1), -1):
				if i == index:
					self._insert_next_node(current_node, data)
				else:
					current_node = current_node.prev_node

	def append(self, data):
		"""
		Вставка ноды в конец списка
		data - данные ноды, которую аппендим
		"""
		if self.size == 0:
			self._insert_next_node(self.head, data)
		else:
			current_node = self.head.next_node
			for i in range(self.size - 1):
				current_node = current_node.next_node
			self._insert_next_node(current_node, data)

	def clear(self):
		"""
		Очищает список
		"""
		self.size = 0
		self.tail.prev_node = self.head
		self.head.next_node = self.tail

	def find(self, node):
		"""
		Поиск в списке по данным
		:param node: данные для поиска
		:return: возвращает индекс ноды (первой от головы!), в которой найдено искомое
		"""
		current_node = self.head.next_node
		for i in range(self.size):
			if current_node.data == node:
				return i
			else:
				current_node = current_node.next_node
		print('Такого не найдено :(')

	def get_data(self, index):
		"""
		Возвращает ноду по индексу
		:param index: индекс искомой ноды
		:return: данные ноды, которую искали
		"""
		if not isinstance(index, int):
			raise TypeError('index must be int')

		if index >= 0:
			if not 0 <= index <= self.size:
				raise ValueError('Invalid index')
			current_node = self.head.next_node
			for _ in range(self.size):
				if _ == index:
					return current_node
				else:
					current_node = current_node.next_node
		if index < 0:
			if not self.size * (-1) <= index < 0:
				raise ValueError('Invalid index')
			current_node = self.tail.prev_node
			for _ in range(-1, self.size * (-1), -1):
				if _ == index:
					return current_node
				else:
					current_node = current_node.prev_node

	def __remove(self, node: Node):
		"""
		Внутренний метод. Удаляет заданную ноду из списка, убирает ссылки на ее соседей
		Используется в методе delete
		:param node: нода, которую надо удалить
		:return: ничего не возвращает, просто затирает ноду
		"""
		current_node = node
		pr_node = current_node.prev_node
		nx_node = current_node.next_node
		pr_node.next_node = nx_node
		nx_node.prev_node = pr_node
		self.size -= 1
		return

	def delete(self, index):
		"""
		Удаляет ноду с заданным индексом
		:param index: индекс ноды для удаления
		:return: ничего не возвращает, просто затитрает
		"""
		if not isinstance(index, int):
			raise TypeError('index must be int')

		if index >= 0:
			if not 0 <= index <= self.size:
				raise ValueError('Invalid index')
			current_node = self.head.next_node
			for _ in range(self.size):
				if _ == index:
					self.__remove(current_node)
				else:
					current_node = current_node.next_node
		if index < 0:
			if not self.size * (-1) <= index < 0:
				raise ValueError('Invalid index')
			current_node = self.tail.prev_node
			for _ in range(-1, self.size * (-1), -1):
				if _ == index:
					self.__remove(current_node)
				else:
					current_node = current_node.prev_node

	def show(self):
		"""
		Показывает нам Живые ноды из нашего списка
		"""
		if self.size == 0:
			print('Linked list is empty!')
		else:
			current_node = self.head.next_node
			for i in range(self.size):
				print(f'index: {i}, node data: {current_node}')
				current_node = current_node.next_node

# # #

	def __to_dict(self):
		d = {}
		current_node = self.head.next_node
		i = 0
		while i < self.size:
			d[i] = current_node.__str__()
			i += 1
			current_node = current_node.next_node
		return d

	def __from_dict(self, d):
		for index, data in d.items():
			self.insert_node(int(index), data)
		print(self.__to_dict())

	def read(self):
		self.__from_dict(self.__structure_driver.read())

	def write(self):
		self.__structure_driver.write(self.__to_dict())

	def set_structure_driver(self, structure_driver):
		self.__structure_driver = structure_driver


if __name__ == '__main__':
	driver_name = input('enter driver name: ')
	driver_builder = SDFabric.get_sd_driver(driver_name)
	driver = driver_builder.build()

	ll = LinkedList()
	ll.set_structure_driver(driver)
	ll.read()
	ll.show()
