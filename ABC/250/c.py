import sys
sys.setrecursionlimit(10**9)


def main():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]

    pos_to_ball = {} # 並び順: ボール番号
    ball_to_pos = {} # 番号順: 並び番号
    for i in range(N):
        ball_to_pos[i+1] = i+1
        pos_to_ball[i+1] = i+1
    for i_x in x:
        i_pos = ball_to_pos[i_x]
        if i_pos == N:
            left_ball, right_ball = pos_to_ball[N-1], pos_to_ball[N]
            pos_to_ball[N-1], pos_to_ball[N] = right_ball, left_ball
            ball_to_pos[left_ball], ball_to_pos[right_ball] = ball_to_pos[right_ball], ball_to_pos[left_ball]
        else:
            left_ball, right_ball = pos_to_ball[i_pos], pos_to_ball[i_pos+1]
            pos_to_ball[i_pos], pos_to_ball[i_pos+1] = right_ball, left_ball
            ball_to_pos[left_ball], ball_to_pos[right_ball] = ball_to_pos[right_ball], ball_to_pos[left_ball]
    
    ans = ""
    for i_ball in pos_to_ball.values():
        ans += str(i_ball) + " "

    print(ans[0:-1])

    return


if __name__ == "__main__":
    main()
