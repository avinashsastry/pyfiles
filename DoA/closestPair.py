# Closest Pair search
#   - Depends on an eariler merge sort implementation
import random
import math # For srqt and what not.
import quicksort # Get quick sort algo for doing sorts


class point:
    """
    A simple point class to store x and y coordinates for a two dimensional point.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
      return "(%s, %s)" % (self.x, self.y)

class pointUtils:
    """
    Class containing utility methods for doing point-wise calculations such as distance.
    Restricting all methods to static, this just serves as a container class.
    """

    @staticmethod
    def dist(p1, p2):
        """
        Returns the euclidean distance between two points, p1 and p2.
        """
        return math.sqrt((p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y))

    @staticmethod
    def compareX(u, i, j):
      if (u[i].x < u[j].x):
        return -1
      elif (u[i].x > u[j].x):
        return 1
      else:
        return 0

    @staticmethod
    def compareY(u, i, j):
      if (u[i].y < u[j].y):
        return -1
      elif (u[i].y > u[j].y):
        return 1
      else:
        return 0

    @staticmethod
    def sortPoints(pList, coord_str):
        if (coord_str == "x"):
            # Sort by x-coords
            quicksort.quicksort(pList, 0, len(pList)-1, pointUtils.compareX)
        elif (coord_str == "y"):
            # Sort by y-coords
            quicksort.quicksort(pList, 0, len(pList)-1, pointUtils.compareY)
        else:
            # Print error and get out.
            print "ERROR: pointUtils.sortPoint(): Please use param x or y"


    @staticmethod
    def getMedian(a):
      n = len(a)
      if (n % 2):
        # Odd number of elements
        return a[n//2]
      else:
        return a[n//2]


    @staticmethod
    def closestSplitPair(Sx, Sy, d):
      # Find median point by x-coord
      xBar = pointUtils.getMedian(Sx)

      # print "Median: %s" % xBar

      SetY = []
      for p in Sy:
        if (math.fabs(p.x - xBar.x) < d):
          SetY.append(p)

      # print "Set Y: %s" % SetY

      if (len(SetY) == 0):
        return d, None

      i = 0
      j = 1
      dMin = d
      pairMin = None

      for i in xrange(0,len(SetY)):
        j = i+1
        while (j > i and j < len(SetY) and j <= 7):
          dY = pointUtils.dist(SetY[i], SetY[j])
          # print "dY: %s vs dMin: %s" % (dY, dMin)
          if (dY < dMin or dMin == -1):
            dMin = dY
            pairMin = [SetY[i], SetY[j]]
          j = j+1

      # print "Split pair returning: %s at dist %s" % (pairMin, dMin)
      return dMin, pairMin

    @staticmethod
    def closestPair(pList):
        """
        An O(nlogn) time algorithm to find the closest pair of points in a list of given
        points.
        - How it works
          - First create a list of points
          - Sort the list according to x coord and then by y-coord.
          - do a divide and conquer recursive call on the left and right halves of sorted 
              array
          - Now the merge function:
          - Find the median point in the combined list. let's call this x-bar.
          - Now select all points in the y-coord sorted list within distance delta of the 
              median point, such that delta is less than the min distance returned by the 
              recursive calls
          - Go through the list and compare distances of the next 7 points in the list.
          - Return minimum distance point.  
        """

        if (pList is None):
          return -1, None

        # print
        # print "Entering closestPair(): %s" % pList

        if (len(pList) <= 1):
          # Tricky - let's return a negative value to indicate an invalid case.
          # print "returning: -1, None"
          return -1, None

        if (len(pList) == 2):
          d0 = pointUtils.dist(pList[0], pList[1])
          pair0 = pList
          # print "returning %s, %s" % (d0, pair0)
          return d0, pList

        # We define lists Sx, Sy sorted by x-coordinate and y-coordinate respectively
        Sx = pList[:]
        Sy = pList[:]
        pointUtils.sortPoints(Sx, "x")
        pointUtils.sortPoints(Sy, "y")

        Sleft = Sx[0:len(Sx)//2]
        # print "Sx = %s" % Sx

        SRight = Sx[len(Sx)//2:len(Sx)]
        # print "Sy = %s" % Sy

        d1, pair1 = pointUtils.closestPair(Sleft)
        d2, pair2 = pointUtils.closestPair(SRight)

        d = -1
        if (d1 <= d2 or d2 == -1):
          d = d1
          pair = pair1
        elif (d1 > d2 or d1 == -1):
          d = d2
          pair = pair2
        else:
          d = -1
          pair = None

        d3, pair3 = pointUtils.closestSplitPair(Sx, Sy, d)
        if (pair3 is None):
          pair3 = pair

        # print "Returning: %s at %s" % (pair, d3)
        return d3, pair3

def createPoints(n):
  pList = []
  for i in xrange(0, n):
    p = point(random.randint(0,10), random.randint(0,10))
    pList.append(p)
  print "createPoints: %s" % pList
  return pList

def test1():
  pList = createPoints(10)
  d, pair = pointUtils.closestPair(pList)
  print "Closest Pair: %s at distance %s" % (pair, d)

def sortTest():
  pList = createPoints(4)
  print "Array: %s" % pList
  quicksort.quicksort(pList, 0, len(pList)-1, pointUtils.compareX)
  print "Sorted X: %s" % pList

def test3():
  pList = createPoints(10)
  d, pair = pointUtils.closestPair(pList)
  print "Closest Pair: %s at distance %s" % (pair, d)

  dN2 = -1
  pairN2 = None
  for i in xrange(0, 10):
    for j in xrange(0, 10):
      if (i == j):
        dMat = -1
      else:
        dMat = pointUtils.dist(pList[i], pList[j])
      
      if (dMat != -1 and (dN2 == -1 or dMat < dN2)):
        dN2 = dMat
        pairN2 = [pList[i], pList[j]]
  print "Closest by Brute Force: %s at %s" % (pairN2, dN2)