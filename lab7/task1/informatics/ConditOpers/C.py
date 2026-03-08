a = int(input())
b = int(input())
def palindrome(number):
    string = str(number).split('').reverse()
    if string == str(number): return True
    return False
def define_correct(a,b):
    if a > 999 or a < -999:
        if palindrome(a) and b == 1:
            return True
        elif palindrome(a) and b != 1:
            return False
    else:
        if b == 1:
            return False
        return True
    
exp = "YES" if define_correct(a,b) else "NO"
print(exp)