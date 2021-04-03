import sys
sys.setrecursionlimit(10**9)

class AtCoder(object):
    def __init__(self):
        pass

    def main(self):
        N = int(input())
        A = list(map(int, input().split()))

        # index '0' is not used.
        A.insert(0, 0)
        a_sum = [0 for _ in range(N+1)]
        cumul_sum = [0 for _ in range(N+1)]
        each_max = [0 for _ in range(N+1)]

        for i in range(1, N+1):
            a_sum[i] = A[i] + a_sum[i-1]
            cumul_sum[i] = a_sum[i] + cumul_sum[i-1]
            each_max[i] = max(each_max[i-1], a_sum[i])

        max_val = 0
        for i in range(1, N+1):
            now_max = cumul_sum[i-1] + each_max[i]
            max_val = max(max_val, now_max)

        max_val = max(max_val, cumul_sum[N])
        print(max_val)
        return

if __name__ == "__main__":
    obj = AtCoder()
    obj.main()
    exit()
