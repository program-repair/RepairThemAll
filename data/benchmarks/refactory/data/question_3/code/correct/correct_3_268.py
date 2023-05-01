def remove_extras(lst):
    new=[]
    while lst!=[]:
        new=new+[lst[0]]
        check=lst[0]
        i=0
        while i <len(lst):
            if lst[i]==check:
               lst.remove(lst[i])
               i=i
            else:
               i=i+1
    return new
