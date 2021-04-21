# 실패 .. 다시 풀기
# 문제 : https://www.acmicpc.net/problem/1722
# 참고 코드 : https://rhdtka21.tistory.com/40
# 일반적인 순열 구하기로는 시간초과 남.(1 <= N <= 20)

from sys import stdin
input = stdin.readline

def perm(depth, k, pnum):
    global cnt
    if depth == N:
        cnt += 1
        if pnum == 1 and cnt == target_cnt:
            print(*order)
            exit()
        elif pnum == 2 and order == target_list:
            print(cnt)
            exit()
        return

    for i in range(k, N):
        if visited[i]:
            continue
        visited[i] = 1
        order.append(i+1)
        perm(depth+1, k, pnum)
        order.pop()
        visited[i] = 0

# main
N = int(input())
problems = list(map(int, input().split()))
pnum = problems[0]
if pnum == 1:
    target_cnt = problems[1]
elif pnum == 2:
    target_list = problems[1:]

visited = [0] * N
order = []
cnt = 0
perm(0, 0, pnum)