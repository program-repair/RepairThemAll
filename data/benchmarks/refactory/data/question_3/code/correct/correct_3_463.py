def remove_extras(lst):
    new = []
    for ele in lst:
        if ele not in new:
            new = new + [ele,]
    return new# your code here
