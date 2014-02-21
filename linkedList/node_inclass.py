class Node (object):
    
    def __init__(self, value):
        
        self._value = value
        self._next = None
        
    def getValue(self):
        return self._value
    
    def setNext (self, nextnode):
        self._next = nextnode
        
    def getNext (self):
        return self._next