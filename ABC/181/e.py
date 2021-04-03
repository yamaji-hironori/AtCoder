import sys
sys.setrecursionlimit(10**9)
import bisect

class ABC(object):

    def __init__(self):
        pass

    def small(self, H, W):
        ans = float('inf')
        for i_w in W:
            now_ans =  abs(i_w - H[0])
            if now_ans < ans:
                ans = now_ans
        print(ans)
        return

    def main(self):
        N, M = map(int, input().split())
        H = list(map(int, input().split()))
        W = list(map(int, input().split()))

        if N == 1:
            self.small(H, W)
            return

        H.sort()
        culsum_01 = []
        amount = 0
        for i,j in zip(H[0::2],H[1::2]):
            amount += j-i
            culsum_01.append(amount)
        culsum_12 = []
        amount = 0
        for i,j in zip(H[1::2],H[2::2]):
            amount += j-i
            culsum_12.append(amount)

        ans = float('inf')
        for i_w in W:
            now_ans = 0
            index = bisect.bisect_right(H, i_w)
            culsum_index = index // 2
        
            if culsum_index != 0:
                now_ans += culsum_01[culsum_index - 1]
            else:
                pass

            if culsum_index == 0:
                now_ans += culsum_12[-1]
            else:
                now_ans += culsum_12[-1] - culsum_12[culsum_index - 1]

            now_ans += abs(i_w - H[culsum_index*2])

            if now_ans < ans:
                ans = now_ans

        print(ans)
        return


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)