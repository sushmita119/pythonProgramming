size, k = list(map(int, input().split()))
li = list(map(int, input().split()))

print(sorted(li[:k]) + sorted(li[k:], reverse = True))
