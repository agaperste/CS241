def simple (n):
    for i in n:
        for j in n:
            print 'Hello'

def simple2 ():
    for i in n:
        print 'Hello'

# simple (3)
# rate: n^2

"""simple(n)
for i in range(200):
    simple2()
(n^2)+200*n
n^2"""

# 200*n^2 = n^2 [constant doesn't matter]

def evensimpler(n):
    print 'Hello'
    
def b(n):
    while n >1:
        print 'hellow'
        n = n//2
    
"""simple = O(n^2)
evensimpler = O(1)
b(16)
# 16, 8,4,2, not 1"""

def compoundfunction (n):
    simple(n)
    evensimpler(n)
#rate: O(n^2)+O(1)
#so we simplify: O(n^2)