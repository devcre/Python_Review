def sliding_puzzle():
    board = create_init_board()
    goal = set_goal_board()
    # 빈공간
    empty = (0,0)
    while True:
        print_board(board)
        if board == goal:
            print("Congratulations!")
            break
        num = get_number()
        if num == 0:
            break
        pos = find_position(num, board)
        (empty, board) = move(pos, empty, board)
    print("Please come again.")

# 만든 퍼즐게임보드
def create_init_board():
    return [[0,15,14,13],
            [12,11,10,9],
            [8,7,6,5],
            [4,3,2,1]]

# 해답 게임보드
def set_goal_board():
    return [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,0]]

# 중첩리스트로 표현된 퍼즐보드를 인수로 받아서 실행창에 보드를 프린트하는 함수
def print_board(board):
    for i in range(0,4):
        for j in range(0,4):
            if j != 3:
                if (board[i][j] == 0):
                    print('  ', end=' ')
                else:
                    print(str(board[i][j]).rjust(2), end=' ')
            else:
                if (board[i][j] == 0):
                    print('  ')
                else:
                    print(str(board[i][j]).rjust(2))
    return 0

# 실행창에서 사용자에게서 0부터 15사이의 수를 입력받아 정수로 출력하는 함수,
# 0부터 15사이의 입력인지 입력확인하고 정상입력을 받을때까지 재입력을 받는다.
def get_number():
    while True:
        num = input('Type the number you want to move (Type 0 to quit): ')
        if num.isdigit() == True:
            num = int(num)
            if (num >= 0) & (num  <= 15):
                break
    return num

# 1부터 15사이의 정수 num과 퍼즐보드 board를 인수로 받아
# num의 위치좌표를 행번호와 열번호의 튜플로 내주는함수
def find_position(num, board):
    for i in range(0,4):
        for j in range(0,4):
            if (board[i][j] == num):
                pos = (i,j)
                break
    return pos

# 이동할 번호의 위치좌표 pos와 빈칸의 좌표 empty 그리고 퍼즐보드 board를 인수로 받아서,
# pos가 empty와 이웃해 있는지 확인하고 만약 그렇다면 pos와 empty의 위치가 바뀐 board와 바뀐 empty를 쌍으로 내주는 함수.
# 만약 pos와 empty가 이웃해 있지 않다면 움직일 수 없다는 매세지를 출력하고 바뀌지 않은 상태의 empty와 보드를 그대로 내준다.
def move(pos, empty, board):
    # 옮길 숫자
    num = board[pos[0]][pos[1]]
    emp = board[empty[0]][empty[1]]
    x, y = pos[0], pos[1]
    if ((x == empty[0] and y-1 == empty[1])or
        (x == empty[0] and y+1 == empty[1])or
        (x-1 == empty[0] and y == empty[1])or
        (x+1 == empty[0] and y == empty[1])):
        board[pos[0]][pos[1]], board[empty[0]][empty[1]] = emp, num
        pos, empty = empty, pos
    else:
        print("Can't move! Try again.")
        print('')
    return (empty, board)

sliding_puzzle()