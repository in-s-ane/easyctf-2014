# This one is pretty easy, just the old run-of-the-mill prime generator and a way to locate the different primes, yeah

import math

def primeGen(n):
  primeList = [2]
  test = 2;
  while len(primeList) < n:
    test = test + 1;
    factor = 2;
    isPrime = True;
    while factor <= math.sqrt(test):
      if test % factor == 0:
        isPrime = False;
        break;
      factor += 1;
    if isPrime:
      primeList.append(test);
  return primeList

def Q(n):
  ret = 0;
  primeList = primeGen(n);
  largerPrimeList = primeGen(primeList[-1])
  for prime in primeList:
    ret = ret + largerPrimeList[prime-1]
  return ret

print Q(args[0]) + Q(args[1])
