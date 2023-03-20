"""
A02 - Linear Search
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_b
"""

def main() -> None:
    _, X = map(int, input().split())
    A_list = [int(_) for _ in input().split()]
    if (X in A_list):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
