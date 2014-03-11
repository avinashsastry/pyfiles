# inversion counter in an array
# An inversion is defined as (a[i] > a[j]) when (i < j)

# def mergeCount(arr1, arr2):
#     n = 0
#     i = 0
#     j = 0

#     for i in xrange(0, len(arr1)):
#         for j in xrange(0, len(arr2)):
#             if (arr1[i] > arr2[j]):
#                 # print "%s > %s" % (arr1[i], arr2[j])
#                 n = n+1

#     print "%s, %s: %s" % (arr1, arr2, n)
#     return n


def mergeCount(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    N = m + n

    i = 0
    j = 0
    count = 0
    arr3  = []

    print "%s, %s" % (arr1, arr2)

    for k in xrange(0,N):
        if (arr1[i] <= arr2[j]):
            arr3.append(arr1[i])
            if (i < m-1):
                i = i+1
            else:
                arr3 = arr3 + arr2[j:n]
                break
        else:
            # this is an inversion
            arr3.append(arr2[j])
            if (j < n-1):
                count = count + (m-i)
                j = j+1
            else:
                count = count + (m-i)
                arr3 = arr3 + arr1[i:m]
                break

    print "%s: %s" % (count,arr3)
    return arr3, count


def splitArray(arr):
    m = len(arr)//2
    a = arr[0:m]
    b = arr[m:len(arr)]
    return a, b


def invCount(arr):
    """
    Function to count the number of inversions in an array using a merge-sort type
    divide and conquer algo.
    """

    if (len(arr) == 1):
        # no inversions in a single length array
        return arr, 0

    arr1, arr2 = splitArray(arr)

    print "Split Input: %s, %s" % (arr1, arr2)

    temp1, n1 = invCount(arr1)
    temp2, n2 = invCount(arr2)
    arr3, n3 = mergeCount(temp1, temp2)
    return arr3, (n1+n2+n3)

#arr = [5, 4, 1, 2, 6, 3, 8, 7]
arr = [1, 3, 5, 2, 4, 6]
arr2, n = invCount(arr)
print "Number of Inversions: %s" % n