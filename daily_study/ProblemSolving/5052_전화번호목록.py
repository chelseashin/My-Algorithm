from sys import stdin
input = stdin.readline

def solve():
    numbers.sort()
    for i in range(n-1):    #정렬되어 있으므로 i번째는 i+1번째와만 비교해보면 된다
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            return "NO"
    return "YES"

# main
t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [input().rstrip() for _ in range(n)]
    print(solve())