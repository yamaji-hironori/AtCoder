Wrote profile results to d.py.lprof
Timer unit: 1e-06 s

Total time: 0.254063 s
File: d.py
Function: calc_x at line 9

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     9                                           @profile
    10                                           def calc_x(a: int, b: int) -> int:
    11    123659     254063.0      2.1    100.0      return a**3 + a**2 * b + a * b**2 + b**3

Total time: 0.891164 s
File: d.py
Function: binaly_search at line 13

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    13                                           @profile
    14                                           def binaly_search(a: int, left: int, right: int) -> Union[int, float]:
    15    123659      43781.0      0.4      4.9      if right < left:
    16     10001      41609.0      4.2      4.7          return calc_x(a, left)
    17    113658      45381.0      0.4      5.1      middle = (left + right) // 2
    18    113658     448031.0      3.9     50.3      now_x = calc_x(a, middle)
    19    113658      42481.0      0.4      4.8      if now_x == N:
    20                                                   return now_x
    21    113658      40400.0      0.4      4.5      elif now_x < N:
    22         4          4.0      1.0      0.0          left = middle + 1
    23         4          4.0      1.0      0.0          match_x = binaly_search(a, left, right)
    24    113654      39038.0      0.3      4.4      elif now_x > N:
    25    113654      44344.0      0.4      5.0          right = middle - 1
    26    113654     109851.0      1.0     12.3          match_x = binaly_search(a, left, right)
    27                                               else:
    28                                                   raise Exception('unexpected')
    29    113658      36240.0      0.3      4.1      return match_x

Total time: 1.33395 s
File: d.py
Function: main at line 31

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    31                                           @profile
    32                                           def main():
    33                                               # a = 10 ** 6
    34         1          4.0      4.0      0.0      a = 10 ** 4
    35                                               global min_x
    36     10002       3682.0      0.4      0.3      for i in range(a+1):
    37     10001    1322637.0    132.3     99.2          now_x = binaly_search(i, 0, i)
    38     10001       7597.0      0.8      0.6          if (now_x >= N): min_x = min(min_x, now_x)
    39         1         30.0     30.0      0.0      print(min_x)
    40         1          0.0      0.0      0.0      return
