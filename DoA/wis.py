# WIS: the maximum weighted independent set problem 
# A dynamic programming approach

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

# recursion => wis(a) = max(wis(a-1), wis(a-2))
def wis(a):
	# print "Entering: A=%s" % a
	if (len(a) == 0):
		return 0

	if (len(a) <= 1):
		return a[0]

	if (len(a) == 2):
		if (a[0] >= a[1]):
			return a[0]
		else:
			return a[1]

	if (len(a) == 3):
		if (a[0] + a[2] >= a[1]):
			return a[0] + a[2]
		else:
			return a[1]

	n = len(a)
	return max(wis(a[0:n-1]), wis(a[0:n-2]) + a[n-1])

def dyn_wis(a):
	""" 
	Dynamic Programming version of the recursive WIS algorithm
	expects a global variable A to track weights.
		- a = array of weights
	"""
	n = len(a)
	A = zeros(1, n)
	B = []
	for i in xrange(0, n):
		w = 0
		if (i == 0):
			B.append(0)
			w = a[0]
		elif (i == 1):
			if (a[0] >= a[1]):
				w = a[0]
			else:
				B.remove(0)
				B.append(1)
				w = a[1]
		else:
			w1 = A[i-1]
			w2 = A[i-2]+a[i]
			if (w2 > w1):
				if i-1 in B: B.remove(i-1)
				B.append(i)
			w = max(w1, w2)
		A[i] = w
		print "i=%s, A=%s, B=%s" % (i,A,B)

		Bstr = "["
		for j in xrange(0, len(B)-1):
			Bstr += "%s," % a[B[j]]
		Bstr += "%s]" % a[B[len(B)-1]]
		print "%s" % Bstr
	return A[n-1]

a = [5, 2, 8, 1, 3, 7]
W = dyn_wis(a)
print W