items = int(input())
itemList=[]
for i in range(items):
    itemList.append(input().split(","))
list2=[]
for i in itemList:
    i.append((int(i[1])*int(i[2]))//100)
    list2.append(i[3])

result=[]  
minimum = min(list2)
for i in itemList:
    if i[3] == minimum:
        result.append(i[0])
for i in result:
    print(i)
