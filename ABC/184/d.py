import sys
sys.setrecursionlimit(10**9)

class ABC(object):

    def __init__(self):
        # index '0' is not used.
        self.abc = [[[0 for _ in range(101)] for _  in range(101)] for _  in range(101)]
        pass


    def main(self):
        A, B, C = map(int, input().split())
        self.abc[A][B][C] = 1

        for a in range(100):
            for b in range(100):
                for c in range(100):
                    now_abc = self.abc[a][b][c]
                    if now_abc == 0:
                        continue
                
                    self.abc[a+1][b][c] += now_abc * (a/(a+b+c))
                    self.abc[a][b+1][c] += now_abc * (b/(a+b+c))
                    self.abc[a][b][c+1] += now_abc * (c/(a+b+c))

        ans = 0
        for i in range(100):
            for j in range(100):
                ans += ((100-A)+(i-B)+(j-C))*self.abc[100][i][j]
                ans += ((i-A)+(100-B)+(j-C))*self.abc[i][100][j]
                ans += ((i-A)+(j-B)+(100-C))*self.abc[i][j][100]

        print(ans)
        return


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)