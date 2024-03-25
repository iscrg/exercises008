import functools
import math

a, b, c = map(int, input().split())
nums = list(range(a, b+1))
nums_filtered = list(filter(lambda x: math.sqrt(x).is_integer() and x % c == 0, nums))
res = functools.reduce(lambda x, y: x * y, nums_filtered)

print(res)
