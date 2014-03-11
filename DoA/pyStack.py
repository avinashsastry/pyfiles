# pyStack: Implementation of a stack data structure

class pyStack:
    """
    Basic implementation of a stack data structure. 
    """

    def __init__(self):
        self.length = 0
        self.items = []

    def __repr__(self):
        if (self.length > 0):
            resultStr = "pyStack["
            for i in xrange(0,self.length-1):
                resultStr += "%s, " % self.items[i]
            resultStr += "%s]" % self.items[self.length-1]
            return resultStr
        else:
            return "Empty!"

    def push(self, obj):
        self.items.append(obj)
        self.length = self.length + 1

    def pop(self):
        if (self.length > 0):
            retObj = self.items[self.length-1]
            self.items.remove(retObj)
            self.length = self.length - 1
            return retObj
        else:
            return None

    def getLength(self):
        return self.length

    def isEmpty(self):
        if (self.length > 0):
            return False
        else:
            return True

def test1():
    print "Starting..."
    s = pyStack()

    a = 5
    b = ["monkey", 6, True]
    c = "donkey"
    d = 6.7
    e = pyStack()

    e.push(75)
    e.push(80)
    e.push(85)

    s.push(a)
    s.push(b)
    s.push(c)
    s.push(d)
    s.push(e)

    print "Stack after pushing elements:"
    print(repr(s))

    l = s.getLength()
    for i in xrange(1,l+2):
        print ""
        print "After %s pop(s)" % i 
        r = s.pop()
        print(repr(s))
        print "Popped object: %s" % r


