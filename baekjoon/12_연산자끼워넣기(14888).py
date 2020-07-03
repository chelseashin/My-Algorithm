import sys
sys.stdin = open('12_input.txt')

def dfs(depth, k):
    global Max, Min
    if depth == S:
        # 연산자 순서 출력
        print(result)
        ans = numbers[0]
        for i in range(len(result)):
            if result[i] == 0:
                ans += numbers[i+1]
            elif result[i] == 1:
                ans -= numbers[i+1]
            elif result[i] == 2:
                ans *= numbers[i+1]
            else:
                if ans < 0:
                    ans = (abs(ans) // numbers[i+1]) * (-1)
                else:
                    ans //= numbers[i+1]
        # print(ans)
        if ans > Max:
            Max = ans
        if ans < Min:
            Min = ans
        return
    for i in range(k, 4):
        if not operators[i]:
            continue
        operators[i] -= 1
        result.append(i)
        dfs(depth+1, k)
        operators[i] += 1
        result.pop()

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
S = sum(operators)
Max = float('-inf')
Min = float('inf')
result = []
dfs(0, 0)

print(Max)
print(Min)
