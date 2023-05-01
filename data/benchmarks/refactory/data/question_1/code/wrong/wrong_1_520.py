def search(x, seq):
    if x not in seq:
        result = 0 
    elif x > seq[len(seq) - 1]:
        return len(seq)
    else:
        result = 0
        for i, elem in enumerate(seq):
            if x < (elem + 1):
                result = i
                return
        return result 
