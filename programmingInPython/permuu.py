from itertools import permutations as pr
nums = input()
l=[]
p=[''.join(permutation) for permutation in pr(nums)]
for i in p:
    l.append(int(i))
for i in sorted(l):
    if len(str(i))==len(nums):
        print(i)
        break
