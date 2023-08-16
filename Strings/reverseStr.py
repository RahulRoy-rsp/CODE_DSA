st = "Hola"


# Approach 1
def rev(st):
    return st[::-1]
print(rev(st))

# Approach 2
def rev(st):
    new = ''
    for i in st:
        new = i + new
    return new
print(rev(st))


# Approach 3
def rev(st):
    return "".join(reversed(st))
print(rev(st))


# Approach 4
from collections import deque
def rev(st):
    q = deque()
    for i in st:
        q.appendleft(i) 
    return "".join(q)
print(rev(st))
