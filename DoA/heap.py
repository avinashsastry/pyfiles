# Heap - simple implementation in python
# We'll implement a heap using an array 
# makes it simple and efficient.

class heap():
	"""
	Simple heap implementation using an array
	"""
	def __init__(self):
		self.items = []
		self.count = 0

	def __repr__(self):
		return "%s" % self.items

	def parent(self, i):
		return (i-1)//2

	def lchild(self, p):
		v = 2*p+1
		if (v < self.count):
			return v
		else:
			return None

	def rchild(self, p):
		v = 2*p+2
		if (v < self.count):
			return v
		else:
			return None

	def insert(self, key):
		self.items.append(key)
		self.count = self.count + 1
		self.heapify(self.count-1)
		print "Heap after insert: %s" % self

	def swap(self, i, j):
		if (i >= self.count or j >= self.count):
			return
		if (i < 0 or j < 0):
			return

		a = self.items[i]
		self.items[i] = self.items[j]
		self.items[j] = a

	def heapify(self, i):
		"""
		Function to restore the heap property after inserting an element
			- First check whether the parent obeys the property
			- If yes, then good.
			- if no, then swap and heapify the parent.
		"""
		if (i >= self.count):
			return
		p = self.parent(i)
		if (self.items[i] < self.items[p]):
			# child is greater than parent. Swap and heapify
			# print "Swapping parent=%s, child=%s" % (self.items[p], self.items[i])
			self.swap(i, p)
			self.heapify(p)
		else:
			# Nothing to do
			pass

	def revHeapify(self, p):
		"""
		Bubble an element down from the root to the leaves using heap property
		"""
		if (self.count <= 0):
			return
		else:
			lc = self.lchild(p)
			rc = self.rchild(p)

			if (not lc and not rc):
				# no children to check, yay!
				return

			c = -1
			if (not lc):
				c = self.items[rc]
			elif (not rc):
				c = self.items[lc]
			else:
				if (self.items[lc] <= self.items[rc]):
					c = lc
				else:
					c = rc

			if self.items[p] > self.items[c]:
				# swap and propagate down
				self.swap(c, p)
				self.revHeapify(c)
			else:
				return

	def readMin(self):
		"""
		Read out the min but not extract it. (look instead of pop)
		"""
		if (self.count <= 0):
			return None
		else:
			return self.items[0]

	def extractMin(self):
		"""
		Function to get the min element
		"""
		if (self.count <= 0):
			return None
		else:
			val = self.items[0]
			# replace this with the last element
			self.items[0] = self.items[self.count-1]
			self.items.remove(self.items[self.count-1])
			self.count = self.count - 1
			# now call reverse-heapify on the root
			self.revHeapify(0)
			return val

def test1():
	h = heap()
	
	h.insert(3)
	h.insert(5)
	h.insert(2)
	h.insert(7)
	h.insert(1)

	v = h.extractMin()
	print "Extracted: v = %s" % v


test1()




