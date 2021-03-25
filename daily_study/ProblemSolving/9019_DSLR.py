# 참고 : https://jjangsungwon.tistory.com/36
from sys import stdin
input = stdin.readline
from collections import deque

def bfs(start, end):
    Q = deque([(start, '')])
    visited = [0] * 10000
    visited[start] = 1
    while Q:
        num, temp = Q.popleft()

        if num == end:       # 목표 숫자에 도달하면 리턴
            return temp
        # D
        if not visited[num*2 % 10000]:
            visited[num*2 % 10000] = 1
            Q.append((num*2 % 10000, temp+"D"))
        # S
        if not visited[(num-1) % 10000]:
            visited[(num-1) % 10000] = 1
            Q.append(((num-1) % 10000, temp+"S"))
        # L
        if not visited[num % 1000 * 10 + num//1000]:
            visited[num % 1000*10 + num//1000] = 1
            Q.append((num % 1000*10 + num//1000, temp+"L"))
        # R
        if not visited[num % 10*1000 + num//10]:
            visited[num % 10*1000 + num//10] = 1
            Q.append((num % 10*1000 + num//10, temp+"R"))


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))