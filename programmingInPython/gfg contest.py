def rearrange(array, n):
    l1=[]
    for i in range(n+1):
        if i in array:
            l1[array.index(i)]=array[i]
    print(l1)
            #print(str(array[i])+" " +"at index"+str(array.index(i))) 
n=int(input())
for _ in range(n):
    m=int(input())
    l=list(map(int,input().split()))[:m]
    rearrange(l,m)
