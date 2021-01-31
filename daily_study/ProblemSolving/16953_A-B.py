import sys
input = sys.stdin.readline


def dfs(depth, temp):
    global MIN
    if temp == B:
        MIN = min(MIN, depth)
        return
    elif temp > B:
        return
    dfs(depth + 1, temp * 2)
    dfs(depth + 1, int(str(temp) + '1'))

# main
A, B = map(int, input().split())
# 방법 1 - dfs 완전탐색
# MIN = float('inf')
# dfs(1, A)
# if MIN == float('inf'):
#     print(-1)
# else:
#     print(MIN)

# 방법 2. B -> A를 만들어가는 과정
cnt = 1
while True:
    if A == B:
        print(cnt)
        break
    elif A > B:
        print(-1)
        break
    else:
        cnt += 1
        if B % 2 == 0:      # 짝수이면 2로 나누기
            B //= 2
        elif B % 10 == 1:   # 나머지가 1이면 10으로 나누기
            B //= 10
        else:
            print(-1)
            break
    print(B)