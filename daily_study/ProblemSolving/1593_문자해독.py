from sys import stdin
input = stdin.readline

# main
wlen, slen = map(int, input().split())
w = input().strip()
s = input().strip()
wInfo = [0] * 52
sInfo = [0] * 52

for i in range(wlen):
    if 'a' <= w[i] <= 'z':
        wInfo[ord(w[i]) - ord('a')] += 1        # 소문자 처리
    else: 
        wInfo[ord(w[i]) - ord('A') + 26] += 1   # 대문자 처리

start, length, result = 0, 0, 0
for i in range(slen):
    if 'a' <= s[i] <= 'z':
        sInfo[ord(s[i]) - ord('a')] += 1
    else: 
        sInfo[ord(s[i]) - ord('A') + 26] += 1
    length += 1             # 길이 1칸 늘리기

    # Sliding Window
    if length == wlen:      # 탐색 길이와 찾을 문자열 길이가 같으면
        if wInfo == sInfo:  # 찾는 문자열과 구성 일치
            result += 1
        if 'a' <= s[start] <= 'z':
            sInfo[ord(s[start]) - ord('a')] -= 1
        else: 
            sInfo[ord(s[start]) - ord('A') + 26] -= 1
        start += 1          # 시작 위치 1칸 밀고
        length -= 1         # 길이는 1칸 줄이기

print(result)