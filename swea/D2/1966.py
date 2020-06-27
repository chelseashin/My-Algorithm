import sys
sys.stdin = open("input.txt")

# T = int(input())
# for tc in range(T):
#     N = int(input())
#     L = sorted(list(map(int, input().split())))
#     print("#{}".format(tc+1), end =" ")
#     print(*L)

# 메모리 최소
tc = int(input())
for i in range(1, tc + 1):
    n = int(input())
    num = list(map(int, input().split()))
    num.sort()

    print(f'#{i} {" ".join([str(x) for x in num])}')