import sys
sys.stdin = open("24_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    count = 1
    if N % 2: nn = N//2+1
    else: nn = N//2
    for i in range(nn, 0, -1):
        temp = i
        for j in range(i-1, 0, -1):
            temp += j
            if temp == N:
                count += 1
                break
            if temp > N:
                break

    print("#{} {}".format(tc+1, count))
