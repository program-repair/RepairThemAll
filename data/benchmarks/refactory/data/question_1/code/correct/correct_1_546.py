def search(x, seq):
    if not seq:
        i = 0
    else:
        if x > seq[len(seq)-1]:
            i = len(seq)
        else:
            for i, elem in enumerate(seq):
                if x <= elem:
                    i
                    break       
    return i
