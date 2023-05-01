def remove_extras(lst):
    newseq = []
    for element in lst:
        if element not in newseq:
            newseq += [element]
    return newseq
