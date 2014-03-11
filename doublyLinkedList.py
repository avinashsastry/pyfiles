# Implementation of a doubly linked list

# define the node
class DLLNode:
    """
    DLLNode: Basic Implementation of a doubly linked list node
    """
    
    def __init__(self, value, forward=None, backward=None):
        self.val = value
        self.fwd = forward
        self.bwd = backward

    def __repr__(self):
        return "%s" % self.va

class DLL:
    """
    DLL: Basic Implementation of a doubly-linked list
    """

    def __init__(self, head_node=None, tail_node=None):
        self.head_node = head_node
        self.tail_node = tail_node

    def getNodeAtIndex(self, i):
        temp_node = self.head_node
        if (temp_node):
            j = 0
            while(temp_node.fwd):
                if (i == j):
                    break
                temp_node = temp_node.fwd
                j = j+1
            return temp_node
        else:
            return None

    def __repr__(self):
        temp_node = self.head_node
        if temp_node == None:
            return ""
        else:
            resultStr = ""
            i = 0
            while temp_node.fwd:
                resultStr += "%s:%s, " % (i, temp_node.val)
                temp_node = temp_node.fwd
                i = i + 1
            resultStr += "%s:%s" % (i, temp_node.val)
            return resultStr

    def appendNode(self, new_node):
        temp_node = self.tail_node
        if temp_node:
            temp_node.fwd = new_node
            new_node.bwd = temp_node
            self.tail_node = new_node
        else:
            # No nodes exist, start the list
            self.head_node = new_node
            self.tail_node = new_node

    def addNodeAtIndex(self, new_node, i):

        if new_node == None:
            return false

        temp_node = self.head_node
        if temp_node:
            temp_node = self.getNodeAtIndex(i)
            if temp_node:
                b_node = temp_node.bwd
                if b_node:
                    b_node.fwd = new_node

                new_node.bwd = b_node
                new_node.fwd = temp_node
                temp_node.bwd = new_node
                return True
            else:
                return false
        else:
            # First node in the list
            self.head_node = new_node
            self.tail_node = new_node
            return True

    def removeNodeAtIndex(self, i):
        if self.head_node:
            temp_node = self.getNodeAtIndex(i)
            if temp_node:
                b_node = temp_node.bwd
                f_node = temp_node.fwd

                if b_node:
                    b_node.fwd = f_node
                if f_node:
                    f_node.bwd = b_node

                temp_node.bwd = None
                temp_node.fwd = None
                temp_node = None
                return True
            else:
                return None
        else:
            return True



dll = DLL()
for i in xrange(1,10):
    n = DLLNode(2*i)
    dll.appendNode(n)

print(repr(dll))

nn = dll.getNodeAtIndex(5)
if nn:
    dll.removeNodeAtIndex(5)
else:
    print "Node at 5 not found!"

print(repr(dll))

aa = DLLNode(76)
dll.addNodeAtIndex(aa, 5)

print(repr(dll))