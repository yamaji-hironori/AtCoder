import sys

def main():
    N = int(input())
    A_list = list(map(int, input().split()))

    h_list = [0] * N

    for i, i_A in enumerate(A_list):
        if i - i_A >= 0:
            h_list[i-i_A] += 1

    total_pair = 0
    for i, i_A in enumerate(A_list):
        if i+i_A <= N-1:
            total_pair += h_list[i+i_A]

    print(total_pair)
    return
    
if __name__ == '__main__':
    main()
    sys.exit(0)