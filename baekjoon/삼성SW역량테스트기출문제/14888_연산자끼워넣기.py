import sys
sys.stdin = open('14888_input.txt')

def perm(depth):
    global MIN, MAX
    if depth == S:
        # print(result)
        temp = num[0]
        for i in range(S):
            if result[i] == 0:
                temp += num[i+1]
            elif result[i] == 1:
                temp -= num[i+1]
            elif result[i] == 2:
                temp *= num[i+1]
            else:
                if temp >= 0:
                    temp //= num[i+1]
                else:
                    temp = -(-temp // num[i+1])
        MAX = max(MAX, temp)
        MIN = min(MIN, temp)
        return

    for i in range(4):
        if not operators[i]:
            continue
        operators[i] -= 1
        result.append(i)
        perm(depth + 1)
        result.pop()
        operators[i] += 1

# main
N = int(input())
num = list(map(int, input().split()))
operators = list(map(int, input().split()))
S = sum(operators)
MAX = float('-inf')
MIN = float('inf')

result = []
perm(0)
print(MAX)
print(MIN)