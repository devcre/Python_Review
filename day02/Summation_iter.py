# 문제: 자연수인 n을 인수로 받아 1부터 n까지의 합을 계산하여 내주는 함수
# 음수 인수는 모두 0으로 취급
# 반복(Iteration)
def summation(n):
    sum = 0
    while n > 0:
        sum = sum + n
        n = n - 1
    return sum

print(summation(10))