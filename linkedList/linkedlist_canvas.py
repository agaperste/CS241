from node import Node

class LinkedList (object):

    def __init__(self):
        self._headNode = None

    def append(self, value):

        n = Node(value)
        if self._headNode == None:
            self._headNode = n
        else:
            temp = self._headNode
            while temp.getNext() != None:
                temp = temp.getNext()
            temp.setNext(n)

    def __getitem__(self, index):
        temp = self._headNode
        for i in range(0, index):
            temp = temp.getNext()
            if temp == None:
                raise StopIteration()

        return temp.getValue()


    def __str__(self):
        toReturn = ""
        toReturn += "["
        temp = self._headNode
        while temp != None:
            toReturn += str(temp.getValue())
            if temp.getNext() != None:
                toReturn += ", "
            temp = temp.getNext()
        toReturn += "]"
        return toReturn


if __name__ == "__main__":
    mylist = LinkedList()
    mylist.append(3)
    mylist.append(5)
    mylist.append(7)
    print str(mylist)
    print mylist[1]

