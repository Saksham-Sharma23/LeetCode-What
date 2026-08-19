def stair(n):
    if n == 0 or n == 1 :
        return n 

    return stair(n-1) + stair(n-2)

check = {}

def fib(n) :
    if n == 0 or n == 1 :
        return n 
    if n in check:
        return check[n]
    res = fib(n-1) + fib(n-2)
    check[n] = res
    return res

print(fib(7))


import time

def fib_normal(n):
    if n <= 1:
        return n

    return fib_normal(n - 1) + fib_normal(n - 2)


check = {}

def fib_dp(n):
    if n <= 1:
        return n

    if n in check:
        return check[n]

    check[n] = fib_dp(n - 1) + fib_dp(n - 2)

    return check[n]


n = 35

start = time.time()
print(fib_normal(n))
end = time.time()

print("Normal:", end - start)


start = time.time()
print(fib_dp(n))
end = time.time()

print("DP:", end - start)

print()
print()
print(check)