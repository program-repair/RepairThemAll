def search(x, seq):
    for element in seq:
        if x <= element:
            return list(seq).index(element)
        else:
            continue
