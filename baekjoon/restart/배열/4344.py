import sys
sys.stdin = open('4344.txt')

N = int(input())
for _ in range(N):
    L = list(map(int, input().split()))
    AVG = sum(L[1:]) / L[0]
    # print(L, AVG)
    cnt = 0
    for i in L[1:]:
        if i > AVG:
            cnt += 1
    num = cnt / (len(L)-1) * 100
    # print(str(round(cnt / (len(L)-1) * 100, 3)) + "%")
    print('%.3f' % num + "%")