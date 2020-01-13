import sys
sys.stdin = open("1244_input.txt")

# N은 주어진 수의 길이, k는 기회 수
def perm(N, k):
    global chance, visited, ans
    if visited[k][int("".join(num))]:
        return
    else: visited[k][int("".join(num))] = 1

    if k == chance:
        money = int("".join(num))
        if ans < money:
            ans = money
    else:
        for i in range(N-1):
            for j in range(i+1, N):
                num[i], num[j] = num[j], num[i]
                perm(N, k+1)
                num[i], num[j] = num[j], num[i]


T = int(input())
for tc in range(T):
    num, chance = input().split()
    num = [n for n in str(num)]
    chance = int(chance)
    # 방문관리, 상태관리
    visited = [[0] * 1000000 for _ in range(chance + 1)]
    # print(visited)
    ans = 0
    perm(len(num), 0)
    print("#{} {}".format(tc+1, ans))