from sys import stdin
input = stdin.readline

N = int(input())
answer = 0
for _ in range(N):
    word = input()
    check = set()
    check.add(word[0])
    for i in range(1, len(word)-1):
        if word[i-1] == word[i]:    # 전 문자와 같으면 넘기고
            continue
        elif word[i] not in check:  # 전 문자와 다른데, 처음 나온 문자라면
            check.add(word[i])      # check Set에 추가
        else:             # 전 문자와 다른데, 이미 나왔던 문자라면
            break         # break로 반복문 탈출
    else:   # 위 반복문에서 탈출해서 도달한 게 아니라면 그룹 단어이므로 += 1
        answer += 1
print(answer)