ns = [2,3,5,7,11]
t = ('ERICA',2015)
s1 = '한양대학교'
s2 = 'ERICA'

print(3 in ns)
print(8 in ns)
print('ERICA' in t)
print('에' in s2)
print(ns+ns)
print('\n')
print(ns[2:4])

# tuple은 수정 불가능, list는 수정 가능
print('\n')
for x in s1:
    print(x)

def fib3(n):
    old, new = 0 ,1
    for _ in range(1,n):
        old, new = new, old + new
    return new

# 1부터 n까지 피보나치 수를 모두 찾아서 리스트로 내주는 함수
def fib_list(n):
    count = 1
    fl = [1]
    old, new = 0, 1
    while count < n:
        old, new = new, old + new
        ele = [new]
        fl = fl + ele
        count += 1
    return fl

print('\n\n')
print(fib_list(40))
print(fib_list(40).pop())

# 모범답안
def fibseq(n):
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs.append(fibs[i-1] + fibs[i-2])
    return fibs