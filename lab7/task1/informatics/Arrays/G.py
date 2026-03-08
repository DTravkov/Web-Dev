a = int(input())

lst = list(map(int ,input().strip().split(' ')))
window = []

def reverse_manual(lst:list):
    for i in range(int(len(lst) / 2)):
        j = len(lst) - 1 - i
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp

reverse_manual(lst)
for i in lst:
    print(i, end=' ')



