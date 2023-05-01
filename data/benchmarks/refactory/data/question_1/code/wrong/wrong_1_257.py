def search(x, seq):
    position=enumerate(seq)
    if x>seq[-1]:
        return len(seq)
    else: 
        for i in seq:
            if x<=i:
                for index in position:
                    if index[1]==i:
                        return index[0]
