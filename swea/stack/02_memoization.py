# Memoization
# recursive 방식 : fibo1()
# 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 overhead가 발생할 수 있음
def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0, 1]
print(fibo1(7))