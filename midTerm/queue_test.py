class Node (object):

    def __init__(self, value):
        self.next = None
        self.value = value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

class Queue (object):
    def __init__ (self):
        self._qhead = None
        self._qtail = None
        self._count = 0
        
    def isEmpty (self):
        return self._qhead is None
    
    def __len__ (self):
        return self._count
    
    def push (self, value):
        node = Node (value)
        if self.isEmpty ():
            self._qhead = node
        else: 
            self._qtail.next = node
        self._qtail = node
        self._count += 1
    
    def lpop (self):
        assert not self.isEmpty (), "Cannot pop from an empty queue."
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None 
            self._qhead = self._qhead.next
            self._count -= 1
            return node.getValue()
        else:
            self._qhead = self._qhead.next
            self._count -=1
            return node.getValue()
    
    def rpop (self):
        assert not self.isEmpty (), "Cannot pop from an empty queue."
        node = self._qtail
        if self._qtail is self._qhead:
            self._qtail = None
            self._qhead = None
            self._count -= 1
            return node.getValue()
        else:
            temp = self._qhead
            n = 0
            while n < self._count:
                temp = temp.next
                n += 1
            self._qtail = temp
            return node.getValue ()

q = Queue ()
q.push (3)
q.push (5)
q.push (7)
q.push (9)
print q.lpop ()
print q.rpop ()
        
        