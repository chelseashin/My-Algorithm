# DP(동적계획법)
# iterative 방식 : fibo2()
# Memoization을 재귀적 구조에 사용하는 것보다 
# 반복적 구조로 DP를 구현한 것이 성능 면에서 보다 효율적
def fibo2(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]

print(fibo2(7))