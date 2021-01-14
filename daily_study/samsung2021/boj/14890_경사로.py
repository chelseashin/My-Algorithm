import sys
sys.stdin = open("14890_input.txt")

def check_slope(L):
    cnt = 1
    for i in range(1, N):
        # 다음 칸이 현재 칸과 같은 경우
        if L[i-1] == L[i]:
            cnt += 1
        # 다음 칸이 현재 칸보다 높을 경우, 그 동안 지나온 칸이 S개 보다 크거나 같다면
        elif L[i] - L[i-1] == 1 and cnt >= S:
            cnt = 1
        # 다음 칸이 현재 칸보다 낮은 경우, 바로 다음의 칸이 또 한칸 낮지 않은지 확인하기 위한 조건문
        elif L[i-1] - L[i] == 1 and cnt >= 0:
            cnt = -S+1
        else:   # 나머지는 모두 불가
            return 0
    # break 되어 반복문 나온 것이 아니라면 실행
    if cnt >= 0:
        return 1
    return 0

# main
N, S = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    result += check_slope(A[i])
    temp = []
    for j in range(N):
        temp.append(A[j][i])
    result += check_slope(temp)
print(result)