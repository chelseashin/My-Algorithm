# DP로 풀기(iteractive 방식) 
# - Memoization을 재귀적 구조에 사용하는 것보다
# 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적
def fibo(n):
    L = [0, 1]
    for i in range(2, N+1):
        L.append(L[i-2] + L[i-1])
    return L[N]

# 재귀로 풀기 - 내부에 시스템 호출 스택을 사용하는 overhead가 발생할 수 있음
def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0, 1]
N = 10

# N = int(input())
print(fibo1(N))
print(fibo(N))