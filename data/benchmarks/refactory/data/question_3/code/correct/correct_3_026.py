def remove_extras(lst):
    new=[]
    for i in lst:
        new=new+[i] if i not in new else new
    return new
