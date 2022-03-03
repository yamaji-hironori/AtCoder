import sys
sys.setrecursionlimit(10**9)

import bisect

class ABC:
    def __init__(self):
        self.A = []

    def main(self):
        Q = int(input())
        for _ in range(Q):
            i_query = list(map(int, input().split()))
            if (i_query[0] == 1):
                self.add_A(i_query[1])
                pass
            elif (i_query[0] == 2):
                self.find_k_number_le_x(i_query[1], i_query[2])
            elif (i_query[0] == 3):
                self.find_k_number_ge_x(i_query[1], i_query[2])
            else:
                raise Exception("unexcepted number: i_query[0]")
        return

    def add_A(self, x):
        target_index = bisect.bisect_left(self.A, x)
        self.A.insert(target_index, x)

    def find_k_number_le_x(self, x, k):
        start_index = bisect.bisect_right(self.A, x) - 1
        tmp = len(self.A)
        if (start_index < k-1):
            print(-1)
        else:
            print(self.A[start_index - (k-1)])

    def find_k_number_ge_x(self, x, k):
        start_index = bisect.bisect_left(self.A, x)
        if ((len(self.A) - start_index) < k):
            print(-1)
        else:
            print(self.A[start_index + (k-1)])


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)
