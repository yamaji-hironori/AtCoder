import sys
sys.setrecursionlimit(10**9)
from collections import deque

class ABC(object):

    def __init__(self):
        pass


    def main(self):
        H, W = map(int, input().split())
        town = [input() for i in range(H)]

        # search start
        for i_H in range(H):
            for i_W in range(W):
                if town[i_H][i_W] == 'S':
                    start = (i_H, i_W)

        q = deque()
        q.append(start)
        while q:
            y, x = q.popleft()
            for dy, dx in [(0,-1), (-1,0), (0,1), (1,0)]:
                y_next, x_next = y_now+dy, x_now+dx
                if (y_next <= -1 or H <= y_next) or (x_next <= -1 or W <= x_next):
                    continue
                
        return


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)