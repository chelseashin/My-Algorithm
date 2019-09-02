import sys
sys.stdin = open('08_input.txt', 'r')

L, C = map(int, input().split())
password = sorted(list(map(str, input().split())))

def comb(depth, k):
    if depth == L:
        # print(order)
        ans = ''
        flag = 0
        for o in order:
            if password[o] in ['a', 'e', 'i', 'o', 'u']:
                flag += 1
            ans += password[o]
        if flag and len(ans) - flag >= 2:
            print(ans)
        return
    else:
        for i in range(k, C - (L - depth) + 1):
            order.append(i)
            comb(depth+1, i+1)
            order.pop()
order = []
comb(0, 0)

# import itertools
# comb = list(itertools.combinations(password, 4))
# for c in comb:
#     flag = 0
#     for i in c:
#         if i in ['a', 'e', 'i', 'o', 'u']:
#             flag = 1
#     if flag:
#         print(''.join(c))