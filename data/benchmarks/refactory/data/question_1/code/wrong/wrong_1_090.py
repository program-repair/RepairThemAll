def search(x, seq):
    count = 0
    for i in range (0, len(seq)):
        if seq[count] < x:
            count += 1
    return count if seq[-1] > x else len(seq)
