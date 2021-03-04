# DP는 코드 자체는 짧은 것을 확인할 수 있다.
# 점화식을 잘 세우고 문제에서 요구하는 원리를 잘 파악하는 것이 관건!

import sys
input = sys.stdin.readline

n = int(input())
check = [0, 1, 2] + [0] * n
for i in range(3, n+1):
    check[i] = (check[i-1] + check[i-2]) % 15746

print(check[n])