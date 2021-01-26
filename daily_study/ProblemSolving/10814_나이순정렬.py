import sys
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    input_data = input().split()
    A.append((int(input_data[0]), input_data[1]))

A.sort(key=lambda x: x[0])
for age, name in A:
    print(age, name)