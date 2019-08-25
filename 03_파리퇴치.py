import sys
sys.stdin = open("03_input.txt")

def catch(a, b):
    sum = 0
    for i in range(M):
        for j in range(M):
            sum += arr[a+i][b+j]
    return sum

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    max_sum = 0
    sum = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            # sum += arr[x+N][y+N]
            if max_sum < catch(x, y):
                max_sum = catch(x, y)
    print("#{} {}".format(tc+1, max_sum))
