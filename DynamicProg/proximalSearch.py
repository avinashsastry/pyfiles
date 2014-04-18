# proximal search
import sys # for ags, if any

def explode(text, delim=" "):
	text_array = [""]
	k = 0
	for t in text:
		if t == delim:
			k = k + 1
			text_array.append("")
		else:
			text_array[k] = text_array[k]+t
	return text_array

def arrayToDict(text_array):
	# convert an array to a dict where each word is the key
	# if the key is found for the first time, note down its pos.
	# else, store this also, we need to track multiple positions for words
	d = {}
	for i in xrange(0, len(text_array)):
		t = text_array[i]
		if t in d:
			# do nothing 
			pass
		else:
			d[t] = []
		d[t].append(i)
	return d

def implode(text_array, delim=" "):
	text = ""
	for t in text_array:
		text += (t + delim)
	return text

def filterArrayToDict(text_array, words):
	D = {}
	i = 0
	for i in xrange(0, len(text_array)):
		t = text_array[i]
		if t in words:
			if not (t in D):
				D[t] = []
			D[t].append(i)
	return D

def ones(a, b):
	arr = []
	if (a > 1):
		for i in xrange(0, a):
			arr.append([])
			for j in xrange(0, b):
				arr[i].append(1)
	else:
		for j in xrange(0, b):
			arr.append(1)
	return arr

def getMinLength(pos_array, new_pos):
	"""
	Returns length and a new pos array
	"""
	minI = pos_array[0]
	maxI = pos_array[1]
	
	if (new_pos > maxI):
		maxI = new_pos
	elif (new_pos < minI):
		minI = new_pos
	else:
		# no change if equal
		pass
	L = maxI - minI + 1
	return L, [minI, maxI]

def dyn_mcs(dt):
	A = []
	L = []

	n = len(dt) # number of rows
	i = 0
	for dt_arr in dt.values():
		# add a new row for each i
		A.append([])
		L.append([])
		m = len(dt_arr) # number of columns
		for j in xrange(0, m):
			A[i].append(0) # add a initial value
			L[i].append(0)
			if (i == 0):
				# ones for each of the initial entries
				A[i][j] = [dt_arr[j], dt_arr[j]]
				L[i][j] = 1
			else:
				# for each position in the list
				minL = 0
				minArr = []
				for k in xrange(0, len(A[i-1])):
					L_val, L_arr = getMinLength(A[i-1][k], dt_arr[j])
					if (L_val < minL or minL == 0):
						minL = L_val
						minArr = L_arr
				A[i][j] = minArr
				L[i][j] = minL
		i += 1

	# get the min of the last row of A
	print A
	print L

	# find the min L value in the last row of L
	# return the array from A in that pair
	minValue = 0
	minIndex = -1
	for i in xrange(0, len(L[n-1])):
		if (minValue == 0 or L[n-1][i] < minValue):
			minValue = L
			minIndex = i

	return A[n-1][minIndex]

def getMinSequence(text_array, words):
	# put search words into a dict
	dw = arrayToDict(words)

	# put text words into another dict if they are present in search words
	dt = filterArrayToDict(text_array, dw)
	# print dt

	# Now we have a dict of all words that are present in the long text with their positions.
	# Use dynamic prog to return the min containing sequence (MCS)
	pos_array = dyn_mcs(dt)
	return text_array[pos_array[0]:pos_array[1]+1]

def getMinContainingSequence(text_array, words):
	minI = -1
	maxI = -1
	maxL = 0

	# separate to dict
	d = arrayToDict(text_array)

	for w in words:
		if w in d:
			# check if less than min or greater than max
			i_array = d[w]

			# now i_arr is an array containing indices. if only 1 then easy, otherwise we need to check the sequence length with all possibilities?
			cur_len = 0
			prevMin = minI
			prevMax = maxI
			for i in i_array:
				if i < minI or minI == -1:
					minI = i 
				if i > maxI or maxI == -1:
					maxI = i

				cur_len = maxI - minI + 1

				if (len(i_array) == 1):
					# nothing to do here
					pass
				else:
					if (cur_len > maxL):
						# restore old values
						minI = prevMin
						maxI = prevMax
					else:
						# do nothing
						pass
				# update max length
				maxL = cur_len
		else:
			# do nothing?
			pass

	# print "min=%s, max=%s" % (minI, maxI)

	# Note the i+1 is b because of python's range notation for arrays
	ans_array = text_array[minI:maxI+1]
	# print ans_array

	new_text = implode(ans_array)
	return new_text

def test3():
	# get the input - space separated
	words = "the holy cat"
	words = explode(words)
	text = "dog mice cat usa eu the abc holy cat good dog"
	print text 
	text_array = explode(text)
	new_text = getMinSequence(text_array, words)
	print "Answer: %s" % new_text

def test2():
	words = "Debit Banking online"
	words = explode(words)
	text = "Flipkart is a leading destination for online shopping in India offering some of the best prices and a completely hassle free experience with options of paying through Cash on Delivery Debit Card Credit Card and Net Banking processed through secure and trusted gateways"
	print text 
	text_array = explode(text)
	new_text = getMinSequence(text_array, words)
	print "Answer: %s" % new_text

def test1():
	words = "buy a"
	words = explode(words)
	text = "I buy a lot of things online"
	print text 
	text_array = explode(text)
	new_text = getMinSequence(text_array, words)
	print "Answer: %s" % new_text

def test4():
	# read from file this time - use for custom cases
	f = open("flipkartTest.txt")
	text = ""
	for ft in f:
		text += ft

	print text
	words = "Debit Banking online"
	words = explode(words)
	text_array = explode(text)
	new_text = getMinContainingSequence(text_array, words)
	print "Answer: %s" % new_text

def testDictionary():
	words = "Debit Banking online"
	words = explode(words)
	text = "Flipkart is a leading destination for online shopping in India offering some of the best prices and a completely hassle free experience with options of paying through Cash on Delivery Debit Card Credit Card and Net Banking processed through secure and trusted gateways"
	print text 
	text_array = explode(text)

	dw = arrayToDict(words)
	dt = filterArrayToDict(text_array, dw)
	print dt
	for dt_arr in dt.values():
		print dt_arr

test1()
print "---"
test2()
print "---"
test3()
print "---"
# test4()
# print "---"
# testDictionary()