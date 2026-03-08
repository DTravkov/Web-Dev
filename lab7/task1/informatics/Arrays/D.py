a = int(input())

lst = list(map(int ,input().strip().split(' ')))

prev = None
cur = None
cnt = 0
for i in lst:
    if prev and cur and prev < cur and i < cur:
        cnt += 1

print(cnt)