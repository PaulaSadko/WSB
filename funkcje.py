def add(x,y):
    return x+y

def multiply (x, y):
    return x * y

def fissbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return 'fiss'
    elif i % 5 == 0:
        return  'buzz'
    else:
        return i
