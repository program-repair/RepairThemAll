def search(x, seq):
    enum_seq = enumerate(seq)
    new_seq = tuple(map(lambda x: x[0], enum_seq))
    if seq == ():
        return 0
    for a in range(len(seq)):        
        if x < seq[a]:
            return new_seq[a]
        elif x == seq[a]:
            return new_seq[a]
    return len(seq)
