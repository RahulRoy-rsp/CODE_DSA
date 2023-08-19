s1 = "maark"
s2 = "kmra"

# Approach 1
def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    dict1 = {}
    dict2 = {}

    def store(dic, stri):
        for i in stri:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
    
    store(dict1, s1)
    store(dict2, s2)
    
    return dict1 == dict2

print(isAnagram(s1, s2))


# Approach 2
s1 = "mark"
s2 = "kmra"

from collections import Counter
def isAnagram(s1, s2):
    return Counter(s1) == Counter(s2)

print(isAnagram(s1, s2))


# Approach 3
s1 = "mark."
s2 = "k.mra"

def isAnagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(isAnagram(s1, s2))

