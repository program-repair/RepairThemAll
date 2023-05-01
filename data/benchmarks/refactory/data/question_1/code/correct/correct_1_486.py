def search(x, seq):
    if len(seq) == 0 or x < seq[0] :
        return 0
    elif x > seq[len(seq)-1]:
        return len(seq)
    else:
        result = 0
        for i, element in enumerate(seq):
            if x < (element + 1):
                result = i
                break
        return result
