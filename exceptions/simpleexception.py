class MyException (Exception):
    
    def __init__(self, message):
        self._message = message
    
    def getMessage(self):
        return self._message
    
def dosomething(n):
    if n < 0:
        raise MyException("Number was less than zero")
    else:
        return n

try:
    print str(dosomething(-5))
    print str(dosomething(5)) #this will not be called, program will exit when -5 is executed
except MyException as e:
    print e.getMessage
except ZeroDivisionError:
    print "You divded by zero"
except IOError:
    print "Something went wrong on the harddisk"
except: #all-catch error, use "except"
    print "Some other exceptions i didn't expect happened"
    

StopIteration
IndexError 