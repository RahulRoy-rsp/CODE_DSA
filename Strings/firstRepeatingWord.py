st = "Today was not a good day, but tomorrow will be a good day"

# Approach 1
def firstRepeating(st):
    lis = []
    for i in st.split():
        if i not in lis:
            lis.append(i)
        else:
            return i
    return -1

print(firstRepeating(st))


# Approach 2
def firstRepeating(st):
    dict_ = {}
    for i in st.split():
        if i not in dict_:
            dict_[i] = True
        else:
            return i
    return -1

print(firstRepeating(st))


# Approach 3
from collections import Counter
def firstRepeating(st):
    wordCount = Counter(st.split())
    for i, j in wordCount.items():
        if j > 1:
            return i
    return -1

print(firstRepeating(st))
