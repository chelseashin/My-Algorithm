# 12:07 start
# 12:30 전혀 모르겠어서 아이디어 참고 중..
# 아하 문자열로 바꿔 BFS로 접근해보자.
# 14:07 pass
# 2시간 소요

from sys import stdin
input = stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    check = set([start])
    q = deque([(start, 0)])
    while q:
        temp, cnt = q.popleft()     # 현재 문자열, 이동 횟수
        if temp == "123456780":          # 타겟 문자열과 같으면 그 때의 이동 횟수 리턴
            return cnt

        idx = temp.index("0")   # 0인 곳의 인덱스 
        r, c = idx//3, idx%3    # 이차원 맵 내 좌표로 변환
        for d in range(4):      # 4방향 중 위치 바꿀 수 있는 곳
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < 3 and 0 <= nc < 3):   # 범위 밖은 숫자 교환 불가
                continue

            nextTemp = list(temp)           # 위치 교환 쉽게 하기 위해 리스트로 변환
            nextIdx = nr * 3 + nc           # 위치 교환할 인덱스
            nextTemp[idx], nextTemp[nextIdx] = nextTemp[nextIdx], nextTemp[idx]     # 위치 교환
            nextTemp = ''.join(nextTemp)    # 문자열로 재변환
            
            if nextTemp in check:           # 이미 방문한 곳인지 확인
                continue
            check.add(nextTemp)
            q.append((nextTemp, cnt+1))

    return -1

# main
start = ""               # 시작 문자열
for _ in range(3):
    start += ''.join(list(input().split()))
print(bfs())

