import sys
sys.stdin = open('14890_input.txt')

# 참고
# https://rebas.kr/788

def check_slope(L):
    cnt = 1
    for i in range(1, N):
        # 땅의 높이가 이전 땅의 높이와 같을 때
        if L[i-1] == L[i]:
            cnt += 1
        # 땅의 높이가 이전 땅의 높이보다 높을 때
        elif L[i-1] + 1 == L[i] and cnt >= S:
            cnt = 1
        # 땅의 높이가 이전 땅의 높이보다 낮을 때
        elif L[i-1] - 1 == L[i] and cnt >= 0:
            cnt = -S+1
        # 불가능한 모든 경우
        else:
            break
    # break에 걸리지 않았으면 실행
    else:
        if cnt >= 0:
            return True
    return False

# main
N, S = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 가로 검사
for row in range(N):
    # 행마다 길 검사
    if check_slope(A[row]):
        ans += 1

# A = list(map(list, zip(*A)))
A = list(zip(*A))

# 세로 검사
for col in range(N):
    if check_slope(A[col]):
        ans += 1

print(ans)