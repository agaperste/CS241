class QueuePoppedWhenEmptyException (Exception):
    def __init__(self, message):
        self._message = message
    def __str__ (self):
        return self._message 
    
class Node (object):

    def __init__(self, value):
        self._prev = None
        self._next = None
        self._value = value

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value

    def setNext(self, nextnode):
        self._next = nextnode
    def getNext(self):
        return self._next

    def setPrev(self, prevnode):
        self._prev = prevnode
        
class Queue (object):

    def __init__(self):
        self._headNode = None
        self._tailNode = None

    def push (self, value):
        n = Node(value)
        if self._headNode == None:
            self._headNode = n
            self._tailNode = n
        else:
            self._headNode.setPrev(n)
            n.setNext( self._headNode )
        self._headNode = n

    def pop (self, value):
        # return value of the right node
        if self._headNode == None:
            raise QueuePoppedWhenEmptyException("tried to pop empty queue")
        elif self._headNode == self._tailNode:
            temp = self._headNode
            self._headNode = None
            self._tailNode = None
            return temp.value
        else:
            temp = self._tailNode
            self._tailNode.prevnode.nexnode = None
            self._tailNode = temp.prevnode
            self._nextNode = None
            temp.prevnode = None
            return temp.value
    
    def __str__(self):
        toReturn = ""
        t = self._headNode
        while t != None:
            toReturn += str(t.getValue())
            toReturn += ","
            t = t.getNext()
        return toReturn


if __name__ == "__main__":
    q = Queue ()
    q.push (3)
    q.push (6)
    q.push (9)
    q.push (12)
    print str (q)
    a = q.pop()



