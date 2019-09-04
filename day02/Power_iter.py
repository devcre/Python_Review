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