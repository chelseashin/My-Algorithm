import sys
sys.stdin = open("4013_input.txt")

T = int(input())
for tc in range(T):
    K = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]
    turn = [list(map(int, input().split())) for _ in range(K)]
    print(turn)