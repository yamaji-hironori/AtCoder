import sys
import bisect

def use_dp_v(N, W, VW):
    INF = float('inf')
    dp_v = [INF] * 200001
    dp_v[0] = 0

    for v, w in VW:
        for i in range(200000, -1, -1):
            if dp_v[i] == INF:
                continue
            if (dp_v[i]+w) > W:
                continue
            dp_v[i+v] = min(dp_v[i+v], (dp_v[i]+w))

    for i in range(200000, -1, -1):
        if dp_v[i] != INF:
            ans = i
            break
    return ans


def use_dp_w(N, W, VW):
    dp_w = [-1] * 200001
    dp_w[0] = 0

    for v, w in VW:
        for i in range(200000, -1, -1):
            if dp_w[i] == -1:
                continue
            if (i+w) > W:
                continue
            dp_w[i+w] = max(dp_w[i+w], (dp_w[i]+v))

    ans = max(dp_w)
    return ans

def enum_full(start, end, ele, W, VW):
    pattern = []
    for i_bin in range(2**ele):
        v, w = 0, 0
        for j_N in range(start, end):
            if i_bin & (1 << (j_N-start)) == 0:
                continue
            v += VW[j_N][0]
            w += VW[j_N][1]
        if w <= W:
            pattern.append([v, w])
        
    pattern.sort()
    pre_v ,pre_w = float('inf'), float('inf')
    del_vw = []
    for i_v, i_w in pattern[::-1]:
        if i_v == pre_v and i_w < pre_w:
            del_vw.append([pre_v, pre_w])
        elif i_v != pre_v and i_w >= pre_w:
            del_vw.append([i_v, i_w])
        else:
            pre_v, pre_w = i_v, i_w
    pattern = [vw for vw in pattern if not vw in del_vw]
    wv = [[w,v] for v,w in pattern]
    return wv

def enum_semi_full(N, W, VW):
    if N == 1:
        if VW[1] <= W:
            return VW[0]
        else:
            return 0

    half_N = N // 2

    wv_a = enum_full(0, half_N, half_N, W, VW)
    wv_b = enum_full(half_N+1, N, N-half_N, W, VW)

    v_combi = []
    w_a = [w for w, _ in wv_a]
    for i_w, i_v in wv_b:
        pair_w = W - i_w
        pair_index = bisect.bisect_right(w_a, pair_w)
        v_combi.append(i_v + wv_a[max(0, pair_index-1)][1])

    ans = max(v_combi)
    return ans


def main():
    N, W = map(int, input().split())
    VW = [[int(_) for _ in input().split()] for i in range(N)]

    max_v, max_w = 0, 0
    for v, w in VW:
        max_v, max_w = max(max_v, v), max(max_w, w)

    if max_v <= 1000:
        ans = use_dp_v(N, W, VW)
    elif max_w <= 1000:
        ans = use_dp_w(N, W, VW) 
    else:
        ans = enum_semi_full(N, W, VW)

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)