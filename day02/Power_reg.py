# 문제: 정수 b와 자연수 n을 인수로 받아 b**n을 계산하여 내주는 함수 power을 만드시오
# 음수 인수는 모두 0으로 취급
# 회귀(Regression)
def power(b, n):
    if n > 0:
        return b * power(b, n-1)
    else:
        return 1

print(power(0,0))