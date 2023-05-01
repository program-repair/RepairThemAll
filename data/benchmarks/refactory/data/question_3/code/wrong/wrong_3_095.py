def remove_extras(values):
    output = []
    for value in values:
        if value not in seen:
            output.append(value)
    return output
