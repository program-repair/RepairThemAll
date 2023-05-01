def sort_age(lst):
    oldtoyoung=[]
    while lst:
        younger=lst[0]
        for older in lst:
            if older[1]>younger[1]:
                younger=older
        lst.remove(younger)
        oldtoyoung.append(younger)
    return oldtoyoung
