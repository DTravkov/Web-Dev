a = int(input())

lst = input().split(' ')

for i in lst:
    if abs(int(i)) % 2 == 0:
        print(i, sep=' ')