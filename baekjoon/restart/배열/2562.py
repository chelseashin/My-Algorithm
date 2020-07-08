import sys
sys.stdin = open('2562.txt')

max_value = 0
max_index = 0
numbers = [int(input()) for _ in range(9)]
for idx, value in enumerate(numbers):
    if value > max_value:
        max_value = value
        max_index = idx + 1
print(max_value)
print(max_index)