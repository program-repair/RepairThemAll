def remove_extras(lst):
    lst.sort()
    store = []
    for ele in lst:
        if ele not in store:
            store += [ele]
    return store
