"""
1.幅と枚数のdpを作成する。
2.小さいスクリーンショットから計算していく。
3.枚数が多いdpに対して2.のスクリーンショットを加えた重要度を考えていく。
4.最終的に全てのdpの中から最大の値を取得する。
"""
def main():
    MaxWidth = int(input())
    NumSheets, MaxSheets = map(int, input().split())
    WidthImportance = \
                   [[int(_) for _ in input().split()] for i in range(NumSheets)]

    # dp[number of sheets][width]: Maximum importance in that sheets and width.
    dp = [[-1]*(MaxWidth+1) for _ in range(MaxSheets+1)]
    dp[0][0] = 0

    for i_width, i_importance in WidthImportance:
        for j_sheet in range(MaxSheets-1, -1, -1):
            
            for k_width, k_importance in enumerate(dp[j_sheet]):
                if k_importance == -1:
                    continue

                next_width = k_width + i_width
                if next_width <= MaxWidth and \
                        dp[j_sheet+1][next_width] < k_importance + i_importance:
                    dp[j_sheet+1][next_width]= k_importance + i_importance

    max_importance = 0
    for i_dp in dp:
        max_importance = max(max_importance, max(i_dp))
    print(max_importance)

if __name__ == '__main__':
    main()