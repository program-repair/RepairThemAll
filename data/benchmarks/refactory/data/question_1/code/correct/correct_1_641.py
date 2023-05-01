def search(x, seq):
    if seq:
        for i in range(len(seq)):
            if x <= seq[i]:
                return i
        return len(seq)
    else:
        return 0
   


