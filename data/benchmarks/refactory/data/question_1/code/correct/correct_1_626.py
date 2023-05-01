def search(x, seq):
    if len(seq) == 0:
        return 0
    elif x < seq[0]:
        return 0
    elif x > seq[len(seq)-1]:
        return len(seq)
    else:
        product = 0
        for i in range(len(seq)-1):
            if x == seq[i]:
                product = i
            elif (seq[i] <= x and x <= seq[i+1]):
                product = product + i + 1
        return product
