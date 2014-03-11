# pyQueue: basic Queue implementation (first-in first-out data structure)
class pyQueue():
    def __init__(self):
        # do basic init
        self.elements = []
        self.length = 0

    def __repr__(self):
        return "pyQueue%s" % self.elements

    def push(self, value):
        self.elements.append(value)
        self.length = self.length + 1

    def pop(self):
        if (self.length > 0):
            value = self.elements[0]
            self.elements = self.elements[1:self.length]
            self.length = self.length-1
            return value
        else:
            return None

    def isEmpty(self):
        if (self.length > 0):
            return False
        else:
            return True

def test1():
    Q = pyQueue()
    Q.push(3)
    Q.push(4)
    Q.push(5)
    Q.push(6)
    Q.push(7)

    print "%s" % Q

    print "Pop: %s" % (Q.pop())
    print "Pop: %s" % (Q.pop())
    print "Pop: %s" % (Q.pop())
    print "Pop: %s" % (Q.pop())
    print "Pop: %s" % (Q.pop())
    print "Pop: %s" % (Q.pop())
    print "Pop: %s" % (Q.pop())
    print "Pop: %s" % (Q.pop())
    print "Pop: %s" % (Q.pop())
    print "Pop: %s" % (Q.pop())
    print "Pop: %s" % (Q.pop())
