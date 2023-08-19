s = "abcabca"


# Approach 1
def substringWithABC(s):
    left = 0
    ans = 0
    counts = {'a': 0, 'b': 0, 'c': 0}
    
    for right in range(len(s)):
        if s[right] in counts:
            counts[s[right]] += 1
            
            while all(counts[c] > 0 for c in 'abc'):
                if s[left] in counts:
                    counts[s[left]] -= 1
                
                ans += len(s) - right
                left += 1
    return ans

print(substringWithABC(s))


# Approach 2
def substringWithABC(s):
    left = 0
    ans = 0
    while left < len(s):
        right = left + 2
        while right <= len(s):
            if 'a' in s[left:right] and 'b' in s[left:right] and 'c' in s[left:right]:
                ans += 1
            right += 1
        left += 1
    return ans

print(substringWithABC(s))
