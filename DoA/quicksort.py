# Quicksort - this is an implementation of the famous quick-sort algorithm
# Here is how it works:
#   - choose a pivot element - this is done by randomly picking an array element
#   - partition the input array around the pivot
#   - recursively call quicksort on the left and right partitions.

import random

def choosePivot(u, l, r):
    """ 
    Simple method to pick a random element from an array as the pivot for quicksort
    """
    p = random.randint(l, r)
    return p

def swap(u, i, j, l, r):
    """ 
    sub-routine to swap elements at two indices of an array
    """
    if (i < l or i > r):
        return
    if (j < l or j > r):
        return
    if (i == j):
        return
    x1 = u[i]
    x2 = u[j]
    u[i] = x2
    u[j] = x1

def normalCompare(u, i, j):
    if (u[i] < u[j]):
        return -1
    elif (u[i] > u[j]):
        return 1
    else:
        return 0

def partition(u, p, l, r, compare_fn=None):
    """
    Partitioning sub-routine. In-place implementation that partitions a given array around a chosen pivot
    """

    # Graphical description:
    # [ p | u1 | u2 | u3 | .... | u(n-1) | u(n) ]
    # 0---1---u<p---i-----u>p---j---------------#

    # swap the pivot with the first element - so that we keep the pivot's locations unchanged.
    swap(u, p, l, l, r)

    # Create two pointers i, j
    i = l+1 # i is the point at which the partition is separated
    j = l+1 # j is the point at which the partitioned portion of the array ends

    # replace compare_fn with the default compare function if it is not defined.
    if (compare_fn is None):
        compare_fn = normalCompare
    
    # Run a for loop and compare each element with the pivot.
    # If it is less, then swap with the i-th element
    # Increment j after each run of the loop.
    while j <= r:
        # print "processing: %s" % u
        if (compare_fn(u, j, l) <= 0):
            # swap with the (i)th element
            swap(u, i, j, l, r)
            i = i + 1
        j = j + 1

    # swap the pivot to its rightful place in the array
    swap(u, l, i-1, l, r)
    return i-1

def quicksort(u, l, r, compare_fn=None):
    """
    Quick sort implementation where:
        - u => unsorted array
        - l => starting index of the array
        - r => ending index of the array
    """

    if (r-l < 1):
        return

    p = choosePivot(u, l, r) # Pivot here is the index, not the element.

    # print "pivot: %s at %s" % (u[p], p)

    i = partition(u, p, l, r, compare_fn) 

    # print "Partitions: %s, %s" % (u[l:i], u[i+1:r+1])
    # print ""

    quicksort(u, l, i-1, compare_fn)
    quicksort(u, i+1, r, compare_fn)


# rselect() is a randomized selection algorithm 
# to select the k-th smallest element in a given
# array. It works in linear time using the partition
# algorithm from quicksort()

def rselect(u, l, r, k, compare_fn=None):
    """
    rselect() implementation:
        - u = unsorted array
        - l = starting index
        - r = ending index of the array
        - k = k-th order statistic of the array
    """

    print "Entering... u = %s, l=%s, r=%s, k=%s" % (u[l:r+1], l, r, k)

    if (r-l < k-1):
        # Ensure that the order k is always smaller than the length of the array
        # Why is this needed?
        # k = r-l+1
        # print "Resetting k to array length: %s" % k
        print "Returning... l=%s, r=%s, k=%s" % (l, r, k)
        return None

    if (r-l < 1):
        # the array has only one element - r and l are the same.
        print "Returning... l=%s, r=%s, k=%s" % (l, r, k)
        return u[l]

    p = choosePivot(u, l, r)
    print "pivot: %s at %s" % (u[p], p)
    
    i = partition(u, p, l, r, compare_fn)

    print "Partitions: %s, %s at i=%s" % (u[l:i], u[i+1:r+1], i)
    print ""

    # NOTE: the indexing is a little confusing - remember that the starting index is not necessarily 0
    # it is l instead, so be careful with that. remember to subtract l from i during all index calculations.

    if (i == l+k-1):
        return u[i]
    elif (i < l+k-1):
        # k-th order statistic is greater than i, so in the second half
        return rselect(u, i+1, r, l+k-i-1, compare_fn)
    else:
        # k-th order statistic is lesser than p-th element - so first half
        return rselect(u, l, i-1, k, compare_fn)

def test1():
    """
    Test for the basic case for quicksort on a simple unsorted integer array
    """
    arr = [3, 5, 4, 6, 2, 7, 1, 8]
    print "Array: %s" % (arr)
    quicksort(arr, 0, len(arr)-1)
    print "%s" % arr

def testCompare(u, i, j):
    """
    Compare function for test2()
    """
    if (u[i][0] < u[j][0]):
        return -1
    elif (u[i][0] > u[j][0]):
        return 1
    else:
        return 0

def test2():
    """
    Test for a case where a special compare function is passed into the sorting function.
    Passing in an array containing arrays - and the compare function will sort them by their first element.
    """
    arr = [
        [3, 5, 7],
        [4, 2, 1],
        [7, 3, 2],
        [2, 4, 6],
        [1, 4, 5],
        [9, 5, 2],
        [1, 4, 6]
    ]
    print "Array: %s" % arr
    quicksort(arr, 0, len(arr)-1, testCompare)
    print "Sorted: %s" % arr

def test3(): 
    """
    Simple test function to check the working of rselect()
    """
    arr = [3, 5, 4, 6, 2, 7, 1, 8]
    k = 6
    kVal = rselect(arr, 0, len(arr)-1, k)
    print "%s-th order statistic is: %s" % (k, kVal)

test3()
# test1()
# test2()