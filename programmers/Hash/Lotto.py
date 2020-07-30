########## 로 또 성 공 !!!! #############
# 로또 좀 됐으면 좋겠다..
# lottos = ["10 18 23 33 (15) 29 45",
#           "42 (5) 45 32 15 23 12",
#           "19 6 12 16 35 34 (17)",
#           "(15) 23 26 21 20 37 12",
#           "15 20 39 9 (18) 5 12",
#           "18 (20) 11 5 22 21 25",
#           "42 44 23 8 5 22 (20)"]

lottos = ["15 10 39 5 1 21 (22)",
          "11 5 (10) 39 1 8 44",
          "(39) 10 5 22 15 9 20",
          "22 10 5 1 (15) 3 2",
          "10 (5) 22 1 15 41 38",
          "10 5 39 33 17 14 (1)"]

N = len(lottos)
L = [list(lottos[i].split()) for i in range(N)]

numLst = [0] * 46
bonusLst = [0] * 46
numDict = {7 : [], 6 : [], 5 : [], 4 : [], 3 : [], 2 : [], 1 : [], 0 : []}
bonusDict = {7 : [], 6 : [], 5 : [], 4 : [], 3 : [], 2 : [], 1 : [], 0 : []}

for week in L:
    for i in week:
        if i[0] == "(":
            i = i[1:-1]
            bonusLst[int(i)] += 1
        else:
            numLst[int(i)] += 1
# print(numLst)
# print(bonusLst)
for n in range(1, len(numLst)):
    numDict[numLst[n]].append(n)
    bonusDict[bonusLst[n]].append(n)
# print(numDict)
# print(bonusDict)

result = []
for d in numDict.values():
    if len(result) == 6:
        break
    for i in d:
        result.append(i)
# print(result)
bonusnum = 0
for b in bonusDict.values():
    if bonusnum:
        break
    for n in b:
        if n not in result:
            result.append(n)
            bonusnum = n
            break

# print(sorted(result))
answer = []
for s in sorted(result):
    if s == bonusnum:
        answer.append("(" + str(s) + ")")
    else:
        answer.append(str(s))
# print(*answer)
print(' '.join(answer))

