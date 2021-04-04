# https://atcoder.jp/contests/arc012/tasks/arc012_3
import sys

class MyException(Exception):
    pass


def my_input():
    input_num = 19
    b_array = [input() for _ in range(input_num)]
    # b_array example:
    # ...................
    # ...o.........o.....
    # ...o....x..........
    # ........x.x........
    #
    # expected value: '.' or 'o' or 'x'
    return b_array


def check_win(b_array):
    win_color = None
    last_xy = None

    for y, y_b in enumerate(b_array):
        # y_b example: ..o..........x.....
        for x, x_b in enumerate(y_b):
            # x_b example: '.' or 'o' or 'x'
            if x_b == '.':
                continue

            now_color = x_b
            for add_x, add_y in [[1,0], [0,1], [1,1], [-1, 1]]:
                _x = x
                _y = y
                cnt = 1
                while True:
                    try:
                        _x, _y = _x+add_x, _y+add_y
                        if b_array[_y][_x] == now_color:
                            cnt +=1
                        else:
                            break
                    except IndexError:
                        # Conditions to enter this process:
                        # x <= -1 or 19 <= x or 19 <= y
                        break

                if cnt >= 10:
                    raise MyException('except 1')

                elif cnt >= 5:
                    if win_color is None:
                        win_color = x_b
                        win_array = [[x,y]]
                        _x, _y = x, y
                        for _ in range(cnt-1):
                            _x, _y = _x+add_x, _y+add_y
                            win_array.append([_x, _y])

                    else: # win_color is 'o' or 'x'
                        if win_color != now_color:
                            raise MyException('except 2')

                        # win_color == now_color
                        win_array2 = [[x,y]]
                        _x, _y = x, y
                        for _ in range(cnt-1):
                            _x, _y = _x+add_x, _y+add_y
                            win_array2.append([_x, _y])

                        dup_xy = [x for x in win_array if x in win_array2]
                        if len(dup_xy) == 0:
                            raise MyException('except 3')
                        elif len(dup_xy) == 1:
                            if last_xy is None:
                                last_xy = dup_xy
                            elif last_xy == dup_xy:
                                pass
                            else:
                                # Multi WIN line exist
                                raise MyException('except 4')
                        else:
                            # Previous line
                            pass

    return win_color


def count_ox(b_array):
    x_num, y_num = 0, 0
    for y_b in b_array:
        # y_b example: ..o..........x.....
        for x_b in y_b:
            # x_b example: '.' or 'o' or 'x'
            if x_b == 'o':
                x_num += 1
            elif x_b == 'x':
                y_num += 1
            else: # x_b == '.'
                pass
    return x_num, y_num

def main():
    b_array = my_input()

    # Which color win
    try:
        win_color = check_win(b_array)
    except MyException as err:
        print('NO')
        return

    x_num, y_num = count_ox(b_array)
    try:
        if win_color == 'o':
            # black win
            if x_num != y_num + 1:
                raise MyException
        elif win_color == 'x':
            # white win
            if x_num != y_num:
                raise MyException
        else:
            # no winner
            if x_num != y_num + 1 and x_num != y_num:
                raise MyException

    except MyException:
        print('NO')
        return

    print('YES')
    return


if __name__ == '__main__':
    main()
    sys.exit()