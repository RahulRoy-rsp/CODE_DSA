st = "steve jobs"

# Approach 1
from collections import Counter
def dupCounts(st):
    charCounts = Counter(st)
    for i, j in charCounts.items():
        if  j > 1:
            print(f"{i}: {j}")
    
dupCounts(st)


# Approach 2
st = "shimlamirch"
def dupCounts(st):
    charCounts = {}
    for i in st:
        if i not in charCounts:
            charCounts[i] = 1
        else:
            charCounts[i] += 1

    for i, j in charCounts.items():
        if  j > 1:
            print(f"{i}: {j}")
    
dupCounts(st)
