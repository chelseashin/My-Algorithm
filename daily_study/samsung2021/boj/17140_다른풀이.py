import sys
input = sys.stdin.readline

def solve():
    global row, col
    for time in range(101):
        if A[r][c] == k:
            return time
        if row >= col:      # R 연산
            for i in range(1, row+1):
                chk = [0] * 101
                for j in range(1, col+1):
                    if A[i][j]:
                        chk[A[i][j]] += 1
                        A[i][j] = 0         # 값 지우고
                temp = []
                for j in range(1, 101):
                    if chk[j]:
                        temp.append((chk[j], j))
                temp.sort()     # 정렬
                col = max(col, len(temp) * 2)
                j = 1
                for x in temp:
                    A[i][j+1], A[i][j] = x      # 갯수와 수 위치 바꾸며 넣기
                    j += 2
        else:               # C 연산
            for i in range(1, col+1):
                chk = [0] * 101
                for j in range(1, row+1):
                    if A[j][i]:
                        chk[A[j][i]] += 1
                        A[j][i] = 0
                temp = []
                for j in range(1, 101):
                    if chk[j]:
                        temp.append((chk[j], j))
                temp.sort()
                row = max(row, len(temp)*2)
                j = 1
                for x in temp:
                    A[j+1][i], A[j][i] = x      # 해당 열에 값 채우기
                    j += 2
    return -1

# main
r, c, k = map(int, input().split())
A = [[0]*101 for _ in range(101)]
row, col = 3, 3

for i in range(1, 4):
    # 큰 맵을 그리고 그 안에서 연산
    A[i][1], A[i][2], A[i][3] = map(int, input().split())
print(solve())