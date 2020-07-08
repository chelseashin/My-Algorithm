import sys
sys.stdin = open("10818_input.txt")

N = int(input())
L = list(map(int, input().split()))
MIN = float('inf')
MAX = float('-inf')

for i in L:
    if i < MIN:
        MIN = i
    if i > MAX:
        MAX = i

print(MIN, MAX)