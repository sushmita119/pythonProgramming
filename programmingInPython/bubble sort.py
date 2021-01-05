def bubble(l,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                
                temp = l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    print(l)
l=[4,3,7,2,1,8,40,5]
n=len(l)
bubble(l,n)
