# Implementation of a doubly linked list Queue

class DLLQNode():
	def __init__(self, value):
		"""
		Node is initialized by passing an object or value.
		"""
		self.value = value
		self.prev = None
		self.next = None

class DLLQueue():
	def __init__(self, length):
		"""
		Init function takes in max queue length.
		"""
		self.maxLength = length
		self.curLength = 0
		self.head = None
		self.tail = None

	def appendNode(self, node):
		"""
		Append a DLLQNode to the queue.
		"""
		if (node is None):
			return
		if (self.curLength == self.maxLength):
			return

		if (self.curLength == 0):
			# Init head and tail
			self.head = node
			self.tail = node
		else:
			# add this to the tail
			self.tail.next = node
			node.prev = self.tail
			self.tail = node
		self.curLength += 1

	def prependNode(self, node):
		"""
		Prepend a node to the queue.
		"""
		if (node is None):
			return
		if (self.curLength == self.maxLength):
			return

		if (self.curLength == 0):
			self.head = node
			self.tail = node
		else:
			self.head.next = node
			node.prev = self.head
			self.head = node
		self.curLength += 1

	def addNode(self, value):
		"""
		Create a new node and append it to the list.
		"""
		newNode = DLLQNode(value)
		if (newNode is None):
			return
		self.appendNode(newNode)

	def removeNode(self, node):
		"""
		Remove a node from the queue.
		"""
		if (self.curLength > 0):
			pNode = node.prev
			nNode = node.next
			if pNode: pNode.next = nNode
			if nNode: nNode.prev = pNode
			self.curLength -= 1

	# Queue functions follow
	def push(self, value):
		"""
		Add a node to the front of the queue. If successful, it will return the node.
		"""
		newNode = DLLQNode(value)
		if (newNode is None):
			return None
		self.prependNode(newNode)
		# Optional: return the node that you just added.
		return newNode

	def pop(self):
		"""
		Remove the last node and return the value.
		"""
		popObj = self.tail.value
		self.removeNode(self.tail)
		return popObj

	def isEmpty(self):
		if (self.curLength == 0):
			return True
		else:
			return False



