def remove_extras(lst):
    output = []
    for i in lst:
        if i in output:
            output.append(i)
    return output
