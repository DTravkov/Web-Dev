value = list(map(int, input().strip().split(' ')))
a = bool(value[0])
b = bool(value[1])


def xor (b1,b2):
    return b1 == 0 and b2 == 1 or b1 == 1 and b2 == 0

print(int(xor(a,b)))