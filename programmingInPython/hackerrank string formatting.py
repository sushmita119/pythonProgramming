def print_formatted(number):
    width = len("{0:b}".format(number))
    print(width)
    for i in range(1, number+1):
        print("{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}".format(i=i, width=width))
print_formatted(20)
