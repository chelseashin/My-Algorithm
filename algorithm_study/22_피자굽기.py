import sys
sys.stdin = open("22_input.txt")

T = int(input())
for tc in range(T):
    # N : 화덕의 크기, M : 피자의 개수
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    # 피자에 번호 붙이기
    new = []
    for i in range(M):
        new.append([i+1, Ci[i]])
    
    # Queue 채우기
    Q = new[:N]

    idx = N
    while Q:
        temp = Q.pop(0)
        if temp[1] // 2 != 0:
            temp[1] = temp[1] // 2
            Q.append(temp)
        elif idx < M:
            Q.append(new[idx])
            idx += 1

    print("#{} {}".format(tc+1, temp[0]))