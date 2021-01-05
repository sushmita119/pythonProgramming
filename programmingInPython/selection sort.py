def selection(l,n):
    for i in range(n-1):
        m=i
        for j in range(i+1,n):
            if( l[j]<l[m]):
                m=j
        l[i],l[m]=l[m],l[i]
    print(l)
l=[2 ,4 ,1 ,9 ,4 ,10 ,3]
n=len(l)
selection(l,n)
        
