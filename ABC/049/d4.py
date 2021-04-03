import sys
sys.setrecursionlimit(10**9)
import collections

class UnionFind(object):
    def __init__(self, node):
        # index '0' is not used
        self.parent = [i for i in range(node+1)]


    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 <= parent2:
            self.parent[parent2] = parent1
        else:
            self.parent[parent1] = parent2

        return


    def find(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]


class ABC(object):

    def __init__(self):
        pass


    def main(self):
        N, K, L = map(int, input().split())
        uf_car = UnionFind(N)
        uf_train = UnionFind(N)

        for _ in range(K):
            p, q = map(int, input().split())
            uf_car.union(p, q)

        for _ in range(L):
            r, s = map(int, input().split())
            uf_train.union(r, s)

        pair = [(uf_car.find(i), uf_train.find(i)) for i in range(1, N+1)]
        counter = collections.Counter(pair)

        ans = [counter[pair[i]] for i in range(N)]

        print(*ans)
        return


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)
