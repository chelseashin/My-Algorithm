N = 9

def star(r, c, size):
    if size == 1:
        return
    new_size = size // 3
    for ri in range(3):
        for ci in range(3):
            if ri == 1 and ci == 1:
                for rj in range(r + ri*new_size, r + (ri+1)*new_size):
                    for cj in range(c + ci*new_size, c + (ci+1)*new_size):
                        arr[rj][cj] = ' '
            star(r + ri*new_size, c + ci*new_size, new_size)

# N = int(input())
arr = [list('*' * N) for _ in range(N)]
star(0, 0, N)
print(arr)
for a in arr:
    print(''.join(a))