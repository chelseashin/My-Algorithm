import sys
sys.stdin = open('2170_input.txt')

# 시간 복잡도 O(N*logN)
# 성공코드
# but 나중에 생각 좀더 해보기!

N = int(input())
lines = []
for i in range(N):
    s, e = map(int, input().split())
    lines.append((s, e))
lines.sort()
# print(lines)

# 차례대로 선의 길이를 더해가며
# 현재 시작점과 끝점이 이전 시작점과 끝 점에 포함되거나 겹치는 경우를
# 조건문으로 분기해 중복된 선의 길이를 제거
ans = 0
bS = bE = 0
for s, e in lines:
    if not ans:
        ans = abs(e - s)
        bS = s
        bE = e
        continue
    if bS <= s and bE >= e:
        continue
    ans += abs(e-s)
    if bE > s:
        ans -= abs(bE-s)
    bS = s
    bE = e
print(ans)