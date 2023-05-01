def remove_extras(values):
    output = []
    for value in values:
        if value not in output:
            output.append(value)
    return output
