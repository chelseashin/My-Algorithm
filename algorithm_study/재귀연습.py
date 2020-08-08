# 재귀함수
# 하나의 함수에서 자기 자신을 다시 호출해 작업을 수행하는 알고리즘

# N부터 1까지 수 차례로 출력
def func1(n):
    if n == 0:
        return
    print(n, end=' ')
    return func1(n-1)

func1(5)
print()

# 1부터 N까지 합 구하기
def func2(n):
    if n == 0: return 0
    return n + func2(n-1)

print(func2(10))

def fibo(n):
    if n <= 1: return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(10))