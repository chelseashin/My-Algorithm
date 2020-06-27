import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    data = input()

    j = 0
    for i in range(1, 30):
        if data[i] == data[j]:
            j += 1
        else:
            j = 0
    print("#{} {}".format(tc+1, 30-j))