import sys

def main():
    N, M, X = map(int, input().split())
    C_A_list = [[int(_) for _ in input().split()] for i in range(N)]

    bit = 1 << N
    INF = float('inf')
    min_price = INF
    for i_bit in range(bit):
        price = 0
        understand_list = [0] * M
        for j_N in range(N):
            if i_bit & (1 << j_N) == 0:
                continue

            price += C_A_list[j_N][0]
            for i, i_A in enumerate(C_A_list[j_N][1:]):
                understand_list[i] += i_A

        for i_understand in understand_list:
            if i_understand < X:
                break
        else:
            min_price = min(min_price, price)

    if min_price == INF:
        print(-1)
    else:
        print(min_price)  

    return


if __name__ == "__main__":
    main()
    sys.exit(0)