from itertools import permutations
# 1. product : 복원 순열
# 2. permutation : (비복원) 순열
# 3. combinations_with_replacement : 복원 조합
# 4. combinations : (비복원) 조합

# print(list(permutations(range(1, 5), 2)))

N, M = 4, 4
# N, M = map(int, input().split())
# for x in list(permutations(range(1, N+1), M)):
#     print(*x)

def perm(depth):
    global N, M
    if depth == M:
        print(*order)
        return
    for i in range(1, N+1):
        # 중복순열 할라면! 밑에 두줄 주석
        if visited[i]:
            continue
        visited[i] = 1
        order.append(i)
        perm(depth+1)
        order.pop()
        visited[i] = 0

visited = [0] * (N+1)
order = []
perm(0)