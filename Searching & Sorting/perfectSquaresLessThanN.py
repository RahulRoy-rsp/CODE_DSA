n = 3

def cs(n):
    sq = 1
    for i in range(1, n):
        sq = i**2
        if sq >= n:
            return i-1
    return sq
    
print(cs(n))
