n, q = map(int,input().split())
a = list(map(int,input().split()))
s = [0] * (n+1)
for i in range(n):
    s[i+1] = s[i] + a[i]

for _ in range(q):
    query = list(map(int,input().split()))
    t = query[0]

    if t == 1:
        x = query[1]
        x -= 1
        a[x], a[x+1] = a[x+1], a[x]
        s[x+1] = s[x] + a[x]
    else:
        l, r = query[1], query[2]
        l -= 1
        print(s[r] - s[l])
