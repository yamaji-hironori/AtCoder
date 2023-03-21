"""
B02 - Divisor Check
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ca
"""

def main() -> None:
    A, B = map(int, input().split())
    for i in range(A, B+1):
        if 100 % i == 0:
            print('Yes')
            break
    else:
        print('No')


if __name__ == '__main__':
    main()
