def search(x, seq):
    if seq == () or []:
        return 0
    else:
        for i, element in enumerate(seq):
            for element in seq:
                if x > element:
                    i+=1
            return i
