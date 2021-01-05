from itertools import combinations
s="12"
l=[]
for i in range(len(s)):
    for j in combinations(s, i+1):
        print(j)
        l.append("".join(j))
print(l)
