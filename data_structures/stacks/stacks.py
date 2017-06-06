class Stack(object):
	def __init__(self):
		self.stack = []
		self.count = 0

	def push(self, x):
		self.stack.append(x)
		self.count += 1

	def pop(self):
		self.stack.pop()
		self.count -= 1

	def peek(self):
		return self.stack[-1]

	def empty(self):
		return self.count == 0

	def size(self):
		return self.count
