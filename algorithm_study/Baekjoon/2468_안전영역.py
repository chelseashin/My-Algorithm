# https://chldkato.tistory.com/14?category=876515
import sys
sys.stdin = open('2468_input.txt')

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
print(A)