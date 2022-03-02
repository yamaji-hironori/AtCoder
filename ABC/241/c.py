import sys
sys.setrecursionlimit(10**9)

class ABC:
    def __init__(self):
        pass

    def main(self):
        self.N = int(input())
        self.S = [input() for i in range(self.N)]

        for x in range(self.N):
            for y in range(self.N):
                if ( self.check_vertical(x, y)
                  or self.check_horizontal(x, y)
                  or self.check_diagonal(x, y)
                  or self.check_diagonal_reverse(x, y)):
                    print("Yes")
                    return
        print("No")

    def check_vertical(self, x, y):
        if (x >= self.N-5):
            return False

        check_6 = []
        for dx in range(6):
            check_6.append(self.S[x+dx][y])
        if (check_6.count("#") >= 4):
            return True
        else:
            return False

    def check_horizontal(self, x, y):
        if (y >= self.N-5):
            return False

        check_6 = []
        for dy in range(6):
            check_6.append(self.S[x][y+dy])
        if (check_6.count("#") >= 4):
            return True
        else:
            return False

    def check_diagonal(self, x, y):
        if (x >= self.N-5) or (y >= self.N-5):
            return False

        check_6 = []
        for di in range(6):
            check_6.append(self.S[x+di][y+di])
        if (check_6.count("#") >= 4):
            return True
        else:
            return False

    def check_diagonal_reverse(self, x, y):
        if (x <= 4) or (y >= self.N-5):
            return False

        check_6 = []
        for di in range(6):
            check_6.append(self.S[x-di][y+di])
        if (check_6.count("#") >= 4):
            return True
        else:
            return False


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)
