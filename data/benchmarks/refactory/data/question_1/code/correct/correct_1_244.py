def search(x, seq):
   brokeloop=False
   if len(seq)==0:
       return 0
   for i, elem in enumerate(seq):
       if elem>=x:
           brokeloop=True
           break
   if brokeloop==True:
       return i
   else:
        return i+1
