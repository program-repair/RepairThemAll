def remove_extras(lst):
    final=[]
    for x in lst:
        if x not in final:
            final.append(x)
    return final
    pass
