def search(x, seq):
    for i, element in enumerate(seq):
        for element in seq:
            if x > element:
                i+=1
        return i
