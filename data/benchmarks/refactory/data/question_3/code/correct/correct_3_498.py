def remove_extras(lst):
    output = []
    for item in lst:
        if item not in output:
            output.append(item)
    return output
