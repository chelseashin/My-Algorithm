import sys
sys.stdin = open('14889_input.txt')

from itertools import combinations

# main
N = int(input())
player = [list(map(int, input().split())) for _ in range(N)]
MIN = float('inf')

# 가능한 팀의 조합의 모든 경우
cnt = 0
possible_team = []
for team in combinations(range(N), N//2):
    cnt += 1
    possible_team.append(team)

# combination은 양 끝 결과가 정확하게 대칭을 이루기 때문에 반만 조사
for i in range(cnt//2):
    A, B = 0, 0
    # A팀
    team = possible_team[i]
    for j in range(N//2):   # 같은 팀의 선수들을 인덱스로 찾기 위해
        for k in team:
            A += player[team[j]][k]
    # A를 제외한 나머지 팀
    team = possible_team[-i-1]
    for j in range(N//2):
        for k in team:
            B += player[team[j]][k]
    # print(A, B)
    MIN = min(MIN, abs(A-B))
    # 능력치의 최솟값 나오면 break
    if MIN == 0:
        break

print(MIN)