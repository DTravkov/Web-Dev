v = int(input())
t = int(input())

if v > 0:
    print((v * t) % 109)
else:
    v = abs(v)
    print((109 - ((v * t) % 109)) % 109)