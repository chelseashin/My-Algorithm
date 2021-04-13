# 11:38 start
# 정답 참고 - https://subong0508.github.io/problem-solving/2021/01/31/BOJ-16987.html

from sys import stdin
input = stdin.readline

# (현재 탐색할 계란, 깬 계란 수, 현재 계란 상태) 
def crush(l, cur, eggs):
    global cnt
    # 현재 계란이 가장 오른쪽 계란이면 최댓값 갱신
    if l == n:
        cnt = max(cnt, cur)
        return
    
    # 깨지지 않은 계란이면
    if eggs[l][0] > 0:
        all_broken = True
        for r in range(n):
            # 손에 든 계란이거나 이미 깨진 계란
            if r == l or eggs[r][0] <= 0:
                continue
            all_broken = False
            eggs[l][0] -= eggs[r][1]
            eggs[r][0] -= eggs[l][1]
            cur_ = cur
            cur_ += 1 if eggs[l][0] <= 0 else 0
            cur_ += 1 if eggs[r][0] <= 0 else 0
            crush(l+1, cur_, eggs)
            eggs[l][0] += eggs[r][1]
            eggs[r][0] += eggs[l][1]

        # 다 깨진 계란
        if all_broken:
            crush(l+1, cur, eggs)
    # 손에 든 계란이 깨진 경우
    else:
        crush(l+1, cur, eggs)

# main
n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
# print(eggs)

cnt = 0
crush(0, 0, eggs)
print(cnt)