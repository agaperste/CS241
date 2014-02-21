# CS 241: Assignment 1
# Yingzhu Zhang, ID: 930873790

from point import Point
import math 

class LineSegment(object):
    
    def __init__(self, pointA, pointB):
        self._pointA = pointA
        self._pointB = pointB
        
    def endPointA(self):
        return self._pointA
    
    def endPointB(self):
        return self._pointB
    
    def length(self):
        return math.sqrt((self._pointA.getX() - self._pointB.getX())**2 + 
                         (self._pointA.getY() - self._pointB.getY())**2)
    
    def isVertical(self):
        return self._pointA.getX() == self._pointB.getX()
    
    def isHorizontal(self):
        return self._pointA.getY() == self._pointB.getY()
    
    def isParallel(self,otherLine):
        return self.slope() == otherLine.slope()
    
    def isPerpendicular(self, otherLine):
        return self.slope() == -(1/otherLine.slope())
    
    def slope(self):
        try:
            return float(self._pointA.getY() - self._pointB.getY())/float(self._pointA.getX() - self._pointB.getX())
        except ZeroDivisionError:
            return False
    
    def midpoint(self):
        return Point(float(self._pointA.getX() + self._pointB.getX())/2,
                             float(self._pointA.getY() + self._pointB.getY())/2)        
    
    def __str__(self):
        return "("+str(self._pointA)+")#("+str(self._pointB)+")"