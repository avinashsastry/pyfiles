# A python file for binary search trees. Search trees are great for, well, searching.
# A binary tree orders nodes such that the key of a parent is 
# greater than or equal to that of its left child, and less than that of its right child.

class BSTNode:
	def __init__(self, key, value):
		"""
		A node is initiated with a key and a value.
		"""
		# Key is the sorting number for the tree. Should be an integer.
		self.key = key
		# Value is the object that needs to be stored.
		self.value = value
		# Keep a field for left child.
		self.left = None
		# A field for the right child.
		self.right = None
		# Also one field for the parent.
		self.parent = None

	def __repr__(self):
		return "<Key %s, Value: %s>" % (self.key, self.value)

class BSTTester:
	"""
	Small testing module for the BST class. We'll use this to run a few simple test cases,
	to ensure that our tree works as expected.
	"""
	def __init__(self):
		"""
		Init function to list all runnable test cases.
		"""
		self.testCases = [
			self.testCreateTree,
			self.testSearch,
			self.testPrint
		]

	def runTests(self):
		i = 0
		for t in self.testCases:
			i = i + 1
			print "--- Test Case %s ----" % i
			t()
			print
	
	def __makeTestTree(self):
		B = BST()
		B.setDebug(False)
		B.addNode(4, "hi 1")
		B.addNode(3, "hi 2")
		B.addNode(5, "hi 3")
		B.addNode(1, "hi 4")
		B.addNode(2, "hi 5")
		B.addNode(7, "hi 6")
		B.addNode(4, "hi 7")
		B.addNode(9, "hi 8")
		return B

	def testCreateTree(self):
		"""
		Function to test creation and printing methods of a tree and its nodes.
		"""
		print "Testing creation and printing."
		B = self.__makeTestTree()
		print B

	def testSearch(self):
		"""
		To test searching through the BST.
		"""
		print "Testing Search..."
		B = self.__makeTestTree()
		s = B.search(4)
		print "Looking for 4, Found: %s" % s
		s = B.search(3)
		print "Looking for 3, Found: %s" % s
		s = B.search(7)
		print "Looking for 7, Found: %s" % s
		s = B.search(9)
		print "Looking for 9, Found: %s" % s
		s = B.search(2)
		print "Looking for 2, Found: %s" % s

	def testPrint(self):
		"""
		To test our different printing functions.
		"""
		B = self.__makeTestTree()
		print "In-Order:"
		print B.printTree()
		print "Pre-Order:"
		print B.printTreePre()
		print "Post-Order:"
		print B.printTreePost()

class BST:
	def __init__(self, compare_fn=None):
		"""
		Initalizes an empty tree, with no nodes.
		"""
		# customary debug flag
		self.isDebug = False

		# testing module - to run sanity checks.
		self.tester = BSTTester()

		self.root = None
		if (compare_fn == None):
			self.compare_fn = self.default_compare
		else:
			self.compare_fn = compare_fn

	def __repr__(self):
		return self.printTree()

	def printTree(self, startNode=None):
		"""
		Default print function for the tree. We will use an in-order traversal.
		"""
		Bstr = ""
		if (startNode is None):
			startNode = self.root

		if (startNode):
			if (startNode.left):
				Bstr += self.printTree(startNode.left)
			Bstr += "%s " % startNode
			if (startNode.right):
				Bstr += self.printTree(startNode.right)
		else:
			# only if tree is empty
			Bstr += "<Empty>"
		return Bstr

	def printTreePre(self, startNode=None):
		"""
		Additional print function - We will use a pre-order traversal.
		"""
		Bstr = ""
		if (startNode is None):
			startNode = self.root

		if (startNode):
			Bstr += "%s " % startNode
			if (startNode.left):
				Bstr += self.printTreePre(startNode.left)
			if (startNode.right):
				Bstr += self.printTreePre(startNode.right)
		else:
			# only if tree is empty
			Bstr += "<Empty>"
		return Bstr

	def printTreePost(self, startNode=None):
		"""
		Another print function to demonstrate a post-order traversal.
		"""
		Bstr = ""
		if (startNode is None):
			startNode = self.root

		if (startNode):
			if (startNode.left):
				Bstr += self.printTreePost(startNode.left)
			if (startNode.right):
				Bstr += self.printTreePost(startNode.right)
			Bstr += "%s " % startNode
		else:
			# only if tree is empty
			Bstr += "<Empty>"
		return Bstr


	def default_compare(self, x, y):
		"""
		Standard compare function used to sort the tree. Consider passing in a different one if the sorting needs to be different.
		Assumes key values are integers.
		"""
		if (x < y):
			return -1
		elif (x > y):
			return 1
		else:
			return 0

	def runTests(self):
		self.tester.runTests()

	def setDebug(self, isDebug):
		self.isDebug = isDebug

	def addNode(self, key, value):
		"""
		Adds a particular key, value pair by creating a node within itself.
		"""
		newNode = BSTNode(key, value)

		if (self.isDebug):
			print "Adding node: %s" % newNode

		if (self.root):
			# Insert the node at its correct position.
			tempNode = self.root
			while tempNode:
				if (self.isDebug):
					print "Comparing %s vs. %s" % (newNode, tempNode)
				if (self.compare_fn(tempNode.key, newNode.key) > 0):
					if (tempNode.left):
						tempNode = tempNode.left
					else:
						tempNode.left = newNode
						newNode.parent = tempNode
						break
				else:
					if (tempNode.right):
						tempNode = tempNode.right
					else:
						tempNode.right = newNode
						newNode.parent = tempNode
						break
		else:
			# empty tree, add this node as the root
			self.root = newNode

	def search(self, key, startNode=None):
		"""
		The basic search function for this class. Locates a key and retrieves its node in O(lg(n)) time.
		"""
		if (startNode is None):
			startNode = self.root

		if (startNode):
			comp_value = self.compare_fn(key, startNode.key)
			if (comp_value < 0):
				if (startNode.left):
					return self.search(key, startNode.left)
				else:
					return None
			elif (comp_value > 0):
				if (startNode.right):
					return self.search(key, startNode.right)
				else:
					return None
			else:
				# case that they are equal.
				return startNode
		else:
			return None

	def removeNode(self, key):
		"""
		Function to remove a node from the tree. 
		If a node has no children, then it is a leaf node, and there is nothing to be done.
		If it does have children, then we will need to swap it's position with one of its children before removing.
		"""

Btree = BST()
Btree.runTests()
