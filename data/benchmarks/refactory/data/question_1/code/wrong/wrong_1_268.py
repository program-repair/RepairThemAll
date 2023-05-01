def search(x, seq):
    counter = 0
    new_seq = list(seq)
    for element in seq:
        if x <=element:
            return counter
        if x > seq[len(seq)-1]:
            return len(seq) 
        else:
            counter += 1
            continue
