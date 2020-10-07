import sys
sys.stdin = open('17136_input.txt')
input = sys.stdin.readline

# Backtracking + Brute Force

# 단순하게 생각하기!
# (0, 0)에서 시작해서 범위 넘으면 열, 행 순으로 밀어주면서 좌표 이동
# 붙일 수 있는 여부 판단해서 붙이고 재귀로 해당 위치 다음부터 재탐색

def dfs(r, c, cnt):
    global result
    if r >= 10:     # 행의 크기가 맵 크기 넘어가면 탐색 완료, 최솟값 갱신
        result = min(result, cnt)
        return
    if c >= 10:     # 열의 크기가 맵 크기 넘어가면 다음 행으로 넘어가기
        dfs(r+1, 0, cnt)
        return
    if A[r][c]:
        for size in range(5):
            # 색종이 붙일 수 있는 기초 조건 확인
            if papers[size] == 5:
                continue
            if r+size >= 10 or c+size >= 10:
                continue

            flag = 1    # 색종이 붙일 수 있는 여부 판단
            for i in range(r, r+size+1):
                for j in range(c, c+size+1):
                    if A[i][j] == 0:
                        flag = 0
                        break
                if not flag:
                    break

            if flag:
                for i in range(r, r+size+1):
                    for j in range(c, c+size+1):
                        A[i][j] = 0    # 색종이 붙이기

                papers[size] += 1           # 색종이 사용
                dfs(r, c+size+1, cnt+1)     # 행은 그대로, 열은 다음 위치부터 탐색
                papers[size] -= 1           # 색종이 복원

                for i in range(r, r+size+1):
                    for j in range(c, c+size+1):
                        A[i][j] = 1    # 색종이 떼기
    else:
        dfs(r, c+1, cnt)    # 값 없으면 다음 열의 값으로 넘어가기


A = [list(map(int, input().split())) for _ in range(10)]
papers = [0] * 5
result = 26
dfs(0, 0, 0)

if result == 26:
    print(-1)
else:
    print(result)