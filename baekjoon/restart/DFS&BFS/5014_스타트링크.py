F, S, G, U, D = 10, 1, 10, 2, 1

# F : 건물 높이
# S : 강호가 있는 층
# G : 면접장이 있는 곳(도착점)
# U : 위로 U층 올라가는 버튼
# D : 아래로 D층 올라가는 버튼

from collections import deque

def bfs():
    global ans
    Q = deque([S])  # 강호 위치
    state = False
    while Q:
        s = Q.popleft()
        if s == G:    # 면접장에 도착하면
            state = True
            break
        for i in [U, -D]:
            ns = s + i
            if 0 < ns <= F and not building[ns] and ns != S:
                building[ns] = building[s] + 1
                Q.append(ns)
    if state:
        ans = building[G]
    else:
        ans = "use the stairs"
    return


# main
# F, S, G, U, D = map(int, input().split())

building = [0] * (F+1)
bfs()
print(ans)