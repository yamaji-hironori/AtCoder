def main():
    N = [int(_) for _ in input().split()]
    D = N[0]
    G = N[1]
    Q = [[int(_) for _ in input().split()] for i in range(D)]

    print(N, Q)

if __name__ == "__main__":
    main()