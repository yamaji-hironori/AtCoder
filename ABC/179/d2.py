import sys
sys.setrecursionlimit(10**9)

class ABC(object):

    def __init__(self):
        pass


    def main(self):
        N, K = map(int, input().split())
        LR = [[int(_) for _ in input().split()] for i in range(K)]
        mod = 998244353

        enable_step = []
        for l, r in LR:
            for i in range(l, r+1):
                enable_step.append(i)
            
        # '0' index is not used.
        step_pattern = [0]*(N+1)
        step_pattern[1] = 1

        for i_n in range(1, N):
            for l, r in LR:
                if (i_n + r) > N:
                    r = N
                
                step_pattern[i_n + j_enable_step] += step_pattern[i_n]
                step_pattern[i_n + j_enable_step] %= mod
        
        ans = step_pattern[N] % mod
        print(ans)
        return


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)