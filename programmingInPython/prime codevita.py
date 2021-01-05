n=int(input())
primes=[i for i in range (2,n+1) if all(i%j !=0 for j in range(2,int(i**0.3)))]
print(primes)
