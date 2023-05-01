def search(x, seq):

    new_lst = []

    if len(seq) == 0:

        return 0

    for i, elem in enumerate(seq):

        new_lst.append((i, elem))

    for i in new_lst:

        if x <= i[1]:

            return i[0]

        else:

            continue

    return len(seq)
