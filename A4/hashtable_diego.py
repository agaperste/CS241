from collections import Hashable

class ListNode (object):

    def __init__(self, key, value):
        self._key = key
        self._value = value
        self._next = None

    def getValue(self):
        return self._value
    
    def setNext (self, value):
        self._next = value

class LinkedList (object):
    # insert your assignment 2 here


class Hashtable (object):

    def __init__(self, hashFunction, size=500):


        """ Initialize a blank hashtable

        hashFunction - a function that contains 2 arguments, key and size of hash
            and returns an index to a bucket
        size - the number of buckets in your hash
        """

        self.hashFunc = hashFunction
        self.size = size
        self.bucket = []
        
        for x in range (self.size):
            linkedlist = LinkedList ()
            self.bucket.append(linkedlist)
        

    def __setitem__(self, key, value):
        """ Sets the value at the key to value

        key - any immutable object
        value - any object

        if key is mutable, raise a TypeError
        """

        if isinstance (key, Hashable) == False: #this checks if key is mutable 
            raise TypeError
        else: 
            index = self.hashFunc (key, self.size)
            for x in self.bucket[index]:
                if x._key == key:    
                    x._value = value
                    return None
            self.bucket[index].append (key, value)
        

    def __getitem__(self, key):
        """ Returns the value at the key 
        key - immutable key value

        if there is no value at key, raise AttributeError
        """
        
        index = self.hashFunc (key, self.size)
        for x in self.bucket[index]:
            if x._key == key:
                return x._value
        else:
            return AttributeError



    def __len__(self):
        """ Returns the total number of items in the hash"""
        
        count = 0
        for x in self.bucket:
            count += len (x)
        return count 


    def __contains__(self, key):
        """ Returns True is the hash has a key """

        index = self.hashFunc (key, self.size)
        for x in self.bucket[index]:
            if x._key == key:
                return True
        return False
    
    def getBucketSizes (self):
        for bucket in self.bucket:
            yield len(bucket)



def hashFunction(key, numbuckets): 
    indexcount = 0
    key = str(key)
    key = key.lower()
    for letter in key:
        temp = ord(letter)
        
        indexcount += temp
    
    indexcount = indexcount % numbuckets
    return indexcount
        

if __name__ == "__main__":
    h = Hashtable(hashFunction, 1000)
    h["cat"] = "a feline"
    h["memphis"] = "a city"
   
    print h["cat"]
    print h['memphis']
    print 'Does h contain {}, {}'.format('cat', 'cat' in h)
    print 'Does h contain {}, {}'.format('piano', 'piano' in h)
    print 'h has a size {}'.format(len(h))