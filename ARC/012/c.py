import sys


def MyException(Exception):
    pass


def my_input():
    input_num = 19
    b_array = [input() for _ in range(input_num)]
    return b_array


def check_win(b_array):
    win_color = None

    for y, y_b in enumerate(b_array):
        for x, x_b in enumerate(y_b):
            if x_b == '.':
                continue

            now_color = x_b
            try:
                for add_x, add_y in [[1,0], [0,1], [1,1]]:
                    cnt = 0
                    while True:
                        x, y = x+add_x, y+add_y
                        if b_array[y][x] == now_color:
            except IndexError:
                pass

    return win_color


def main():
    b_array = my_input()
    print(b_array)
    print(b_array[0][0])
    print(b_array[18][18])
    # check win
    # black win
    # white win

    # check num
    # black == white
    # black+1 == white

    # check ok
    return


if __name__ == '__main__':
    main()
    sys.exit()
