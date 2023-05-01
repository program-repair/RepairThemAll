def remove_extras(values):
    output = []
    seen = ()
    for value in values:
        if value not in seen:
            output.append(value)
            seen += (value,)
    return output
