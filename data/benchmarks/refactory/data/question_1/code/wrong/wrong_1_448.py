def search(x, seq):
    count=0
    for i in seq:
        if x<i:
            return count
        count+=1
    return len(seq)
