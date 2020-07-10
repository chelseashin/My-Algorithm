# 재귀 이용
# def hanoi(n, a, b, c):
#     if n == 1:
#         move.append((a, c))
#         return
#     else:
#         hanoi(n - 1, a, c, b)
#         move.append((a, c))
#         hanoi(n - 1, b, a, c)
#
# N = int(input())
# move = []
# hanoi(N, 1, 2, 3)
# print(move)
# print(len(move))
# for a, b in move:
#     print(a, b)

# 최적화
# def hanoi(n, from_, to_, by_):
#     if n == 1:
#         print(from_, by_)
#     else:
#         hanoi(n-1, from_, by_, to_)
#         print(from_, by_)
#         hanoi(n-1, to_, from_, by_)

def hanoi(n, from_, to_, by_):
    if n == 0:
        return
    else:
        hanoi(n-1, from_, by_, to_)
        print("{}에서 {}로 이동한다".format(from_, by_))
        hanoi(n-1, to_, from_, by_)

# n = int(input())
n = 3
total = 2**n - 1
print(total)
hanoi(n,1,2,3)