n=int(input())
l=list(map(int,input().split()))[:n]
count=1
l1=[]
for i in l:
    if i>i+1:
        count=count+1
    else:
        l1.append(count)
        count=0
        i=i+1
        if i>i+1:
            count=count+1
print(l)
print(l1)
            
       
        
         
    
    
