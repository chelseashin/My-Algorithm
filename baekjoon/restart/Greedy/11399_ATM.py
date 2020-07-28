import sys
sys.stdin = open('11399_input.txt')

N = int(input())
P = list(map(int, input().split()))
temp = 0
waiting = 0
for i in sorted(P):
    waiting += i
    temp += waiting
print(temp)