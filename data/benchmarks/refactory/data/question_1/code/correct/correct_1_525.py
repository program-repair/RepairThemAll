def search(x, seq):
    if seq==() or seq==[]:
            return 0
    else:
        largest=seq[0]
        for i in range(len(seq)):
            if x<=seq[i]:
                return i
            elif x>seq[len(seq)-1]:
                return len(seq)
