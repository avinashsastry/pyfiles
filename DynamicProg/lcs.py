# Longest common subsequence
# first let's try the regular recursive way

def rec_lcs(x, i, m, y, j, n):
	if (i == m or j == n):
		return 0, ""

	# print "Comparing.. x[%s]=%s vs y[%s]=%s" % (i, x[i], j, y[j])

	if (x[i] == y[j]):
		a, seq = rec_lcs(x, i+1, m, y, j+1, n)
		# print "Returning.. %s" % seq+x[i]
		return 1 + a, seq+x[i]
	if (x[i] != y[j]):
		a, seqA = rec_lcs(x, i+1, m, y, j, n)
		b, seqB = rec_lcs(x, i, m, y, j+1, n)
		if (a > b):
			# print "Returning.. %s" % seqA
			return a, seqA
		else:
			# print "Returning.. %s" % seqB
			return b, seqB

# Dynamic programming algo to find the longest common subsequence.
# this is actually an alignment problem rather than a longest common subsequence problem
# once the two strings have been optimally aligned, the equal elements at the aligned
# points will constitute the longest subsequence.


def print2D(A):
	Astr = "[\n"
	for i in xrange(0, len(A)):
		for j in xrange(0, len(A[i])):
			Astr += "%s,\t" % A[i][j]
		Astr += "\n"
	Astr += "]"
	print Astr
	return Astr

def dyn_align(x, y):
	# penalty matrix
	A = []
	n = len(x)
	m = len(y)

	for i in xrange(0, n+1):
		# init value for A[i]
		A.append([])
		for j in xrange(0, m+1):
			# init value to 0 for A[j]
			A[i].append(0)
			if (i == 0 or j == 0):
				if (i == 0 and j == 0):
					A[i][j] = 0
				elif (i == 0):
					A[i][j] = 1 + A[i][j-1]
				elif (j == 0):
					A[i][j] = 1 + A[i-1][j]
				else:
					pass
			else:	
				if (x[i-1] == y[j-1]):
					# both are equal, fall back to previous case
					A[i][j] = A[i-1][j-1]
				else:
					A[i][j] = 1 + min(A[i-1][j], A[i][j-1])
	print2D(A)
	return A[n][m], A

def reconst(A, x, y):
	"""
	Function to reconstruct the two aligned strings from the cost matrix.
	"""
	i = len(x)
	j = len(y)

	x1 = ""
	y1 = ""

	while i > 0 and j > 0:
		print "i=%s, j=%s" % (i, j)
		minA = A[i][j]
		# choose the minimum of the 3 possibilities
		minI = -1
		if (A[i-1][j-1] <= minA):
			minA = A[i-1][j-1]
			minI = 2
		if (A[i-1][j] <= minA):
			minA = A[i-1][j]
			minI = 0
		if (A[i][j-1] <= minA):
			minA = A[i][j-1]
			minI = 1

		if minI == 0:
			# go up one space and add a space in Y
			i -= 1
			x1 += x[i]
			y1 += '-'
		elif minI == 1:
			# go left one space and add a space in X
			j -= 1
			x1 += '-'
			y1 += y[j]
		elif minI == 2:
			i -= 1
			j -= 1
			# check the difference - if 0 then go this way, if 2 then add alt spaces for both
			if (A[i][j] == A[i-1][j-1]):
				# add both letters
				x1 += x[i]
				y1 += y[j]
			elif (A[i][j] - A[i-1][j-1] == 2):
				# add alternate spaces for both of them
				x1 += x[i]
				i -= 1
				y1 += '-'
				
				x1 += '-'
				y1 += y[j]
				j -= 1
			else:
				# shouldn't come here. do nothing.
				pass

	print "i=%s, j=%s" % (i, j)

	if i >= 0:
		y1 += y[0]
		x1 += x[i]
		i = i-1
		while i >= 0:
			y1 += '-'
			x1 += x[i]
			i -= 1
	elif j >= 0:
		x1 += x[0]
		y1 += y[j]
		j = j-1
		while j >= 0:
			y1 += y[i]
			x1 += '-'
			j -= 1
	return x1[::-1], y1[::-1]

def lcs(x, y):
	i = 0
	j = 0
	m = len(x)
	n = len(y)
	l, seq = rec_lcs(x, i, m, y, j, n)
	return l, seq

def test1():
	x = "abcbdab"
	y = "bdcaba"
	l, seq = lcs(x, y)
	print l
	print seq

def test2():
	x = "abcbdab"
	y = "bdcaba"
	l, A = dyn_align(x, y)
	print l
	x1, y1 = reconst(A, x, y)
	print (x1)
	print (y1)

# test1()
test2()