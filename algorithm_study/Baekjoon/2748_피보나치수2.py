def fibo(n):
    L = [0, 1]
    for i in range(1, N):
        L.append(L[-2] + L[-1])
    return L[N]

N = int(input())
print(fibo(N))