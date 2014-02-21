def even_gen(n):
    "generates even sequence"
    i = 0
    while i < n:
        yield i
        i = i + 2

def fibgen():
    "generates fib sequence"
    yield 0
    x,y = 0, 1
    while True:
        yield y
        x,y = y, x+y

if __name__ == "__main__":
    f = fibgen()
    print f.next()

