from animal import Animal

class Zoo (object):
    
    def __init__(self):
        self._pens = []
        
    def addAnimal(self, animal):
        self._pens.append(animal)
        
    def __len__(self):
        return len(self._pens)
    
    def __iter__(self): # create a generator
        for a in self._pens:
            yield a
            
    def getByNumLegs(self, n):
        #convert this to a generator
        ret = []
        for a in self._pens:
            if a.getNumLegs() == n:
                ret.append(a)
        return ret

if __name__ == "__main__":
    z = Zoo()
    croc = Animal ("croc", 4)
    badger = Animal ("Honey Badger", 4)
    snake = Animal ("snake", 0)
    
    z.addAnimal(croc)
    z.addAnimal(badger)
    z.addAnimal(snake)
    print len(z)
    
    for a in z:
        print a.getName()
    
    for a in z.getByNumLegs(4):
        print a.getName()
        