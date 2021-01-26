import sys
input = sys.stdin.readline

stack = []
result = []
cnt = 1

N = int(input())
for _ in range(N):          # 데이터 갯수만큼 반복
    num = int(input())
    while cnt <= num:       # 입력받은 데이터에 도달할 때까지 삽입
        stack.append(cnt)
        cnt += 1
        result.append("+")
    if stack[-1] == num:    # 스택의 최상위 원소가 데이터와 같을 때까지 출력
        stack.pop()
        result.append("-")
    else:                   # 불가능한 경우
        print("NO")
        exit(0)
print('\n'.join(result))    # 가능한 경우