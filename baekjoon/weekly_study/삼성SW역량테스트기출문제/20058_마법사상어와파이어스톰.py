import sys
sys.stdin = open("20058_input.txt")

# main
N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2 ** N)]
L = list(map(int, input().split()))
B = 2 ** N      # 얼음판 크기
print(B)
print(N, Q)
for a in A:
    print(a)
print(L)

# 파이어스톰 시전
for step in L:
    size = 2 ** step
    print(size)
    zeros = [[1] * (B+2) for _ in range(B+2)]
    for sr in range(0, B, size):
        for sc in range(0, B, size):
            temp = [[0] * size for _ in range(size)]
            # 조각마다 90도 회전
            for i in range(size):
                for j in range(size):
                    temp[j][size-i-1] = A[sr+i][sc+j]
            print(temp)
            for i in range(size):
                for j in range(size):
                    A[sr+i][sc+j] = temp[i][j]
                    if temp[i][j]:
                        zeros[sr+i+1][sc+j+1] = 0
    
    # 얼음판 전체 탐색
    for i in range(B):
        for j in range(B):
            if A[i][j] and (zeros[i][j+1] + zeros[i+1][j+2] + zeros[i+1][j] + zeros[i+2][j+1]) >= 2:
                A[i][j] -= 1
                
    
for z in zeros:
    print(z)
print()
for a in A:
    print(a)