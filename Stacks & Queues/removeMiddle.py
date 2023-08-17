st = [4, 2, 3, 1, 5, 1]

def delMiddle(st):
    left = 0
    right = len(st) - 1
    mid = (left+right)//2
    st.remove(st[mid])
    
    return st

print(delMiddle(st))
