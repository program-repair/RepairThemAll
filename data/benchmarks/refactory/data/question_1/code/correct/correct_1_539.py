def search(x, seq):
    if type(seq) == tuple:
        if seq == ():
            return 0
        else:
            for i in range(len(seq)):
                if x <= seq[i]:
                    seq = seq[:i] + (x,) + seq[i:]
                elif seq[len(seq)-1] < x:
                    seq = seq + (x,)

    elif type(seq) == list:
        if seq == []:
            return 0
        else:
            for i in range(len(seq)):
                if x <= seq[i]:
                    seq = seq[:i] + [x,] + seq[i:]
                elif seq[len(seq)-1] < x:
                    seq = seq + [x,]

    for i in enumerate(seq):
        if x == i[1]:
            return i[0]
