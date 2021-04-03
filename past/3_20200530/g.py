import sys
from collections import deque

def main():
    N, X, Y = map(int, input().split())
    obstacle = [[int(_) for _ in input().split()] for i in range(N)]

    grid = [[None]*405 for _ in range(405)]
    # Assume that the bridge has obstacles.
    grid[0], grid[-1] = [False]*405, [False]*405
    for i_grid in grid:
        i_grid[0], i_grid[-1] = False, False

    for i_x, i_y in obstacle:
        ind_x, ind_y = 202+i_x, 202+i_y
        grid[ind_x][ind_y] = False
    
    now_pos = [202, 202]
    grid[202][202] = 0
    goal_x, goal_y = X+202, Y+202

    dq = deque()
    dq.append(now_pos)
    while len(dq) > 0:
        now_x, now_y = dq.popleft()
        if now_x == goal_x and now_y == goal_y:
            print(grid[now_x][now_y])
            return
        
        for dx, dy in ((1,1),(0,1),(-1,1),(1,0),(-1,0),(0,-1)):
            next_x, next_y = now_x+dx, now_y+dy
            if grid[next_x][next_y] is not None:
                continue

            grid[next_x][next_y] = grid[now_x][now_y] + 1
            dq.append([next_x, next_y])

    print(-1)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)