class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BST:
	def __init__(self):
		self.root = None

	#inset a value
	def insert(self, val):
		#if the root is None
		if self.root is None:
			#make a new Node
			newNode = Node(val)
			#make the head this node
			self.root = newNode
		#else call __insert method
		else:
			self.__insert(self.root, val)

	#private inset method
	def __insert(self, node, val):
		#check if node is empty
		if node is None:
			#then input it here
			new_node = Node(val)
			node = new_node
		#elif it's less than root
		elif node.value > val
			#input it to the left
			node.left = self.__insert(node, val)
		#elif it's more than root
		elif node.value < val
			#input it to the right
			node.right = self.__insert(node,val)
		#else
		else:
			#it is already present
			print("Value is already present in BST")

	def remove(self, val):
		if self.root is None:
			print("Value not in BST")
		else:
			self.__remove(self.root, val)

	def __remove(self, node, val):
		if node is None:
			print("Value is not in BST")
		elif node.val > val:
		elif node.val < val:
		else:
			print("Va")


	def find(self, val):
		pass

	def __find(self, node, val):
		pass

	def findMin(self, node):
		pass

	def __finrMin(self, node):
		pass

	def findMax(self):
		pass

	def __findMax(self):
		pass

	def preOrder(self):
		pass

	def __preOrder(self, node):
		pass

	def preOrder(self):
		pass

	def __preOrder(self, node):
		pass

	def preOrder(self):
		pass

	def __preOrder(self, node):
		pass