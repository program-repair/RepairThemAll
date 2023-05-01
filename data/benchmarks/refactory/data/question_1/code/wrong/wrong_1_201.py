def search(x, seq):
    if seq == ():
        return (x,)
    elif seq == []:
        return [x,]
    else:
        for i,elem in enumerate(seq):
            if x < seq[-1]:
                if x > elem:
                    continue
                elif x < elem and type(seq) == tuple:
                    seq = seq[:i] + (x,) + seq[i:]
                elif x < elem and type(seq) == list:
                    seq = seq[:i] + [x,] + seq[i:]
            elif x > seq[-1]:
                if type(seq) == tuple:
                    seq += (x,)
                elif type(seq) == list:
                    seq += [x,]
        return seq.index(x)
