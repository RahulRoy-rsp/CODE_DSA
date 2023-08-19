strs = ["flower","flow","flight"]

def longestCommonPre(strs):
    start_ = min(strs)
    end_ = max(strs)

    pre_ = ''

    for char in range(min(len(start_), len(end_))):
        if start_[char] == end_[char]:
            pre_ += start_[char]
        else:
            break

    return pre_

print(longestCommonPre(strs))
