def perm(n, r):
    if r == 0:
        print(t)
    else:
        for i in range(n-1,-1,-1):
            a[i], a[n-1] = a[n-1], a[i]
            t[r-1] = a[n-1]
            perm(n-1, r-1)
            a[i], a[n - 1] = a[n - 1], a[i]

def perm2(k):
    if k == R:
        print(a)
    else:
        for i in range(k,N):
            a[i], a[k] = a[k], a[i]
            perm2(k+1)
            a[i], a[k] = a[k], a[i]

def perm3(k):
    if k == N:
        print(t)
    else:
        for i in range(N):
            if visited[i] : continue
                t[k] = a[i]
                visited[i] = 1
                perm3(k+1)
                visited[i] = 0
            N = 3
            R = 3
            a=[1,2,3]
            t=[0] * R# perm(3,3)# perm2(0)visited=[0]*Nperm3(0)