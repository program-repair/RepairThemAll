def search(x, seq):
    result = 0
    for i in range(len(seq)):
        if x > seq[i]:
            result += 1
    return result
