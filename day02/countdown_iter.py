# 문제: 자연수 n을 인수로 받아 n부터 1씩 줄여가면서 화면에 1초에 하나씩 프린트하고, 0이되면 '발사!'를 프린트하는 함수 countdown을 만드시오.
# 음수 인수는 모두 0으로 취급
# 반복(Iteration)
import time
def Countdown(n):
    while n > 0:
        print(n)
        n = n - 1
        time.sleep(1)
    print("Fire!")

Countdown(10)