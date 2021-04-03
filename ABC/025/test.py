b = [list(map(int,input().split())) for i in range(2)]
s = sum(b[0])+sum(b[1])
c = [list(map(int,input().split())) for i in range(3)]
s += sum(c[0])+sum(c[1])+sum(c[2])
ma = [0 for i in range(9)]
def score(t):
    count = 0
    for i in range(3):
        for j in range(3):
            if i != 2 and t[i*3+j] == t[(i+1)*3+j]:
                count+=b[i][j]
            if j != 2 and t[i*3+j] == t[i*3+j+1]:
                count+=c[i][j]
    return count

def dfs(i,t):
    if i == 9:
        for j in range(9):
            if t[j] == 0:
                t = t[:j] + [1] + t[j+1:]
        k = score(t)
        return k
    else:
        if i % 2 == 0:
            tmp2 = []
            for j in range(9):
                if t[j] == 0:
                    tmp2.append(dfs(i+1,list(t[:j] + [2] + t[j+1:])))
            return min(tmp2)
        else:
            tmp2 = []
            for j in range(9):
                if t[j] == 0:
                    tmp2.append(dfs(i+1,list(t[:j] + [1] + t[j+1:])))
            return max(tmp2)
ans = dfs(1,ma)
print(ans)
print(s-ans)
