def digit(n):
    s=0
    for i in str(n):
        s+=int(i)
    return s
sun = digit(70)
print(sun)
