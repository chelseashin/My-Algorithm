from sys import stdin
input = stdin.readline

# 부등호 만족하는지 True, False로 리턴
def isSatisfied(num1, sign, num2):
    if sign == ">":
        return num1 > num2
    else:
        return num1 < num2

def perm(depth, temp):
    global MIN, MAX
    if depth == N+1:
        # print(temp)
        MIN = min(MIN, int(temp))
        MAX = max(MAX, int(temp))
        return
    for n in range(10):
        if check[n]:
            continue
        # 첫 번째 수이거나 부등호를 만족하는 경우에만 방문 표시하고 재귀로 넘어감
        if depth == 0 or isSatisfied(int(temp[-1]), sign[depth-1], n):
            check[n] = 1
            perm(depth+1, temp + str(n))
            check[n] = 0

# main
N = int(input())
sign = input().split()

MIN, MAX = float('inf'), float('-inf')
check = [0] * 10
perm(0, "")
print(str(MAX))
if len(str(MIN)) < N+1:
    print("0"+str(MIN))
else:
    print(str(MIN))