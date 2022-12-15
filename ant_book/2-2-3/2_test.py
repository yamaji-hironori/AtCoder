KeyString = input()
PartString = input()

ans = "UNRESTORABLE"

for i in range(len(KeyString)-len(PartString)+1):

    for j in range(len(PartString)):
        isRestorable = True
        if not s[j+i] == PartString[j] and not s[j+i] == "?":
            isRestorable = False
            break

    if isRestorable:
        ans = KeyString[0:i] + PartString + KeyString[i+len(PartString):len(KeyString)]
        ans = ans.replace("?", "a")
print(ans)