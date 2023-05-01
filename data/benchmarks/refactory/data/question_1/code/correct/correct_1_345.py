def search(x, seq):
    if len(seq) ==0 :
        return 0
    else:
        seq = list(seq)
        max_value = max(seq)
        for i,elem in enumerate(seq):
            if x > max_value:
                seq.insert(seq.index(max_value) + 1,x)
                break
            elif x<elem:
                y = max(0,i)
                seq.insert(y,x)
                break
    return seq.index(x)
