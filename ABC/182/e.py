import sys
sys.setrecursionlimit(10**9)

class AtCoder(object):
    def __init__(self):
        self.height = None
        self.width = None
        self.block = -1
        self.sparkle = 1
        self.dark = 0
        self.squares_y = None
        self.squares_x = None

    def spark(self, x, y, dx, dy, squares):
        if x+dx > self.width \
                or y+dy > self.height \
                or x+dx < 1 \
                or y+dy < 1 \
                or squares[y+dy][x+dx] == self.block:
            return

        squares[y+dy][x+dx] = self.sparkle
        self.spark(x+dx, y+dy, dx, dy, squares)
        return

    def main(self):
        H, W, N, M = map(int, input().split())
        self.height = H
        self.width = W
        AB = [[int(_) for _ in input().split()] for i in range(N)]
        CD = [[int(_) for _ in input().split()] for i in range(M)]

        # index '0' is not used.
        self.squares_y = [[self.dark for _ in range(W+1)] for _ in range(H+1)]
        self.squares_x = [[self.dark for _ in range(W+1)] for _ in range(H+1)]

        for c, d in CD:
            self.squares_y[c][d] = self.block
            self.squares_x[c][d] = self.block

        for i_squares, grad in [[self.squares_y, [(-1,0),(1,0)]], \
                                [self.squares_x, [(0,-1),(0,1)]]]:
            for a, b in AB:
                y = a
                x = b
                if i_squares[y][x] == self.sparkle:
                    continue
                for dy, dx in grad:
                    i_squares[y][x] = self.sparkle
                    self.spark(x, y, dx, dy, i_squares)

        ans = 0
        for y in range(1, H+1):
            for x in range(1, W+1):
                if self.squares_y[y][x] == self.sparkle \
                        or self.squares_x[y][x] == self.sparkle:
                    ans += 1

        print(ans)
        return

if __name__ == "__main__":
    obj = AtCoder()
    obj.main()
    exit()
