from itertools import combinations as c
def comb(l):
    l1=[]
    combination=c(l,2)
    for i in list(combination):
        l1.append(i)
    print(l1)
l=[1,2,3,4,5]
comb(l)
