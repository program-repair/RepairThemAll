def search(x, seq):
    for item in seq:
        if x < item:
            return index(item)
