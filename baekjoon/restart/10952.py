import sys
sys.stdin = open('10952_input.txt')

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break