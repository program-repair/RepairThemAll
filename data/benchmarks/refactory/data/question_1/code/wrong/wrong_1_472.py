def search(x, seq):
    for i, element in enumerate(seq):
        if seq == ():
                return 0
        else:
            for element in seq:
                if x > element:
                    i+=1
            return i
