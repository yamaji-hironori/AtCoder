import sys

def main() -> None:
    h, w, x, y = map(int, input().split())
    s_list = [input() for _ in range(h)]

    # x,yを要素番号に合わせる
    x, y = x-1, y-1

    ans = 1
    for add_x, add_y in [[0,1],[1,0],[-1,0],[0,-1]]:
        _x, _y = x, y
        while True:
            _x, _y = _x+add_x, _y+add_y
            if _x <= -1 or _y <= -1:
                break

            try:
                if s_list[_x][_y] == '.':
                    ans += 1
                else:
                    break
            except IndexError:
                break

    print(ans)

if __name__ == '__main__':
    main()
    sys.exit()