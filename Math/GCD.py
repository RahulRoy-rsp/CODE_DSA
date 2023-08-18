i = 74
j = 2

# Approach 1
from math import gcd
def calGCD(i, j):
    return gcd(i, j)
    
print(calGCD(i, j))


# Approach 2
def calGCD(i, j):    
    if j == 0:
        return i
    else:
        return calGCD(j, i % j)

print(calGCD(i, j))


# Approach 3
def calGCD(i, j):
    ans = 1
    for x in range(1, min(i, j) + 1):
        if i % x == 0 and j % x == 0:
            ans = x

    return ans
    
print(calGCD(i, j))
