import sys
sys.stdin = open("09_input.txt")

T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    MAX = 0
    for i in str1:
        temp = 0
        for j in str2:
            if i == j:
                temp += 1
        if temp > MAX:
            MAX = temp

    print("#{} {}".format(tc+1, MAX))