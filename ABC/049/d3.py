import sys
sys.setrecursionlimit(10**9)

class ABC(object):

    def __init__(self):
        # index '0' is not used.
        self.parent_pq = [-1]*(2*10**5 + 1)
        self.parent_rs = [-1]*(2*10**5 + 1)
        pass


    def find(self, x, parent):
        if parent[x] < 0:
            return x

        parent[x] = self.find(parent[x], parent)
        return parent[x]


    def unit(self, a, b, parent):
        if a == b:
            return


        p_a = self.find(a, parent)
        p_b = self.find(b, parent)
        if p_a < p_b:
            parent[b] = p_a
        else:
            parent[a] = p_b
        return


    def main(self):
        N, K, L = map(int, input().split())
        pq = [[int(_) for _ in input().split()] for i in range(K)]
        rs = [[int(_) for _ in input().split()] for i in range(L)]

        for p, q in pq:
            self.unit(p, q, self.parent_pq)

        for r, s in rs:
            self.unit(r, s, self.parent_rs)

        return


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)
