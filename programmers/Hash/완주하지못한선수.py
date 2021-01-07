participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

def solution(participant, completion):
    temp = 0
    D = {}
    for part in participant:
        D[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= int(hash(com))
    print(temp)
    print(D)
    return D[temp]

print(solution(participant, completion))

# print(hash("marina"), hash("nikola"))
# for i in range(5):
#     print(hash(participant[i]))