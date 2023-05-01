def search(x, seq):
    if seq == ():
        return 0
    elif x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        seq_enum = [i for i in enumerate(seq)]
        for j in range(len(seq_enum) - 1):
            if x >= seq_enum[j][1] and x <= seq_enum[j+1][1]:
                return j+1
