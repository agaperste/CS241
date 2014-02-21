# CS 243 Assignment 2
# Yingzhu (Jacqueline) Zhang


class ListNode (object):

    def __init__(self, data):
        self._data = data
        self._next = None

    def getValue(self):
        return self._data
    
    def getNext (self):
        return self._next()

#------------------------------------------------------------------------------

class _ListIterator:
    def __init__(self, listHead):
        self._curNode = listHead
        
    def __iter__(self):
        return self
    
    def next(self):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode._data
            self._curNode = self._curNode._next
            return item

#------------------------------------------------------------------------------

class LinkedList(object):
    
    def __init__(self, pythonList = None):
        #creates a blank Linked List
        #creates a new Linked List by taking a Python list as an argument and making a new node for each.
        if (pythonList == None):
            self._headNode = None
            self._size = 0
        else:
            self._size = 1
            count = 0
            self._headNode = ListNode(pythonList[0])
            prevNode = self._headNode
            for number in pythonList[1:]:
                count += 1
                prevNode._next = ListNode(pythonList[count])
                prevNode = prevNode._next
                self._next = prevNode
                self._size += 1

    def append(self, data):
        node = ListNode(data)        
        if self._headNode == None:
            self._headNode = node
        else:
            temp = self._headNode
            while temp._next != None:
                temp = temp._next
            temp._next = node
        self._size += 1
    
    def __str__(self):
    #returns a String representation for the Linked List, groups of items separated by commas in square brackets
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
    #returns the value at the node positioned at the value of key (i.e. a[8] would return the 9th element in the linked list)
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
    #sets the value at position key a particular value
        count = 0
        curNode = self._headNode
        while(count <= key):
            if (count < key):
                curNode = curNode._next
                count += 1
            else:
                curNode._data = value
                count += 1
    
    def __len__(self):
    #returns the size of the linked list as an integer
        return self._size
    
    def __contains__(self, value):
    #scans the list for a node with the value passed in, returns true if the value exists in the linked list
        curNode = self._headNode
        while curNode._next != None:
            if value == curNode._next.getValue():
                return True
            return False        
    
    def __iter__(self):
    #return a new generator that returns the values in the LinkedList, throws a StopIteration exception when the end of the linked list is reached.
        return _ListIterator(self._headNode)
    
    def __getslice__(self, i, j):
    #returns a new linked list with the subset of nodes in the original linked list from i and j non-inclusive.  
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
    
  