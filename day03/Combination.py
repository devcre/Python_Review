# 조합: n개에서 순서에 상관없이 r개를 뽑는 가지수
# nCr = n-1Cr-1 + n-1Cr (r != 0 and r != n), cC0 = 1, nCn = 1
def comb(n,r):
    if r != 0 and r != n:
        return comb(n-1,r-1) + comb(n-1,r)
    else:
        return 1

# 파스칼 삼각형(Pascal's Triangle)
def pascal(n,r):
    # 중첩 리스트 만들기
    table = [[]]*(n-r+1)
    # 첫 번째 행을 (r+1)개 원소를 모두 1로 초기화
    table[0] = [1]*(r+1)

    # 맨 왼쪽 열을 모두 1로 초기화
    for i in range(1,n-r+1):
        table[i] = [1]
    
    # 모든 리스트를 채우는 반복문
    for i in range(1,n-r+1):
        # 한 행을 채우는 반복문
        for j in range(1,r+1):
            newvalue = table[i][j-1] + table[i-1][j]
            table[i].append(newvalue)
    return table[n-r][r]