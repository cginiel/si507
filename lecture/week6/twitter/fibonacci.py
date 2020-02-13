import datetime

def fib(n):
    '''returns the nth number in the fibonacci sequence
    '''
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i - 2] + fib_seq[i - 1])
    return fib_seq[-1]

print (fib(200000)) # start with 100000 and increase until it's annoying


FIB_CACHE = {} # define at module scope so it persists across fn calls

def fib_with_cache(n):
    if n in FIB_CACHE.keys(): # is result for n already there?
        return FIB_CACHE[n]   # if so, look up result and return it
    else:                     # cache miss! 
        FIB_CACHE[n] = fib(n) # do the operation and save the result
        return FIB_CACHE[n]   # return the newly saved result

inp = input("What Fibonacci number would you like? ")
t1 = datetime.datetime.now().timestamp()
print(fib_with_cache(int(inp)))
t2 = datetime.datetime.now().timestamp()

inp = input("What Fibonacci number would you like? ")
t3 = datetime.datetime.now().timestamp()
print(fib_with_cache(int(inp)))
t4 = datetime.datetime.now().timestamp()


print("time without caching: ", (t2 - t1) * 1000, "ms")
print("time with caching: ", (t4 - t3) * 1000, "ms")