# CS 241 Assignment 3
# Yingzhu (Jacqueline) Zhang
 
class Node (object):
    
    def __init__(self, value):
        self.value = value
        self.north = None
        self.south = None
        self.east = None
        self.west = None
    
    def getValue(self):
        return self.value

class MatrixIterator:
    def __init__(self, headnode):
        self.x = headnode
        self.y = headnode
        
    def __iter__(self):
        return self
    
    def next(self):
        if self.x is None:
            raise StopIteration
        else:
            item = self.x.getValue()
            if self.x.east != None:
                self.x = self.x.east
            elif self.y.south != None:
                self.y = self.y.south
                self.x = self.y
            else:
                self.x = None 
            return item
    
class LinkedMatrix (object) :

    def __init__(self, x, y, defaultValue=None):
        """ creates a new matrix with x columns and y rows with default value """
        self.headnode = None
        self.defaultValue = defaultValue
        self.dimensions = (x, y)
        self.numColumn = x
        self.numRow = y
        
        if x <= 0 or y <= 0:
            return 
        # linking the columns by two-way linked nodes
        headnode = Node (defaultValue)
        self.headnode = headnode
        
        temp1 = headnode 
        for n in range (self.numColumn - 1):
            newnode = Node (defaultValue)
            temp1.east = newnode 
            newnode.west = temp1
            temp1 = newnode
        
        # linking the rows by two way linked nodes
        temp2 = headnode         
        for n in range(self.numRow -1):
            newnode = Node (defaultValue)
            temp2.south = newnode
            newnode.north = temp2
            temp2 = newnode
            temp1 = temp2
            for j in range (self.numColumn - 1):
                newnode = Node (defaultValue)
                temp1.east = newnode 
                newnode.west = temp1
                temp1 = newnode
                
        # linking the rest together
        star1 = headnode
        star2 = headnode
        
        for n in range(self.numRow-1):
            for j in range(self.numColumn-1):
                star1.east.south = star1.south.east
                star1.south.east.north = star1.east
                star1 = star1.east
                
            star2 = star2.south
            star1 = star2

                
                
    def __str__(self):
        """ return the string representation of the matrix """
        toReturn = ""
        
        temp1 = self.headnode
        for n in range (self.numColumn):
            toReturn += str(temp1.getValue())
            if temp1.east != None:
                temp1 = temp1.east
        
        toReturn += "\n"
            
        temp2 = self.headnode
        for n in range(self.numRow-1):
            temp2 = temp2.south
            toReturn += str(temp2.getValue())
            
            temp1 = temp2.east
            for j in range(self.numColumn-1):
                toReturn += str(temp1.getValue())
                if temp1.east != None:
                    temp1 = temp1.east
            toReturn += "\n"
        
        return toReturn 

  

    def __getitem__(self, index):
        """ return the element at the index expressed as a tuple """
        if index[0]<0 or index[0]>=self.numColumn or index[1]<0 or index[1]>=self.numRow:
            raise IndexError
        else: 
            temp = self.headnode
            
            for n in range (index[0]):
                temp = temp.east
            for j in range(index[1]):
                temp = temp.south
        return temp.getValue()
                

    def __setitem__(self, index, a):
        """ set value at index to a """
        if index[0]<0 or index[0]>=self.numColumn or index[1]<0 or index[1]>=self.numRow:
            raise IndexError
        else: 
            temp = self.headnode
            
            for n in range (index[0]):
                temp = temp.east
            for j in range(index[1]):
                temp = temp.south
        temp.value = a
        

    def __iter__(self):
        """returns a list of all the items in the matrix first across down then across repeat"""
        
        return MatrixIterator (self.headnode)


    def insertRow(self, rowIndex, defaultValue=None):
        """inserts a row at the given index, shifting columns if necessary"""
        if rowIndex > self.numRow or rowIndex < 0:
            raise IndexError 
        
        elif rowIndex != 0 and rowIndex != self.numRow:
            temp1 = self.headnode
            for n in range (rowIndex):
                temp2 = temp1.south
            for n in range (self.numColumn):
                curnode = temp2
                if temp2.east != None:
                    temp2 = temp2.east 
                newnode = Node(defaultValue)
                curnode.north = newnode
                newnode.south = curnode
                newnode.north = temp1
                temp1.south = newnode
                temp1 = temp1.east

            self.numRow += 1
            self.dimensions = (self.numColumn, self.numRow)                
            
            temp = self.headnode
            for n in range (rowIndex):
                temp = temp.south
            temp3 = temp
            temp4 = temp3.south.east.north
            for n in range (self.numColumn-1):
                temp3.east = temp4
                temp4.west = temp3
                temp3 = temp3.east
                if temp4.south.east != None: 
                    temp4 = temp4.east
                
        elif rowIndex == 0:
            temp = self.headnode
            for n in range (self.numColumn):
                curnode = temp
                temp = temp.east
                newnode = Node(defaultValue)
                curnode.north = newnode
                newnode.south = curnode
            
            self.numRow += 1
            self.dimensions = (self.numColumn, self.numRow)            
            
            headnode = self.headnode
            headnode = headnode.north
            temp1 = headnode
            temp2 = headnode.south.east.north
            for n in range (self.numColumn-1):
                temp1.east = temp2
                temp2.west = temp1
                temp1 = temp1.east
                if temp2.south.east != None:
                    temp2 = temp2.south.east.north
        
        else:
            temp = self.headnode
            for n in range(self.numRow-1):
                temp = temp.south
            
            for n in range(self.numColumn):
                curnode = temp
                if temp.east != None:
                    temp = temp.east
                newnode = Node(defaultValue)
                curnode.south = newnode
                newnode.north = curnode
                
            self.numRow += 1
            self.dimensions = (self.numColumn, self.numRow)        
            
            temp = self.headnode
            for n in range(self.numRow-1):
                temp = temp.south
            for n in range(self.numColumn-1):            
                temp1 = temp               
                temp2 = temp1.north.east.south                
                temp1.east = temp2
                temp2.west = temp1
                temp = temp2
                

    def insertColumn(self, colIndex, defaultValue=None):
        """inserts a column at the given index, shifting columns if necessary"""
        if colIndex > self.numColumn or colIndex < 0:
            raise IndexError 
        
        elif colIndex != 0 and colIndex != self.numColumn:
            temp1 = self.headnode
            temp2 = temp1.east
            if colIndex != 1:
                for n in range (colIndex-1):
                    temp1 = temp1.east
                    temp2 = temp1.east
            for n in range (self.numRow): # might not need to -1
                curnode = temp2
                if temp2.south != None:
                    temp2 = temp2.south 
                newnode = Node(defaultValue)
                curnode.west = newnode
                newnode.east = curnode
                newnode.west = temp1
                temp1.east = newnode
                if temp1.south != None:
                    temp1 = temp1.south
            
            self.numColumn += 1
            self.dimensions = (self.numColumn, self.numRow)            
            
            temp = self.headnode
            for n in range (colIndex):
                temp = temp.east
            temp3 = temp
            temp4 = temp3.west.south.east
            for n in range (self.numRow-1):
                temp3.south = temp4
                temp4.north = temp3
                temp3 = temp3.south
                if temp4.west.south != None:
                    temp4 = temp4.west.south.east
                
        elif colIndex == 0:
            temp = self.headnode
            for n in range (self.numRow):
                curnode = temp
                temp = temp.south
                newnode = Node(defaultValue)
                curnode.west = newnode
                newnode.east = curnode
            
            self.numColumn += 1
            self.dimensions = (self.numColumn, self.numRow) 
            
            self.headnode = self.headnode.west
            headnode = self.headnode
            temp1 = headnode
            temp2 = temp1.east.south.west
            for n in range (self.numRow-1):
                temp1.south = temp2
                temp2.north = temp1
                temp1 = temp1.south
                if temp2.east.south != None:
                    temp2 = temp2.east.south.west 
        
        else:
            temp = self.headnode
            for n in range(self.numColumn-1):
                temp = temp.east
            
            for n in range(self.numRow):
                curnode = temp
                temp = temp.south
                newnode = Node(defaultValue)
                curnode.east = newnode
                newnode.west = curnode
                
            self.numColumn += 1
            self.dimensions = (self.numColumn, self.numRow) 
            
            temp = self.headnode
            for n in range(self.numColumn-2): 
                temp = temp.east
                
            for n in range(self.numRow-1):
                temp1 = temp.east               
                temp2 = temp.south.east              
                temp1.south = temp2
                temp2.north = temp1
                temp = temp.south 

    def removeRow(self, rowIndex):
        """removes a row at the given index, shifting columns if necessary"""
        if rowIndex >= self.numRow or rowIndex < 0:
            raise IndexError 
        
        elif rowIndex != 0 and rowIndex != self.numRow-1:
            temp = self.headnode
            for n in range (rowIndex):
                temp1 = temp.south
                temp2 = temp1.south
            for n in range (self.numColumn-1):
                star = temp1.north
                curnode = temp2
                temp2 = temp2.east 
                curnode.north = star
                star.south =  curnode 
                temp1.north = None
                temp1.south = None
                temp1 = temp1.east
                
        elif rowIndex == 0:
            temp1 = self.headnode
            self.headnode = temp1.south
            for n in range (self.numColumn-1):
                curnode = temp1
                if temp1.east != None:
                    temp1 = temp1.east
                temp2 = curnode.south
                curnode.south = None
                temp2.north = None

        else:
            temp = self.headnode
            for n in range(self.numRow-1):
                temp1 = temp.south
            
            for n in range(self.numColumn-1):
                curnode = temp1
                if temp1.east != None:
                    temp1 = temp1.east
                temp2 = curnode.north
                curnode.north = None
                temp2.south = None
        
        self.numRow -= 1 
        self.dimensions = (self.numColumn, self.numRow)

    def removeColumn(self, colIndex):
        """removes a column at the given index, shifting columns if necessary"""
        if colIndex > self.numColumn-1 or colIndex < 0:
            raise IndexError 
        
        elif colIndex != 0 and colIndex != self.numColumn-1:
            temp = self.headnode
            for n in range (colIndex):
                temp1 = temp.east
                temp2 = temp1.east
            for n in range (self.numRow): # might not need to -1
                curnode = temp2
                if temp2.south != None:
                    temp2 = temp2.south 
                curnode.west = temp
                temp.east = curnode
                temp1.east = None
                temp1.west = None
                if temp1.south != None:
                    temp1 = temp1.south
                    temp = temp1.west
                
        elif colIndex == 0:
            temp1 = self.headnode
            self.headnode = temp1.east
            for n in range (self.numRow-1):
                curnode = temp1
                temp1 = temp1.south
                temp2 = curnode.east
                curnode.east = None
                temp2.west = None

        else:
            temp1 = self.headnode
            for n in range(colIndex):
                temp1 = temp1.east
            
            for n in range(self.numColumn-1):
                curnode = temp1
                temp1 = temp1.south
                temp2 = curnode.west
                temp2.east = None
                curnode.west = None
        
        self.numColumn -= 1
        self.dimensions = (self.numColumn, self.numRow)        


"""lm = LinkedMatrix (2, 3, "p")
print lm
lm.removeColumn(1)
print lm
lm.insertColumn(1, "m")
print lm"""

"""#lm = LinkedMatrix (3, 2, "p")
print lm
lm.removeColumn (1)
print lm
lm.insertColumn (1, "m")
print lm"""