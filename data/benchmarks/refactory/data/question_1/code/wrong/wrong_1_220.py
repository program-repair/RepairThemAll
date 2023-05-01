def search(x, seq):
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
        elif i == len(seq) - 1 and x > elem:
            return i + 1
