import sys
sys.stdin = open("14890_input.txt")
input = sys.stdin.readline

N, L = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
print(N, L, A)

result = 0
for i in range(N):
    # print(A[i])
    # result += check(A[i])
    temp = []
    for j in range(N):
        temp.append(A[j][i])
    print(temp)
    # result += check(temp)
