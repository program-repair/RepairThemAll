def search(x, seq):
    if seq == () or seq == []:
        return 0
    else:
        for i, elem in enumerate(seq):
            if x <= elem:
                return i
            elif i == len(seq) - 1 and x > elem:
                return i + 1
