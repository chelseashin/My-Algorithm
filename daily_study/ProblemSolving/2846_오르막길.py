from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
maxGap = 0
for i in range(N):
    for j in range(i+1, N):
        if A[j-1] < A[j]:
            maxGap = max(maxGap, A[j]-A[i])
        else:
            break
print(maxGap)