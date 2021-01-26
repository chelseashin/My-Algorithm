import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))
ascending = True
descending = True

for i in range(7):
    if numbers[i] < numbers[i+1]:
        descending = False
    elif numbers[i] > numbers[i+1]:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")