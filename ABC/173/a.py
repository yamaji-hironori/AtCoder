import sys
sys.setrecursionlimit(10**9)

def main():
    n = int(input())

    price = 0
    while True:
        if n <= price:
            break
        price += 1000

    print(price - n)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)