# A basic version of an LRU Cache that uses the following data structures:
#	1. A queue implemented using a doubly linked list
#	2. A hash table to store the index of the page

import abc # for abstract classes

class baseCache:
	"""
	An abstract base class to define the interface for a Cache
	"""
	__metaclass__ = ABC.Meta

	def __init__(self, numPages):
		pass

	@abc.abstractmethod
	def createCacheObj(self, key, value):
		"""
		Create the corresponding cache obj
		"""

	@abc.abstractmethod
	def set(self, key, value):
		"""
		Set method for a given key and value (object)
		"""

	@abc.abstractmethod
	def get(self, key):
		"""
		Get method for a given key to return the object or None
		"""

	@abc.abstractmethod
	def add(self, key, value):
		"""
		Add method to add a new key in to the cache
		"""

	@abc.abstractmethod
	def delete(self, key):
		"""
		Delete method to remove a key and its object from the cache
		"""

class cacheObj:
	"""
	An abstract class to define a basic unit of the cache interface.
	"""
	__metaclass__ = ABC.Meta

	def __init__(self, key, value):
		self.key = key
		self.value = value

class LRUCacheObj(cacheObj):
	pass

class LRUCache(baseCache):
	""" 
	Class LRUCache implements the baseCache interface using a doubly linked list Queue, and a hash table.
		- Hash Table: To store queue nodes with their corresponding keys
		- Queue: To store nodes in the order in which they were updated.
	"""

	def __init__(self, numPages=1024):
		"""
		Initialize takes in the total number of pages that the cache can support.
		Each page corresponds to a key.
		"""
		# Initialize the basic variables
		self.DLLQueue = DLLQueue(numPages)
		self.hashTable = {}
		self.numItems = 0

	def createCacheObj(self, key, value):
		return LRUCacheObj(key, value)

	def isFull(self):
		if self.numItems == self.numPages:
			return True
		else:
			return False

	def set(self, key, value):
		"""
		Updating a value is fine because we are going by pages, not by absolute memory.
		This is ok to explore the logic and implementation of the cache.
		"""
		if (key in self.hashTable):
			QNode = self.hashTable[key]
			# remove it from the Q and add it to the beginning.
			self.DLLQueue.removeNode(QNode)
			# update the value
			QNode.value = createCacheObj(key, value)
			self.DLLQueue.prependNode(QNode)
			return True
		else:
			return None

	def get(self, key):
		"""
		Get the value if it exists, and update the node's position in the queue.
		"""
		if (key in self.hashTable):
			QNode = self.hashTable[key]
			# remove it from the Q and add it to the beginning.
			self.DLLQueue.removeNode(QNode)
			self.DLLQueue.prependNode(QNode)
			# Since Qnode.value is an LRU Cache Obj
			return QNode.value.value 
		else:
			return None

	def add(self, key, value):
		"""
		When you add a new value to the cache, it is important to check whether we need to evict something.
		If yes, then pop from the Queue to get the LRU element/key.
		"""
		# Check if a value exists, if yes, then return false.
		if (key in self.hashTable):
			return False
		while (self.isFull()):
			# evict a key
			DNode = self.DLLQueue.pop()
			self.delete(DNode.key)
		# add the new node
		value = createCacheObj(key, value)
		QNode = self.DLLQueue.push(value)
		self.hashTable[key] = QNode
		self.numItems += 1

	def delete(self, key):
		"""
		Delete a key from the cache
		"""
		if (self.numItems == 0):
			return

		if (key in self.hashTable):
			QNode = self.hashTable[key]
			self.DLLQueue.removeNode(QNode)
			self.hashTable.pop(key, None)
			self.numItems -= 1


