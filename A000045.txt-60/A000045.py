
def fibh(i,prev,curr):
    if i == 1:
        return curr
    else:
        return fibh(i-1,curr,prev+curr)

def fib(i):
    if i == 0:
        return 0
    return fibh(i,0,1)

# ^^^ those fibs ( i think it's called tail recursion )

f = open("A000045.txt").read()
stuff = len(f)
i = 0
s=""
while (fib(i) < stuff):
    s+=f[fib(i)]
    i+=1

print s
#printed the fibonacci indeces
