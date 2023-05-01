def remove_extras(lst):
    #your code here
    result = []
    for entry in lst:
        if entry not in result:
            result = result + [entry]
    return result
