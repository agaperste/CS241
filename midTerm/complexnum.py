import math

class ComplexNum (object):
    def __init__ (self, re, im):
        self.re = re
        self.im = im
        
    def __setValue__ (self, value):
        self.value = value
    
    def __getValue__ (self):
        return self.value
    
    def __str__ (self):
        num = ""
        num += str(self.re) + "+" + str(self.im)
        num += "i"
        
        return num
    
    def __add__ (self, otherComplexNum):
        sre = self.re + otherComplexNum.re
        sim = self.im + otherComplexNum.im
        self.re, self.im = sre, sim
        return str(self) 
    
    def __sub__ (self, otherComplexNum):
        sre = self.re - otherComplexNum.re
        sim = self.im - otherComplexNum.im
        self.re, self.im = sre, sim
        return str(self)
    
    def magnitude (self):
        length = math.sqrt(self.re^2 + self.im^2)
        return length

        
    