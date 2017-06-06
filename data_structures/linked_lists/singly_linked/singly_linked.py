class Node(object):
	def __init__(self, data, next = None):
		self.data = data
		self.next_node = next
	def get_next(self):
		return self.next_node
	def set_next(self, next):
		self.next_node = next
	def get_data(self):
		return self.data
	def set_data(self, next):
		self.data = data

class SinglyLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def print_list(self):
		# if self.size < 3:
		# 	return "{} -> {}".format(self.head.get_data(), self.tail.get_data())
		# else:
		node = self.head
		li = []
		while node:
			li.append(node.get_data())
			node = node.get_next()
		return li

	def append(self, data):
		#create a new node
		new_node = Node(data)
		#add to the list
		if self.head is None:
			self.head = new_node
		else:
			self.tail.set_next(new_node)
		#set it as the tail
		self.tail = new_node
		#increment size
		self.size += 1
		#return list
		return self.print_list()

	# def find(self, value):
	# 	#set variable to equal head, count
	# 	new_node = self.head
	# 	count = 0
	# 	#iterate through list check for equality, increment head
	# 	for i in range(self.size):
	# 		if new_node.get_data() != value:
	# 			new_node = new_node.get_next()
	# 			count += 1
	# 		else:
	# 			return count

	def find(self, index):
		new_node = self.head
		for i in range(index):
			new_node = new_node.get_next()
		return new_node

	def delete(self, value):
		if value != self.head.get_data():
			return self.find(value-1).set_next(self.find(value+1))
		else:
			
		# print self.head.get_data()
		# print self.head.get_next().get_next()
		# self.find(value-1).set_next(self.find(value).get_next())

new_list = SinglyLinkedList()
print new_list.append(5)
print new_list.append(9)
print new_list.append(12)
print new_list.append(1)
print new_list.delete(2)
print new_list.print_list()

