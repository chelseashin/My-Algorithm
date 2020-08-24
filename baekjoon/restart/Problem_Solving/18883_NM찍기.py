N, M = 3, 4
# N, M = map(int, input().split())

num = 0
for i in range(N):
    for j in range(M):
        num += 1
        if num % M == 0:
            print(num, end='')
        else:
            print(num, end=' ')
    print()