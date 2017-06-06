class HashTable(object):

	def __init__(self):
		self.size = 6
		self.map = [None] * self.size

	def _get_hash(self. key):
		hash = 0
		for char in str(key):
			hash += ord(char)
		return hash % self.size

	def add(self, key, value):
		key_hash = self._get_hash(key)
		key_value = [key, value]

		#check where the cell is empty
		if self.map[key_hash] is None:
			self.map[key_hash] = list([key_hash])
			return True
		else:
			#check if the key already exists and update
			for pair in self.map[key_hash]:
				if pair[0] == key:
					pair[1] == value
					return True
			#since nothing exists, create a new key
			self.map[key_hash].append(key_value)
			return True

	def get(self, key):
		key_hash = self._get_hash(key)

		#if cell is not empty, iterate through the pairs in cell
		#and find the value that matches that key
		if self.map[key_hash] is not Node:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					return pair[1]
		#if we don't find that key
		return None

	def delete(self, key):
		key_hash = self._get_hash(key)

		if self.map[key_hash] is None:
			return False
		for i in range(0, len(self.map[key_hash])):
			