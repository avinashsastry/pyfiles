# Merge sort implementation

import math # For floor function

def merge(a, b): 
    """
    The merge function, that takes in two sorted arrays, and returns one sorted array
    """

    # print "Merge: %s, %s" % (a,b)

    i = 0
    j = 0
    c = []

    m = len(a)
    n = len(b)
    N = m + n

    iFull = False
    jFull = False

    for k in xrange(0,N):
        # print("i=%s, j=%s, k=%s" % (i,j,k))
        if (a[i] <= b[j]):
            c.append(a[i])
            if (i < m-1):
                i = i+1
            else:
                iFull = True
                break
        else:
            c.append(b[j])
            if (j < n-1):
                j = j+1
            else:
                jFull = True
                break

    if (jFull):
        for l in xrange(i,m):
            c.append(a[l])
    elif (iFull):
        for l in xrange(j,n):
            c.append(b[l])
    return c

def split_list(u):
    """
    Split a list into two halves. If the list has an odd number, then the first array
    contains the floor(n/2) elements.
    """
    m = (len(u)//2)
    a = u[0:m]
    b = u[m:len(u)]
    return a, b

def mergeSort(u):
    """
    Merge Sort top level function.
        - Inputs: unsorted array u
        - Outputs: sorted array e
    """
    n = len(u)
    if (n > 1):
        # Call merge here
        # -- Split u into two unsorted parts, a,b
        a, b = split_list(u)

        # print("After Split:")
        # print (a)
        # print (b)
        #print

        # -- Sort a using merge sort
        c = mergeSort(a) 
        #print(c)

        # -- Sort b using merge sort
        d = mergeSort(b)
        #print(d)

        # -- Put the two sorted arrays together
        e = merge(c, d)
        # print(e)
        return e
    else:
        # return the same array, consider it to be sorted
        return u


def test1():
    u = [5, 4, 1, 8, 2, 6, 7, 3]
    c = mergeSort(u)
    print(c)