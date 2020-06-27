import sys
sys.stdin = open("input.txt")

# T = int(input())
# for tc in range(T):
#     S = input()
#     C = ""
#     for i in range(len(S)-1, -1, -1):
#         C += S[i]
#     if S == C: ans = 1
#     else: ans = 0
#
#     print("#{} {}".format(tc+1, ans))

# 2
# T = int(input())
# for tc in range(T):
#     s = input()
#     if s == s[::-1]:
#         ans = 1
#     else:
#         ans = 0
#     print("#{} {}".format(tc+1, ans))

# 3
T = int(input())
for tc in range(T):
    s = input()
    for i in range(len(s)//2):
        if s[i] == s[-i-1]:
            ans = 1
        else:
            ans = 0
    print("#{} {}".format(tc+1, ans))