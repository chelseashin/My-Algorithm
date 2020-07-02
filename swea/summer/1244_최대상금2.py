import sys
sys.stdin = open("1244_input.txt")

# 메모리 너무 큼..
# 숫자 길이, swap 찬스
def perm(n, c):
    global result, change
    if visited[c][int(''.join(num))]:
        return
    else:
        visited[c][int(''.join(num))] = 1
    if c == change:
        temp = int(''.join(num))
        if result < temp:
            result = temp
    else:
        for i in range(n-1):
            for j in range(i+1, n):
                num[i], num[j] = num[j], num[i]
                perm(n, c+1)
                num[i], num[j] = num[j], num[i]

T = int(input())
for tc in range(T):
    num, change = input().split()
    change = int(change)
    num = list(num)
    visited = [[0] * 1000000 for _ in range(change + 1)]
    result = 0

    perm(len(num), 0)
    print("#{} {}".format(tc+1, result))

# 너무 느림
# def perm(change):
#     global result
#     if change == 0:
#         if int(''.join(a)) > result:
#             result = int(''.join(a))
#             return
#     else:
#         for i in range(len(a) - 1):
#             for j in range(i + 1, len(a)):
#                 if a[i] == a[j]:
#
#                     if change == 1:
#                         if int(''.join(a)) > result:
#                             result = int(''.join(a))
#                     else:
#                         change -= 1
#                 else:
#                     a[i], a[j] = a[j], a[i]
#                     perm(change - 1)
#                     a[i], a[j] = a[j], a[i]
#
# T = int(input())
# for tc in range(T):
#     a, change = input().split()
#     change = int(change)
#     a = list(a)
#     result = 0
#     if change > len(a):
#         change = len(a)
#     perm(change)
#     print("#{} {}".format(tc+1, result))