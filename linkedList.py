# Simple Implementation of a singly linked list
class node:
    
    def __init__(self, value, forward):
        self.val = value
        self.fwd = forward

    def setNext(forward):
        self.fwd = forward

    def __repr__(self):
        return "%s" % self.val

class linkedList:

    def __init__(self, head_node):
        self.head = head_node

    def getNodeAtIndex(self, i):
        temp_node = self.head
        j = 0
        while (temp_node.fwd):
            if (i == j):
                break
            temp_node = temp_node.fwd
            j = j + 1
        return temp_node

    def appendNode(self, new_node):
        temp_node = self.head
        while (temp_node.fwd):
            temp_node = temp_node.fwd
        temp_node.fwd = new_node

    def removeNode(self, rem_node):
        temp_node = self.head
        prev_node = None

        while (temp_node.fwd):
            if (temp_node == rem_node):
                break
            prev_node = temp_node
            temp_node = temp_node.fwd

        if prev_node:
            prev_node.fwd = temp_node.fwd
        else:
            #remove the head
            self.head = temp_node.fwd

    def __repr__(self):
        retStr = ""
        temp_node = self.head
        i = 0;
        while(temp_node.fwd):
            retStr += "%s:%s, " % (i, repr(temp_node))
            temp_node = temp_node.fwd
            i = i+1
        retStr += "%s:%s" % (i, repr(temp_node))
        return retStr

head_node = node(5, None)
ll = linkedList(head_node)

for x in xrange(6,15):
    nn = node(x, None)
    ll.appendNode(nn)
print(repr(ll))

rn = ll.getNodeAtIndex(3)
repr(rn)

ll.removeNode(rn)
print(repr(ll))

