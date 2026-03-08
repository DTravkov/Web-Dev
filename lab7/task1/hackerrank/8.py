
n = int(input())
lst = list(map(int, input().split()))

scores_set = list(set(lst)).sort(reverse=True)

print(scores_set[1])