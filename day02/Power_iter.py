# 문제: 정수 b와 자연수 n을 인수로 받아 b**n을 계산하여 내주는 함수 power을 만드시오
# 음수 인수는 모두 0으로 취급
# 반복(Iteration)
def power(b, n):
    ans = 1
    while n > 0:
        ans = ans * b
        n = n - 1
    return ans

print(power(5,3))

# 계산을 빠르게 하는 방법
def power_short(b,n):
    ans = 1
    while n > 0:
        if n % 2 == 0:
            b , n = b**2, n//2
        else:
            ans, n = b*ans, n-1
    return ans

print(power_short(5,3))