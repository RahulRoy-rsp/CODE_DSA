s = "nevergiveup"

def longestSub(s):
    maxi = 0
    left, right = 0, 0
    sub = []
    while right < len(s):
        if s[right] not in sub:
            sub.extend(s[right])
            right += 1
        else:
            curr = len(sub)
            maxi = max(maxi, curr)
            left += 1
            sub.remove(sub[0])

    return maxi

print(longestSub(s))
