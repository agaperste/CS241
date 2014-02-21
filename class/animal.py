class Animal(object):
    def __init__(self, name, num_legs):
        self._name = name
        self._num_legs = num_legs
    
    def getName(self):
        return self._name
    def getNumLegs(self):
        return self._num_legs
    