import sys
sys.setrecursionlimit(10**9)

from collections import deque

class AtCoder(object):
    def __init__(self):
        self.white = 1
        self.black = -1

    def main(self):
        N = int(input())

        # index '0' is not used.
        tree = [[] for _ in range(N+1)]
        for _ in range(N-1):
            u, v, w = map(int, input().split())
            tree[u].append([v, w])
            tree[v].append([u, w])

        dq = deque()
        # append: now_node, cost, pre_node_color
        dq.append([1, 0, self.white])
        # index '0' is not used.
        node_color = [None for _ in range(N+1)]
        while dq:
            now_node, cost, pre_node_color = dq.pop()
            if node_color[now_node] is not None:
                continue

            if cost % 2 == 0:
                node_color[now_node] = pre_node_color
            else:
                node_color[now_node] = -1 * pre_node_color

            for next_node, cost in tree[now_node]:
                dq.append([next_node, cost, node_color[now_node]])

        for i in range(1, N+1):
            if node_color[i] == self.white:
                print(1)
            elif node_color[i] == self.black:
                print(0)
            else:
                raise Exception

        return

if __name__ == "__main__":
    obj = AtCoder()
    obj.main()
    exit()
