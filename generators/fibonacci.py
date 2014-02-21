def fibonacci():
    i = 0 
    n = 1
    
    while True:
        yield i
        f = i
        i = n
        n = f+n