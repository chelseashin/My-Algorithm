import sys
sys.stdin = open("20055_input.txt")

N, K = map(int, input().split())
belt = list(map(int, input().split()))

print(N, K, belt)

zeroCnt = 0
time = 0
while True:
    if zeroCnt == K:
        break
    belt = [belt[-1]] + belt[:-1]
    zeroCnt += 1
    
    print(zeroCnt, belt)