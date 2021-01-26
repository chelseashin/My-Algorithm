N = int(input())
D = dict()
for _ in range(N):
    book = input()
    if book not in D.keys():
        D[book] = 1
    else:
        D[book] += 1
target = max(D.values())
A = []
for name, value in D.items():
    if target == value:
        A.append(name)
print(sorted(A)[0])