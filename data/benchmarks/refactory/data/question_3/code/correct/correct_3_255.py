def remove_extras(lst):
    store = []
    for ele in lst:
        if ele not in store:
            store += [ele]
    return store
