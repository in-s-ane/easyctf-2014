# Memoized fibonacci, courtesy of http://stackoverflow.com/a/24846766
def fib(n, cache={}):
    if n in cache:
        return cache[n]
    elif n > 1:
        return cache.setdefault(n, fib(n-1) + fib(n-2))
    return n

tmp = 0
i = 1
offset = 0
while (True):
    tmp = fib(i)
    if ("1618" in str(tmp) and tmp % 1618 == 0):
        offset += 1
        if (offset == 16):
            print tmp
            break
    i += 1
