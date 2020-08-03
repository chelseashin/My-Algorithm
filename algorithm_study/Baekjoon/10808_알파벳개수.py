S = 'baekjoon'
# S = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
A = [0] * 26
for s in S:
    A[ord(s)-ord('a')] += 1
    # A[alphabet.index(s)] += 1
print(*A)
