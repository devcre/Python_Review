# Functions
def input_base():
    print('섭씨(C)를 화씨(F)로 변환하려면 1을')
    print('화씨(F)를 섭씨(C)로 변환하려면 2를')
    base = input('입력해주세요. ')

    while not(base == '1' or base == '2'):
        base = input('올바른 숫자를 입력해주세요.')
    return base

def isdigit_signed(s):
    return s.isdigit() or \
        s[0] == '-' and s[1:].isdigit() or\
        s[0] == '+' and s[1:].isdigit()

def input_temperature(fro, to):
    print(fro + '를' + to + '로 변환해드립니다.')
    tin = input(fro + '온도를 입력해주세요. ')
    while not isdigit_signed(tin):
        tin = input('올바른' + fro + '온도를 입력해주세요. ')
    return tin

def c2f(c):
    f = 9.0 / 5.0 * c + 32
    return f

def f2c(f):
    c = (5 * f -160) / 9.0
    return c

# Main Program
print('섭씨-화씨 온도변환기')
base = input_base()
if base == '1':
    tin = input_temperature('섭씨(C)', '화씨(F)')
elif base == '2':
    tin = input_temperature('화씨(F)', '섭씨(C)')
print()

# 계산 및 출력
tin = int(tin)
if base == '1':
    print('섭씨', tin, '도(C)는 화씨', round(c2f(tin)), '도(F) 입니다.')
elif base == '2':
    print('화씨', tin, '도(F)는 섭씨', round(f2c(tin)), '도(C) 입니다.')
print('감사합니다. 또 찾아주세요.')