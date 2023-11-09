from math import *
def findNPrime(n):
    p=3
    primes=[2]
    while len(primes) < n:
        for i in range(2, floor(sqrt(p))+1):
            if p % i == 0:
                break
        else:
            primes.append(p)
        p+=1
    return primes[-1]