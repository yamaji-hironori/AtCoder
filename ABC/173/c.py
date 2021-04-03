import sys
sys.setrecursionlimit(10**9)

def main():
    h, w, k = map(int, input().split())
    c = [input() for i in range(h)]

    h_bin = 1 << h
    w_bin = 1 << w

    ans = 0
    for i_h in range(h_bin):
        for i_w in range(w_bin):
            now_count = 0

            for i_line in range(h):
                now_line = 1 << i_line
                if i_h & now_line == 0:
                    continue

                for j_raw in range(w):
                    now_raw = 1 << j_raw
                    if i_w & now_raw == 0:
                        continue

                    if c[i_line][j_raw] == '#':
                        now_count += 1
                    
                    if now_count > k:
                        break

            if now_count == k:
                ans += 1

    print(ans)
    return


if __name__ == "__main__":
    main()
    sys.exit(0)