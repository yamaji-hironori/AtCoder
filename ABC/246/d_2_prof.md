Wrote profile results to d_2.py.lprof
Timer unit: 1e-06 s

Total time: 0.230107 s
File: d_2.py
Function: calculate at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           @profile
     7                                           def calculate(a: int, b: int) -> int:
     8    123659     230107.0      1.9    100.0      return a**3 + a**2*b + a*b**2 + b**3

Total time: 0.872367 s
File: d_2.py
Function: binary_search at line 10

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    10                                           @profile
    11                                           def binary_search(left: int, right: int, a: int, N: int) -> int:
    12    123659      42567.0      0.3      4.9      if right < left:
    13     10001      36601.0      3.7      4.2          return calculate(a, left)
    14    113658      44185.0      0.4      5.1      middle = (left + right) // 2
    15    113658     424566.0      3.7     48.7      i_X = calculate(a, middle)
    16    113658      58415.0      0.5      6.7      i_min_X = float('inf')
    17    113658      40443.0      0.4      4.6      if i_X == N:
    18                                                   return i_X
    19    113658      38411.0      0.3      4.4      elif i_X < N:
    20         4          2.0      0.5      0.0          left = middle + 1
    21         4          4.0      1.0      0.0          i_min_X = binary_search(left, right, a, N)
    22                                               else:
    23    113654      42198.0      0.4      4.8          right = middle - 1
    24    113654     108117.0      1.0     12.4          i_min_X = binary_search(left, right, a, N)
    25                                           
    26    113658      36858.0      0.3      4.2      return i_min_X

Total time: 2.61199 s
File: d_2.py
Function: main at line 28

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    28                                           @profile
    29                                           def main() -> None:
    30         1    1317861.0 1317861.0     50.5      N = int(input())
    31                                               # a = 10**6
    32         1          1.0      1.0      0.0      a = 10**4
    33         1          3.0      3.0      0.0      min_X: Union[int, float] = float('inf')
    34     10002       3635.0      0.4      0.1      while a >= 0:
    35     10001    1279641.0    128.0     49.0          i_min_X = binary_search(0, a, a, N)
    36     10001       6650.0      0.7      0.3          if N <= i_min_X: min_X = min(min_X, i_min_X)
    37     10001       4170.0      0.4      0.2          a -= 1
    38                                           
    39         1         32.0     32.0      0.0      print(min_X)
    40         1          0.0      0.0      0.0      return
