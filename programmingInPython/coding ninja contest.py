#ninja mnc


n,m=map(int,input().split())
#s = set()
for i in range(m):
    a,b = map(int,input().split())
'''
    s.add(a)
    s.add(b)
diff= abs(n-len(s))
print(1+diff)
'''
diff = abs(m-n)
print(1+diff)
    
