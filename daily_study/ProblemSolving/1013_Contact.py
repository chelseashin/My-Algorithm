from sys import stdin
input = stdin.readline
import re

N = int(input())
for _ in range(N):
    wave = input().strip()
    p = re.compile('(100+1+|01)+')
    result = p.fullmatch(wave)
    if result:
        print("Yes")
    else:
        print("No")