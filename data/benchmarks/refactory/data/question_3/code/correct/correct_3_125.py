def remove_extras(lst):
    output = []
    for x in lst:
        if x not in output:
            output.append(x)
    return output
            
        
