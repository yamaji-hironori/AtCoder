import sys
sys.setrecursionlimit(10**9)
import collections

class ABC(object):

    def __init__(self):
        i = 0
        cnt = 0
        multi8 = []
        while cnt < 1000:
            multi8.append(cnt)
            i += 1
            cnt = 8 * i

        self.str_multi8 = []
        for i_multi8 in multi8:
            if '0' in str(i_multi8):
                continue
            elif i_multi8 < 10:
                self.str_multi8.append('00'+str(i_multi8))
            elif i_multi8 < 100:
                self.str_multi8.append('0'+str(i_multi8))
            else:
                self.str_multi8.append(str(i_multi8))


    def main(self):
        S = input()
        if len(S) == 1:
            S = '00' + S
        elif len(S) == 2:
            S = '0' + S
        counter = collections.Counter(S)

        for i_multi8 in self.str_multi8:
            counter8 = collections.Counter(i_multi8)
            for j_8key, j_8value in counter8.items():
                if counter[j_8key] < j_8value:
                    break
            else:
                print('Yes')
                break
        else:
            print('No')
        return


if __name__ == "__main__":
    obj = ABC()
    obj.main()
    sys.exit(0)