l=['MH04CC2','MH04C2820','MH04BB3232','MH04C6565','MH04CC2113','MH04CC2878','MH04BB8','MH04CC2888','MH04CC1313','MH04CC2222','MH04C1201','MH04CC555','MH04C6565']
n=int(input())
s=input()
if n ==1:
    if s in l:
        print("car parked at",l.index(s))
elif n==2:
    if s in l:
        print("car  position :",l.index(s))
        
   
