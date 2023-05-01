def search(x, seq):
    for i in range(0, len(seq)):
        no = len(seq)
        if x > seq[i]:
            continue
        elif x <= seq[i]:
            no = i
            break
    return no
