#def search(x, seq):
 #   if len(seq)==0:
  #      return 0
   # for i in range(len(seq)):
    #    if x<= seq[i]:
     #       a=i
      #      break
       # elif x> seq[len(seq)-1]:
        #    a=len(seq)
    #return a

#def search(x, seq):
 #   if len(seq)==0:
  #      a=0
   # elif x>seq[len(seq)-1]:
    #    a= len(seq)
#    else:
 #       for i,elem in enumerate(seq):
  #          if  x <=elem:
   #             a=i
    #            break
    #return a
def search(x, seq):
    for i,elem in enumerate(seq):
            if  x <=elem:
                a=i
                break
    if len(seq)==0:
        a=0
    elif x>seq[len(seq)-1]:
        a= len(seq)
    return a
 
