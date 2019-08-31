import itertools

pool = range(1, 10)
# print(list(itertools.permutations(pool, 2)))  # 3개의 원소로 수열 만들기
# print(list(map(''.join, itertools.permutations(pool, 2))))  # 2개의 원소로 수열 만들기

# print(list(itertools.combinations(pool, 3)))

result =[]
def dfs(depth):
    # if result[2] == 5:
    #     return
    if depth == 10:
        check(result)
    for i in range(1, 10):
        result.append(i)
        dfs(depth + 1)
        result.pop()



def check():
    return



# for each in itertools.permutations(pool):
#     check(each)

# for i in range(1, 5):
#     for each in itertools.permutations(pool, i):
#         if each[0] == 1:
#             continue
#         print(each)
#
# for i in range(3, 6):
#     for comb in itertools.combinations(pool, i):
#         print('여기서 시작')
#         for perm in itertools.permutations(comb):
#             print(perm)


ro = range(2, 5)
print(list(itertools.permutations(ro, 2)))
print(list((itertools.product(ro, repeat=3))))
# for i in range(2, 5):
#     for j in range(2, 5):
#         print(i, j)

