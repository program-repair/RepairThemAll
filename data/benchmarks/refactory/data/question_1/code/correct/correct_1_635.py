def search(x, seq):
    result = 0
    for i in range(len(seq)):
        if seq[i] >= x:
            result = i
            break
        elif x > seq[i]:
            result = i + 1
    return result
