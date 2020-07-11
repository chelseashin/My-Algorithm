import sys
sys.stdin = open('14888_input.txt')

# 연산자 순열 구하고 계산 하면서 최댓값, 최솟값 구하기
def calculate(depth):
    global numbers, S, MAX, MIN
    if depth == S:
        temp = numbers[0]
        for s in range(S):
            if order[s] == 0:
                temp += numbers[s+1]
            elif order[s] == 1:
                temp -= numbers[s+1]
            elif order[s] == 2:
                temp *= numbers[s+1]
            else:
                if temp < 0:
                    temp = (abs(temp) // numbers[s+1]) * -1
                else:
                    temp //= numbers[s+1]
        if temp > MAX:
            MAX = temp
        if temp < MIN:
            MIN = temp

        return
    for i in range(4):
        if not operators[i]:
            continue
        operators[i] -= 1
        order.append(i)
        calculate(depth + 1)
        order.pop()
        operators[i] += 1


N =  int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
S = sum(operators)
MAX = float('-inf')
MIN = float('inf')

order = []
calculate(0)
print(MAX)
print(MIN)