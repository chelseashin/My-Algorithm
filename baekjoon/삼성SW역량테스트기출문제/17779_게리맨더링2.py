import sys
sys.stdin = open('17779_input.txt')

# 참고
# https://chldkato.tistory.com/129

# 구역 나누기
def divide(r, c, dis1, dis2):
    global MIN
    while True:
        while True:
            lr, lc, rr, rc = r+dis1, c-dis1, r+dis2, c+dis2
            if not (rr < N-1 and rc < N):
                break
            nr = r + dis1 + dis2
            nc = c - dis1 + dis2
            if not (0 <= nr < N and 0 <= nc < N):
                break
            temp = find_min(r, c, lr, lc, rr, rc, nc)
            MIN = min(temp, MIN)
            dis2 += 1
        dis1 += 1
        if not (r+dis1 < N-1 and 0 < c-dis1):
            break
        dis2 = 1
    return MIN

def find_min(r, c, lr, lc, rr, rc, nc):
    global total, N, A
    cntLst = [0] * 5

    # 구역 1
    d = 0
    for i in range(lr):
        for j in range(c+1):
            if i == r+d and j == c-d:
                d += 1
                break
            cntLst[0] += A[i][j]
    # 구역 2
    d = 1
    for i in range(rr+1):
        for j in range(N-1, c, -1):
            if i == r+d and j == c+d:
                d += 1
                break
            cntLst[1] += A[i][j]
    # 구역 3
    d = 0
    for i in range(lr, N):
        for j in range(nc):
            if i == lr+d and j == lc+d:
                d += 1
                break
            cntLst[2] += A[i][j]
    # 구역 4
    d = 1
    for i in range(rr+1, N):
        for j in range(N-1, nc-1, -1):
            if i == rr+d and j == rc-d:
                d += 1
                break
            cntLst[3] += A[i][j]

    cntLst[4] = total - sum(cntLst)
    # print(cntLst)
    max_cnt = max(cntLst)
    min_cnt = min(cntLst)
    return max_cnt - min_cnt

# main
N = int(input())
A = []
total = 0
for _ in range(N):
    row = list(map(int, input().split()))
    total += sum(row)
    A.append(row)

MIN = float('inf')
for i in range(N-2):
    for j in range(1, N-1):
        divide(i, j, 1, 1)

print(MIN)