def search(x, seq):
    i = 0
    while (x<seq[i] and i < len(seq)):
        i += 1
    if i==len(seq):
        seq.append(x)
    else:
        seq.insert(i, x)
    return seq
