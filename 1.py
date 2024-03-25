def check(letter):
    return letter.isupper()


i, j = map(int, input())
line = list(input().split())[i-1:j+1]
res = filter(check, line)
print(len(list(res)))
