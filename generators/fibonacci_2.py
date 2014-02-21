def fibgen():
    yield 0
    x, y = 0, 1
    while True:
        yield y
        x, y = y, x+y  #assign the values simultaneously