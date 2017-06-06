class Queue:
	def __init__(self):
		self.queue = []
		self.count = 0

	def enqueue(self, x):
		self.queue.insert(0,x)
		self.count += 1

	def dequeue(self):
		return self.queue.pop()
		self.count -= 1

	def peek(self):
		return self.queue[-1]

	def empty(self):
		return self.count == 0

	def size(self):
		return self.count