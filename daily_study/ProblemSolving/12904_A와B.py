# 23:38 start
# 24:06 finish

from sys import stdin
input = stdin.readline

# 완전탐색 시간초과 코드..

# def comb(depth, temp):
#     global flag
#     if depth == N:
#         if temp == T:
#             flag = 1
#         return
#     for i in range(2):
#         if i == 0:
#             comb(depth+1, temp + ["A"])
#         else:
#             comb(depth+1, list(reversed(temp)) + ["B"])

# # main
# S = list(input().rstrip())
# T = list(input().rstrip())
# N = len(T) - len(S)

# flag = 0
# comb(0, S)
# if flag:
#     print(1)
# else:
#     print(0)

# Greedy 정답 코드
S = list(input().rstrip())
T = list(input().rstrip())

# T에서 S로 바꾼다고 생각하면 편함!
while len(S) != len(T):
    if T[-1] == "A":    # T의 마지막 문자가 "A"이면 pop
        T.pop()
    else:               # T의 마지막 문자가 "B" 이면 pop하고 뒤집기
        T.pop()
        T.reverse()

# 같으면 1 다르면 0 출력
if S == T:
    print(1)
else:
    print(0)