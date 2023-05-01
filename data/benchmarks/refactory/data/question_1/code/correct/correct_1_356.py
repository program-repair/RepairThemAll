def search(x, seq):
    if type(seq) == list:
        seq.append(x)
        seq.sort()
        for i, elem in enumerate(seq):
            if elem == x:
                return i
    else:
        seq+=(x,)
        for i, elem in enumerate(sorted(seq)):
            if elem == x:
                return i
