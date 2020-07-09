import sys
sys.stdin = open("input.txt")

# N = int(input())
# L = [int(input()) for _ in range(N)]
# for i in sorted(L):
#     print(i)


# Bubble Sort(버블 정렬)
# 시간복잡도 O(n^2)

# 오름차순으로 풀기
def bubbleSort(data):
    for i in range(len(data)-1, 0, -1):   # 범위의 끝 위치 : 4, 3, 2, 1 순서로 들어옴
        for j in range(i): # 4, 3, 2, 1 : 오름차순
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
# bubbleSort(L)
# for i in L:
#     print(i)

# print(L)

def CountingSort(a, b, c):
    for i in range(len(a)):
        c[a[i]] += 1
    for j in range(1, len(c)):
        c[j] += c[j-1]
    for k in range(len(a)-1, -1, -1):
        b[c[a[k]]-1] = a[k]
        c[a[k]] -= 1
#
# b = [0] * N
# c = [0] * 10
# CountingSort(L, b, c)
# for i in b:
#     print(i)

# 메모리 초과
# n = int(sys.stdin.readline())
# b = [0] * 10001
# for i in range(n):
#     b[int(sys.stdin.readline())] += 1
# # print(b)
# for j in range(len(b)):
#     if b[j]:
#         for k in range(b[j]):
#             print(j)

# N = int(input())
# cnt_list = [0] * 10001
#
# for i in range(N):
#     cnt_list[int(input())] += 1
# for i in range(10001):
    # 정답
    # sys.stdout.write('%s\n' % i * cnt_list[i])
    # 메모리초과
    # if cnt_list[i]:
    #     for j in range(cnt_list[i]):
    #         print(i)

# 2108
# N = int(input())
# L = sorted([int(input()) for _ in range(N)])
# D = {}
# for num in L:
#     # if D.get(num) is None:
#     if num not in D.keys():
#         D[num] = 1
#     else:
#         D[num] += 1
# most = max(D.values())
# most_list = []
# for key, value in D.items():
#     if value == most:
#         most_list.append(key)
# if len(most_list) > 1:
#     M = most_list[1]
# else:
#     M = most_list[0]
#
# print(round(sum(L)/N))
# print(L[N//2])
# print(M)
# print(max(L)-min(L))

# 1427
# N = list((input()))
# L = [int(i) for i in N]
# L.sort(reverse=True)
#
# for i in L:
#     print(i, end="")

# 11650
# N = int(input())
# L = [list(map(int, input().split())) for _ in range(N)]
# L.sort(key=lambda x: (x[0], x[1]))
# for a, b in L:
#     print(a, b)

# 11651
# N = int(input())
# L = [list(map(int, input().split())) for _ in range(N)]
# L.sort(key=lambda x: (x[1], x[0]))
# for a, b in L:
#     print(a, b)

# 1181
# N = int(input())
# words_list = []
# for i in range(N):
#     word = input()
#     word_count = len(word)
#     words_list.append((word, word_count))
#
# words_list = list(set(words_list))
# words_list.sort(key=lambda x: (x[1], x[0]))
# # print(words_list)
# for word in words_list:
#     print(word[0])

# 10814
N = int(input())
L = [list(map(str, input().split())) for _ in range(N)]
L.sort(key=lambda x:int(x[0]))
for a, b in L:
    print(a, b)