def search(x, seq):
    n = len(seq)
    for counter in range(n):
        if x > seq[n-1]:
            result = n
            break
        elif seq[counter] >= x:
            result = counter
            break
        else:
            continue
    return result
