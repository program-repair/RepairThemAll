def remove_extras(n):
    result = []
    counter = 0
    while counter < len(n):
        temp = n[counter]
        if temp not in result:
            result.append(temp)
        counter = counter + 1
    return result
