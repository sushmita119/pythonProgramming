def smallestK(n):
    # code here
    # retured value will be printed by driver code
    i=1
    while(True):
        s=1
        for j in str(i):
            s*=int(j)
        if s == n:
           
            return i
        else:
            i+=1
n=12
res=smallestK(n)
print(res)
