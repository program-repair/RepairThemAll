def search(x, seq):
    count = 0
    for i in seq:
        if x > i:
            count += 1
    return count
