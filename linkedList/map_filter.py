words = ['apple', 'sushi', 'carrots']
#[len(x) for x in words]

def wordlength(word): 
    return len(word)
#map (wordlength, words)

def iseven(n):
    return n%2 == 0

mylist = [3,8,5,88,13]
#map(iseven, mylist)
#filter(iseven, mylist)

def product(x, y):
    return x*y

#reduce(product, mylist)
#=product(3, product(8, product(5, product(88,13))))

from queue import Queue
q = Queue()
q.push(2)
q.push(5)
q.push(10)

#reduce(product, q)
#map(iseven, q)
#filter(iseven,q)
#reduce, map filter = functional programming