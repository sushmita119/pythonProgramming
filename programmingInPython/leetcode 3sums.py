'''
from collections import Counter
n=[1,2,2,-2-1,0,4,-4,1]
c=Counter(n)
print(c)
'''
n=[1,2,2,-2-1,0,4,-4,1]
dict_={}
for i in n:
    dict_[i]=n.count(i)
print(dict_)
