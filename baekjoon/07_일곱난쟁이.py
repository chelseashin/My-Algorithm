import sys
sys.stdin = open('07_input.txt')

dwarf = [int(input()) for _ in range(9)]
# 외부 라이브러리 사용
# import itertools
# for comb in list(itertools.combinations(dwarf, 7)):
#     sum = 0
#     L = []
#     for c in comb:
#         sum += c
#         L.append(c)
#     if sum == 100:
#         for l in sorted(L):
#             print(l)
#         break


def comb(depth, k):
    global count
    if depth == 7:
        print(order)
        count += 1
        return
        # sum = 0
        # ans = []
        # for o in order:
        #     sum += dwarf[o]
        #     ans.append(dwarf[o])
        # if sum == 100:
        #     for i in sorted(ans):
        #         print(i)
        #     return
    for i in range(k, 9):
        order.append(i)
        comb(depth+1, i+1)
        order.pop()

order = []
count = 0
comb(0, 0)
print("조합 갯수 :", count, "개")
