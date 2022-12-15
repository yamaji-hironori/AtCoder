def main():
    from collections import deque

    Height, Width = map(int, input().split())
    Map = [input() for _ in range(Height)]
    min_break_map = [[Height*Width]*Width for _ in range(Height)]
    research_point = deque()

    for y in range(Height):
        for x in range(Width):
            if Map[y][x] == 's':
                y_start = y
                x_start = x
                break
        else:
            continue
        break

    wall_break_num = 0
    min_break_map[y_start][x_start] = wall_break_num

    research_point.append([y_start, x_start])
    while len(research_point) > 0:
        y_now, x_now = research_point.popleft()

        for dy, dx in [(0,-1), (-1,0), (0,1), (1,0)]:
            y_next, x_next = y_now+dy, x_now+dx
            if (y_next <= -1 or Height <= y_next) or \
                                              (x_next <= -1 or Width <= x_next):
                continue

            if Map[y_next][x_next] == '.' and \
                    min_break_map[y_now][x_now] < min_break_map[y_next][x_next]:
                min_break_map[y_next][x_next] = min_break_map[y_now][x_now]
                research_point.append([y_next, x_next])

            elif Map[y_next][x_next] == '#' and \
             min_break_map[y_now][x_now]+1 < min_break_map[y_next][x_next] and \
                                                min_break_map[y_now][x_now] < 2:
                min_break_map[y_next][x_next] = min_break_map[y_now][x_now] + 1
                research_point.append([y_next, x_next])

            elif Map[y_next][x_next] == 'g':
                print('YES')
                exit()

    print('NO')
    exit()

if __name__ == '__main__':
    main()