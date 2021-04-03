import sys

num = [None]*10
num[0] = ['###','#.#','#.#','#.#','###']
num[1] = ['.#.','##.','.#.','.#.','###']
num[2] = ['###','..#','###','#..','###']
num[3] = ['###','..#','###','..#','###']
num[4] = ['#.#','#.#','###','..#','..#']
num[5] = ['###','#..','###','..#','###']
num[6] = ['###','#..','###','#.#','###']
num[7] = ['###','..#','..#','..#','..#']
num[8] = ['###','#.#','###','#.#','###']
num[9] = ['###','#.#','###','..#','###']

def decide_num(s):
    global num

    for i, i_num in enumerate(num):
        if i_num == s:
            break
    return i

def main():
    N = int(input())
    S = [input() for i in range(5)]

    ans = ''
    for i in range(1, N+1):
        s = []
        for i_S in S:
            s.append(i_S[4*i-3:4*i])

        num = decide_num(s)
        ans += str(num)

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)