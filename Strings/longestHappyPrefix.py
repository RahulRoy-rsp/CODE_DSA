stri = 'ababab'

def longestHappyPrefix(stri):
    n = len(stri)
    
    for i in range(n-1, 0, -1):
        if stri[:i] == stri[n-i:]:
            return stri[:i]
        
    return ""
    
print(longestHappyPrefix(stri))
