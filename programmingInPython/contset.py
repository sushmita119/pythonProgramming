
def convert(list): 
    res = int("".join(map(str, list)))
    t=(a**res)%1337
      
    return t 
  

a=int(input())
if a>=1 and a<=2147483647:
    n=int(input())
    if n>=1 and n<= (3*(10**6)):
        l=list(map(int,input().split()))[:n]
        if all(i<= 9 for i in l):
            print(convert(l))

