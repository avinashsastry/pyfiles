# Knapsack Solver 

import abc

class KnapsackUtils():
	"""
	Container class to hold common utility functions
	used by the algorithms.
	"""
	def __init__(self):
		pass

	@staticmethod
	def zeros(a, b):
		arr = []
		if (a > 1):
			for i in xrange(0, a):
				arr.append([])
				for j in xrange(0, b):
					arr[i].append(0)
		else:
			for j in xrange(0, b):
				arr.append(0)
		return arr

	@staticmethod
	def print2D(A):
		Astr = "[\n"
		for i in xrange(0, len(A)):
			for j in xrange(0, len(A[i])):
				Astr += "%s,\t" % A[i][j]
			Astr += "\n"
		Astr += "]"
		print Astr
		return Astr

class KnapsackAlgo():
	""" 
	Abstract base class for solving knapsacks. Describes a basic algorithm.
	"""
	__metaclass__ = abc.ABCMeta

	def __init__(self, isDebug=False):
		self.isDebug = isDebug

	@abc.abstractmethod
	def solve(self, C, S, V):
		""" 
		Abstract method that will be implemented by concrete algo classes.
		"""

class ZeroOneAlgo(KnapsackAlgo):

	def solve(self, C, S, V):
		# implementation of the bounded problem 0/1
		# the weights are the cols
		# items are the rows
		n = len(S) # num of items will be cols
		A = KnapsackUtils.zeros(n, C+1)
		for i in xrange(0, n):
			for j in xrange(1, C+1):
				if (j-S[i] >= 0):
					A[i][j] = max(A[i-1][j], V[i] + A[i-1][j-S[i]])
				else:
					A[i][j] = A[i-1][j]
		return A[n-1][C], A

class UnboundedAlgo(KnapsackAlgo):

	def __backtrack(self, I, A, S, V):
		""" 
		Private method used by this class to backtrack and find the solution.
		"""

		n = len(I)
		# traverse backwards through the arrays
		i = n-1
		Ilist = []
		curV = A[n-1]
		while i >= 0:
			if (I[i] > 0):
				# we added an item
				item = I[i]
				Ilist.append(item)
				i -= S[item]
			else:
				# we fell back to an old solution - nothing to do
				i = i-1
		return Ilist

	def solve(self, C, S, V):
		# Unbounded problem the correct way - using only O(n) space
		n = len(S)
		A = KnapsackUtils.zeros(1, C+1)
		I = []
		for j in xrange(1, C+1):
			# for every weight
			maxV = 0
			maxItem = -1
			prevWeight = -1
			for i in xrange(0, n):
				if (j-S[i] >= 0) and (A[j-S[i]] + V[i] > maxV):
					maxV = A[j-S[i]] + V[i]
					maxItem = i
					prevWeight = j-S[i]
			A[j] = max(A[j-1], maxV)
			if (A[j] == maxV):
				# that means we added an item
				if (maxItem > 0):
					I.append(maxItem)
				else:
					I.append(-1)
		if (self.isDebug): print I
		Ilist = self.__backtrack(I, A, S, V)
		if (self.isDebug): print Ilist
		return A[C], A

class KnapsackTester():
	"""
	Small tester class to run pre-defined tests to check that the algorithms are correct.
	"""
	def __init__(self, parentMod):
		# Initialize the parent module
		self.parentMod = parentMod

		# Initialize an empty array
		# and popuate it with all the tests that we require.
		self.testMethods = [
			self.test1,
			self.test2,
			self.test3,
			self.test4
		]

	def run(self):
		for t in self.testMethods:
			t()

	def test1(self):
		S = [1, 3, 2, 7, 8]
		V = [2, 5, 3, 9, 7]
		C = 18
		self.parentMod.setAlgo(0, True)
		maxV, A = self.parentMod.solve(C, S, V)
		print maxV
		print A

	def test2(self):
		S = [3, 5, 2, 7, 9]
		V = [1, 2, 1, 5, 4]
		C = 10
		self.parentMod.setAlgo(0, True)
		maxV, A = self.parentMod.solve(C, S, V)
		print maxV
		print A

	def test3(self):
		S = [1, 3, 2, 7, 8]
		V = [2, 5, 3, 9, 7]
		C = 18
		self.parentMod.setAlgo(1, True)
		maxV, A = self.parentMod.solve(C, S, V)
		print maxV
		KnapsackUtils.print2D(A)

	def test4(self):
		S = [3, 5, 2, 7, 9]
		V = [1, 2, 1, 5, 4]
		C = 10
		self.parentMod.setAlgo(1, True)
		maxV, A = self.parentMod.solve(C, S, V)
		print maxV
		KnapsackUtils.print2D(A)

class KnapsackSolver():
	"""
	A wrapper class for the Knapsack solving algorithms that are commonly used.
	There are two types:
	 - The 0/1 Knapsack Solver
	 - The Unbounded Solver
	"""

	SOLVER_UNBOUNDED = 0
	SOLVER_ZERO_ONE = 1

	def __init__(self, solverType, isDebug=False):
		# A utils module to hold common util functions
		# that are used by the different algos
		self.KnapsackUtils = KnapsackUtils()

		# A tester module to run pre-defined tests.
		self.tester = KnapsackTester(self)

		# A debug flag that will be used to control 
		# whether logs withint the module are printed or not.
		self.debug = isDebug

		# Init the algos based on solver type.
		self.setAlgo(solverType, self.debug)

	def runTests(self):
		# Run all tests and display output.
		self.tester.run()

	def solve(self, C, S, V):
		return self.algo.solve(C, S, V)

	def setAlgo(self, i, isDebug=False):
		"""
		Method to change the algo object - useful for testing/initialization.
		"""
		if (i == 0):
			self.algo = UnboundedAlgo(isDebug)
		elif (i == 1):
			self.algo = ZeroOneAlgo(isDebug)
		else:
			print "Invalid argument given. Enter 0 for Unbounded, 1 for ZeroOne Knapsack."

K = KnapsackSolver(0)
K.runTests()