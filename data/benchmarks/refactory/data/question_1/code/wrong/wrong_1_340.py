def search(x, seq):
    counter = 0
    for counter in range(len(seq)):
        if x <= seq[counter]:
            return counter
        elif x > seq[counter] and counter == len(seq) - 1:
            return len(seq)
        elif x > seq[counter]:
            counter = counter + 1
