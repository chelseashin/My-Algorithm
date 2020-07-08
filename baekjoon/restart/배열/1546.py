import sys
sys.stdin = open('1546.txt')

N = int(input())
L = list(map(int, input().split()))
MAX = max(L)
new = 0
for i in L:
    new += i/MAX*100
print(new/N)