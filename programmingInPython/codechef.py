t=int(input())
if t >=1 and t<=1000:
    
    for i in range(t):
        n=int(input())
        if n >=1 and n<=4:
            
            l=list(map(int,input().split()))[:n]
            if all(i>=1 and i<=5 for i in l):
                
                l.sort(reverse = True)
                #print(l)

                diff=abs(l[0]-l[1])
                #print(diff)
                diff2 = abs(diff - l[2])
                #print(diff2,l[2])
                add = l[0]+diff2
                print(add)
                
            
        

