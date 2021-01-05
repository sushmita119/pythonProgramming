from itertools import product as pd
def cal(num):
    l=[]
    d={'1':'','2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
    if digits=="":
        return []
    else:
        l=[d[i] for i in digits]
        return["".join(j) for j in pd(*l)]
digits="23"
res=cal(digits)
print(res)


