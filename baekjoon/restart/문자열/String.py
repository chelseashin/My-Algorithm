import sys
sys.stdin = open("input.txt")

# 11720
# N = int(input())
# S = input()
# cnt = 0
# for i in S:
#     cnt += int(i)
# print(cnt)

# 10809
# S = "baekjoon"
# # S = input()
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# n = len(alphabet)
# L = [-1] * n
#
# for i in range(len(S)):
#     a = alphabet.index(S[i])
#     if L[a] == -1:
#         L[a] = i
# print(*L)

# 2675
# T = int(input())
# for _ in range(T):
#     N, S = map(str, input().split())
#     ans = ""
#     for s in S:
#         ans += s * int(N)
#     print(ans)

# S = 'zzbbww'
# S = input()
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# cnt = [0] * 26
# for s in S.upper():
#     cnt[alphabet.index(s)] += 1
# if cnt.count(max(cnt)) == 1:
#     ans = alphabet[cnt.index(max(cnt))]
# else:
#     ans = "?"
# print(ans)

# 1152
# S = "The Curious Case of Benjamin Button"
# # S = input()
#
# a = S.split(" ")
# cnt = 0
# for i in a:
#     if not i:
#         continue
#     else:
#         cnt += 1
# print(cnt)

# 2908
# A, B = map(str, input().split())
# a, b = int(A[::-1]), int(B[::-1])
# if a > b:
#     print(a)
# else:
#     print(b)

# 5622
# S = "UNUCIC"
# S = input()
# cnt = len(S)
# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# N = len(dial)
# for i in S:
#     for j in dial:
#         if i in j:
#             cnt += dial.index(j) + 2
# print(cnt)

# 2941
# croatia = input()
# S = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#
# for i in S:
#     croatia = croatia.replace(i, "*")
# print(len(croatia))

# 16922
N = int(input())
L = [str(input()) for i in range(N)]
cnt = 0
for words in L:
    for i in range(len(words)):
        if i != len(words) - 1:
            if words[i] == words[i+1]:
                continue
            elif words[i] in words[i+1:]:
                break
        else:
            cnt += 1
print(cnt)

# 다른 방법
# def checker(word):
#     stack = []
#     for i, c in enumerate(word):
#         if c not in stack:
#             stack.append(c)
#         else:
#             if i != 0 and word[i] != word[i-1]:
#                 return 0
#     return 1
#
# N = int(input())
# words = [str(input()) for i in range(N)]
# cnt = 0
# for w in words:
#     cnt += checker(w)
# print(cnt)