s = input()
t = input()
# 初期値の設定(結果が偽の場合の値を初期値にしてしまう)
ans = "UNRESTORABLE"
# i文字目から代入した場合、を検証していく
for i in range(len(s)-len(t)+1):
    # iから一文字ずつ、不正な点が無いか検証。
    for j in range(len(t)):
        isRestorable = True
        if not s[j+i] == t[j] and not s[j+i] == "?":
            isRestorable = False
            break
    # 文字が代入できるなら、代入した場合の文字を変数に入れる。
    # これをループしていくので、ansには最終的に、辞書最小値が格納される、というロジック。
    if isRestorable:
        ans = s[0:i] + t + s[i+len(t):len(s)]
        ans = ans.replace("?", "a")
print(ans)