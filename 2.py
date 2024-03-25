a, b, c, d = map(int, input().split())

nums = list(range(a, b+1))
res = list(filter(lambda x: x % c == 0 and x % d == 0, nums))

print(sum(res))
