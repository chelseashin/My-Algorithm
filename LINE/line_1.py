import sys
sys.stdin = open('line_1.txt')

M, N = map(int, input().strip().split(' '))

T = []
for i in range(M):
    time = int(input())
    T.append(time)
print(T)

total = 0