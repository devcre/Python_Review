# 문제: 자연수인 n을 인수로 받아 1부터 n까지의 합을 계산하여 내주는 함수
# 음수 인수는 모두 0으로 취급
# 재귀(Regression)
def summation(n):
    if n > 0:
        return n + summation(n - 1)
    else:
        return 0

print(summation(10))