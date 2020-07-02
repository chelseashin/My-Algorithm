import sys
sys.stdin = open("1244_input.txt")

# 숫자리스트, 찬스, 자리
def dfs(N, C, I):
    global MAX
    if C <= 0:
        N = int(''.join(map(str, N)))
        if N > MAX:
            MAX = N
        return

    for i in range(I, size):
        for j in range(i+1, size):
            if N[j] >= N[i]:
                temp = [i for i in N]
                temp[i], temp[j] = temp[j], temp[i]
                dfs(temp, C-1, i)
                # print(temp)


T = int(input())
for tc in range(T):
    n, c = input().split()
    numbers = list(map(int, list(n)))
    chance = int(c)
    size = len(numbers)
    MAX = 0
    dfs(numbers, chance, 0)
    print("#{} {}".format(tc+1, MAX))


#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645