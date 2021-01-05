def common(strs):
    col=list(zip(*strs))
    print(col)
    if not col:
        return("")
    for i, cl in enumerate(col):
            if len(set(cl))!= 1:
                return(strs[0][:i])
    return(strs[0][:i+1])
l=list(map(str,input().split()))
print(common(l))




