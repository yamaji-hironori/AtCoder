N, M = map(int, input().split())
xy = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

max_group = 1

for mask in range(1 << N):
    group = set()
    for i in range(N):
        if mask & 1 << i:
            for mem in group: # グループ追加判定
                if [mem, i] in xy:
                    continue # つながりがある
                break # つながりがないためこのパターンは失敗
            else: # breakしない ... グループ追加成功
                group.add(i)
                continue
            break # グループ追加失敗、次のパターンへ
    else: # すべてのグループ追加に成功
        max_group = max(max_group, len(group))

print(max_group)