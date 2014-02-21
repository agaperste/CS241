class Node (object) :

    def __init__(self, value):

        self._value = value
        self._next = None

    def getValue(self):
        return self._value

class LinkedList (object):

    def __init__(self):

        self._headNode = None

    def append(self, value):

        node = Node(value)

        if self._headNode == None:
            self._headNode = node
        else:
            temp = self._headNode
            while temp._next != None:
                temp = temp._next
            temp._next = node

    def __str__(self):
        toReturn = "["
        # insert magic here
        temp = self._headNode
        while temp != None:
            toReturn += str(temp.getValue())
            temp = temp._next
            if temp != None:
                toReturn += ", "

        toReturn += "]"

        return toReturn
        


if __name__ == "__main__":
    l = LinkedList()
    l.append(5)
    l.append(6)
    l.append(7)
    l.append(8)
    print str(l)
    [5,6,7,8]
