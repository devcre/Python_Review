# 미니 수독은 수독과 똑같은 요령으로 숫자를 채워넣는 퍼즐이나
# 가로 4칸, 세로 4칸의 정사각형 보드에 1부터 4까지 채워넣는 것만 다르다.

## 규칙 ##
# 퍼즐보드에 숫자를 채우는 규칙은 수독과 동일하게 같은 줄에 숫자가 겹치지 않아야 하고,
# 2x2 크기로 4등분 한 작은 격자 내부에도 숫자가 겹치지 않아야 한다.

## 개발 요구사항 ##
# 퍼즐을 표준 입출력 창에서 인터액티브하게 진행하도록 한다.
# 빈칸이 많을 수록 퍼즐 풀기가 어려워진다. 따라서 난이도를 다음 중에서
# 사용자가 선택하도록 한다.
# 하: 숫자를 10개 채워준다. 중: 숫자를 8개 채워준다. 빈칸 8개 상: 숫자를 6개 채워준다. 빈칸 10개
# 퍼즐게임을 사작하면서 상 또는 중 또는 하 세가지 난이도 중에서 하나를 선택하여 입력하도록 한다.
# "난이도 (상,중,하) 중에서 하나 선택하여 입력: "

# 보드는 아래와 같이 그린다.
# + 1 2 3 4
# 1 4 3 . .
# 2 . 1 . 4
# 3 . . . .
# 4 . . 4 3
# 빈칸은 점으로 표시한다.
# 가로와 세로 줄번호는 각각 1, 2, 3, 4로 번호를 매겨서 왼쪽과 위쪽에 각각 표시한다.

# 사용자는 가로줄번호, 세로줄번호, 숫자를 차례로 다음 순으로 입력한다.
# 가로줄번호(1~4): 2
# 세로줄번호(1~4): 1
# 숫자(1~4): 2

#위치와 숫자가 모두 맞으면 빈칸을 입력한 숫자로 채우고 갱신된 퍼즐보드를 보여준다.

# 빈칸이 아닌 위치를 입력한 경우 숫자를 입력받기 전에 "빈칸이 아닙니다." 라는 메시지를 보여주면서
# 다시 처음부터 입력받는다.
# 빈칸이지만 틀린 숫자를 입력할 경우 그 숫자를 보여주며 "2가 아닙니다. 다시 해보세요." 라는
# 메시지를 보여주면서 줄 번호부터 다시 입력받는다.

# 사용자 입력은 모두 입력확인하여 부적절한 입력의 경우 재입력 받도록 해야한다.
# 빈칸이 다 채워지면 "잘 하셨습니다. 또 들리세요." 라는 메시지를 보여주면서 프로그램을 종료한다.
import random

def sudokmini():
    solution = create_solution_board()
    no_of_holes = get_level() # number of holes
    puzzle = copy_board(solution)
    (puzzle,holeset) = make_holes(puzzle,no_of_holes)
    show_board(puzzle)
    while True:
        i = get_integer("가로줄번호(1~4): ",1,4)-1
        j = get_integer("세로줄번호(1~4): ",1,4)-1
        if (i,j) not in holeset:
            print('빈칸이 아닙니다.')
            continue # while 루프의 처음으로
        n = get_integer("숫자 (1~4): ",1,4)
        sol = solution[i][j]
        if n == sol:
            puzzle[i][j] = sol
            show_board(puzzle)
            holeset.remove((i,j))
            no_of_holes -= 1
        else:
            print(n, "가 아닙니다. 다시 해보세요.")
        if no_of_holes == 0:
            print("잘 하셨습니다. 또 들리세요.")
            break

# 무작위로 퍼즐 정답보드를 만들어 내준다. solution 변수에 저장
def create_solution_board():
    board = create_board()
    board = shuffle_ribbons(board)
    board = transpose(board)
    board = shuffle_ribbons(board)
    board = transpose(board)
    return board

def create_board():
    seed = [1, 2, 3, 4]
    random.shuffle(seed)
    row0 = seed[:]
    row1 = seed[2:] + seed[:2]
    row2 = seed[1:2] + seed[0:1] + seed[3:4] + seed[2:3]
    row3 = row2[2:] + row2[:2]
    return [row0, row1, row2, row3]

# 가로줄을 두 줄씩 무작위로 바꾸는 함수
def shuffle_ribbons(board):
    top = board[:2]
    bottom = board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom

# 보드를 인수로 받아 가로와 세로를 바꾸어 내주는 함수
# (0,1) -> (1,0), (0,2) -> (2,0)
def transpose(board):
    transposed = []
    for i in range(len(board)):
        transposed.append([])
    for a in range(0,4):
        for z in range(0,4):
            transposed[z].append(board[a][z])
    return transposed

# 사용자에게서 입력받은 난이도에 따라 빈칸의 개수를 정한다. 빈칸의 개수는 no_of_holes에 저장
def get_level():
    level = input("난이도 (상,중,하) 중에서 하나 선택하여 입력 : ")
    while level not in {'상','중','하'} :
        level = input("난이도 (상,중,하) 중에서 하나 선택하여 입력 : ")
    if level == '상':
        return 10
    elif level == '중':
        return 8
    else:
        return 6

# 퍼즐보드를 만들기 위해 solution과 똑같은 보드를 하나 복사하여 puzzle에 저장
def copy_board(board):
    board_clone = []
    for row in board:
        row_clone = row[:]
        board_clone.append(row_clone)
    return board_clone

# puzzle과 no_of_holes(빈칸의 개수)를 인수를 받아서 퍼즐의 빈칸을 만든다.
# no_of_holes만큼 퍼즐보드의 빈칸의 개수를 만드는 함수
# 빈칸의 선택은 무작위로 하고, 빈칸은 0으로 채운다.
# 무작위로 빈칸을 넣은 퍼즐보드와 빈칸의 좌표 집합을 내준다.
def make_holes(board, no_of_holes):
    holeset = set()
    while no_of_holes > 0:
        i = random.randint(0,3)
        j = random.randint(0,3)
        if int(board[i][j]) == 0:
            continue
        else:
            board[i][j] = 0
            holeset.add((i,j))
            no_of_holes -= 1
    return (board, holeset)

# 입력받은 퍼즐보드를 보여준다.
# 왼쪽에는 가로줄 번호를 1~4으로 붙이고 위쪽에는 세로줄 번호를 1~~4으로 붙인다.
# 퍼즐보드에서 0값을 가지고 있는 빈칸은 '.'으로 표시한다.
def show_board(board):
    # 1번째 줄
    for f in range(0,5):
        if f == 0:
            print('+ |', end=' ')
        else:
            print(str(f).rjust(2), end=' ')
    print('\n----------------')

    for i in range(1,5):
        print(i, end=' ')
        print('|', end=' ')
        for j in range(0,4):
            if int(board[i-1][j]) != 0:
                print(str(board[i-1][j]).rjust(2), end=' ')
            else:
                print('.'.rjust(2), end=' ')
        print('')
    return 0

# 사용자로부터 수를 입력받아 내줌
def get_integer(comment, a, b):
    integer = input(comment)
    while integer not in {'1','2','3','4'}:
        integer = input(comment)
    return int(integer)

sudokmini()