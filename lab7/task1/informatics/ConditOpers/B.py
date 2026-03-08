a = int(input())

def define_year(year):
    if a % 400 == 0 or (a % 4 and a % 100 != 0):
        return "YES"
    return "NO"

print(define_year(a))