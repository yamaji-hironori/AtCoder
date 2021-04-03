import sys

def main():
    X = int(input())

    for a in range(-1000, 1000):
        for b in range(-1000, 1000):

            if X == a**5 - b**5:
                break

        else:
            continue
        break

    print(a, b)
    return

if __name__ == '__main__':
    main()
    sys.exit(0)