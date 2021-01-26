N = int(input())
time = 0
i = 1
while N > 0:
    if i > N:
        i = 1
    N -= i
    i += 1
    time += 1
print(time)