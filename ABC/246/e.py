from pprint import pprint
import sys
from typing import List, Tuple
sys.setrecursionlimit(10**9)

xydir = (
    (1, 1),
    (1, -1),
    (-1, -1),
    (-1, 1),
)

def main():
    N = int(input())
    Ax, Ay = map(int, input().split())
    Bx, By = map(int, input().split())
    _S = [input() for _ in range(N)]
    S: List[List[str]] = []
    for i_S in _S:
        S.append([i_c for i_c in i_S])

    from collections import deque
    _queue: deque[Tuple[int, int, int, Tuple[int, int]]] = deque()
    count = 0
    S[Ax-1][Ay-1] = "0"
    direction = None
    _queue.append((Ax, Ay, count, direction)) # type: ignore
    while _queue:
        i_x, i_y, i_count, i_direction = _queue.popleft()
        for next_x, next_y in xydir:
            next_x_pos = i_x + next_x - 1
            next_y_pos = i_y + next_y - 1
            if next_x_pos < 0 or N-1 < next_x_pos or next_y_pos < 0 or N-1 <next_y_pos:
                continue
            if i_direction == (next_x, next_y):
                next_count = i_count
            elif i_direction == (-1 * next_x, -1 * next_y):
                continue
            else:
                next_count = i_count + 1
            if S[next_x_pos][next_y_pos] == "#":
                continue
            elif S[next_x_pos][next_y_pos] == ".":
                S[next_x_pos][next_y_pos] = str(next_count)
                if i_direction == (next_x, next_y):
                    _queue.appendleft((i_x+next_x, i_y+next_y, next_count, (next_x, next_y)))
                else:
                    _queue.append((i_x+next_x, i_y+next_y, next_count, (next_x, next_y)))
            elif next_count < int(S[next_x_pos][next_y_pos]):
                S[next_x_pos][next_y_pos] = str(next_count)
                if i_direction == (next_x, next_y):
                    _queue.appendleft((i_x+next_x, i_y+next_y, next_count, (next_x, next_y)))
                else:
                    _queue.append((i_x+next_x, i_y+next_y, next_count, (next_x, next_y)))
            elif next_count == int(S[next_x_pos][next_y_pos]):
                next_x_pos += next_x
                next_y_pos += next_y
                while next_x_pos >= 0 and N-1 >= next_x_pos and next_y_pos >= 0 and N-1 >= next_y_pos:
                    if S[next_x_pos][next_y_pos] == "#":
                        break
                    elif S[next_x_pos][next_y_pos] == ".":
                        S[next_x_pos][next_y_pos] = str(next_count)
                        _queue.appendleft((next_x_pos+1, next_y_pos+1, next_count, (next_x, next_y)))
                        break
                    elif next_count > int(S[next_x_pos][next_y_pos]):
                        break
                    elif next_count < int(S[next_x_pos][next_y_pos]):
                        S[next_x_pos][next_y_pos] = str(next_count)
                        _queue.appendleft((next_x_pos+1, next_y_pos+1, next_count, (next_x, next_y)))
                        break
                    next_x_pos += next_x
                    next_y_pos += next_y

    if S[Bx-1][By-1] == ".":
        print(-1)
    else:
        print(S[Bx-1][By-1])

    return


if __name__ == "__main__":
    main()
