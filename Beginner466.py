from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
d = defaultdict(int) # 存在しないキーにアクセスすると自動で(intの場合は)0を返す
for v in a:
    # vよりも小さい数字がない場合はd[v]が1になる
    # vよりも小さい数字がある場合はd[v]がd[v-1]+1になる
    d[v] = max(d[v], d[v-1] + 1)
print(max(d.values()))
