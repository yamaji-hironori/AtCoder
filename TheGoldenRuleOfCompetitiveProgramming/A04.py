"""
A04 - Binary Representation 1
https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_d
"""

def main() -> None:
    N = int(input())
    binary = bin(N)[2:]
    binary = binary.zfill(10)
    print(binary)



if __name__ == '__main__':
    main()
