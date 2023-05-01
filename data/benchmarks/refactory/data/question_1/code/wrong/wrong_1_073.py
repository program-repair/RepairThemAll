def search(x, seq):
    for i in range(len(seq)):
        if x<= seq[i]:
            a=i
            break
        elif x> seq[len(seq)-1]:
            a=len(seq)
    return a
