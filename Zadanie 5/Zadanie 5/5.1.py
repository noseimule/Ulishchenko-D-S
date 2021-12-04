# -- coding: utf-8 --
n = int(input())
x = 0
i = 1
print(':;;:')
while x <= n:
    x = i**2
    i += 1
    if x <= n:
        print (x)