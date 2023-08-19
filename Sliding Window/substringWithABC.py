s = "abcabca"

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
