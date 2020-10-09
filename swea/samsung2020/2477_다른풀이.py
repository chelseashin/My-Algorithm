import sys
sys.stdin = open('2477_input.txt')

# 다른 풀이

# main
T = int(input())
for tc in range(T):
    # 접수창구 수, 정비창구 수, 이용고객 수, 지갑 분실한 고객이 사용한 창구 번호 A, B
    N, M, K, A, B = map(int, input().split())
    recept = list(map(int, input().split()))     # 접수창구별 소요시간
    repair = list(map(int, input().split()))     # 정비창구별 소요시간
    customer = list(map(int, input().split()))    # K명 고객의 도착시간
    result = 0
    new = []
    recnum = []
    repnum = [0] * K
    rectime = [-1] * N  # 접수
    reptime = [-1] * M  # 정비
    for c in range(K):  # 고객 c
        flag = 0
        for num in range(N):
            if rectime[num] < customer[c]:
                rectime[num] = customer[c] + recept[num] - 1
                recnum.append(num)
                flag = 1
                new.append([rectime[num]+1, num, c])
                break
        if flag == 0:
            idx = rectime.index(min(rectime))
            recnum.append(idx)
            rectime[idx] += recept[idx]
            new.append([rectime[idx]+1, idx, c])
    for i in sorted(new):
        flag = 0
        for num in range(M):
            if reptime[num] < i[0]:
                reptime[num] = i[0] + repair[num] - 1
                repnum[i[2]] = num
                flag = 1
                break
        if flag == 0:
            idx = reptime.index(min(reptime))
            repnum[i[2]] = idx
            reptime[idx] += repair[idx]
    for k in range(K):
        if recnum[k] + 1 == A and repnum[k] + 1 == B:
            result += (k+1)
    if result == 0:
        result = -1

    print("#{} {}".format(tc+1, result))