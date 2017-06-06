class Node:
	def __init__(self, x):
		self.val = x
		self.next = None
		self.prev = None

class Deque:
	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0

	def pushFront(self, x):
		node = Node(x)

		if self.count == 0:
			self.head = node
			self.tail = self.head

		else:
			node.next = self.head
			self.head.prev = node
			self.head = node

		self.count += 1

	def pushBack(self, x):
		node = Node(x)

		if self.count == 0:
			self.head = node
			self.tail = self.head

		else:
			self.tail.next = node
			node.prev = self.tail
			self.tail = node

	def popFront(self):
		if self.count == 0:
			return None
		elif self.count == 1:
			self.head = None
			self.head = None
		else:
			self.head = self.head.next
			self.head.prev = None

		self.count -= 1

	def popBack(self):
		if self.count == 0:
			return None
		elif self.count == 1:
			self.head = None
			self.tail = None
		else:
			self.tail = self.tail.prev
			self.tail.next = None

	def peekFront(self):
		if self.head is None:
			return None
		return self.head.val

	def peekBack(self):
		if self.tail is None:
			return None
		return self.tail.val

	def size(self):
		return self.count

	def empty(self):
		return self.count == 0