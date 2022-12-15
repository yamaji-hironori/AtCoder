import sys
from io import StringIO
import unittest
import sys
from bisect import bisect_left
def resolve():
    # ★トレース★ 入力の取得
    n = int(input())
    WH = [list(map(int, input().split())) for _ in range(n)]

    # ★トレース★ 2段階にソート。高さの昇順([xx[1])、幅の降順(-xx[0])
    WH.sort(key=lambda xx: [xx[1], -xx[0]])
    # これによりこんな感じにソートされる。
    # 幅,高
    # 4,1
    # 3,1
    # 1,1
    # 1,2
    # 2,3
    # 3,4
    # 2,5
    # 3,8
    # 2,8

    # ★トレース★ 結果保管用のリスト作成。まず「初めの箱の幅 = 高さ最小の箱の内、最も大きい幅」を入れる。
    L = [WH[0][0]]

    # ★トレース★ ループごとに幅が小さく、高さが大きくなる。
    # ★トレース★ 1~箱数分ループ
    for i in range(1, n):
        # ★トレース★ 箱の幅を取得
        w = WH[i][0]

        # ★トレース★
        # 「高さの昇順、幅の降順」のリストに対して
        # 「箱の幅が「最後の箱の幅」を超える場合」とは = 高さが変わるタイミング。
        if L[-1] < w:
            # ★トレース★ 箱を「最後の箱」として追加。(=高さの分だけ、リストが追加される)
            L.append(w)

        # 高さが変わるタイミング以外 = 幅が変わる(減る)タイミング
        else:
            # ★トレース★
            # リストL中の「該当の幅の添え字」を取得
            # 例： L = [3,4] w = 2 の時は「0」が帰ってくる。
            x = bisect_left(L, w)
            # リストL中の「該当の幅を保持している」場所の幅を上書き
            # 例： L = [3,4] w = 2 の時は Lが[2,4]に上書きされる。
            L[x] = w

    print(len(L))


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例1(self):
        input = """3
3 3
1 1
2 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """2
4 5
4 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4
2 5
3 3
4 5
6 6"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """5
8 8
5 3
2 2
4 2
2 1"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()
