import sys
sys.setrecursionlimit(10**9)

def main():
    n = int(input())
    a = [input() for i in range(n)]

    C = {'AC': 0,
         'WA': 0,
         'TLE': 0,
         'RE': 0
         }

    for i_a in a:
        for j_C, j_num in C.items():
            if i_a == j_C:
                C[j_C] = j_num + 1

    for j_C, j_num in C.items():
        print('%s x %s' % (j_C, j_num))
    return


if __name__ == "__main__":
    main()
    sys.exit(0)