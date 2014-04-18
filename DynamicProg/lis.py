# Dynamic programming example to find the longest increasing subsequence in a given sequence of numbers
# Let us consider a sequence [5, 2, 8, 6, 3, 6, 9, 7]
# Our task is to find the longest subsequence within this array where each term is followed by a term greater than itself.

def rec_lis(num_array):
	""" 
	Let us first try to write this problem down recursively. A recursive implementation would be
	of the form where each valid subsequence is 1+the longest subsequence discovered so far.
	"""

	print "Entering rec_lis: %s" % num_array

	if (len(num_array) <= 1):
		return 0

	if (len(num_array) == 2):
		if (num_array[0] < num_array[1]):
			return 1
		else:
			return 0

	max_length = 0
	for j in xrange(0, len(num_array)):
		for i in xrange(0, j):
			l = rec_lis(num_array[i:j])
			if (l > max_length):
				max_length = l

	print "Answer for %s: %s" % (num_array, 1+max_length)
	return (1 + max_length)

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

def dyn_lis(num_array):

	n = len(num_array)
	A = zeros(1, n)
	L = 0
	for j in xrange(0, n):
		if (j <= 1):
			L = 0
		elif (j == 2):
			if num_array[0] < num_array[1]:
				L = 1
			else:
				L = 0
		else:
			L = 0
			for i in xrange(0, j):
				if (num_array[i] < num_array[j]):
					L_j = A[i] + 1 
				else:
					L_j = A[i]
				if L_j > L:
					L = L_j

		A[j] = L

	print "Longest sequence found: %s" % A[n-1]
	print "Sequence lengths: A=%s" % A
	return A[n-1] + 1

def test1():
	"""
	Test for a small sorted sequence
	"""
	arr = [1, 2, 3, 4, 5]
	L = rec_lis(arr)
	print L
	print "Expected answer: 5"

def test2():
	"""
	Test for a reverse-sorted sequence
	"""
	arr = [6, 4, 2, 1]
	L = rec_lis(arr)
	print L
	print "Expected answer: 0"

def test3():
	"""
	Test for a regular sequence with no sorting
	"""
	arr = [5, 2, 8, 6, 3, 6, 9, 7]
	L = rec_lis(arr)
	print L
	print "Expected Answer: 4"

def test4():
	arr = [5, 2, 8, 6, 3, 6, 9, 7]
	L = dyn_lis(arr)

test4()