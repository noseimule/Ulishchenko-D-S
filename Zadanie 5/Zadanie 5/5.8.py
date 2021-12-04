# -- coding: utf-8 --
from typing import no_type_check


i = -1
k = 0
n = 0
e = int(input())
while e != 0:
    if i == e:
        k += 1
    else:
        i = e
        n = max(n, k)
        k = 1
    e = int(input())
n = max(n, k)
print(n)