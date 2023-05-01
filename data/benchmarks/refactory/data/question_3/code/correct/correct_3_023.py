def remove_extras(lst):
    output = []
    for i in lst:
        if i not in output:
            output += [i]
    return output
