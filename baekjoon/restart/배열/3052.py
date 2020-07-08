import sys
sys.stdin = open('3052.txt')

numbers = [int(input()) for _ in range(10)]
S = set()
for i in numbers:
    S.add(i%42)
print(len(S))