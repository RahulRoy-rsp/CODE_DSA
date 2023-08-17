st = "Kacey"

from collections import deque
def revUsingQueue(st):
    q = deque()
    for i in st:
        q.appendleft(i)
        
    return "".join(q)

print(revUsingQueue(st))
