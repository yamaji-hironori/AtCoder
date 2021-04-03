import sys
import copy

B = []
C = []
MAN = 0
WOMAN = 1


def get_point(board):
    point = 0
    board = [board[0:3], board[3:6], board[6:9]]

    for i in range(3):
        for j in range(2):
            if board[i][j] == board[i][j+1]:
                point += C[i][j]

            if board[j][i] == board[j+1][i]:
                point += B[j][i]
          
    return point


def dfs(board, cnt):
    if cnt == 10:
        return get_point(board)

    if cnt % 2 == 1:
        who = MAN
        min_or_max = max
    else:
        who = WOMAN
        min_or_max = min

    score = []
    for i in range(9):
        if board[i] is None:
            score.append(dfs(list(board[:i]+[who]+board[i+1:]),cnt+1))

    point = min_or_max(score)
    return point


def main():
    global B
    global C
    b = [list(map(int, input().split())) for _ in range(2)]
    c = [list(map(int, input().split())) for _ in range(3)]
    B, C = b, c
    total = sum(b[0])+sum(b[1])+sum(c[0])+sum(c[1])+sum(c[2])

    board = [None]*9
    ans = dfs(board, 1)

    print(ans)
    print(total - ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)