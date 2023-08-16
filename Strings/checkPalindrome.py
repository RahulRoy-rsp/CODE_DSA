st = "pizza"

# Appropach 1
from collections import deque
def palind(st):
    q = deque()
    for i in st:
        q.appendleft(i)
    return "".join(q) == st
    
print(palind(st))


# Approach 2
st = "nitin"
def palind(st):
    return st[::-1] == st
    
print(palind(st))


# Approach 3
st = "pizz"
def palind(st):
    l = 0
    r = len(st) - 1
    while l <= r:
        if st[l] != st[r]:
            return False
        l += 1
        r -= 1
    return True
    
print(palind(st))
