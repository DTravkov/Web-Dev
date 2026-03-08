a = int(input())

lst = list(map(int ,input().strip().split(' ')))
window = []
def find_lower_neighs(lst:list):
    if len(lst) < 3:
        return 0
    
    cnt = 0

    
    window = lst[0:2]
    lst = lst[2:]
    
    for i in lst:
        
        window.append(i)
        if window[1] > window[0] and window[1] > window[2]:
            cnt += 1
        window.pop(0)
        

    return cnt

print(find_lower_neighs(lst))



