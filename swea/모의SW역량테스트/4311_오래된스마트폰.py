import sys
sys.stdin = open('4311_input.txt')

T = int(input())
for tc in range(T):
    N, O, M = map(int, input().split())
    touch_num = list(map(int, input().split()))
    touch_op = list(map(int, input().split()))
    W = int(input())
    