import math   
t=int(input())
if t>=1 and t<=1000:
    
    while(t):
        t-=1
        a,b = map(int,input().split())
        if a>=1 and a<=1000000000 and b>=1 and b<= 1000000000:
            
            val = b*math.ceil(a/2)
            print(val)
            
                
     
