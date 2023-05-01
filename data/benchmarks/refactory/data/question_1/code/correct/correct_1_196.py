def search(x, seq):
    position=enumerate(seq)
    if len(seq)==0:
        return 0
    elif x>seq[-1]:
        return len(seq)
    else: 
        for i in seq:
            if x<=i:
                for index in position:
                    if index[1]==i:
                        return index[0]
