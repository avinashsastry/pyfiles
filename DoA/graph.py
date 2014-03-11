# A Graph module with basic functions like 
# breadth-first search, depth-first search,
# shortest path, djikstra's algorithm, topological sorting.

import pyStack  # For DFS
import pyQueue  # For BFS 

class gNode():
    """
    Simplest possible graph node implementation. Only has a value.
    """
    def __init__(self, value):
        self.value = value
        self.edges = [] # All edges for which it is the tail.

    def addEdge(self, edge):
        self.edges.append(edge)

    def __repr__(self):
        return "<Value: %s>" % (self.value)

class gEdge():
    """
    Edge class for our graph, takes two grpah nodes to be connected as input
    """
    def __init__(self, node1, node2, weight=1, isDirected=False):
        self.weight = weight
        self.head = node1
        self.tail = node2
        self.isDirected = isDirected

    def go(self, startNode):
        """ 
        The edge should be the one to decide whether or not the next node is accessible
        """
        if (startNode is None):
            return None
        if (startNode is self.head):
            return self.tail
        if (startNode is self.tail and not(self.isDirected)):
            return self.head

    def __repr__(self):
        return "<Weight: %s, %s to %s>" % (self.weight, self.head.value, self.tail.value)

class graph():
    """
    Simple graph implementation, providing basic methods.
    """
    # a debug flag to add prints and logs
    isDebug = True

    def __init__(self, nodeList=None, edgeList=None):
        """
        Takes in an array of nodes and edges
        """
        if (nodeList):
            self.nodes = nodeList
        else:
            self.nodes = []
        
        if (edgeList):
            self.edges = edgeList
        else:
            self.edges = []

    def __repr__(self):
        n = "Nodes: %s" % self.nodes
        e = "Edges: %s" % self.edges
        return "%s \n%s" % (n, e)

    def getNodeById(self, node_id):
        if (node_id < len(self.nodes)):
            return self.nodes[node_id]
        else:
            return None

    def addNode(self, node):
        if (node is None):
            return
        self.nodes.append(node)
        # We need a way to refer to nodes - we can give them IDs in the order in which they were added to the graph.
        # Or names, but that's just an extension of IDs.
        return len(self.nodes)-1

    def connect(self, node1, node2, weight=1, isDirected=False):
        """
        Connects node1 to node2 with a new edge
        """
        if (node1 is None or node2 is None):
            return
        e = gEdge(node1, node2, weight, isDirected)
        node1.addEdge(e)
        if not(isDirected):
            node2.addEdge(e)
        self.edges.append(e)

    def search(self, value):
        return self.bfs(value)

    def depthSearch(self, value):
        return self.dfs(value, self.nodes[0])

    def dfs(self, value, s, expNodes={}):
        """ 
        DFS implementation using recursive calls
        """
        if (len(self.nodes) == 0):
            return

        if (s is None):
            return None

        if (self.isDebug):
            print
            print "Exploring %s..." % s
            print "Edge List: %s" % s.edges

        if (s.value == value):
            return s
        else:
            expNodes[s.value] = 1

        for edge in s.edges:
            n = edge.tail
            if (self.isDebug):
                print "Next Node: %s" % n
            if (n and not(n.value in expNodes)):
                return self.dfs(value, n, expNodes)

    def bfs(self, value, startNode=None):
        """
        Algorithm for breadth-first search from a starting node
            - Maintain an array of explored nodes
            - a node is considered explored if its value has been compared
            - Use a queue to explore nodes
        """
        if (len(self.nodes) == 0):
            return None

        if (startNode is None):
            startNode = self.nodes[0]

        expNodes = {}
        q = pyQueue.pyQueue()
        q.push(startNode)

        while not(q.isEmpty()):
            # explore the next node in q
            e = q.pop()
            if (e and not (e.value in expNodes)):
                if (self.isDebug):
                    print "Exploring %s..." % e
                if (e.value == value):
                    # Search ends here
                    if (self.isDebug):
                        print "Found: %s!" % e
                    return e
                else:
                    for edge in e.edges:
                        q.push(edge.tail)
                    expNodes[e.value] = 1 # Mark that this node is explored


# Utils and test functions
def createGraph():
    g = graph()
    
    g.addNode(gNode("s"))
    g.addNode(gNode("a"))
    g.addNode(gNode("b"))
    g.addNode(gNode("c"))
    g.addNode(gNode("d"))
    g.addNode(gNode("e"))

    # get all nodes
    s = g.getNodeById(0)
    a = g.getNodeById(1)
    b = g.getNodeById(2)
    c = g.getNodeById(3)
    d = g.getNodeById(4)
    e = g.getNodeById(5)

    # S To A
    g.connect(s, a)
    # S To B
    g.connect(s, b)
    # A to B, C
    g.connect(a, b)
    g.connect(a, c)
    # B to D
    g.connect(b, d)
    # C to D,E
    g.connect(c, d)
    g.connect(c, e)
    # D to E
    g.connect(d, e)
    return g

def test1():
    """ 
    Test the creation of the graph
    """
    g = createGraph()
    print "Graph: %s" % (g)

def test2():
    """
    Test for breadth-first search for the first node with a given value
    """
    g = createGraph()
    n = g.search("d")
    print n

def test3():
    """
    Function to test DFS
    """
    g = createGraph()
    print g
    n = g.depthSearch("e")
    print n

test3()

