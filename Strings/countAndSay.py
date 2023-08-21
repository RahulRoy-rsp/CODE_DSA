n = 4

def countAndSay(n):
    if n == 1:
        return "1"
    
    rec = countAndSay(n-1)
    i, j, ans = 0, rec[0], ''
    for x in range(1, len(rec)):
        if rec[x] != j:
            ans += str(x-i) + j
            i, j = x, rec[x]
    ans += str(len(rec)-i) + j
    
    return ans
    
print(countAndSay(n))
