import sys
sys.stdin = open("2869_input.txt")

A, B, V = map(int, input().split())
days = (V-B) / (A-B)
if days == int(days):
    print(int(days))
else:
    print(int(days)+1)