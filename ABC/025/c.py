import sys
import copy


B = []
C = []
MAN = 0
WOMAN = 1


def get_point(board):
    point = 0

    for i in range(3):
        for j in range(2):
            if board[i][j] == board[i][j+1]:
                point += C[i][j]
            else:
                point -= C[i][j]

            if board[j][i] == board[j+1][i]:
                point += B[j][i]
            else:
                point -= B[j][i]            

    return point


def dfs(board, cnt):
    for i in board:
        if None in i:
            break
    else:
        return get_point(board)

    score = []
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                next_board = copy.deepcopy(board)
                next_board[i][j] = MAN
                score.append(dfs(next_board, cnt+1))
                next_board[i][j] = WOMAN
                score.append(dfs(next_board, cnt+1))

    if cnt % 2 == 1:
        point = max(score)
    else:
        point = min(score)
    return point


def main():
    global B
    global C
    b = [list(map(int, input().split())) for _ in range(2)]
    c = [list(map(int, input().split())) for _ in range(3)]
    B, C = b, c
    total = sum(b[0])+sum(b[1])+sum(c[0])+sum(c[1])+sum(c[2])

    board = [[None]*3 for _ in range(3)]
    ans = dfs(board, 0)

    print(ans)
    print(total - ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)