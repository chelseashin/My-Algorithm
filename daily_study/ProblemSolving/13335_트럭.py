# 23:52 start
# 24:13 pass
# 21m 소요

from sys import stdin
input = stdin.readline
from collections import deque

def solve():
    time = 0
    bridge = deque([0] * W)
    while trucks:
        bridge.popleft()
        x = trucks[0]
        if len(bridge) < W and sum(bridge) + x <= L:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
        time += 1
    return time + W

# n : 다리를 건너는 트럭의 수, w : 다리의 길이, L : 다리의 최대하중
N, W, L = map(int, input().split())
trucks = deque(map(int, input().split()))

print(solve())