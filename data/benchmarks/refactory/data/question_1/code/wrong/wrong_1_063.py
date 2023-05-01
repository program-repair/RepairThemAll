def search(x, seq):
    if type(seq) == tuple:
        seq = list(seq)
        seq.append(x)
        sorted(seq)
        return seq.index(x)
        
