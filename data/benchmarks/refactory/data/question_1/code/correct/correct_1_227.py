def search(x, seq):
    counter = 0
    for i in seq:
        if i< x:
            counter += 1
        elif i == x or i>x:
            break
    return counter

