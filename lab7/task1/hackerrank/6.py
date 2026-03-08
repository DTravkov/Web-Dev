
year = int(input().strip())
print(year % 100 != 0 and (year % 4 == 0 or year % 400 == 0))