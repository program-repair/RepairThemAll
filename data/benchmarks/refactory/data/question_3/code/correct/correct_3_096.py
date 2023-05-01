def remove_extras(lst):
    output = []
    for entry in lst:
        if output.count(entry) == 0:
            output == output.append(entry)
    return output
