# 피보나찌 수열(Fibonacci Sequence)
# 자연수의 수열로 이전 두 개의 수를 더하여 다음 수를 정하는 수열이다.
def fib_reg(n):
    if n > 1:
        return fib_reg(n-1) + fib_reg(n-2)
    else:
        return n

def fib_iter(n):
    ans = 0
    old, new = 0, 1
    while n > 1:
        ans = new + old
        old = new
        new = ans
        n = n - 1
    return ans

# 모범답안
def fib2(n):
    k = 1
    old, new = 0 ,1
    while k < n:
        k = k + 1
        old, new = new, old + new
    return new

print(fib_reg(10))
print(fib_iter(10))