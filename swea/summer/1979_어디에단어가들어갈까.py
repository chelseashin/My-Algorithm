import sys
sys.stdin = open("1979_input.txt")

def check_row(x, y):
    if puzzle[x][y - 1] == 0 and puzzle[x][y + K] == 0:
        cnt = 0
        for i in range(K+1):
            if puzzle[x][y+i]:
                cnt += 1
        if cnt == K:
            return 1
        else:
            return 0
    return 0

def check_col(y, x):
    if puzzle[y - 1][x] == 0 and puzzle[y + K][x] == 0:
        cnt = 0
        for i in range(K+1):
            if puzzle[y+i][x]:
                cnt += 1
        if cnt == K:
            return 1
        else:
            return 0
    return 0

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    puzzle = [[0] * (N+2) for _ in range(N+2)]
    for i in range(1, N+1):
        puzzle[i] = [0] + list(map(int, input().split())) + [0]
    count = 0
    for i in range(1, N+1):
        for j in range(N-K+2):
            if puzzle[i][j] == 1:
                count += check_row(i, j)
            if puzzle[j][i] == 1:
                count += check_col(j, i)

    print("#{} {}".format(tc+1, count))

# 쉬운 풀이 - 문자열로 바꾸어 0 기준으로 나누어 연속된 1의 개수 구하기
# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#     data_row = [''.join(input().split()) for _ in range(N)]
#     data_col = [''.join(i) for i in zip(*data_row)]
#     print(data_row)
#     print(data_col)
#     total = data_row + data_col
#     ans = 0
#     for i in total:
#         result = i.split('0')
#         # print(result)
#         if '1' * K in result:
#             ans += result.count('1' * K)
#     print("#{} {}".format(test_case + 1, ans))

#1 2
#2 6
#3 6
#4 0
#5 14
#6 2
#7 45
#8 0
#9 98
#10 7