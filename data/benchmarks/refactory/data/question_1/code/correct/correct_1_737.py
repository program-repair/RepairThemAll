def search(x, seq):
    num = 0
    for i in seq:
        if x <= seq[num]:
            return num
        num += 1
    else:
            return num
