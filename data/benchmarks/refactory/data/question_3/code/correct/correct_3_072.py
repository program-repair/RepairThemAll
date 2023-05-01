def remove_extras(lst):
    x = tuple(lst)
    store = ()
    for ele in lst:
        if ele not in store:
            store += (ele,)
    return list(store)
