# CS 241
# Yingzhu Zhang, ID: 930873790

class Point (object):
    
    # constructor
    def __init__(self, x, y):
        # dynamic types
        self._x = x
        self._y = y
        
    # setters and getters
    def setX(self, x):
        self._x = x
        
    def setY(self, y):
        self._y = y
        
    def getX(self):
        return self._x
        
    def getY(self):
        return self._y
    
    def __eq__(self, otherPoint):
        if self.getX() == otherPoint.getX() and self.getY() == otherPoint.getY():
            return True 
        else:
            return False 
        
    # method
    # overloaded method
    def __add__(self, otherPoint):
        return Point(self.getX() + otherPoint.getX(),
                self.getY() + otherPoint.getY())
                
    def __neg__(self):
        return Point(-self.getX(), -self.getY())
        
    def __sub__(self, otherPoint):
        return self + -otherPoint
    
    # overloaded method
    def __str__(self):
        return str(self._x) + ", " + str(self._y)
  
if __name__ == "__main__":    
    a = Point(5,5)
    b = Point(2,3)
    
    print "x" + str(a.getX())
    # no implicit type-casting
    
    c = a + b
    d = -a
    
    print "c:" + str(c)
    # int, fload, string
    # instance of type Point
    # object instance and a class