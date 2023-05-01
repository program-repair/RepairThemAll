def search(x, seq):
    count = 0
    for i in seq:
        if x > i:
            count = count + 1
        else:
            break
    return count
