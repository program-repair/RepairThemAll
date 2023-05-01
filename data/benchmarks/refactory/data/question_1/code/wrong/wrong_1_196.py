def search(x, seq):
    for i, elem in enumerate(seq):
        if seq == ():
            return (i,)
        elif seq == []:
            return [i]
        elif x <= elem:
            return i
        elif x > seq[len(seq)-1]:
            return len(seq)
