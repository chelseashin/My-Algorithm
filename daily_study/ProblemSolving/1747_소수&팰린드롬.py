# 78%에서 틀렸습니다..

from sys import stdin
input = stdin.readline

# limit = 1000001
# prime = [0, 0] + [1] * (limit-2)
# for i in range(2, int(limit**0.5)+1):
#     if prime[i]:
#         for j in range(i+i, limit, i):
#             if prime[j]:
#                 prime[j] = 0

def isPalindrome(n):
    length = len(n) // 2
    for i in range(length):
        if n[i] != n[-i-1]:
            return False
    return True

def isPrimeNumber(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            return False
    return True

# main
N = int(input())
while True:
    if isPalindrome(str(N)) and isPrimeNumber(N):
        break
    N += 1
print(N)