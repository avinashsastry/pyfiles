# Binary search on a sorted array

# Unexpected util method that I have to write so that I can sort points by order.
def binSearch(x, sortedList, i, n, isAscending=True):
    """
    Binary search through a sorted list. If it is descending, pass False as the third arg.
    """
    # Now set c - the comparison index
    c = i + (n - i)//2
    
    print "i=%s, n=%s, c=%s" % (i, n, c)
    r = raw_input("Press any key to continue.")

    if (n==i):
        # Then c will never move. Game over. Not found.
        return None

    if (isAscending):
        if (x < sortedList[c]):
            return binSearch(x, sortedList, i, c-1, isAscending)
        elif (x > sortedList[c]):
            return binSearch(x, sortedList, c+1, n, isAscending)
        else:
            return c
    else:
        if (x > sortedList[i]):
            return binSearch(x, sortedList, i, c-1, isAscending)
        elif (x < sortedList[i]):
            return binSearch(x, sortedList, c+1, n, isAscending)
        else:
            return c


def test1():
    arr = [2, 4, 6, 8, 10, 13, 15, 17]
    x = 7
    i = binSearch(x, arr, 0, len(arr)-1)
    if i:
        print "Found Index %s: %s" % (i, arr[i])
    else:
        print "Not found: %s" % x
