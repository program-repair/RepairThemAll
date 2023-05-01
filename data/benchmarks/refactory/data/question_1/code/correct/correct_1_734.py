def search(x, seq):
    for i, elem in enumerate(seq):
        if x > elem and i == len(seq) - 1:
                        # specifies case where i has reached the last element in the tuple or list
            return i + 1
        elif x > elem:
            continue
        else:
            return i
    if len(seq) == 0:
        return 0
    # this is if seq is empty
    # if not defined, task 3(a) won't work
