# def isPrime(N):
#     cnt = 1
#     for j in range(2, N//2):
#         if N%j == 0:
#             cnt += 1
#             return False
#     if cnt == 1:
#         return True
#
# def solution(n):
#     answer = 0
#     for i in range(2, n+1):
#         if isPrime(i) == True:
#             answer += 1
#             print(i)
#     return answer

def solution(n):
    a = set([i for i in range(3, n+1, 2)])
    for i in range(3, n+1, 2):
        if i in a:
            a -= set([i for i in range(i*2, n+1, i)])
    return len(a) + 1
print(solution(10))