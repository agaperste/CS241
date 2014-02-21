class Node (object):
    
    def __init__(self,value):
        
        self._value = value
        self._next = None
        
    def getValue(self):
        return self._value
    
    def getNext(self):
        return self._next()
    
#-------------------------------------------------------------------------------

class _ListIterator:
    def __init__(self, listHead):
        self._curNode = listHead
        
    def __iter__(self):
        return self
    
    def next(self):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode._value
            self._curNode = self._curNode._next
            return item
    
#-------------------------------------------------------------------------------

class LinkedList (object):
    
#    def __init__(self):
        
#      self._headNode = None
#      self._size = 0
    
    def __init__(self, pythonlist = None):
        if (pythonlist == None):
            self._headNode = None
            self._size = 0
        else:
            self._size = 1
            count = 0
#           listIndex = 0
            self._headNode = Node(pythonlist[0])
            oldNode = self._headNode
            for number in pythonlist[1:]:
                count += 1
                oldNode._next = Node(pythonlist[count])
                oldNode = oldNode._next
                self._next = oldNode
                self._size += 1
#           while(count < len(pythonlist)):
#               newNode = Node(pythonlist[listIndex])
#               oldNode._next = newNode
#               self._size += 1
#               count += 1
#               listIndex += 1
#               oldNode = newNode
        
    def append(self, value):
        node = Node(value)        
        if self._headNode == None:
            self._headNode = node
        else:
            temp = self._headNode
            while temp._next != None:
                temp = temp._next
            temp._next = node
        self._size += 1
    
    def __str__(self):
        toReturn = "["
        temp = self._headNode
        while temp != None:
            toReturn += str(temp.getValue())
            temp = temp._next
            if temp != None:
                toReturn += ", "
        toReturn += "]"
        return toReturn      
        
    def __getitem__(self, key):
        if key > self._size:
            raise IndexError
        elif key < 0:
            count = 0 
            temp = self._headNode
            newkey = len(self) + key
            while count < newkey:
                if temp._next == None:
                    return temp.getValue()
                else:
                    temp = temp._next
                    count += 1
            return temp.getValue()
        else:
            count = 0
            temp = self._headNode
            while count < key:
                if temp._next == None:
                    return temp.getValue()
                else:
                    temp = temp._next
                    count += 1
            return temp.getValue()
        
    def __setitem__(self, key, value):
        count = 0
        curNode = self._headNode
        while(count <= key):
            if (count < key):
                curNode = curNode._next
                count += 1
            else:
                curNode._value = value
                count += 1
        
    def __len__(self):
        return self._size
    
    def __contains__(self, target):
        curNode = self._headNode
        while curNode._next != None:
            if target == curNode._next.getValue():
                return True
            return False
        
    def __iter__(self):
        return _ListIterator(self._headNode)
    
    def __getslice__(self, i, j):
        count = 0
        ret = LinkedList()
        curNode = self._headNode
        while (count < len(self)):
            if (count < i):
                curNode = curNode._next
                count += 1
            elif (count >= i and count < j):
                ret.append(curNode.getValue())
                count += 1
                curNode = curNode._next
            else:
                count += 1
        return ret