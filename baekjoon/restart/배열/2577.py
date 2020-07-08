import sys
sys.stdin = open('2577.txt')

A = int(input())
B = int(input())
C = int(input())
temp = str(A * B * C)
cnt = [0] * 10

for i in temp:
    cnt[int(i)] += 1
for i in cnt:
    print(i)