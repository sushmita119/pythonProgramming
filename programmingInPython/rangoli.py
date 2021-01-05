import string
def print_rangoli(n): 
    alpha = string.ascii_lowercase


    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))


    print('\n'.join(L[::-1]+L[1:]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
