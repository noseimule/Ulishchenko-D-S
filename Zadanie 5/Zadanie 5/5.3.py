# -- coding: utf-8 --
n = int(input())
i = 1
l = 0
print(':;;:')
while i <= n:
    i *= 2
    l += 1
    if i <= n:
        print(i, l)